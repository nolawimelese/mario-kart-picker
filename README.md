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

- [ ] Design database schema
- [ ] Seed database with track data and optimal strategies
- [ ] Rule-based recommendation engine
- [ ] Frontend UI

### Prerequisites

- Node.js
- Python 3
