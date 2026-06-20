from database import engine, SessionLocal
from models import Base, Track

Base.metadata.create_all(bind=engine)

mushroom_cup_tracks = [
    {"id": 1, "name": "Mario Kart Stadium"},
    {"id": 2, "name": "Water Park"},
    {"id": 3, "name": "Sweet Sweet Canyon"},
    {"id": 4, "name": "Thwomp Ruins"},
]

db = SessionLocal()

try:
    for track_data in mushroom_cup_tracks:
        existing = db.query(Track).filter(Track.id == track_data["id"]).first()
        if not existing:
            db.add(Track(**track_data))
    db.commit()
    print("Mushroom Cup tracks seeded successfully.")
finally:
    db.close()
