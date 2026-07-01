# MKPicker

A web app that recommends which track to vote for in Mario Kart World based on your finishing position in the last race and the three tracks up for vote.

## How It Works

1. Enter your finishing position from the last race
2. Enter the three available tracks to vote on
3. Get a recommendation based on optimal starting grid position and race conditions for each track

## Tech Stack

**Frontend:** React, TypeScript, Vite

**Backend:** FastAPI, Pydantic, Uvicorn

- REST API with typed request/response validation

**Database:** SQLite

## Roadmap

- Develop Components
  - Browse Tab
    - [x] UI
    - [ ] Seed track table with information contained on each track card
    - [ ] Remove template cards, link backend so cards contain real information
    - [ ] Add icons for cup, and dlc status
  - Track Picker (flagship feature)
    - [ ] UI
    - [ ] Seed strategies table
    - [ ] Develop rule based algo
    - [ ] Pre racing tips & tricks page
  - Kart combo previewer
    - TBD
