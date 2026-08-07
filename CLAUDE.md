# CLAUDE.md

## Project

MKPicker recommends which track to vote for in Mario Kart 8 Deluxe based on your finishing
position in the last race and the three tracks up for vote. The flagship feature is the Track
Picker (rule-based recommender); a Browse tab lists tracks. See `README.md` for the roadmap.

## Workflow

Always consult Context7 for a package's docs before implementing against it, at the version this
repo pins — backend versions in `backend/requirements.txt`, frontend versions in
`frontend/package.json`.

## Commands

### Backend (`backend/`, FastAPI + SQLAlchemy + SQLite)

```bash
cd backend
pip install -r requirements.txt
python seed_all.py      # create + seed mariokart.db with all 96 tracks (required before first run; DB is checked into the repo)
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

**Backend request flow:** `main.py` defines `GET /` and `GET /health` (both trivial
`{"status": "ok"}` checks), `GET /tracks` (every track, without its strategies), and
`POST /recommend`. The scoring logic lives entirely in `recommender.py`; `main.py` only
validates input, loads tracks (with their
strategies) from the DB, calls `score_track`, sorts, and flags the top result as `recommended`.
`database.py` holds the SQLite engine/session; `models.py` defines the two tables; `seed_all.py`
is the canonical source of track/strategy data — the full 96-course, 24-cup catalog — and is
idempotent (tracks matched by id, strategies by `track_id` + band).

Always seed a fresh DB with `seed_all.py` alone.

**The recommender (`recommender.py`)** is the heart of the app. A track's score = a graded
position-band fit plus a small trait adjustment:

- Each `Strategy` targets a starting-grid band `[position_min, position_max]` on a fixed 12-kart
  grid (`FIELD_SIZE = 12`, 1 = pole). `band_fit` returns 1.0 inside the band and decays linearly
  to 0 over `FALLOFF` positions outside it. A track can have multiple strategies (e.g. a front
  "defend" band and a back "gamble" band) and `score_track` picks the best-fitting one, but that
  is the exception: 93 of the 96 seeded tracks carry a single band, only 3 carry two. Every
  seeded track has at least one, so `score_track`'s "no strategy defined" fallback only fires
  against a partially seeded DB.
- `trait_adjust` nudges the score using `TRAIT_LEAN` (per-trait bias in [-1, +1]: negative favors
  the front, positive favors the back), weighted by `TRAIT_BONUS_WEIGHT` so traits break ties but
  never override band fit. Tuning the recommender means editing these constants and the seed data.
- The raw score is normalized by `MAX_RAW_SCORE` (best band fit + strongest possible trait bonus)
  so scores land in [0, 1]; the frontend renders them as a 0–100 pick score.

**Data model:** `Track` (name, cup, laps, header_color, description, terrain, `traits` as JSON,
`dlc`) has a one-to-many `strategies` relationship to `Strategy` (position band, `tips` as JSON).
`terrain` is the MK8DX slippery off-road classification — `"None"`, `"Sand"`, or `"Ice"` — and is
**display-only today**: it drives the Browse badge and terrain filter but is not read by
`score_track`.

**Trait strings are a three-way invariant.** The same nine trait strings must agree across the
seed data in `seed_all.py`, the `TRAIT_LEAN` keys in `recommender.py`, and `ALL_TRAITS` in
`frontend/src/Browse.tsx`. A trait missing from `TRAIT_LEAN` silently scores 0; one missing from
`ALL_TRAITS` is invisible in the Browse filter. Adding or renaming a trait means editing all
three.

**API contract / naming:** The backend serializes with a camelCase alias generator
(`to_camel`), so Python snake_case fields cross the wire as camelCase (`header_color` →
`headerColor`). The frontend `Track` interface in `frontend/src/api/tracks.ts` must stay in sync
with backend `TrackOut`.

**Frontend structure:** `App.tsx` toggles between a `Splash` screen and `Home`. `Home` renders
`TopNav` plus the active tab — `Browse` and `CoursePicker` are both live. API calls go through
`frontend/src/api/` (`tracks.ts` for `GET /tracks`, `recommend.ts` for `POST /recommend`).

- **`CoursePicker.tsx`** is a four-phase state machine (`Phase`): `input` (pick a finishing
  position, search-and-add 3 ballot tracks) → `loading` (arcade spin held for at least
  `MIN_SPIN_MS` even if the API returns sooner) → `ranked` (top pick plus runners-up, scores
  rendered 0–100 via `pickScore`) → `tips`. The `tips` phase is reached only through the "which
  track won?" `Dialog`: the lobby's actual winner may not be our top pick, so the user logs it
  and gets that track's `strategyTips`. This is what the README roadmap calls the "pre racing
  tips & tricks page" — it's a phase of the picker, not a separate tab. The `input` phase surfaces
  a fetch-failure hint (`isError` off the `tracks` query) so a downed backend fails visibly
  instead of leaving the ballot search silently empty.
- **`Browse.tsx`** filters the catalog client-side: name-only search plus terrain and trait tags,
  all ANDed. Terrain options are derived from the loaded catalog at runtime (so new sandy/icy
  tracks self-register) with `"None"` dropped.

The dev server proxies `/api/*` to `http://localhost:8000` (see `vite.config.ts`), stripping the
`/api` prefix; `VITE_API_URL` overrides the base. CORS on the backend reads its allowlist from
the `ALLOWED_ORIGINS` env var (comma-separated, defaults to `http://localhost:5173`) — set it to
the deployed frontend origin(s) in production.

**Design system (`frontend/src/design-system/`)** is a self-contained component library exported
through one barrel (`index.ts`) — import UI from `./design-system`, not from individual files.
Design tokens (colors, spacing, fonts, etc.) are CSS custom properties under `tokens/`; components
and seed data reference colors via `var(--...)` (e.g. `header_color: "var(--boost-500)"`), so
color values live in CSS, not in TS/Python.

**Design notes:** `docs/surface-traits-design.md` proposes classifying each track by a dominant
surface (Water / Anti-grav / Glider / None) to feed a future kart-combo scoring layer, kept
deliberately separate from the front/back `TRAIT_LEAN` axis. It is **proposed only — no code
written**; read it before reworking the recommender, but don't treat it as describing today's
behavior.
