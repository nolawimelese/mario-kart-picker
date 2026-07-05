from database import engine, SessionLocal
from models import Base, Track

Base.metadata.create_all(bind=engine)

mushroom_cup_tracks = [
    {
        "id": 1,
        "name": "Mario Kart Stadium",
        "cup": "Mushroom Cup",
        "laps": 3,
        "header_color": "var(--boost-500)",
        "traits": ["Beginner", "Anti-grav", "Glider"],
        "description": (
            "A roaring stadium circuit built to show off the basics — wide "
            "boost-pad straights, a gentle anti-grav loop, and a glider ramp "
            "over the crowd to the finish."
        ),
    },
    {
        "id": 2,
        "name": "Water Park",
        "cup": "Mushroom Cup",
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "traits": ["Beginner", "Water", "Anti-grav"],
        "description": (
            "A seaside amusement park where the track dives underwater past "
            "a sunken carousel — forgiving turns, but the submerged stretch "
            "rewards clean drift lines."
        ),
    },
    {
        "id": 3,
        "name": "Sweet Sweet Canyon",
        "cup": "Mushroom Cup",
        "laps": 3,
        "header_color": "var(--star-purple)",
        "traits": ["Glider", "Water", "Shortcuts"],
        "description": (
            "A candy-coated canyon of donut tunnels and soda lakes, with a "
            "glider launch through a stained-glass window and a breakable "
            "chocolate wall hiding a shortcut."
        ),
    },
    {
        "id": 4,
        "name": "Thwomp Ruins",
        "cup": "Mushroom Cup",
        "laps": 3,
        "header_color": "var(--mushroom)",
        "traits": ["Technical", "Anti-grav", "Water"],
        "description": (
            "Ancient ruins patrolled by rolling and slamming Thwomps — timing "
            "your line through the crushers and the anti-grav temple interior "
            "is everything here."
        ),
    },
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
