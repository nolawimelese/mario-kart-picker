import os

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from sqlalchemy.orm import Session, joinedload
from starlette.middleware.base import BaseHTTPMiddleware

from database import SessionLocal
from models import Track
from recommender import FIELD_SIZE, score_track

app = FastAPI()

allowed_origins = [
    origin.strip()
    for origin in os.environ.get("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
    if origin.strip()
]

# Origins that can't be enumerated ahead of time -- notably Netlify deploy
# previews, which get a per-PR hostname like
#   https://deploy-preview-7--<site>.netlify.app
# Starlette matches this with re.fullmatch, so the pattern must cover the whole
# origin (scheme included). Unset means no regex matching, exact origins only.
allowed_origin_regex = os.environ.get("ALLOWED_ORIGIN_REGEX", "").strip() or None

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


@app.get("/tracks", response_model=list[TrackOut])
def list_tracks(db: Session = Depends(get_db)):
    return db.query(Track).all()


@app.post("/recommend", response_model=list[RecommendationOut])
def recommend(req: RecommendRequest, db: Session = Depends(get_db)):
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
