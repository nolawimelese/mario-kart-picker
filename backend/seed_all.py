"""
Seed the complete Mario Kart 8 Deluxe catalog — all 24 cups / 96 courses.
"""

from database import engine, SessionLocal
from models import Base, Track, Strategy

Base.metadata.create_all(bind=engine)

#  NON dlc cups (dlc: False), ids 1-48

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

flower_cup_tracks = [
    {
        "id": 5,
        "name": "Mario Circuit",
        "cup": "Flower Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
        "description": (
            "A sleek Grand Prix circuit with an anti-gravity Mobius twist — a "
            "figure-eight ribbon you ride along the wall and ceiling before a "
            "glider drop back to the tarmac."
        ),
    },
    {
        "id": 6,
        "name": "Toad Harbor",
        "cup": "Flower Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Shortcuts", "Hazards"],
        "description": (
            "A sun-drenched harbor town of split levels — trolley tracks, a "
            "breezy upper road, and a plunge past the pier — where picking the "
            "right branch matters more than raw speed."
        ),
    },
    {
        "id": 7,
        "name": "Twisted Mansion",
        "cup": "Flower Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Anti-grav", "Hazards"],
        "description": (
            "A creaking haunted manor where the track climbs the walls in "
            "anti-gravity, floods through a ballroom, and skirts snapping "
            "ghosts — grip and nerve beat outright pace."
        ),
    },
    {
        "id": 8,
        "name": "Shy Guy Falls",
        "cup": "Flower Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider", "Water"],
        "description": (
            "A scenic climb up a Shy Guy gem quarry — waterwheels, an "
            "anti-gravity ascent straight up the falls, and a glider leap from "
            "the summit back to the base."
        ),
    },
]

star_cup_tracks = [
    {
        "id": 9,
        "name": "Sunshine Airport",
        "cup": "Star Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Glider", "Anti-grav"],
        "description": (
            "A gleaming terminal-to-runway sprint — moving walkways, an "
            "anti-gravity loop over the concourse, and a glider launch across "
            "the taxiway as jets roll by."
        ),
    },
    {
        "id": 10,
        "name": "Dolphin Shoals",
        "cup": "Star Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Water", "Hazards"],
        "description": (
            "A long dive through a coral seabed — most of the lap is "
            "underwater, past a giant moray eel that lunges from its cave, "
            "before a ramp and glider back to the surf."
        ),
    },
    {
        "id": 11,
        "name": "Electrodrome",
        "cup": "Star Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
        "description": (
            "A pulsing neon nightclub where the track lights up to the beat — "
            "an anti-gravity bowl, twin split ramps, and a glider drop through "
            "a wall of speakers."
        ),
    },
    {
        "id": 12,
        "name": "Mount Wario",
        "cup": "Star Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Glider", "Shortcuts"],
        "description": (
            "A one-shot downhill sprint run once through three sections — a "
            "helicopter drop, an avalanche-lined dam, and a twisting forest — "
            "with no second lap to recover a mistake."
        ),
    },
]

special_cup_tracks = [
    {
        "id": 13,
        "name": "Cloudtop Cruise",
        "cup": "Special Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
        "description": (
            "A flight through the clouds atop a giant beanstalk — anti-gravity "
            "spirals, cannon blasts between islands, and a glider run past a "
            "crackling thundercloud."
        ),
    },
    {
        "id": 14,
        "name": "Bone-Dry Dunes",
        "cup": "Special Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "Heavy Sand",
        "traits": ["Anti-grav", "Hazards"],
        "description": (
            "A parched graveyard desert of loose sand and rattling Dry Bones — "
            "an anti-gravity dive through a torch-lit cavern and a sinking sand "
            "basin ringed by bone bridges."
        ),
    },
    {
        "id": 15,
        "name": "Bowser's Castle",
        "cup": "Special Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Anti-grav", "Hazards"],
        "description": (
            "A menacing fortress of lava moats and magma geysers — an "
            "anti-gravity ride up a giant Bowser statue that slams a fist "
            "across the track before the run to the drawbridge."
        ),
    },
    {
        "id": 16,
        "name": "Rainbow Road",
        "cup": "Special Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
        "description": (
            "A dazzling ribbon through space-station orbit — anti-gravity "
            "loops, a barrel roll around the hull, and narrow glider stretches "
            "with nothing but stars below a single slip."
        ),
    },
]

shell_cup_tracks = [
    {
        "id": 17,
        "name": "Wii Moo Moo Meadows",
        "cup": "Shell Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Hazards"],
        "description": (
            "A cheerful countryside loop past a big red barn — wandering cows, "
            "popping Monty Moles, and a boost-pad straight, gentle enough for a "
            "clean run but never quite empty."
        ),
    },
    {
        "id": 18,
        "name": "GBA Mario Circuit",
        "cup": "Shell Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Glider"],
        "description": (
            "A breezy retro Grand Prix circuit reborn with sweeping ramps — "
            "flat, fast corners and a couple of glider jumps that reward a "
            "tidy, uninterrupted racing line."
        ),
    },
    {
        "id": 19,
        "name": "DS Cheep Cheep Beach",
        "cup": "Shell Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Water"],
        "description": (
            "A tropical shoreline where the tide rolls in and out across the "
            "sand — shallow-water lines, hopping Cheep Cheeps, and a beach that "
            "narrows as the waves surge."
        ),
    },
    {
        "id": 20,
        "name": "N64 Toad's Turnpike",
        "cup": "Shell Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Hazards"],
        "description": (
            "A busy multi-lane freeway thick with cruising cars and trucks — an "
            "anti-gravity remake where you can ride the walls, weaving traffic "
            "that punishes a wandering line."
        ),
    },
]

banana_cup_tracks = [
    {
        "id": 21,
        "name": "GCN Dry Dry Desert",
        "cup": "Banana Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "Heavy Sand",
        "traits": ["Hazards"],
        "description": (
            "A blistering loop around a sinking sun temple — a Pokey-guarded "
            "oasis, a churning quicksand whirlpool at the center, and loose "
            "sand off the racing line that drags down anyone who drifts wide."
        ),
    },
    {
        "id": 22,
        "name": "SNES Donut Plains 3",
        "cup": "Banana Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Shortcuts"],
        "description": (
            "A rolling retro plain of wooden bridges and Piranha-lined fences — "
            "a tight, low-wall circuit where a daring fence-hop cut can steal "
            "the positions raw speed can't."
        ),
    },
    {
        "id": 23,
        "name": "N64 Royal Raceway",
        "cup": "Banana Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Glider"],
        "description": (
            "A regal circuit sweeping up to Peach's castle — long, confident "
            "curves and a grand ramp that launches you into a long glide over "
            "the moat to the finish."
        ),
    },
    {
        "id": 24,
        "name": "3DS DK Jungle",
        "cup": "Banana Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Hazards"],
        "description": (
            "A thumping trek through Donkey Kong's jungle — an anti-gravity "
            "temple climb, rolling barrels and bouncing Tikis, and a torch-lit "
            "cavern drumming with tribal beats."
        ),
    },
]

leaf_cup_tracks = [
    {
        "id": 25,
        "name": "DS Wario Stadium",
        "cup": "Leaf Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
        "description": (
            "A rowdy dirt motocross arena of big table-top jumps and an "
            "anti-gravity half-pipe — huge airtime over flaming hoops before "
            "the launch down the finishing straight."
        ),
    },
    {
        "id": 26,
        "name": "GCN Sherbet Land",
        "cup": "Leaf Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "Heavy Ice",
        "traits": ["Cave", "Hazards"],
        "description": (
            "A glittering frozen cavern where the ice sends karts skating wide "
            "— dodging shellfish and Freezies through a crystal grotto that "
            "rewards a delicate, patient throttle."
        ),
    },
    {
        "id": 27,
        "name": "3DS Music Park",
        "cup": "Leaf Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Hazards"],
        "description": (
            "A whimsical concert of a track where giant piano keys and "
            "bouncing note blocks slam down on the beat — time your run to the "
            "music or get bounced off the tempo."
        ),
    },
    {
        "id": 28,
        "name": "N64 Yoshi Valley",
        "cup": "Leaf Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Shortcuts", "Hazards"],
        "description": (
            "A tangled valley of forking paths where the position board gives "
            "up guessing — a maze of branching routes past a rolling giant egg, "
            "made for a bold gamble from the back."
        ),
    },
]

lightning_cup_tracks = [
    {
        "id": 29,
        "name": "DS Tick-Tock Clock",
        "cup": "Lightning Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Anti-grav", "Hazards"],
        "description": (
            "A race inside a giant clock where sweeping second-hands and "
            "spinning gears shove karts around — an anti-gravity dash timed "
            "against the machinery itself."
        ),
    },
    {
        "id": 30,
        "name": "3DS Piranha Plant Slide",
        "cup": "Lightning Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Water", "Hazards"],
        "description": (
            "A plunge through underground waterworks — a rushing canal past "
            "snapping Piranha Plants, pipe tunnels, and a musical water-jet "
            "finale that speeds you toward the light."
        ),
    },
    {
        "id": 31,
        "name": "Wii Grumble Volcano",
        "cup": "Lightning Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Hazards", "Shortcuts"],
        "description": (
            "A crumbling volcano mid-eruption — the road collapses into lava as "
            "fireballs rain down, opening and closing rocky cuts that reward "
            "nerve over caution."
        ),
    },
    {
        "id": 32,
        "name": "N64 Rainbow Road",
        "cup": "Lightning Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
        "description": (
            "A one-lap grand tour of the cosmos run through three sections — an "
            "anti-gravity ride past a starry Chain Chomp planet and long glider "
            "stretches over the void, no lap to spare."
        ),
    },
]

egg_cup_tracks = [
    {
        "id": 33,
        "name": "GCN Yoshi Circuit",
        "cup": "Egg Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Glider", "Shortcuts"],
        "description": (
            "A circuit shaped like Yoshi himself — a technical run of hairpins "
            "tracing the outline, with a cheeky glider cut across the head for "
            "anyone brave enough to line it up."
        ),
    },
    {
        "id": 34,
        "name": "Excitebike Arena",
        "cup": "Egg Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Hazards"],
        "description": (
            "A retro dirt-bike track of muddy straights and rows of jump ramps "
            "that rearrange every race — read the randomized layout and hit the "
            "boost pads for maximum air."
        ),
    },
    {
        "id": 35,
        "name": "Dragon Driftway",
        "cup": "Egg Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Anti-grav"],
        "description": (
            "A high-speed spiral around a coiling serpent dragon — a nonstop "
            "anti-gravity drift up and around its body, all sweeping curves "
            "that never let you off the drift."
        ),
    },
    {
        "id": 36,
        "name": "Mute City",
        "cup": "Egg Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav"],
        "description": (
            "An F-Zero super-highway suspended in neon — an all anti-gravity "
            "circuit where magnetic strips replace coins, rewarding a smooth, "
            "flat-out line through the banked curves."
        ),
    },
]

triforce_cup_tracks = [
    {
        "id": 37,
        "name": "Wii Wario's Gold Mine",
        "cup": "Triforce Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Anti-grav", "Hazards", "Shortcuts"],
        "description": (
            "A rickety descent through Wario's mine — dodging trundling "
            "minecarts and swooping bats along cliff-edge rails, with an "
            "anti-gravity wall ride around the cavern."
        ),
    },
    {
        "id": 38,
        "name": "SNES Rainbow Road",
        "cup": "Triforce Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Anti-grav", "Hazards"],
        "description": (
            "A retro rainbow ribbon with no guardrails — an anti-gravity revamp "
            "dotted with Thwomps and sharp turns over the abyss, where one "
            "greedy corner ends the lap."
        ),
    },
    {
        "id": 39,
        "name": "Ice Ice Outpost",
        "cup": "Triforce Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "Medium Ice",
        "traits": ["Shortcuts"],
        "description": (
            "A frozen research outpost split into twin parallel ice tracks — "
            "weave between the two ribbons to find grip and passing room across "
            "the slippery, wind-scoured straights."
        ),
    },
    {
        "id": 40,
        "name": "Hyrule Circuit",
        "cup": "Triforce Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Coins"],
        "description": (
            "A Hyrule-themed circuit where rupees stand in for coins and a "
            "swing of the Master Sword opens the gate — an anti-gravity run "
            "through the castle past watchful Guardians."
        ),
    },
]

crossing_cup_tracks = [
    {
        "id": 41,
        "name": "GCN Baby Park",
        "cup": "Crossing Cup",
        "dlc": False,
        "laps": 7,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["Anti-grav", "Hazards"],
        "description": (
            "A tiny oval run seven frantic laps long — no real corners, just an "
            "anti-grav straight-and-back where shells and bananas fly nonstop "
            "and the lead changes hands every few seconds."
        ),
    },
    {
        "id": 42,
        "name": "GBA Cheese Land",
        "cup": "Crossing Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Anti-grav", "Hazards"],
        "description": (
            "A whimsical land of moon-cheese hills and craters — an anti-gravity "
            "romp dodging a rampaging Chain Chomp, with sticky off-cheese edges "
            "that swallow a sloppy line."
        ),
    },
    {
        "id": 43,
        "name": "Wild Woods",
        "cup": "Crossing Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Glider", "Shortcuts"],
        "description": (
            "A hidden forest village built into the treetops — a winding "
            "descent past waterfalls and around giant trunks, with branching "
            "wooden ramps and a glider drop into the glade."
        ),
    },
    {
        "id": 44,
        "name": "Animal Crossing",
        "cup": "Crossing Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Coins"],
        "description": (
            "A cozy stroll through the seasonal village — a gentle, low-risk "
            "loop past townsfolk and falling leaves that shifts with the "
            "seasons, ideal for cruising a clean lead home."
        ),
    },
]

bell_cup_tracks = [
    {
        "id": 45,
        "name": "3DS Neo Bowser City",
        "cup": "Bell Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Hazards"],
        "description": (
            "A rain-slicked neon metropolis where the wet road slides karts "
            "toward the walls — tight anti-gravity switchbacks through "
            "skyscraper canyons that punish braking too late."
        ),
    },
    {
        "id": 46,
        "name": "GBA Ribbon Road",
        "cup": "Bell Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
        "description": (
            "A ribbon of racetrack looping through a child's bedroom — over "
            "gift boxes and game consoles, with anti-gravity climbs up the "
            "walls and glider hops between the presents."
        ),
    },
    {
        "id": 47,
        "name": "Super Bell Subway",
        "cup": "Bell Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Hazards"],
        "description": (
            "A dash through a busy subway system where live trains roar down "
            "the tracks you're racing on — time the platform gaps and "
            "turnstiles as the express thunders past."
        ),
    },
    {
        "id": 48,
        "name": "Big Blue",
        "cup": "Bell Cup",
        "dlc": False,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Water"],
        "description": (
            "An F-Zero coastal speedway run once through three sections — a "
            "flat-out anti-gravity blast along magnetic straights and around a "
            "great waterfall, no lap to reclaim lost ground."
        ),
    },
]

# dlc cups (dlc: True), ids 49-96

golden_dash_cup_tracks = [
    {
        "id": 49,
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
        "id": 50,
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
        "id": 51,
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
        "id": 52,
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

lucky_cat_cup_tracks = [
    {
        "id": 53,
        "name": "Tour Tokyo Blur",
        "cup": "Lucky Cat Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A neon dash through downtown Tokyo that rewrites its own route "
            "every lap — expressway ramps, shrine backstreets, and harbor bends "
            "swap in and out so no two laps run the same line."
        ),
    },
    {
        "id": 54,
        "name": "DS Shroom Ridge",
        "cup": "Lucky Cat Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Hazards"],
        "description": (
            "A winding mountain highway shared with civilian traffic — cars and "
            "buses drift across the cliffside lanes, so threading the gaps "
            "matters as much as carrying speed."
        ),
    },
    {
        "id": 55,
        "name": "GBA Sky Garden",
        "cup": "Lucky Cat Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Glider"],
        "description": (
            "A serene garden floating in the clouds — looping vine bridges and "
            "beanstalk arches with glider hops between the islands, flowing and "
            "forgiving high above the sky."
        ),
    },
    {
        "id": 56,
        "name": "Ninja Hideaway",
        "cup": "Lucky Cat Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Shortcuts"],
        "description": (
            "A sprawling ninja fortress of hidden passages and spinning shuriken "
            "— an anti-gravity climb across walls and ceilings with branching "
            "secret routes for those who know them."
        ),
    },
]

turnip_cup_tracks = [
    {
        "id": 57,
        "name": "Tour New York Minute",
        "cup": "Turnip Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A high-energy sprint through Manhattan that changes route each lap "
            "— Central Park paths, neon avenues, and rooftop detours that "
            "reshuffle so no lap runs the same."
        ),
    },
    {
        "id": 58,
        "name": "SNES Mario Circuit 3",
        "cup": "Turnip Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Glider"],
        "description": (
            "A flat, old-school Mario Circuit of tidy right-angles and "
            "Piranha-lined pipes — no gimmicks but a couple of ramps, rewarding "
            "clean drifts and an unbroken racing line."
        ),
    },
    {
        "id": 59,
        "name": "N64 Kalimari Desert",
        "cup": "Turnip Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "Medium Sand",
        "traits": ["Hazards"],
        "description": (
            "A sun-baked desert loop crossed by a running steam train — time "
            "the level crossings or duck through the tunnel, with loose sand off "
            "the rails waiting to bog you down."
        ),
    },
    {
        "id": 60,
        "name": "DS Waluigi Pinball",
        "cup": "Turnip Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Hazards"],
        "description": (
            "A plunge into a giant pinball table — dodging colossal steel "
            "pinballs and bumper-lined chutes down the neon slopes, pure chaos "
            "that scatters the pack every lap."
        ),
    },
]

propeller_cup_tracks = [
    {
        "id": 61,
        "name": "Tour Sydney Sprint",
        "cup": "Propeller Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A sunlit tour of Sydney harbor that reroutes every lap — "
            "opera-house promenades, botanic-garden paths, and beachfront "
            "straights swapping in and out lap to lap."
        ),
    },
    {
        "id": 62,
        "name": "GBA Snow Land",
        "cup": "Propeller Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "Medium Ice",
        "traits": ["Hazards"],
        "description": (
            "A frosty retro trek through drifting snow — slick ice patches and "
            "waddling penguins line a low-walled circuit where a careless "
            "throttle sends you skating into the banks."
        ),
    },
    {
        "id": 63,
        "name": "Wii Mushroom Gorge",
        "cup": "Propeller Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Cave"],
        "description": (
            "A bounding ride across giant springy mushrooms over a deep gorge — "
            "hop the bounce-caps in the right rhythm and dive through the "
            "crystal cave without missing a landing."
        ),
    },
    {
        "id": 64,
        "name": "Sky-High Sundae",
        "cup": "Propeller Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Glider"],
        "description": (
            "A sugary cruise through a floating ice-cream land — wafer bridges, "
            "syrup waterfalls, and a glider drop past candy-cane spires on a "
            "sweet, flowing, forgiving layout."
        ),
    },
]

rock_cup_tracks = [
    {
        "id": 65,
        "name": "Tour London Loop",
        "cup": "Rock Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A grand loop through London that redraws itself each lap — past Big "
            "Ben and the palace, over Tower Bridge, with riverside detours that "
            "reshuffle the route lap to lap."
        ),
    },
    {
        "id": 66,
        "name": "GBA Boo Lake",
        "cup": "Rock Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Water", "Hazards"],
        "description": (
            "A moonlit haunted lake of rickety plank bridges — leaping gaps over "
            "the black water past drifting Boos, where a mistimed jump drops you "
            "straight into the drink."
        ),
    },
    {
        "id": 67,
        "name": "3DS Rock Rock Mountain",
        "cup": "Rock Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Hazards", "Cave", "Glider"],
        "description": (
            "A climb up a craggy mountainside dodging tumbling boulders — a cave "
            "burrow through the rock and a glider leap across the canyon, with "
            "rockslides raining on the narrow ledges."
        ),
    },
    {
        "id": 68,
        "name": "Wii Maple Treeway",
        "cup": "Rock Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Glider", "Hazards"],
        "description": (
            "A romp across the branches of a colossal maple in autumn — a cannon "
            "blast into the canopy, glider hops between limbs, and giant "
            "Wigglers stomping the leaf-strewn path."
        ),
    },
]

moon_cup_tracks = [
    {
        "id": 69,
        "name": "Tour Berlin Byways",
        "cup": "Moon Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A brisk tour of Berlin that reroutes each lap — past the "
            "Brandenburg Gate and along the river Spree, with boulevard and "
            "backstreet segments swapping in lap to lap."
        ),
    },
    {
        "id": 70,
        "name": "DS Peach Gardens",
        "cup": "Moon Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Shortcuts", "Hazards"],
        "description": (
            "A stroll through Peach's manicured gardens — a hedge maze of "
            "branching paths past a lumbering Chain Chomp and popping Monty "
            "Moles, where the right fork hides real time."
        ),
    },
    {
        "id": 71,
        "name": "Merry Mountain",
        "cup": "Moon Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "Light Ice",
        "traits": ["Glider"],
        "description": (
            "A festive descent down a snow-dusted holiday mountain — twinkling "
            "markets and gift-wrapped chalets, a glider drop past the great "
            "tree, and light frost that nudges wide karts."
        ),
    },
    {
        "id": 72,
        "name": "3DS Rainbow Road",
        "cup": "Moon Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
        "description": (
            "A sleek cosmic tour past a space station and a moon base — "
            "anti-gravity banks, a glider run through a comet's tail, and neon "
            "straights arcing through the star-field."
        ),
    },
]

fruit_cup_tracks = [
    {
        "id": 73,
        "name": "Tour Amsterdam Drift",
        "cup": "Fruit Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A canal-hopping tour of Amsterdam that reroutes each lap — over "
            "arched bridges and along tram-lined streets, with waterfront and "
            "market segments trading places lap to lap."
        ),
    },
    {
        "id": 74,
        "name": "GBA Riverside Park",
        "cup": "Fruit Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Water", "Hazards"],
        "description": (
            "A sun-dappled riverside run through the jungle — splashing across "
            "shallow fords past snapping Piranha Plants, with ramps that hop the "
            "winding river bends."
        ),
    },
    {
        "id": 75,
        "name": "Wii DK Summit",
        "cup": "Fruit Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "Medium Ice",
        "traits": ["Glider", "Hazards"],
        "description": (
            "A snowboard-cross plunge down DK's snowy summit — a cannon launch "
            "to the peak, a half-pipe of powder and jumps, and icy runouts that "
            "skate a loose line into the drifts."
        ),
    },
    {
        "id": 76,
        "name": "Yoshi's Island",
        "cup": "Fruit Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Glider", "Coins"],
        "description": (
            "A papercraft romp through Yoshi's Island — a glider soar over "
            "fluttering hills, Piranha-dotted meadows, and a coin-flower finish, "
            "drawn in the crayon storybook style."
        ),
    },
]

boomerang_cup_tracks = [
    {
        "id": 77,
        "name": "Tour Bangkok Rush",
        "cup": "Boomerang Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A vibrant tear through Bangkok that reroutes each lap — past golden "
            "temples and floating markets, with river-canal and boulevard "
            "segments swapping in lap to lap."
        ),
    },
    {
        "id": 78,
        "name": "DS Mario Circuit",
        "cup": "Boomerang Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Glider"],
        "description": (
            "A classic DS Mario Circuit of flowing corners and a big boost ramp "
            "— a Goomba-guarded, low-drama layout that rewards clean drifting "
            "and a confident, uninterrupted line."
        ),
    },
    {
        "id": 79,
        "name": "GCN Waluigi Stadium",
        "cup": "Boomerang Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Hazards"],
        "description": (
            "A rowdy dirt stadium of towering jumps and flaming rings — muddy "
            "off-camber ruts and snapping Piranha Plants between the ramps, big "
            "air over a roaring crowd."
        ),
    },
    {
        "id": 80,
        "name": "Tour Singapore Speedway",
        "cup": "Boomerang Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A glittering night tour of Singapore that reroutes each lap — past "
            "the marina and supertree gardens, with skyline straights and harbor "
            "bends trading places lap to lap."
        ),
    },
]

feather_cup_tracks = [
    {
        "id": 81,
        "name": "Tour Athens Dash",
        "cup": "Feather Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A sun-bright dash through Athens that reroutes each lap — around "
            "the Acropolis and down marble avenues, with hilltop and plaza "
            "segments swapping in lap to lap."
        ),
    },
    {
        "id": 82,
        "name": "GCN Daisy Cruiser",
        "cup": "Feather Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Water", "Hazards"],
        "description": (
            "A race across the decks of a luxury cruise liner — sliding tables "
            "in the dining hall, a drained-and-flooding pool, and a dip below "
            "the waterline before climbing back topside."
        ),
    },
    {
        "id": 83,
        "name": "Wii Moonview Highway",
        "cup": "Feather Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Hazards", "City"],
        "description": (
            "A moonlit expressway choked with speeding traffic — cars and trucks "
            "barrel down the lanes beneath a glittering skyline, so weaving the "
            "gaps cleanly is the whole game."
        ),
    },
    {
        "id": 84,
        "name": "Squeaky Clean Sprint",
        "cup": "Feather Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Water", "Shortcuts"],
        "description": (
            "A sudsy sprint across a giant bathroom — water-slide chutes, "
            "slippery soap suds, and toothbrush ramps, with pipe shortcuts for "
            "anyone who spots the plughole line."
        ),
    },
]

cherry_cup_tracks = [
    {
        "id": 85,
        "name": "Tour Los Angeles Laps",
        "cup": "Cherry Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A breezy tour of Los Angeles that reroutes each lap — beaches, "
            "palm-lined boulevards, and hillside curves that swap in and out so "
            "no two laps share a route."
        ),
    },
    {
        "id": 86,
        "name": "GBA Sunset Wilds",
        "cup": "Cherry Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "Light Sand",
        "traits": ["Hazards"],
        "description": (
            "A dusty savanna at golden hour where the sun sinks lower each lap — "
            "Shy Guy camps and springy tent-flaps line the sandy trail as the "
            "light fades toward dusk."
        ),
    },
    {
        "id": 87,
        "name": "Wii Koopa Cape",
        "cup": "Cherry Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Water", "Cave"],
        "description": (
            "A tropical cape that plunges into a glass water-tube with a rushing "
            "current — a river run past a beachside cave, mixing surf, shallows, "
            "and a speed-boosting pipe."
        ),
    },
    {
        "id": 88,
        "name": "Tour Vancouver Velocity",
        "cup": "Cherry Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A crisp tour of Vancouver that reroutes each lap — waterfront "
            "seawall, downtown towers, and mountain-park roads swapping segments "
            "so the layout shifts lap to lap."
        ),
    },
]

acorn_cup_tracks = [
    {
        "id": 89,
        "name": "Tour Rome Avanti",
        "cup": "Acorn Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A spirited tour of Rome that reroutes each lap — past the Colosseum "
            "and Trevi Fountain, with cobbled piazzas and riverside lanes "
            "swapping in lap to lap."
        ),
    },
    {
        "id": 90,
        "name": "GCN DK Mountain",
        "cup": "Acorn Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "None",
        "traits": ["Hazards", "Glider"],
        "description": (
            "A blast from a barrel cannon to a volcano peak, then a breakneck "
            "plunge down — dodging boulders bounding up the narrow switchbacks "
            "with a rope-bridge leap near the base."
        ),
    },
    {
        "id": 91,
        "name": "Wii Daisy Circuit",
        "cup": "Acorn Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Coins"],
        "description": (
            "An elegant seaside town circuit past marble fountains and a "
            "lighthouse — smooth, sweeping curves along the coast that reward a "
            "poised, flowing line more than aggression."
        ),
    },
    {
        "id": 92,
        "name": "Piranha Plant Cove",
        "cup": "Acorn Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Water", "Hazards"],
        "description": (
            "A dive through a sunken cove ruled by colossal Piranha Plants — "
            "long underwater stretches past snapping vines and coral arches, "
            "where steady steering beats panicked throttle."
        ),
    },
]

spiny_cup_tracks = [
    {
        "id": 93,
        "name": "Tour Madrid Drive",
        "cup": "Spiny Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boost-500)",
        "terrain": "None",
        "traits": ["City", "Rerouting"],
        "description": (
            "A lively tour of Madrid that reroutes each lap — around grand "
            "plazas and along the river, with boulevard and park segments "
            "swapping in and out lap to lap."
        ),
    },
    {
        "id": 94,
        "name": "3DS Rosalina's Ice World",
        "cup": "Spiny Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--boo-cyan)",
        "terrain": "Heavy Ice",
        "traits": ["Cave", "Hazards"],
        "description": (
            "A glittering trek through a frozen crystal world — luminous ice "
            "caverns and penguin-dotted slopes where the slick surface skates "
            "every kart wide on the sharp bends."
        ),
    },
    {
        "id": 95,
        "name": "SNES Bowser Castle 3",
        "cup": "Spiny Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--star-purple)",
        "terrain": "None",
        "traits": ["Hazards"],
        "description": (
            "A twisting retro fortress of narrow brick corridors — Thwomps "
            "slamming the tight turns and jump gaps over the floor, an "
            "unforgiving maze that rewards precision under pressure."
        ),
    },
    {
        "id": 96,
        "name": "Wii Rainbow Road",
        "cup": "Spiny Cup",
        "dlc": True,
        "laps": 3,
        "header_color": "var(--mushroom)",
        "terrain": "None",
        "traits": ["Anti-grav", "Glider"],
        "description": (
            "The grand finale rainbow through the cosmos — anti-gravity loops, "
            "half-pipe walls, and long glider stretches over the void, a "
            "glittering high-wire act to the last corner."
        ),
    },
]

all_tracks = (
    # base game
    mushroom_cup_tracks
    + flower_cup_tracks
    + star_cup_tracks
    + special_cup_tracks
    + shell_cup_tracks
    + banana_cup_tracks
    + leaf_cup_tracks
    + lightning_cup_tracks
    + egg_cup_tracks
    + triforce_cup_tracks
    + crossing_cup_tracks
    + bell_cup_tracks
    # Booster Course Pass
    + golden_dash_cup_tracks
    + lucky_cat_cup_tracks
    + turnip_cup_tracks
    + propeller_cup_tracks
    + rock_cup_tracks
    + moon_cup_tracks
    + fruit_cup_tracks
    + boomerang_cup_tracks
    + feather_cup_tracks
    + cherry_cup_tracks
    + acorn_cup_tracks
    + spiny_cup_tracks
)

# ---------------------------------------------------------------------------
# STRATEGIES
#
# One or more strategies per track, each keyed to a starting-grid band on the
# fixed 12-kart grid (1 = pole, 12 = back). Most tracks carry a single band; a
# few genuinely bimodal tracks carry both a front "defend" band and a back
# "gamble" band. Traits and band are kept directionally consistent so the
# recommender's trait nudge reinforces (never fights) the band fit.
# ---------------------------------------------------------------------------

strategies = [
    # ---- Mushroom Cup ----
    {
        "track_id": 1, "position_min": 1, "position_max": 4,
        "tips": [
            "Hold the inside line through the anti-grav loop to deny passing room.",
            "Save a coin buffer for top speed on the boost-pad straights.",
            "Take the glider ramp flat to keep momentum to the line.",
        ],
    },
    {
        "track_id": 2, "position_min": 3, "position_max": 8,
        "tips": [
            "Draft the kart ahead down the main straight before committing to a pass.",
            "Drift the submerged section early — underwater steering is sluggish.",
            "Bank defensive items; the pack bunches up in the tunnels.",
        ],
    },
    {
        "track_id": 3, "position_min": 7, "position_max": 12,
        "tips": [
            "Break the chocolate wall shortcut every lap — it's worth the risk from the back.",
            "Carry a mushroom to cut the soda-lake corner.",
            "Line up the stained-glass glider launch for a clean landing.",
        ],
    },
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

    # ---- Flower Cup ----
    {
        "track_id": 5, "position_min": 1, "position_max": 5,
        "tips": [
            "Keep a smooth line onto the anti-grav wall — bumping karts breaks your flow.",
            "Drift the figure-eight sweepers for back-to-back mini-turbos.",
            "Take the glider drop flat and land on the racing line, not the grass.",
        ],
    },
    {
        "track_id": 6, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn which branch is fastest that lap — the upper road often beats the pier.",
            "Cut through the town shortcut when you have a mushroom to spare.",
            "Watch the trolleys; time your entry so one clears just ahead of you.",
        ],
    },
    {
        "track_id": 7, "position_min": 4, "position_max": 10,
        "tips": [
            "Ease off before the flooded ballroom — hydroplaning off-line loses more than it saves.",
            "Ride the wall through the anti-grav climb to shorten the corner.",
            "Keep an item in reserve for the tight gear-room chicane.",
        ],
    },
    {
        "track_id": 8, "position_min": 3, "position_max": 8,
        "tips": [
            "Drift the switchbacks up the falls tight to the inside wall.",
            "Grab the trick ramps for a mini-turbo on every climb.",
            "Set up the summit glider jump straight so you glide the full gap.",
        ],
    },

    # ---- Star Cup ----
    {
        "track_id": 9, "position_min": 1, "position_max": 5,
        "tips": [
            "Ride the moving walkways in the terminal for free speed.",
            "Hold the tight line through the anti-grav loop over the concourse.",
            "Launch the taxiway glider flat and cut back to the racing line on landing.",
        ],
    },
    {
        "track_id": 10, "position_min": 5, "position_max": 11,
        "tips": [
            "Drift the long underwater bends early; steering lags below the surface.",
            "Stay wide of the eel's cave — its lunge is a guaranteed spin.",
            "Save a mushroom to recover if the seabed current pushes you off-line.",
        ],
    },
    {
        "track_id": 11, "position_min": 3, "position_max": 8,
        "tips": [
            "Pick a split ramp early and commit — hesitating costs the mini-turbo.",
            "Ride the anti-grav bowl high to carry speed out of it.",
            "Chain drifts to the beat; the flowing corners reward uninterrupted turbos.",
        ],
    },
    {
        "track_id": 12, "position_min": 4, "position_max": 10,
        "tips": [
            "This is a one-shot sprint — attack every section, there's no lap to recover.",
            "Take the forest shortcut lines cleanly; the trees punish a wide entry.",
            "Bank a mushroom for the final avalanche run to the line.",
        ],
    },

    # ---- Special Cup ----
    {
        "track_id": 13, "position_min": 2, "position_max": 7,
        "tips": [
            "Aim the cannon exits so you land on the boost pads, not the cloud edge.",
            "Keep a tidy line through the anti-grav spirals to hold your speed.",
            "Give the thundercloud a wide berth — a lightning strike shrinks you.",
        ],
    },
    {
        "track_id": 14, "position_min": 5, "position_max": 11,
        "tips": [
            "Stay on the packed line — the deep loose sand scrubs speed hard.",
            "Ride the anti-grav cavern wall to straighten the descent.",
            "Skirt the sinking sand basin; cutting the middle bogs you down.",
        ],
    },
    {
        "track_id": 15, "position_min": 6, "position_max": 12,
        "tips": [
            "Time the run past the Bowser statue so its fist slams behind you.",
            "Ride the anti-grav walls to carry speed through the lava switchbacks.",
            "Fire items into the tight castle corners where the pack bunches.",
        ],
    },
    {
        "track_id": 16, "position_min": 3, "position_max": 9,
        "tips": [
            "Respect the narrow glider stretches — a greedy line drops you into space.",
            "Take the barrel-roll section smoothly; fighting it kills your exit speed.",
            "Hold an item back to defend the anti-grav loop where passes stick.",
        ],
    },

    # ---- Shell Cup ----
    {
        "track_id": 17, "position_min": 3, "position_max": 8,
        "tips": [
            "Watch for wandering cows and popping Monty Moles on the wide bends.",
            "Hit the boost-pad straight with a coin buffer for top speed.",
            "Keep it clean — this is a track you win by not making mistakes.",
        ],
    },
    {
        "track_id": 18, "position_min": 1, "position_max": 5,
        "tips": [
            "Drift the flat right-angle corners tight for consistent mini-turbos.",
            "Take each glider ramp straight to land back on the racing line.",
            "Hold a clean, uninterrupted line — there's little here to catch up on.",
        ],
    },
    {
        "track_id": 19, "position_min": 3, "position_max": 8,
        "tips": [
            "Cross the shallows on the racing line; deep water slows you more.",
            "Read the tide — the beach narrows when the waves surge in.",
            "Hop the Cheep Cheeps rather than braking for them.",
        ],
    },
    {
        "track_id": 20, "position_min": 5, "position_max": 11,
        "tips": [
            "Weave the traffic with small inputs — big swerves cost more time than a bump.",
            "Ride the anti-grav walls to pass where the pack won't risk it.",
            "Keep a mushroom ready to recover from an unavoidable car clip.",
        ],
    },

    # ---- Banana Cup ----
    {
        "track_id": 21, "position_min": 5, "position_max": 11,
        "tips": [
            "Stay on the paved line — the loose sand off-track scrubs speed badly.",
            "Give the central quicksand whirlpool a wide berth; clipping it is race-ending.",
            "Time your pass as leaders slow for the Pokey near the oasis.",
        ],
    },
    {
        "track_id": 22, "position_min": 6, "position_max": 12,
        "tips": [
            "Take the fence-hop cut when you have a mushroom — it's the big time save.",
            "Keep off the grass verges; they bleed speed on this low-wall circuit.",
            "Fire items over the bridges where the pack funnels together.",
        ],
    },
    {
        "track_id": 23, "position_min": 2, "position_max": 7,
        "tips": [
            "Carry maximum speed into the grand ramp for the longest glide.",
            "Drift the long regal sweepers early to bank mini-turbos.",
            "Steer the glide toward the inside of the moat landing.",
        ],
    },
    {
        "track_id": 24, "position_min": 4, "position_max": 10,
        "tips": [
            "Ride the anti-grav temple wall to hold speed through the climb.",
            "Weave the rolling barrels and bouncing Tikis rather than braking.",
            "Keep an item back for the narrow cavern where passing is tight.",
        ],
    },

    # ---- Leaf Cup ----
    {
        "track_id": 25, "position_min": 3, "position_max": 8,
        "tips": [
            "Hit the jump ramps square for a trick boost on landing.",
            "Ride the anti-grav half-pipe high to carry momentum out of it.",
            "Line up the flaming hoops so you land straight on the boost pads.",
        ],
    },
    {
        "track_id": 26, "position_min": 4, "position_max": 10,
        "tips": [
            "Feather the throttle on the ice — full power just skates you into the walls.",
            "Take the cave line tight; the crystal grotto is where time is won or lost.",
            "Dodge the Freezies wide rather than braking on the slick surface.",
        ],
    },
    {
        "track_id": 27, "position_min": 4, "position_max": 10,
        "tips": [
            "Learn the note-block rhythm — they drop on the beat, so time your run.",
            "Drift the swinging piano-key section on the safe side.",
            "Keep an item ready for the bouncy finale where lines get chaotic.",
        ],
    },
    {
        "track_id": 28, "position_min": 6, "position_max": 12,
        "tips": [
            "Commit to one branch and learn which fork is quickest — hesitation kills it.",
            "Time the rolling giant egg so it passes as you clear the gap.",
            "The blind splits reward a bold gamble far more than a cautious line.",
        ],
    },

    # ---- Lightning Cup ----
    {
        "track_id": 29, "position_min": 4, "position_max": 10,
        "tips": [
            "Read the sweeping second-hands and slip through as they pass.",
            "Ride the anti-grav sections to skip the slowest gear paths.",
            "Small, precise inputs beat big corrections on the moving platforms.",
        ],
    },
    {
        "track_id": 30, "position_min": 4, "position_max": 10,
        "tips": [
            "Stay center in the canal; the Piranha Plants snap at the edges.",
            "Ride the water-jet boosts for free speed toward the finish.",
            "Take the pipe tunnels on the racing line — the walls are unforgiving.",
        ],
    },
    {
        "track_id": 31, "position_min": 6, "position_max": 12,
        "tips": [
            "Watch the road crumble and take the rocky cut before it closes.",
            "Weave the falling fireballs rather than braking into them.",
            "From the back, gamble the collapsing edges the leaders won't risk.",
        ],
    },
    {
        "track_id": 32, "position_min": 3, "position_max": 9,
        "tips": [
            "One lap, three sections — push every stretch, there's no recovery lap.",
            "Give the Chain Chomp planet room; its bounce knocks you into the void.",
            "Take the narrow glider runs straight and steady over the abyss.",
        ],
    },

    # ---- Egg Cup ----
    {
        "track_id": 33, "position_min": 4, "position_max": 10,
        "tips": [
            "Trace the tight hairpins that form Yoshi's outline with early drifts.",
            "Line up the glider cut across the head only with a clean approach.",
            "Keep an item back for the neck chicane where passes stick.",
        ],
    },
    {
        "track_id": 34, "position_min": 3, "position_max": 8,
        "tips": [
            "Scout the randomized ramp layout on the opening stretch.",
            "Hit the jumps square and land on the boost pads for trick speed.",
            "Keep off the deep mud at the edges; it drags you to a crawl.",
        ],
    },
    {
        "track_id": 35, "position_min": 3, "position_max": 8,
        "tips": [
            "This track is one long drift — hold the mini-turbo up the dragon's coils.",
            "Ride the anti-grav banking high to keep your line smooth.",
            "Don't over-correct; small steering keeps the drift chain alive.",
        ],
    },
    {
        "track_id": 36, "position_min": 1, "position_max": 5,
        "tips": [
            "Roll over the magnetic recharge strips to keep your boost topped up.",
            "Keep a flat, smooth line through the banked anti-grav curves.",
            "Protect the lead — this fast, clean circuit gives back-markers little to work with.",
        ],
    },

    # ---- Triforce Cup ----
    {
        "track_id": 37, "position_min": 5, "position_max": 11,
        "tips": [
            "Time the minecarts so they pass just before you take the rails.",
            "Ride the anti-grav wall around the cavern to cut the corner.",
            "Take the mine shortcut when you have an item to cover the risk.",
        ],
    },
    {
        "track_id": 38, "position_min": 4, "position_max": 10,
        "tips": [
            "No guardrails — bank a cautious line on the sharp turns over the drop.",
            "Time your run so the Thwomps rise as you reach them.",
            "Resist cutting the greedy inside; it's the classic fall-off line.",
        ],
    },
    {
        "track_id": 39, "position_min": 6, "position_max": 12,
        "tips": [
            "Switch between the twin ice tracks to find grip and open passing room.",
            "Feather the throttle on the slick straights to avoid skating wide.",
            "Use the cross-over points to slingshot past a bunched pack.",
        ],
    },
    {
        "track_id": 40, "position_min": 1, "position_max": 5,
        "tips": [
            "Collect rupees like coins — max count means max top speed.",
            "Take the Master Sword gate line smoothly to keep momentum.",
            "Hold the anti-grav castle corners tight to defend a controlled lead.",
        ],
    },

    # ---- Crossing Cup ----
    {
        "track_id": 41, "position_min": 1, "position_max": 3,
        "tips": [
            "Hoard a defensive item every lap — seven laps means constant shell pressure.",
            "Hug the inside of the oval to deny the pack any passing room.",
            "Don't chase items into traffic; protect the clean inside line.",
        ],
    },
    {
        "track_id": 41, "position_min": 7, "position_max": 12,
        "tips": [
            "Embrace the chaos — with seven short laps there's always time to climb back.",
            "Fire items forward the instant you get them; the leaders are packed tight.",
            "Take the outside on the straights to slingshot past braking karts.",
        ],
    },
    {
        "track_id": 42, "position_min": 4, "position_max": 10,
        "tips": [
            "Ride the anti-grav hills smoothly; the cheese craters upset a rough line.",
            "Time your pass so the Chain Chomp charges away from you.",
            "Keep off the sticky off-cheese edges — they swallow your speed.",
        ],
    },
    {
        "track_id": 43, "position_min": 4, "position_max": 10,
        "tips": [
            "Take the branching wooden ramps that suit your line down the descent.",
            "Set up the glider drop into the glade to land on the boost.",
            "Drift the tight tree corners early to bank mini-turbos.",
        ],
    },
    {
        "track_id": 44, "position_min": 1, "position_max": 5,
        "tips": [
            "Grab coins on the gentle straights to hold top speed up front.",
            "Keep a smooth, low-risk line — mistakes cost more than aggression gains.",
            "Save a defensive item; a clean lead is easy to protect here.",
        ],
    },

    # ---- Bell Cup ----
    {
        "track_id": 45, "position_min": 5, "position_max": 11,
        "tips": [
            "The wet road slides wide — brake earlier than the dry line suggests.",
            "Ride the anti-grav switchbacks tight through the skyscraper canyons.",
            "Attack in the tight downtown corners where the slick surface bunches the pack.",
        ],
    },
    {
        "track_id": 46, "position_min": 3, "position_max": 8,
        "tips": [
            "Ride the anti-grav wall climbs to keep your speed around the room.",
            "Line up the glider hops between presents to land on the ribbon.",
            "Drift the tidy bedroom corners for steady mini-turbos.",
        ],
    },
    {
        "track_id": 47, "position_min": 5, "position_max": 11,
        "tips": [
            "Time the platform gaps so a train has just passed before you cross.",
            "Take the turnstile chicanes tight to keep momentum.",
            "From the back, gamble the tunnel line as the express clears it.",
        ],
    },
    {
        "track_id": 48, "position_min": 3, "position_max": 9,
        "tips": [
            "One flat-out run through three sections — carry every bit of speed.",
            "Ride the anti-grav banking around the great waterfall bend.",
            "Keep a smooth line; there's no lap to reclaim a lost position.",
        ],
    },

    # ---- Golden Dash Cup ----
    {
        "track_id": 49, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn which way the track reroutes each lap — the layout flips.",
            "Cut the museum shortcut when the boulevard section is open.",
            "Save an item for the tight Eiffel Tower dash where passes stick.",
        ],
    },
    {
        "track_id": 50, "position_min": 1, "position_max": 5,
        "tips": [
            "Grab every coin — max coins means max top speed on the long curves.",
            "Chain drifts through the sweepers for uninterrupted mini-turbos.",
            "Keep a clean racing line; there are no shortcuts to fall back on.",
        ],
    },
    {
        "track_id": 51, "position_min": 6, "position_max": 12,
        "tips": [
            "Weave the rolling boulders on the cave descent for time the leaders won't take.",
            "Hug the inside of the narrow ledges to shorten the climb.",
            "Hold a mushroom to recover instantly if a rock clips you.",
        ],
    },
    {
        "track_id": 52, "position_min": 1, "position_max": 4,
        "tips": [
            "Pick the escalator branch moving in your direction for free speed.",
            "Memorize the parking-lot car pattern to protect your lead at the finish.",
            "Block the faster split with a trailing item.",
        ],
    },
    {
        "track_id": 52, "position_min": 7, "position_max": 12,
        "tips": [
            "Take the opposite branch from the pack to find open track.",
            "Use the escalators' speed boost to close gaps between sections.",
            "Gamble through the parking-lot traffic — the leaders slow to dodge it.",
        ],
    },

    # ---- Lucky Cat Cup ----
    {
        "track_id": 53, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the three lap layouts — knowing the next reroute wins you the racing line.",
            "Save a mushroom for the expressway ramp cut when it opens.",
            "Attack in the tight shrine backstreets where the pack bunches and passes stick.",
        ],
    },
    {
        "track_id": 54, "position_min": 4, "position_max": 10,
        "tips": [
            "Thread the drifting traffic with small inputs, not big swerves.",
            "Hold the inside on the cliffside bends to keep the safe line.",
            "Keep a mushroom ready to recover from a car clip.",
        ],
    },
    {
        "track_id": 55, "position_min": 3, "position_max": 8,
        "tips": [
            "Take the glider hops between islands straight for a clean landing.",
            "Drift the looping vine bridges early to bank mini-turbos.",
            "It's forgiving up high — a smooth flowing line beats forcing passes.",
        ],
    },
    {
        "track_id": 56, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the hidden routes — the secret passages are the real time save.",
            "Ride the anti-grav walls and ceilings to cut across the fortress.",
            "Watch the spinning shuriken and time your entry through the gaps.",
        ],
    },

    # ---- Turnip Cup ----
    {
        "track_id": 57, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn each lap's reroute — the avenues and park paths swap around.",
            "Cut the rooftop detour when it opens for a big time save.",
            "Attack in the tight Manhattan corners where the pack funnels together.",
        ],
    },
    {
        "track_id": 58, "position_min": 1, "position_max": 5,
        "tips": [
            "Drift the flat right-angles tight for consistent mini-turbos.",
            "Take the ramps straight to land back on the racing line.",
            "Keep a clean line — this simple circuit gives back-markers little to exploit.",
        ],
    },
    {
        "track_id": 59, "position_min": 5, "position_max": 11,
        "tips": [
            "Time the level crossings so the train has passed before you cross.",
            "Stay on the packed line — the loose desert sand scrubs speed.",
            "Take the tunnel line when the train blocks the surface crossing.",
        ],
    },
    {
        "track_id": 60, "position_min": 5, "position_max": 11,
        "tips": [
            "Read the giant pinballs' paths and slip through the gaps between them.",
            "Ride the bumper walls smoothly rather than fighting them.",
            "From the back, gamble the chaotic chutes where leaders play it safe.",
        ],
    },

    # ---- Propeller Cup ----
    {
        "track_id": 61, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the lap reroutes — the harbor and garden segments swap around.",
            "Cut the promenade shortcut when the layout opens it.",
            "Save an item for the tight beachfront bends where passes stick.",
        ],
    },
    {
        "track_id": 62, "position_min": 4, "position_max": 10,
        "tips": [
            "Feather the throttle over the ice patches to avoid skating into the banks.",
            "Dodge the penguins wide rather than braking on the slick surface.",
            "Keep off the deep snow edges; they drag your speed right down.",
        ],
    },
    {
        "track_id": 63, "position_min": 3, "position_max": 8,
        "tips": [
            "Time your hops so you land square on the next bounce mushroom.",
            "Take the cave line tight and straight to hold speed through it.",
            "Aim your bounces toward the boost pads, not the gorge edges.",
        ],
    },
    {
        "track_id": 64, "position_min": 3, "position_max": 8,
        "tips": [
            "Set up the glider drop past the spires to land on the racing line.",
            "Drift the wafer-bridge corners early for steady mini-turbos.",
            "It's a forgiving flow track — keep momentum rather than forcing passes.",
        ],
    },

    # ---- Rock Cup ----
    {
        "track_id": 65, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — the riverside detours change the flow.",
            "Cut through the palace grounds shortcut when it's open.",
            "Attack on Tower Bridge where the narrow deck bunches the pack.",
        ],
    },
    {
        "track_id": 66, "position_min": 4, "position_max": 10,
        "tips": [
            "Time the plank-bridge jumps precisely — a mistimed leap drops you in the lake.",
            "Take the water crossings on the racing line to limit the slowdown.",
            "Ignore the Boos and focus on clean landings over the gaps.",
        ],
    },
    {
        "track_id": 67, "position_min": 4, "position_max": 10,
        "tips": [
            "Weave the tumbling boulders on the narrow ledges rather than braking.",
            "Take the cave burrow tight to keep speed through the mountain.",
            "Line up the canyon glider leap straight for a clean landing.",
        ],
    },
    {
        "track_id": 68, "position_min": 4, "position_max": 10,
        "tips": [
            "Aim the cannon so you land in the canopy on the boost, not the branches.",
            "Take the glider hops between limbs straight to hold your line.",
            "Give the giant Wigglers room — a stomp is a guaranteed spin.",
        ],
    },

    # ---- Moon Cup ----
    {
        "track_id": 69, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — boulevard and backstreet segments swap.",
            "Cut the riverside shortcut past the Spree when it opens.",
            "Save an item for the tight gate corners where the pack funnels.",
        ],
    },
    {
        "track_id": 70, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the hedge-maze forks — the right branch hides real time.",
            "Time your run so the Chain Chomp lumbers away from your line.",
            "From the back, gamble the tighter maze routes the leaders avoid.",
        ],
    },
    {
        "track_id": 71, "position_min": 3, "position_max": 8,
        "tips": [
            "Set up the glider drop past the great tree to land on the boost.",
            "Feather the throttle on the light frost through the market bends.",
            "Carry momentum down the descent — it's a flowing, forgiving line.",
        ],
    },
    {
        "track_id": 72, "position_min": 3, "position_max": 9,
        "tips": [
            "Hold a smooth line through the anti-grav banks over the star-field.",
            "Take the comet-tail glider run straight and steady.",
            "Keep an item back to defend the narrow neon straights.",
        ],
    },

    # ---- Fruit Cup ----
    {
        "track_id": 73, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — waterfront and market segments trade places.",
            "Cut the canal-bridge shortcut when the layout opens it.",
            "Attack in the tight tram-street corners where the pack bunches.",
        ],
    },
    {
        "track_id": 74, "position_min": 4, "position_max": 10,
        "tips": [
            "Cross the shallow fords on the racing line to limit the slowdown.",
            "Hop the ramps over the river bends rather than braking for them.",
            "Stay clear of the Piranha Plants lining the water's edge.",
        ],
    },
    {
        "track_id": 75, "position_min": 4, "position_max": 10,
        "tips": [
            "Aim the cannon launch to land square on the summit boost.",
            "Feather the throttle on the icy runouts to avoid skating into drifts.",
            "Ride the half-pipe walls high to carry speed through the jumps.",
        ],
    },
    {
        "track_id": 76, "position_min": 2, "position_max": 7,
        "tips": [
            "Grab the coin-flowers on the meadows to keep top speed up front.",
            "Take the glider soar over the hills straight for a long, clean glide.",
            "Drift the storybook corners early to bank mini-turbos.",
        ],
    },

    # ---- Boomerang Cup ----
    {
        "track_id": 77, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — canal and boulevard segments swap around.",
            "Cut the floating-market shortcut when the layout opens it.",
            "Save an item for the tight temple corners where passes stick.",
        ],
    },
    {
        "track_id": 78, "position_min": 2, "position_max": 7,
        "tips": [
            "Drift the flowing corners early to chain mini-turbos.",
            "Hit the big boost ramp square for maximum trick speed.",
            "Keep a clean line — the low-drama layout rewards consistency up front.",
        ],
    },
    {
        "track_id": 79, "position_min": 4, "position_max": 10,
        "tips": [
            "Hit the towering jumps straight and land on the boost pads.",
            "Time the flaming rings so you pass through cleanly, not into the fire.",
            "Keep off the muddy off-camber ruts at the edges.",
        ],
    },
    {
        "track_id": 80, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — the marina and skyline segments swap.",
            "Cut the supertree-garden shortcut when it opens.",
            "Attack in the tight harbor bends where the pack funnels at night.",
        ],
    },

    # ---- Feather Cup ----
    {
        "track_id": 81, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — hilltop and plaza segments swap around.",
            "Cut the Acropolis shortcut when the layout opens it.",
            "Save an item for the tight marble-avenue corners where passes stick.",
        ],
    },
    {
        "track_id": 82, "position_min": 4, "position_max": 10,
        "tips": [
            "Watch the sliding tables in the dining hall and time your gap.",
            "Take the pool section on the racing line whether drained or flooding.",
            "Carry speed through the below-deck dip and back up to the top deck.",
        ],
    },
    {
        "track_id": 83, "position_min": 5, "position_max": 11,
        "tips": [
            "Thread the speeding traffic with small, precise inputs.",
            "Hold the safe lane through the fastest straights, not the wall.",
            "Keep a mushroom ready to recover from an unavoidable car clip.",
        ],
    },
    {
        "track_id": 84, "position_min": 4, "position_max": 10,
        "tips": [
            "Ride the water-slide chutes on the racing line for free speed.",
            "Feather the throttle across the slippery soap suds.",
            "Take the plughole pipe shortcut when you spot the entry.",
        ],
    },

    # ---- Cherry Cup ----
    {
        "track_id": 85, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — beach and hillside segments swap around.",
            "Cut the boulevard shortcut when the layout opens it.",
            "Attack in the tight palm-lined corners where the pack bunches.",
        ],
    },
    {
        "track_id": 86, "position_min": 4, "position_max": 10,
        "tips": [
            "Stay on the packed trail — the loose sand off-line scrubs speed.",
            "Watch the springy tent-flaps; they bounce a careless line off course.",
            "Visibility drops as the sun sets — commit to lines you've learned.",
        ],
    },
    {
        "track_id": 87, "position_min": 3, "position_max": 8,
        "tips": [
            "Ride the water-tube current and let the boost pipe carry you.",
            "Take the beachside cave line tight to hold speed.",
            "Cross the shallows on the racing line to limit the slowdown.",
        ],
    },
    {
        "track_id": 88, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — seawall and downtown segments swap.",
            "Cut the mountain-park shortcut when the layout opens it.",
            "Save an item for the tight waterfront bends where passes stick.",
        ],
    },

    # ---- Acorn Cup ----
    {
        "track_id": 89, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — piazza and riverside segments swap around.",
            "Cut the shortcut past the Colosseum when the layout opens it.",
            "Attack in the tight cobbled corners where the pack funnels together.",
        ],
    },
    {
        "track_id": 90, "position_min": 5, "position_max": 11,
        "tips": [
            "Aim the barrel cannon to land square on the peak boost.",
            "Weave the boulders bounding up the switchbacks on the plunge down.",
            "Take the rope-bridge leap near the base straight for a clean landing.",
        ],
    },
    {
        "track_id": 91, "position_min": 1, "position_max": 5,
        "tips": [
            "Grab coins on the coastal straights to hold top speed up front.",
            "Drift the sweeping seaside curves smoothly to chain mini-turbos.",
            "Protect the lead with a poised line — this circuit rewards composure.",
        ],
    },
    {
        "track_id": 92, "position_min": 4, "position_max": 10,
        "tips": [
            "Drift the long underwater bends early; steering lags below the surface.",
            "Stay center of the coral arches, clear of the snapping Piranha vines.",
            "Steady steering beats a panicked throttle through the deep cove.",
        ],
    },

    # ---- Spiny Cup ----
    {
        "track_id": 93, "position_min": 6, "position_max": 12,
        "tips": [
            "Learn the reroute each lap — plaza and park segments swap around.",
            "Cut the riverside shortcut when the layout opens it.",
            "Save an item for the tight plaza corners where passes stick.",
        ],
    },
    {
        "track_id": 94, "position_min": 4, "position_max": 10,
        "tips": [
            "Feather the throttle on the ice — full power just skates you wide.",
            "Take the crystal cavern line tight to hold speed through it.",
            "Dodge the penguins wide rather than braking on the slick slopes.",
        ],
    },
    {
        "track_id": 95, "position_min": 5, "position_max": 11,
        "tips": [
            "Time the Thwomps so they rise as you reach the tight brick corners.",
            "Take the jump gaps over the floor straight for a clean landing.",
            "Precision beats aggression in the narrow maze — clip a wall and you stall.",
        ],
    },
    {
        "track_id": 96, "position_min": 3, "position_max": 9,
        "tips": [
            "Ride the half-pipe walls high to carry speed through the loops.",
            "Take the long glider stretches straight and steady over the void.",
            "Keep an item back to defend the anti-grav corners on the final run.",
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
    print("All 96 Mario Kart 8 Deluxe tracks and strategies seeded successfully.")
finally:
    db.close()
