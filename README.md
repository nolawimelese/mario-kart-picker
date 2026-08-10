# MKPicker

A web app that recommends which track to vote for in Mario Kart 8 Deluxe based on your finishing position in the last race and the three tracks up for vote.

## How It Works

1. Enter your finishing position from the last race
2. Enter the three available tracks to vote on
3. Get a recommendation based on optimal starting grid position and race conditions for each track

## Tech Stack

**Frontend:** React, Vite, TanStack Query

**Backend:** FastAPI, Uvicorn, Pydantic

- REST API with typed request/response validation

**Database:** SQLite

## Roadmap

<details>
<summary>Development</summary>

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
<summary>Post-Deployment</summary>

> <details>
> <summary>Settings</summary>
>
> - [x] add settings panel
>   - [ ] add dark mode
>     - [ ] add dark mode palette
>     - [ ] add switch in panel
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
