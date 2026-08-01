'''
Rule-based track scoring for the Track Picker.

Given the player's starting grid position (0-12), score how good a candidate track 
is to vote for. The score is a graded position-band fit adjusted by a small trait 
bonus.
'''

from dataclasses import dataclass

# Fixed 12-kart grid: position runs 1 (pole) .. 12 (back).
FIELD_SIZE = 12
# Positions of linear decay outside a strategy's band before its fit hits 0.
FALLOFF = 4
# Keeps the trait adjustment subordinate to the band fit (tie-breaker, not driver).
TRAIT_BONUS_WEIGHT = 0.15

# Per-trait lean in [-1, +1]: negative favors the front (reward a controlled
# lead), positive favors the back (chaos / catch-up potential). Tunable.
TRAIT_LEAN = {
    "Shortcuts": 0.8,
    "Rerouting": 0.7,
    "Hazards": 0.6,
    "City": 0.3,
    "Glider": 0.0,
    "Water": 0.0,
    "Cave": 0.0,
    "Anti-grav": -0.2,
    "Coins": -0.5,
}

# Strongest possible per-track net lean: every same-signed trait stacked together.
_MAX_NET_LEAN = max(
    sum(w for w in TRAIT_LEAN.values() if w > 0),
    -sum(w for w in TRAIT_LEAN.values() if w < 0),
)
# Highest raw score: perfect band fit plus the strongest possible trait bonus
# (|back_bias - 0.5| maxes out at 0.5). Used to normalize scores into [0, 1].
MAX_RAW_SCORE = 1.0 + TRAIT_BONUS_WEIGHT * 0.5 * _MAX_NET_LEAN


@dataclass
class ScoreResult:
    score: float
    strategy_tips: list[str]
    base: float
    adjust: float
    reason: str


def band_fit(position, strategy):
    '''
    Graded membership of ``position`` in a strategy's [min, max] band.
    '''
    if strategy.position_min <= position <= strategy.position_max:
        return 1.0
    if position < strategy.position_min:
        distance = strategy.position_min - position
    else:
        distance = position - strategy.position_max
    return max(0.0, 1.0 - distance / FALLOFF)


def net_lean(track):
    '''Signed sum of a track's trait leans: negative favors the front, positive
    the back. Which way a track leans is a property of the track alone.'''
    return sum(TRAIT_LEAN.get(t, 0.0) for t in (track.traits or []))


def trait_adjust(track, position):
    '''Signed nudge: positive when a back-favoring track meets a back-of-grid
    position (and symmetrically for front-favoring tracks up front).'''
    back_bias = (position - 1) / (FIELD_SIZE - 1)  # 0.0 at P1 -> 1.0 at P12
    return net_lean(track) * (back_bias - 0.5)


def _dominant_traits(track, lean):
    '''Traits driving the track's net ``lean``, strongest first, for the reason.'''
    leaning = [(t, TRAIT_LEAN.get(t, 0.0)) for t in (track.traits or [])]
    # Only traits pulling the same way as the net lean: the reason applies one
    # direction label to whatever this returns, so a counter-leaning trait
    # listed here would be described backwards.
    leaning = [(t, w) for t, w in leaning if w != 0.0 and (w > 0) == (lean > 0)]
    leaning.sort(key=lambda tw: abs(tw[1]), reverse=True)
    return [t for t, _ in leaning[:2]]


def score_track(track, position):
    '''Score a candidate ``track`` for a starting ``position`` (1..12).'''
    strategies = list(track.strategies)
    if not strategies:
        return ScoreResult(
            score=0.0,
            strategy_tips=[],
            base=0.0,
            adjust=0.0,
            reason="No strategy is defined for this track yet.",
        )

    best = max(strategies, key=lambda s: band_fit(position, s))
    base = band_fit(position, best)
    adjust = trait_adjust(track, position)
    raw = base + TRAIT_BONUS_WEIGHT * adjust
    score = max(0.0, raw) / MAX_RAW_SCORE

    reason = (
        f"Suits starts from P{best.position_min}-P{best.position_max} "
        f"(you're on P{position})."
    )
    # Which way the traits lean comes from the track (`lean`); whether that
    # helps comes from the track *and* the position (`adjust`). Reading the
    # direction off `adjust` inverts it for every front-half start.
    lean = net_lean(track)
    dominant = _dominant_traits(track, lean) if lean else []
    if dominant:
        direction = "back-of-grid" if lean > 0 else "front-running"
        verb = "favor" if len(dominant) > 1 else "favors"
        fit = (
            "which suits your spot on the grid"
            if adjust > 0
            else "which is less of an edge from your spot"
        )
        reason += f" Its {', '.join(dominant)} {verb} {direction} play, {fit}."

    return ScoreResult(
        score=score,
        strategy_tips=best.tips or [],
        base=base,
        adjust=adjust,
        reason=reason,
    )
