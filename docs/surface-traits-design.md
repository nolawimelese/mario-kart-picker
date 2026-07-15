# Design: Track Surface Classification and the Kart-Kombo Bridge

Status: proposed (no code written yet)
Scope: how a track's dominant surface should be classified and feed the future kart-combo
scoring layer.

## Motivation

A track's dominant surface is more *defining* than the other traits, and it's the natural join
point to kart kombos. That maps onto the game's own data: a MK8DX kart doesn't have one speed
stat, it has **Ground / Water / Air / Anti-Gravity** speed (and handling). Water, Anti-grav, and
Glider are three of the four surface axes every kart is rated on — so a track's surface is the
key that joins a *track* to a *combo*.

## The model

Each track is classified as **predominantly one** of:

- **Water**     -> the kart's Water stats
- **Anti-grav** -> the kart's Anti-Gravity stats
- **Glider**    -> the kart's Air stats
- **None**      -> no surface bonus (Ground baseline)

This is a single, mutually-exclusive classification, not a set of per-surface booleans. The
"predominantly" judgment is doing the coverage work up front: a track that's mostly water is
`Water`; a track with one glider ramp is not `Glider`.

## Scoring

The classification selects which kart stat contributes; the kart's stat in that surface supplies
the magnitude:

```
surface_bonus = kart_stat[ track.dominant_surface ]   # 0 when None
score = band_fit(...) + surface_weight * normalized(surface_bonus)
```

So a water-classified track rewards a combo with strong Water stats, a glider-classified track
rewards strong Air stats, and so on. A `None` track adds nothing and ranks on band fit alone.

### Why it discriminates between tracks correctly

Fixed kart, candidate tracks classified differently:

- Track A: **Water**     -> + kart.water_stat
- Track B: **Anti-grav** -> + kart.antigrav_stat
- Track C: **Glider**    -> + kart.air_stat
- Track D: **None**      -> + 0

Each track pulls a different stat off the same kart, so the ranking reflects that kart's
strengths: a strong-Air / weak-Anti-grav combo ranks the glider track above the anti-grav track.

## Two tiers — keep this separate from the chaos leans

The current `TRAIT_LEAN` model (`backend/recommender.py`) scores traits on a single
front-favoring <-> back-favoring axis, which is right for **chaos/layout traits** (Shortcuts,
Rerouting, Hazards, Coins, City). Surface is a *different axis* — it has no inherent front/back
directionality, which is why Water/Glider sit at `0.0` there today. Surface classification should
feed the kart-combo layer, not `TRAIT_LEAN`.

`terrain` (`backend/models.py`) already sets the precedent: a separate field, display-only for
now, staged to feed the recommender once kart-combo stats exist. The surface classification is the
same class of thing and sits alongside it.

## One thing that decides whether it behaves

**Scale it, or it swamps band fit.** `band_fit` produces ~0-1; MK8DX surface stats run roughly
1-6. Adding a raw kart stat would drown the position-band signal (currently the primary driver).
Normalize the surface bonus (e.g. to 0-1) and put it behind its own weight, the way
`TRAIT_BONUS_WEIGHT` keeps leans subordinate. Decide deliberately how loud the surface term is
relative to band fit.

## Display

The classification can render as a chip on the card (e.g. a "Water" / "Anti-grav" / "Glider"
badge; nothing for `None`), so it's visible without changing the existing trait chips.

## Open decisions

- Where the classification lives: a new `dominant_surface` field on `Track`, or derived from
  existing data.
- Normalization range and weight for the surface term relative to band fit.
- How to classify genuinely mixed tracks (the `None` vs. a weak-majority surface call).
- Where kart per-surface stats live (new table? seed data?) once kart kombos land.
