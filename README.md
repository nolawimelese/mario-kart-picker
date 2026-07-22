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

- Develop Components
  - Browse Tab
    - [x] UI
    - [x] Seed track table with information contained on each track card
    - [x] Remove template cards, link backend so cards contain real information
      - mushroom cup only is in right now, after testing, full list will go in
    - [x] Add dlc status
    - [x] Seed the remaining tracks
      - all 24 cups / 96 courses via `seed_all.py`; also fills out the terrain filter with real Sand/Ice grades
  - Track Picker (flagship feature)
    - [x] UI
    - [x] Seed strategies table
      - with demo tracks so far
    - [x] Develop rule based algo
      - [x] weigh in track traits to break ties
    - [x] Pre racing tips & tricks page
