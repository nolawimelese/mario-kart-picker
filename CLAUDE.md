# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

MKPicker recommends which track to vote for in Mario Kart 8 Deluxe based on your finishing
position in the last race and the three tracks up for vote. The flagship feature is the Track
Picker (rule-based recommender); a Browse tab lists tracks. See `README.md` for the roadmap.

## Commands

### Backend (`backend/`, FastAPI + SQLAlchemy + SQLite)
```bash
cd backend
pip install -r requirements.txt
python seed.py          # create + seed mariokart.db (required before first run; DB is gitignored)
uvicorn main:app --reload   # serves on http://localhost:8000
```

### Frontend (`frontend/`, React 19 + Vite + TanStack Query)
```bash
cd frontend
npm install
npm run dev       # Vite dev server on http://localhost:5173
npm run build     # tsc -b && vite build (type-check is part of the build)
npm run lint      # eslint
```

There is no test suite in this repo.

## Architecture

Two independent apps talking over a REST API.

**Backend request flow:** `main.py` defines two endpoints — `GET /tracks` and `POST /recommend`.
The scoring logic lives entirely in `recommender.py`; `main.py` only validates input, loads
tracks (with their strategies) from the DB, calls `score_track`, sorts, and flags the top result
as `recommended`. `database.py` holds the SQLite engine/session; `models.py` defines the two
tables; `seed.py` is the sole source of track/strategy data and is idempotent (skips rows that
already exist).

**The recommender (`recommender.py`)** is the heart of the app. A track's score = a graded
position-band fit plus a small trait adjustment:
- Each `Strategy` targets a starting-grid band `[position_min, position_max]` on a fixed 12-kart
  grid (`FIELD_SIZE = 12`, 1 = pole). `band_fit` returns 1.0 inside the band and decays linearly
  to 0 over `FALLOFF` positions outside it. A track can have multiple strategies (e.g. a front
  "defend" band and a back "gamble" band); `score_track` picks the best-fitting one.
- `trait_adjust` nudges the score using `TRAIT_LEAN` (per-trait bias in [-1, +1]: negative favors
  the front, positive favors the back), weighted by `TRAIT_BONUS_WEIGHT` so traits break ties but
  never override band fit. Tuning the recommender means editing these constants and the seed data.

**Data model:** `Track` (name, cup, laps, header_color, `traits` as JSON, `dlc`) has a one-to-many
`strategies` relationship to `Strategy` (name, position band, `tips` as JSON). Traits double as
both display chips and recommender inputs, so the `TRAIT_LEAN` keys must match trait strings used
in `seed.py`.

**API contract / naming:** The backend serializes with a camelCase alias generator
(`to_camel`), so Python snake_case fields cross the wire as camelCase (`header_color` →
`headerColor`). The frontend `Track` interface in `frontend/src/api/tracks.ts` must stay in sync
with backend `TrackOut`.

**Frontend structure:** `App.tsx` toggles between a `Splash` screen and `Home`. `Home` renders
`TopNav` plus the active tab — `Browse` is live; the Course Picker (Track Picker UI) is still a
placeholder. API calls go through `frontend/src/api/tracks.ts`. The dev server proxies `/api/*` to
`http://localhost:8000` (see `vite.config.ts`), stripping the `/api` prefix; `VITE_API_URL`
overrides the base. CORS on the backend only allows `http://localhost:5173`.

**Design system (`frontend/src/design-system/`)** is a self-contained component library exported
through one barrel (`index.ts`) — import UI from `./design-system`, not from individual files.
Design tokens (colors, spacing, fonts, etc.) are CSS custom properties under `tokens/`; components
and seed data reference colors via `var(--...)` (e.g. `header_color: "var(--boost-500)"`), so
color values live in CSS, not in TS/Python.
