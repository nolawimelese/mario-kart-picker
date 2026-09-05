import hashlib
import json
import logging
import os
import re

from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_ipaddr
from sqlalchemy.orm import Session, joinedload
from starlette.middleware.base import BaseHTTPMiddleware

from database import SessionLocal
from models import Track
from recommender import FIELD_SIZE, score_track

# Per-IP request budgets. Without them every request reaches SQLite directly and
# a bare loop saturates a small instance; CORS is no help, since it constrains
# browsers only. `/` and `/health` are deliberately left off so Render's health
# check can never be throttled. In-memory storage (the default) is fine for a
# single instance.
TRACKS_RATE_LIMIT = "60/minute"
RECOMMEND_RATE_LIMIT = "30/minute"

# How long a client may reuse /tracks without revalidating. The catalog only
# changes on reseed, so an hour of browser caching keeps most repeat traffic off
# the instance entirely.
CATALOG_CACHE_SECONDS = 3600

# Render terminates TLS at a proxy, so request.client.host is that proxy for
# every caller -- get_remote_address would put the whole world in one bucket and
# lock everyone out at once. get_ipaddr reads X-Forwarded-For instead. That
# header is client-spoofable, so this slows a casual request loop rather than
# stopping a determined attacker, which is the bar we need here.
limiter = Limiter(key_func=get_ipaddr)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

allowed_origins = [
    origin.strip()
    for origin in os.environ.get("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
    if origin.strip()
]

logger = logging.getLogger(__name__)


def _has_unescaped_dot(pattern: str) -> bool:
    r"""Whether `pattern` contains a `.` acting as a wildcard.

    A left-to-right scan rather than a regex over a regex: a backslash consumes
    the next character (so `\.` and `\d` are fine) and `[...]` is skipped, since
    a dot inside a character class is already literal. A class written `[]]` --
    a leading literal `]` -- ends the class early here; that can only produce a
    false rejection, which is logged loudly rather than failing open, and no
    origin regex looks like that.
    """
    i = 0
    in_class = False
    while i < len(pattern):
        char = pattern[i]
        if char == "\\":
            i += 2
            continue
        if in_class:
            if char == "]":
                in_class = False
        elif char == "[":
            in_class = True
        elif char == ".":
            return True
        i += 1
    return False


def _checked_origin_regex(raw: str) -> str | None:
    """Validate an operator-supplied origin regex, or drop it with a warning.

    Starlette anchors the match (re.fullmatch) but does nothing about escaping,
    so `mysite.netlify.app` also matches `mysiteXnetlifyYapp` -- a domain an
    attacker can register. This value lives in the Render dashboard, outside
    the repo, so it is validated here rather than trusted.

    Dropping the regex is deliberately fail-safe, not fail-closed: the
    production origin comes from ALLOWED_ORIGINS and keeps working, so only
    deploy previews lose CORS. Taking the whole service down over a bad preview
    pattern would be worse than the flaw it guards against.
    """
    pattern = raw.strip()
    if not pattern:
        return None
    if _has_unescaped_dot(pattern):
        logger.warning(
            "Ignoring ALLOWED_ORIGIN_REGEX %r: it contains an unescaped '.', which "
            "matches any character and would allow lookalike domains. Escape every "
            "literal dot (e.g. 'netlify\\.app').",
            pattern,
        )
        return None
    try:
        re.compile(pattern)
    except re.error as exc:
        logger.warning("Ignoring ALLOWED_ORIGIN_REGEX %r: %s", pattern, exc)
        return None
    return pattern


# Origins that can't be enumerated ahead of time -- notably Netlify deploy
# previews, which get a per-PR hostname like
#   https://deploy-preview-7--<site>.netlify.app
# Starlette matches this with re.fullmatch, so the pattern must cover the whole
# origin (scheme included). Unset means no regex matching, exact origins only.
# The value is validated rather than trusted -- see _checked_origin_regex.
allowed_origin_regex = _checked_origin_regex(os.environ.get("ALLOWED_ORIGIN_REGEX", ""))

# The largest body any real request needs: the client posts a position plus
# exactly 3 track ids. Starlette buffers the whole body before Pydantic runs,
# so the model constraints below can't stop a memory-exhaustion POST on their
# own -- this header check rejects one before it is read.
MAX_BODY_BYTES = 8 * 1024


async def limit_body_size(request: Request, call_next):
    """Reject oversized payloads up front. A chunked request sends no
    Content-Length and slips past this; the field constraints on
    RecommendRequest still bound what it can do."""
    content_length = request.headers.get("content-length")
    if content_length is not None:
        try:
            too_big = int(content_length) > MAX_BODY_BYTES
        except ValueError:
            return JSONResponse(
                status_code=400, content={"detail": "invalid Content-Length"}
            )
        if too_big:
            return JSONResponse(
                status_code=413, content={"detail": "request body too large"}
            )
    return await call_next(request)


# Order matters: the last middleware added is the outermost, so CORS must be
# added after the size guard. Otherwise a 413 would go out without
# Access-Control-Allow-Origin and the browser would report an opaque CORS
# failure instead of the real status.
app.add_middleware(BaseHTTPMiddleware, dispatch=limit_body_size)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_origin_regex=allowed_origin_regex,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TrackOut(BaseModel):

    model_config = ConfigDict(
        from_attributes=True, alias_generator=to_camel, populate_by_name=True
    )

    id: int
    name: str
    cup: str
    laps: int
    header_color: str
    terrain: str
    traits: list[str]
    description: str
    dlc: bool


class RecommendRequest(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    position: int = Field(ge=1, le=FIELD_SIZE)
    track_ids: list[int] = Field(min_length=1, max_length=3)


class RecommendationOut(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    track_id: int
    name: str
    score: float
    strategy_tips: list[str]
    reason: str
    recommended: bool


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/health")
def health():
    return {"status": "ok"}


# The serialized /tracks body and its ETag, built on first request and never
# invalidated: Render reseeds during the build, before this process starts, so
# the catalog cannot change under a running server. Locally that means a
# `python seed_all.py` needs a uvicorn restart to show up. Two threadpool
# workers racing to build this produce the same bytes, so there is no lock.
_catalog_snapshot: tuple[str, bytes] | None = None


def _catalog(db: Session) -> tuple[str, bytes]:
    """The (etag, body) pair for /tracks, built once per process."""
    global _catalog_snapshot
    if _catalog_snapshot is None:
        payload = [
            TrackOut.model_validate(track).model_dump(by_alias=True)
            for track in db.query(Track).all()
        ]
        # Same dump options as Starlette's JSONResponse, so the bytes match
        # what FastAPI produced from the response_model before.
        body = json.dumps(
            payload, ensure_ascii=False, allow_nan=False, separators=(",", ":")
        ).encode()
        _catalog_snapshot = (f'"{hashlib.sha256(body).hexdigest()[:32]}"', body)
    return _catalog_snapshot


def _matches_etag(header: str | None, etag: str) -> bool:
    """Whether an If-None-Match header covers `etag`. Weak validators (`W/"..."`)
    count -- the body one was issued for is byte-identical to this one."""
    if not header:
        return False
    return any(
        candidate.strip() == "*" or candidate.strip().removeprefix("W/") == etag
        for candidate in header.split(",")
    )


@app.get("/tracks", response_model=list[TrackOut])
@limiter.limit(TRACKS_RATE_LIMIT)
def list_tracks(request: Request, db: Session = Depends(get_db)):
    etag, body = _catalog(db)
    headers = {
        "ETag": etag,
        "Cache-Control": f"public, max-age={CATALOG_CACHE_SECONDS}",
    }
    if _matches_etag(request.headers.get("if-none-match"), etag):
        return Response(status_code=304, headers=headers)
    return Response(content=body, media_type="application/json", headers=headers)


@app.post("/recommend", response_model=list[RecommendationOut])
@limiter.limit(RECOMMEND_RATE_LIMIT)
def recommend(request: Request, req: RecommendRequest, db: Session = Depends(get_db)):
    tracks = (
        db.query(Track)
        .options(joinedload(Track.strategies))
        .filter(Track.id.in_(req.track_ids))
        .all()
    )
    found_ids = {t.id for t in tracks}
    missing = [tid for tid in req.track_ids if tid not in found_ids]
    if missing:
        raise HTTPException(status_code=404, detail=f"unknown track ids: {missing}")

    scored = [(t, score_track(t, req.position)) for t in tracks]
    scored.sort(key=lambda pair: pair[1].score, reverse=True)

    return [
        RecommendationOut(
            track_id=track.id,
            name=track.name,
            score=round(result.score, 4),
            strategy_tips=result.strategy_tips,
            reason=result.reason,
            recommended=(i == 0),
        )
        for i, (track, result) in enumerate(scored)
    ]
