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
from sqlalchemy.orm import Session, joinedload
from starlette.middleware.base import BaseHTTPMiddleware

from database import SessionLocal
from models import Track
from recommender import FIELD_SIZE, score_track

# Per-IP request budgets
TRACKS_RATE_LIMIT = "60/minute"
RECOMMEND_RATE_LIMIT = "30/minute"

# How long a client may reuse /tracks without revalidating
CATALOG_CACHE_SECONDS = 3600


def client_ip(request: Request) -> str:
    """The calling client's address

    slowapi has get_ipaddr, but it tests `"X_FORWARDED_FOR" 
    in `request.headers` not `X-Forwarded-For`. Test never 
    matches and get_ipaddr silently  degrades to get_remote_address:

    A proxy appends to the header, so the left-most entry is the original
    client; the rest are intermediate proxies.
    """
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        first = forwarded.split(",")[0].strip()
        if first:
            return first
    if request.client and request.client.host:
        return request.client.host
    return "127.0.0.1"


# use forwarded client address instead of TLS
limiter = Limiter(key_func=client_ip)

app = FastAPI()
app.state.limiter = limiter
# Starlette types the handler's `exc` as Exception, slowapi's narrows it to
# RateLimitExceeded -- correct here, lines up with slowapi's own wiring.
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)  # type: ignore[arg-type]

allowed_origins = [
    origin.strip()
    for origin in os.environ.get("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
    if origin.strip()
]

logger = logging.getLogger(__name__)

def _has_unescaped_dot(pattern: str) -> bool:
    r"""Whether `pattern` contains a `.` acting as a wildcard.
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


# for netlify deploy previews, which get a per-PR hostname like
#   https://deploy-preview-7--<site>.netlify.app
allowed_origin_regex = _checked_origin_regex(os.environ.get("ALLOWED_ORIGIN_REGEX", ""))

# The largest body any real request needs, position + exactly 3 track ids.
# rejects big reads before starlette gets to it
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


async def catch_unhandled(request: Request, call_next):
    """Turn any unhandled error into a flat `{"detail": "internal error"}` 500.
    """
    try:
        return await call_next(request)
    except Exception:
        logger.exception("Unhandled error on %s %s", request.method, request.url.path)
        return JSONResponse(status_code=500, content={"detail": "internal error"})


# the order that it's added is important
app.add_middleware(BaseHTTPMiddleware, dispatch=limit_body_size)

app.add_middleware(BaseHTTPMiddleware, dispatch=catch_unhandled)

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
