from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Track

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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tracks", response_model=list[TrackOut])
def list_tracks(db: Session = Depends(get_db)):
    return db.query(Track).all()
