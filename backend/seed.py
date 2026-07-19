from database import engine, SessionLocal
from models import Base, Track, Strategy

Base.metadata.create_all(bind=engine)

mushroom_cup_tracks = [
    {
        "id": 1,
        "name": "Mario Kart Stadium",
        "cup": "Mushroom Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
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
        "terrain": "None",
        "traits": ["Water", "Anti-grav"],
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
        "terrain": "None",
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
        "terrain": "None",
        "traits": ["Anti-grav", "Water"],
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
        "terrain": "None",
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
        "terrain": "None",
        "traits": ["Coins"],
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
        "terrain": "None",
        "traits": ["Hazards", "Cave"],
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
        "terrain": "None",
        "traits": ["Shortcuts", "Hazards"],
        "description": (
            "A bustling shopping mall of escalators, split paths, and roaming "
            "cars in the parking lot finale — pick the right branch and dodge "
            "traffic to nail the exit."
        ),
    },
]

all_tracks = mushroom_cup_tracks + golden_dash_cup_tracks

# One or more strategies per track, each keyed to a starting-grid band on the
# fixed 12-kart grid (1 = pole, 12 = back). Some tracks carry both a front and a
# back strategy — the bimodal case a single band per track cannot represent.
strategies = [
    # Mario Kart Stadium — clean, low-chaos: reward a controlled lead.
    {
        "track_id": 1, "position_min": 1, "position_max": 4,
        "tips": [
            "Hold the inside line through the anti-grav loop to deny passing room.",
            "Save a coin buffer for top speed on the boost-pad straights.",
            "Take the glider ramp flat to keep momentum to the line.",
        ],
    },
    # Water Park — forgiving, slight edge to steady mid-pack driving.
    {
        "track_id": 2, "position_min": 3, "position_max": 8,
        "tips": [
            "Draft the kart ahead down the main straight before committing to a pass.",
            "Drift the submerged section early — underwater steering is sluggish.",
            "Bank defensive items; the pack bunches up in the tunnels.",
        ],
    },
    # Sweet Sweet Canyon — shortcuts reward a bold comeback from the back.
    {
        "track_id": 3, "position_min": 7, "position_max": 12,
        "tips": [
            "Break the chocolate wall shortcut every lap — it's worth the risk from the back.",
            "Carry a mushroom to cut the soda-lake corner.",
            "Line up the stained-glass glider launch for a clean landing.",
        ],
    },
    # Thwomp Ruins — bimodal: defend up front, or gamble on the crushers from the back.
    {
        "track_id": 4, "position_min": 1, "position_max": 3,
        "tips": [
            "Take the crushers on the safe, predictable timing — don't gamble with a lead.",
            "Hold a trailing shell or banana to block the temple entrance.",
            "Stay center through the anti-grav interior to cover both exits.",
        ],
    },
    {
        "track_id": 4, "position_min": 8, "position_max": 12,
        "tips": [
            "Dive the tight Thwomp gaps the leaders won't risk — that's where you gain.",
            "Time entry so a crusher rises just as you reach it.",
            "Spend items aggressively; you have nothing to defend from the back.",
        ],
    },
    # Paris Promenade — rerouting + shortcuts: strong catch-up track.
    {
        "track_id": 5, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn which way the track reroutes each lap — the layout flips.",
            "Cut the museum shortcut when the boulevard section is open.",
            "Save an item for the tight Eiffel Tower dash where passes stick.",
        ],
    },
    # Toad Circuit — flowing, coin-heavy: build a clean boost chain from the front.
    {
        "track_id": 6, "position_min": 1, "position_max": 5,
        "tips": [
            "Grab every coin — max coins means max top speed on the long curves.",
            "Chain drifts through the sweepers for uninterrupted mini-turbos.",
            "Keep a clean racing line; there are no shortcuts to fall back on.",
        ],
    },
    # Choco Mountain — hazards punish, but reward daring lines from behind.
    {
        "track_id": 7, "position_min": 6, "position_max": 12,
        "tips": [
            "Weave the rolling boulders on the cave descent for time the leaders won't take.",
            "Hug the inside of the narrow ledges to shorten the climb.",
            "Hold a mushroom to recover instantly if a rock clips you.",
        ],
    },
    # Coconut Mall — bimodal: split paths let leaders extend or the pack pounce.
    {
        "track_id": 8, "position_min": 1, "position_max": 4,
        "tips": [
            "Pick the escalator branch moving in your direction for free speed.",
            "Memorize the parking-lot car pattern to protect your lead at the finish.",
            "Block the faster split with a trailing item.",
        ],
    },
    {
        "track_id": 8, "position_min": 7, "position_max": 12,
        "tips": [
            "Take the opposite branch from the pack to find open track.",
            "Use the escalators' speed boost to close gaps between sections.",
            "Gamble through the parking-lot traffic — the leaders slow to dodge it.",
        ],
    },
]

db = SessionLocal()

try:
    for track_data in all_tracks:
        existing = db.query(Track).filter(Track.id == track_data["id"]).first()
        if not existing:
            db.add(Track(**track_data))
    db.commit()

    for strat in strategies:
        existing = (
            db.query(Strategy)
            .filter(
                Strategy.track_id == strat["track_id"],
                Strategy.position_min == strat["position_min"],
                Strategy.position_max == strat["position_max"],
            )
            .first()
        )
        if not existing:
            db.add(Strategy(**strat))
    db.commit()
    print("Mushroom Cup and Golden Dash Cup tracks and strategies seeded successfully.")
finally:
    db.close()
