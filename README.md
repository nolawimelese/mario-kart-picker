<div align="center">

<img src=".github/assets/logo.svg" alt="MK Picker" width="100%">

<img src=".github/assets/track.svg" alt="Three karts lapping an oval race track" width="100%">

<br>

**Finish the race, read the ballot, and MKPicker tells you which of the three tracks to vote for — tuned to where you just placed in Mario Kart 8 Deluxe.**

<br>

<table align="center">
  <tr>
    <td align="right"><b>🎮 Frontend</b></td>
    <td>
      <img alt="React 19" src="https://img.shields.io/badge/React-19-2e7df6?style=for-the-badge&logo=react&logoColor=white">
      <img alt="TypeScript 6" src="https://img.shields.io/badge/TypeScript-6-1763d8?style=for-the-badge&logo=typescript&logoColor=white">
      <img alt="Vite 8" src="https://img.shields.io/badge/Vite-8-ffc42e?style=for-the-badge&logo=vite&logoColor=161320">
      <img alt="TanStack Query 5" src="https://img.shields.io/badge/TanStack%20Query-5-ff3b5c?style=for-the-badge&logo=reactquery&logoColor=white">
      <img alt="ESLint 10" src="https://img.shields.io/badge/ESLint-10-ff6a1a?style=for-the-badge&logo=eslint&logoColor=white">
    </td>
  </tr>
  <tr>
    <td align="right"><b>⚙️ Backend</b></td>
    <td>
      <img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-2e7df6?style=for-the-badge&logo=python&logoColor=white">
      <img alt="FastAPI 0.139" src="https://img.shields.io/badge/FastAPI-0.139-18c964?style=for-the-badge&logo=fastapi&logoColor=white">
      <img alt="Pydantic 2.13" src="https://img.shields.io/badge/Pydantic-2.13-ff3b5c?style=for-the-badge&logo=pydantic&logoColor=white">
      <img alt="SQLAlchemy 2.0" src="https://img.shields.io/badge/SQLAlchemy-2.0-ff6a1a?style=for-the-badge&logo=sqlalchemy&logoColor=white">
      <img alt="SQLite" src="https://img.shields.io/badge/SQLite-1763d8?style=for-the-badge&logo=sqlite&logoColor=white">
      <img alt="Uvicorn 0.51" src="https://img.shields.io/badge/Uvicorn-0.51-ffc42e?style=for-the-badge&logoColor=161320">
      <img alt="slowapi 0.1.10" src="https://img.shields.io/badge/slowapi-0.1.10-ff3b5c?style=for-the-badge">
    </td>
  </tr>
  <tr>
    <td align="right"><b>🚀 Hosting</b></td>
    <td>
      <img alt="Netlify" src="https://img.shields.io/badge/Netlify-frontend-2e7df6?style=for-the-badge&logo=netlify&logoColor=white">
      <img alt="Render" src="https://img.shields.io/badge/Render-backend-ff6a1a?style=for-the-badge&logo=render&logoColor=white">
    </td>
  </tr>
</table>

</div>

<img src=".github/assets/divider.svg" alt="" width="100%">

## 🏁 The Race Briefing

Every online lobby runs the same loop: race, vote on the next track, race again. MKPicker sits
in the gap between those two steps. It treats your **finishing position** from the last race as
your spot on the **next starting grid** (1 = pole, 12 = the back of a 12-kart field) and ranks
the three tracks on the ballot by how well each one plays from there.

| | Lap | What happens |
|:-:|:--|:--|
| 🏎️ | **Where did you finish?** | Pick P1 through P12. |
| 🗳️ | **What's on the ballot?** | Search-and-add the three tracks from any of the 96 courses. |
| 🏆 | **Get the verdict** | A recommended pick with a 0–100 pick score, the runners-up, and a plain-English reason for each. |
| 📻 | **Log the winner** | The lobby doesn't always vote your way — tell MKPicker which track actually won and get that track's pre-race tips. |

Two tabs live in the app:

- **Track Picker** — the flagship. A four-phase flow: `input` → `loading` (an arcade spin that
  holds for at least 1.4 s, even when the API is faster) → `ranked` → `tips`.
- **Browse** — the full catalog of 96 courses across 24 cups, filterable by name, terrain
  (Sand / Ice) and trait tags, with a DLC pill on the 48 Booster Course Pass tracks.

Plus a settings panel with **dark mode**, and a footer that discloses exactly how much data the
app collects about you: none.

<img src=".github/assets/divider.svg" alt="" width="100%">

## 🧠 Under the Hood — How the Pick Is Made

The recommender (`backend/recommender.py`) is rule-based, not learned. A track's score is a
**graded position-band fit** plus a **small trait adjustment**:

```text
fit    = band_fit(position, best_strategy)      # 1.0 inside the band; −0.25 per position outside; floor 0
lean   = Σ TRAIT_LEAN[trait]                    # < 0 = a front-runner's track, > 0 = a chaos track
adjust = lean × ((position − 1) / 11 − 0.5)     # −0.5 at P1 … +0.5 at P12
score  = max(0, fit + 0.15 × adjust) / MAX_RAW_SCORE   # normalized to 0–1, shown as 0–100
```

**🎯 Band fit.** Every track carries at least one `Strategy` with a starting-grid band
`[position_min, position_max]`. Inside the band the fit is a perfect `1.0`; outside it decays
linearly to `0` over `FALLOFF = 4` positions. A track can carry more than one band (a front
"defend" plan and a back "gamble" plan) and the best-fitting one wins — 93 of the 96 tracks have
a single band, 3 have two.

**🍄 Trait lean.** Each track is tagged with traits, and each trait leans toward the front or the
back of the grid. The signed sum is the track's *lean*; it's multiplied by how far back you're
starting, so a chaos track scores higher from P12 and a clean-lines track scores higher from P1.
`TRAIT_BONUS_WEIGHT = 0.15` keeps this subordinate to band fit — traits break ties, they never
override the band.

| Trait | Lean | Reads as |
|:--|--:|:--|
| Shortcuts | `+0.8` | back-of-grid — catch-up potential |
| Rerouting | `+0.7` | back-of-grid |
| Hazards | `+0.6` | back-of-grid — chaos |
| City | `+0.3` | back-of-grid |
| Glider · Water · Cave | `0.0` | neutral |
| Anti-grav | `−0.2` | front-running |
| Coins | `−0.5` | front-running — reward a controlled lead |

Tuning the recommender means editing these constants and the seed data.

<img src=".github/assets/divider.svg" alt="" width="100%">

## 🚦 Start Your Engines

MKPicker is two independent apps talking over a REST API. Run them in two terminals.

**You'll need:** [Node.js](https://nodejs.org/) (with npm) and **Python 3.10+**.

### ⚙️ Pit crew, backend side

```bash
cd backend
python -m venv .venv                 # optional — .vscode/settings.json expects it here
# Windows:  .venv\Scripts\activate       macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
python seed_all.py                   # creates + seeds mariokart.db with all 96 tracks (idempotent, safe to re-run)
uvicorn main:app --reload            # → http://localhost:8000
```

The seeded `mariokart.db` ships with the repo, so the seed step is a safety net rather than a
requirement — but `seed_all.py` is the canonical source of track and strategy data, so run it
anyway. Sanity check: `curl http://localhost:8000/health` → `{"status":"ok"}`.

### 🎮 Pit crew, frontend side

```bash
cd frontend
npm install
npm run dev                          # → http://localhost:5173
```

The Vite dev server proxies `/api/*` to `http://localhost:8000` and strips the `/api` prefix
(see `vite.config.ts`), so no CORS setup is needed locally.

| Command | Does |
|:--|:--|
| `npm run dev` | Vite dev server with HMR |
| `npm run build` | `tsc -b && vite build` — type-checking is part of the build |
| `npm run lint` | ESLint |
| `npm run preview` | Serve the production build locally |

### 🟢 Green light

Open **http://localhost:5173**, clear the splash screen, and you're on the Track Picker.

> There is no test suite in this repo. `npm run build` (type-check) and `npm run lint` are the
> gates.

<img src=".github/assets/divider.svg" alt="" width="100%">

## 🎛️ Tuning Knobs

| Variable | Side | Default | What it does |
|:--|:-:|:--|:--|
| `ALLOWED_ORIGINS` | backend | `http://localhost:5173` | Comma-separated CORS allowlist. Set it to the deployed frontend origin(s). |
| `ALLOWED_ORIGIN_REGEX` | backend | *(unset)* | Regex for origins you can't list ahead of time, e.g. Netlify deploy previews. **Escape literal dots** (`netlify\.app`) — the pattern is validated, and one with a bare `.` or that won't compile is dropped with a warning instead of applied. |
| `VITE_API_URL` | frontend | `/api` | Base URL for API calls. Point it at the backend's public URL in production. |

<img src=".github/assets/divider.svg" alt="" width="100%">

## 📡 Pit Radio — The API

Field names cross the wire in **camelCase** (`header_color` → `headerColor`); the backend
serializes with a Pydantic alias generator and accepts either spelling on input.

| Method | Route | Rate limit | Returns |
|:-:|:--|:-:|:--|
| `GET` | `/` | — | `{"status": "ok"}` |
| `GET` | `/health` | — | `{"status": "ok"}` — Render's health check, deliberately never throttled |
| `GET` | `/tracks` | 60/min | Every track (without its strategies). Served from a per-process snapshot with an `ETag` and `Cache-Control: public, max-age=3600`; a matching `If-None-Match` gets a `304`. |
| `POST` | `/recommend` | 30/min | The ballot, ranked best-first, with the top result flagged `recommended` |

Rate limits are per client IP (left-most `X-Forwarded-For` entry, so a proxy doesn't put every
caller in one bucket). Request bodies over 8 KB are refused with a `413` before they're read.

### `POST /recommend`

```jsonc
// request — position 1..12, one to three track ids
{ "position": 9, "trackIds": [1, 2, 3] }
```

```jsonc
// response — real output for the request above
[
  {
    "trackId": 3,
    "name": "Sweet Sweet Canyon",
    "score": 0.8706,
    "strategyTips": [
      "Break the chocolate wall shortcut every lap — it's worth the risk from the back.",
      "Carry a mushroom to cut the soda-lake corner.",
      "Line up the stained-glass glider launch for a clean landing."
    ],
    "reason": "Suits starts from P7-P12 (you're on P9). Its Shortcuts favors back-of-grid play, which suits your spot on the grid.",
    "recommended": true
  },
  { "trackId": 2, "name": "Water Park", "score": 0.6298, "recommended": false, /* … */ },
  { "trackId": 1, "name": "Mario Kart Stadium", "score": 0.0, "recommended": false, /* … */ }
]
```

An unknown id returns `404 {"detail": "unknown track ids: [999]"}`; a position outside 1–12 or
more than three ids is a `422`.

<img src=".github/assets/divider.svg" alt="" width="100%">

## 🗺️ Course Data — The Data Model

Two SQLite tables (`backend/models.py`), one-to-many, seeded by `backend/seed_all.py`:

**`tracks`** — one row per course

| Column | Type | Notes |
|:--|:--|:--|
| `id` | int | Primary key; ids 1–48 are base game, 49–96 are DLC |
| `name`, `cup` | str | e.g. `Sweet Sweet Canyon`, `Mushroom Cup` |
| `laps` | int | |
| `header_color` | str | A design-token reference like `var(--boost-500)` — colors live in CSS, not in Python |
| `description` | str | The flavor blurb on the Browse card |
| `terrain` | str | Slippery off-road class: `"None"`, `"Sand"` or `"Ice"`. Drives the Browse badge and filter only — the recommender doesn't read it (yet) |
| `traits` | JSON list | Tags from the nine-trait vocabulary above |
| `dlc` | bool | Booster Course Pass track — shows the DLC pill |

**`strategies`** — one or two rows per track

| Column | Type | Notes |
|:--|:--|:--|
| `track_id` | FK → `tracks.id` | |
| `position_min`, `position_max` | int | The starting-grid band this plan is built for |
| `tips` | JSON list | The short, actionable tips shown on the `tips` screen |

> **🔩 Contributor note — the trait strings are a three-way invariant.** The same nine names must
> agree across the seed data (`seed_all.py`), `TRAIT_LEAN` in `recommender.py`, and `ALL_TRAITS`
> in `frontend/src/Browse.tsx`. A trait missing from `TRAIT_LEAN` silently scores `0`; one
> missing from `ALL_TRAITS` disappears from the Browse filter. Adding or renaming a trait means
> editing all three. Likewise the frontend `Track` interface (`frontend/src/api/tracks.ts`) must
> mirror the backend `TrackOut` model.

<img src=".github/assets/divider.svg" alt="" width="100%">

## 🔧 Pit Stop

| Symptom | Cause | Fix |
|:--|:--|:--|
| Re-seeded, but the app still shows the old catalog | `/tracks` is served from a snapshot built once per process, and the browser caches it for an hour | Restart `uvicorn`, then **hard-refresh** the browser |
| Ballot search is empty / the picker shows a "couldn't load tracks" hint | The backend isn't running, or isn't on port 8000 | Start it — the input phase surfaces the fetch error on purpose so a downed backend fails visibly |
| `429 Too Many Requests` | Per-IP rate limit (`/tracks` 60/min, `/recommend` 30/min) | Wait a minute; both budgets are in-memory and reset with the process |
| Browser reports an opaque CORS failure in production | The frontend origin isn't in `ALLOWED_ORIGINS`, or `ALLOWED_ORIGIN_REGEX` was dropped for an unescaped `.` | Check the backend logs for the `Ignoring ALLOWED_ORIGIN_REGEX` warning and fix the value |
| `404 unknown track ids` | An id that isn't in the DB | Ids run 1–96; reseed if the DB is partial |

<img src=".github/assets/divider.svg" alt="" width="100%">

## 🚀 Race Day — Deployment

- **Frontend → Netlify.** Build with `VITE_API_URL` set to the backend's public URL.
  `frontend/public/_headers` ships the security headers, including a Content-Security-Policy
  whose `connect-src` must name the backend origin.
- **Backend → Render** as a web service. The build command runs `seed_all.py`, so the catalog is
  rebuilt before each process starts. Set `ALLOWED_ORIGINS` to the Netlify origin and, for deploy
  previews, `ALLOWED_ORIGIN_REGEX` to something like
  `https://deploy-preview-\d+--<site>\.netlify\.app`.
- **Database.** `backend/mariokart.db` is checked in and travels with the backend.

<img src=".github/assets/divider.svg" alt="" width="100%">

## 🏆 Grand Prix Standings — Roadmap

<details>
<summary><b>🏁 Cup 1 — Development</b> (complete)</summary>

> <details>
> <summary>Browse Tab</summary>
>
> - [x] UI
> - [x] Seed track table with information contained on each track card
> - [x] Remove template cards, link backend so cards contain real information
>   - mushroom cup only is in right now, after testing, full list will go in
> - [x] Add dlc status
> - [x] Seed the remaining tracks
>   - all 24 cups / 96 courses via `seed_all.py`; also fills out the terrain filter with real Sand/Ice grades
>
> </details>

> <details>
> <summary>Track Picker</summary>
>
> - [x] UI
> - [x] Seed strategies table
>   - with demo tracks so far
> - [x] Develop rule based algo
>   - [x] weigh in track traits to break ties
> - [x] Pre racing tips & tricks page
>
> </details>

> <details>
> <summary>Deployment</summary>
>
> - [x] finalize app
>   - [x] delete unused files
> - [x] fix lint errors
> - [x] remove ngrok from vite config
> - [x] add health check endpoint
> - [x] research deployment options
> - [x] make CORS origins configurable (`ALLOWED_ORIGINS` env var) for a deployed frontend host
> - [x] ship the seeded database with the repo instead of gitignoring it
> - [x] deploy backend and frontend
> - [x] make deployment adjustments
>
> </details>

</details>

<details>
<summary><b>⭐ Cup 2 — Post-Deployment</b> (in progress)</summary>

> <details>
> <summary>Settings</summary>
>
> - [x] add settings panel
>   - [x] add dark mode
>     - [x] add dark mode palette
>     - [x] add switch in panel
>
> </details>

> <details>
> <summary>Footer</summary>
>
> - [x] add footer
>   - [x] data collection disclosure (or lack of)
>
> </details>

> <details>
> <summary>Mobile</summary>
>
> - [ ] add mobile portrait mode support
>   - (WIP)
>
> </details>

</details>

<img src=".github/assets/divider.svg" alt="" width="100%">

<div align="center">

**🎌 Fine print.** MKPicker is a fan-made project and is not affiliated with or endorsed by
Nintendo. Mario Kart, course names and cup names are trademarks of Nintendo, used here only to
identify the tracks. No Nintendo artwork or assets are included — just the colors and the energy.

</div>
