from database import engine, SessionLocal
from models import Base, Track

Base.metadata.create_all(bind=engine)

mushroom_cup_tracks = [
    {
        "id": 1,
        "name": "Mario Kart Stadium",
        "cup": "Mushroom Cup",
        "dlc": False,
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
        "dlc": False,
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
        "dlc": False,
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
        "dlc": False,
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

golden_dash_cup_tracks = [
    {
        "id": 5,
        "name": "Paris Promenade",
        "cup": "Golden Dash Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "traits": ["City", "Shortcuts", "Rerouting"],
        "description": (
            "A grand tour of Paris that reroutes every lap — cobbled boulevards, "
            "a dash past the Eiffel Tower, and museum shortcuts that change which "
            "way the race flows each time around."
        ),
    },
    {
        "id": 6,
        "name": "Toad Circuit",
        "cup": "Golden Dash Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "traits": ["Beginner", "Sweeping", "Coins"],
        "description": (
            "A sunny, Toad-lined speedway of long sweeping curves and coin-dotted "
            "straights — an easy, flowing circuit perfect for building up a clean "
            "boost chain."
        ),
    },
    {
        "id": 7,
        "name": "Choco Mountain",
        "cup": "Golden Dash Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "traits": ["Technical", "Hazards", "Cave"],
        "description": (
            "A winding climb through a chocolate mountain where rolling boulders "
            "tumble down a cave descent — narrow ledges and falling rocks punish "
            "any sloppy line."
        ),
    },
    {
        "id": 8,
        "name": "Coconut Mall",
        "cup": "Golden Dash Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "traits": ["Technical", "Shortcuts", "Hazards"],
        "description": (
            "A bustling shopping mall of escalators, split paths, and roaming "
            "cars in the parking lot finale — pick the right branch and dodge "
            "traffic to nail the exit."
        ),
    },
]

all_tracks = mushroom_cup_tracks + golden_dash_cup_tracks

db = SessionLocal()

try:
    for track_data in all_tracks:
        existing = db.query(Track).filter(Track.id == track_data["id"]).first()
        if not existing:
            db.add(Track(**track_data))
    db.commit()
    print("Mushroom Cup and Golden Dash Cup tracks seeded successfully.")
finally:
    db.close()
