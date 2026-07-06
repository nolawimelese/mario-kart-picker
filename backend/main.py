from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from sqlalchemy.orm import Session, joinedload

from database import SessionLocal
from models import Track
from recommender import FIELD_SIZE, score_track

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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
    traits: list[str]
    description: str
    dlc: bool


class RecommendRequest(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    position: int
    track_ids: list[int]


class RecommendationOut(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    track_id: int
    name: str
    score: float
    strategy_name: str | None
    strategy_tips: list[str]
    reason: str
    recommended: bool


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tracks", response_model=list[TrackOut])
def list_tracks(db: Session = Depends(get_db)):
    return db.query(Track).all()


@app.post("/recommend", response_model=list[RecommendationOut])
def recommend(req: RecommendRequest, db: Session = Depends(get_db)):
    if not 1 <= req.position <= FIELD_SIZE:
        raise HTTPException(
            status_code=422,
            detail=f"position must be between 1 and {FIELD_SIZE}",
        )

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
            strategy_name=result.strategy_name,
            strategy_tips=result.strategy_tips,
            reason=result.reason,
            recommended=(i == 0),
        )
        for i, (track, result) in enumerate(scored)
    ]
