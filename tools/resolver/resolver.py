"""
The Deep Salts — deterministic combat resolver.

Pure arithmetic for the parts of ruleset v9.4 that shouldn't be eyeballed
mid-session: ESV/weapon damage, Accuracy Tier multipliers, limb stagger/
sever, the Insanity/Influence save DC, Insight tiers, and the tick/track
status maths (Bleeding, Corrosion, Stone Skin, Crust, Fervour).

Source of truth is deep-salts-v9.4.md, not this file. Section references
below (§4, §5, §9, §10, §11) point at that document. If a ruleset numeric
change lands, update this file in the same commit — a stale script is
worse than an LLM DM, because the LLM at least re-reads the current file.

Per-monster limb multipliers/thresholds are almost always overridden on
that monster's own template — the STANDARD_HUMANOID_LIMBS table here is
the documented fallback only (from monster-pass-instructions.md), never
a substitute for pulling the actual statblock.
"""

import math

# ---------------------------------------------------------------------------
# §4 — Effective Scaling Value (soft caps) and weapon damage
# ---------------------------------------------------------------------------

ESV_BRACKETS = [
    (20, 1.0),   # 1-20
    (20, 0.85),  # 21-40
    (20, 0.65),  # 41-60
    (20, 0.5),   # 61-80
    (19, 0.3),   # 81-99
]

GRADE_MULTIPLIERS = {"E": 0.3, "D": 0.5, "C": 0.7, "B": 0.9, "A": 1.1, "S": 1.3}


def esv(score):
    """Cumulative soft-cap conversion of a raw attribute score to ESV."""
    if score <= 0:
        return 0.0
    remaining = score
    total = 0.0
    for width, rate in ESV_BRACKETS:
        take = min(remaining, width)
        total += take * rate
        remaining -= take
        if remaining <= 0:
            return total
    # Ruleset only defines brackets up to score 99. Beyond that, extend the
    # last bracket's rate rather than guess — flag it if this ever actually
    # fires, it means someone leveled a stat past the documented range.
    total += remaining * ESV_BRACKETS[-1][1]
    return total


def weapon_damage(base, score, grade, weight="light"):
    """Damage = Base + (ESV x grade). Heavy ~= 2xBase + ESVxgradex1.5.
    Charged Heavy (the third weight) is 2xBase + ESVxgradex2.0.
    Fractional results always round up (session 6 ruling)."""
    e = esv(score)
    g = GRADE_MULTIPLIERS[grade]
    if weight == "light":
        raw = base + e * g
    elif weight == "heavy":
        raw = 2 * base + e * g * 1.5
    elif weight == "charged_heavy":
        raw = 2 * base + e * g * 2.0
    else:
        raise ValueError(f"unknown weapon weight: {weight!r}")
    return math.ceil(raw)


def double_swing_second_hit(first_hit_raw):
    """Default double-swing reduction: 50% of the first hit's raw, rounded up."""
    return math.ceil(first_hit_raw * 0.5)


# ---------------------------------------------------------------------------
# §10 — Precision Strike tolerance bands and Accuracy Tiers
# ---------------------------------------------------------------------------

# Ordered loosest -> tightest.
TOLERANCE_BANDS = [0.25, 0.20, 0.15, 0.13, 0.10, 0.07, 0.04, 0.02]

# multiplier range -> required tolerance. 1.0 (torso) has no stopwatch at all.
MULTIPLIER_TOLERANCE_TABLE = [
    (0.0, 0.5, 0.25),
    (0.51, 0.70, 0.20),
    (0.71, 0.99, 0.15),
    (1.0, 1.0, None),
    (1.01, 1.25, 0.13),
    (1.26, 1.50, 0.10),
    (1.51, 1.75, 0.07),
    (1.76, 2.00, 0.04),
    (2.01, math.inf, 0.02),
]

# count of tolerance bands the stop fell inside -> damage multiplier.
ACCURACY_TIER_TABLE = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.1, 5: 1.2, 6: 1.3, 7: 1.4, 8: 1.5}

MISS_PUNISHMENT_TABLE = [
    (0.0, 0.5, "Torso — full dmg, no limb effect"),
    (0.51, 0.70, "Torso — full dmg, no limb effect"),
    (0.71, 0.99, "Torso — full dmg, no limb effect"),
    (1.01, 1.25, "Torso — full dmg, no mult, no sever"),
    (1.26, 1.50, "Torso, no sever, + off-balance (-1m next turn)"),
    (1.51, 1.75, "Wide — no dmg, enemy free reactive strike"),
    (1.76, math.inf, "Whiff + exposed — enemy free heavy, or a track"),
]


def tolerance_band_for_multiplier(multiplier):
    for lo, hi, tol in MULTIPLIER_TOLERANCE_TABLE:
        if lo <= multiplier <= hi:
            return tol
    raise ValueError(f"no tolerance band defined for multiplier {multiplier!r}")


def miss_punishment(multiplier):
    for lo, hi, text in MISS_PUNISHMENT_TABLE:
        if lo <= multiplier <= hi:
            return text
    raise ValueError(f"no miss punishment defined for multiplier {multiplier!r}")


def accuracy_tier_multiplier(required_tolerance, deviation):
    """required_tolerance: the attack's own band (tolerance_band_for_multiplier).
    deviation: |actual stopwatch time - target time|, in seconds.
    Raises if deviation falls outside the required tolerance (that's a miss,
    not an Accuracy Tier question)."""
    if required_tolerance is None:
        raise ValueError("multiplier 1.0 (torso) has no stopwatch / Accuracy Tier")
    deviation = abs(deviation)
    if deviation > required_tolerance + 1e-9:
        raise ValueError("deviation exceeds required tolerance — this is a miss")
    if deviation == 0.0:
        return 3.0  # dead centre, always critical regardless of band depth
    start = next(
        i for i, tol in enumerate(TOLERANCE_BANDS) if math.isclose(tol, required_tolerance, abs_tol=1e-9)
    )
    count = 0
    for tol in TOLERANCE_BANDS[start:]:
        if deviation <= tol + 1e-9:
            count += 1
        else:
            break
    return ACCURACY_TIER_TABLE[count]


# ---------------------------------------------------------------------------
# §10 — Limbs: stagger (cumulative) and sever (single hit)
# ---------------------------------------------------------------------------

# Standard humanoid fallback only (monster-pass-instructions.md). Real fights
# should pass the specific monster template's own thresholds/multipliers.
STANDARD_HUMANOID_LIMBS = {
    "head": {"multiplier": 1.5, "threshold": 180},
    "torso": {"multiplier": 1.0, "threshold": 800},
    "arm": {"multiplier": 0.65, "threshold": 200},
    "leg": {"multiplier": 0.75, "threshold": 300},
}


def limb_hit(raw_damage, multiplier, stagger_threshold, accumulated=0):
    """One hit against a limb. Sever = this single hit's effective damage
    alone clears the threshold. Stagger = the threshold is crossed
    cumulatively across hits, this one included. Sever supersedes stagger
    (the limb is gone, not merely staggered) — this isn't spelled out
    verbatim in the ruleset but follows from sever being the stronger,
    permanent effect."""
    effective_damage = math.ceil(raw_damage * multiplier)
    new_accumulated = accumulated + effective_damage
    severed = effective_damage >= stagger_threshold
    staggered = (not severed) and new_accumulated >= stagger_threshold
    return {
        "effective_damage": effective_damage,
        "accumulated": new_accumulated,
        "staggered": staggered,
        "severed": severed,
    }


# ---------------------------------------------------------------------------
# §11 — Insight tiers and window bonus
# ---------------------------------------------------------------------------

INSIGHT_TIER_BREAKPOINTS = [(1, 0), (3, 1), (5, 2), (7, 3), (9, 4)]  # else tier 5
INSIGHT_WINDOW_BONUS = {0: 0.0, 1: 0.02, 2: 0.04, 3: 0.04, 4: 0.06, 5: 0.10}


def insight_tier(score):
    for ceiling, tier in INSIGHT_TIER_BREAKPOINTS:
        if score <= ceiling:
            return tier
    return 5


def insight_window_bonus(score):
    return INSIGHT_WINDOW_BONUS[insight_tier(score)]


# ---------------------------------------------------------------------------
# §5 — The Save Roll (Insanity & Influence)
# ---------------------------------------------------------------------------


def save_dc(track, resolve, insight, situational=0):
    """Succeed on d20 >= this value."""
    return 10 + track - (resolve // 10) + (insight // 2) + situational


# ---------------------------------------------------------------------------
# §5 — Status tick/track maths
# ---------------------------------------------------------------------------


def bleeding_tick(stacks):
    """Damage at the start of the turn equals current stacks, then lose 1."""
    if stacks <= 0:
        return {"damage": 0, "remaining": 0}
    return {"damage": stacks, "remaining": stacks - 1}


def bleeding_total(stacks):
    """Total damage N stacks will deal over their full run: N(N+1)/2."""
    return stacks * (stacks + 1) // 2


def corrosion_tick(stacks, managed_this_turn=False):
    """Damage equals current stacks. Only decrements if an action was spent
    managing it this turn — otherwise it holds indefinitely."""
    damage = stacks
    remaining = stacks - 1 if (managed_this_turn and stacks > 0) else stacks
    return {"damage": damage, "remaining": max(remaining, 0)}


def stone_skin_reduction(stacks):
    """10% damage reduction per stack, cap 3 (i.e. cap 30%)."""
    return min(stacks, 3) * 0.10


def crust_movement_penalty(stacks):
    """-1m movement budget per stack, cap 4."""
    return -min(stacks, 4)


def fervour_bonus(stacks):
    """+3 raw damage and +0.5m movement per stack."""
    return {"bonus_damage": 3 * stacks, "bonus_movement": 0.5 * stacks}


def fervour_whiff_cost(stacks):
    """Self-inflicted HP cost for a turn dealing no damage (including a whiffed parry)."""
    return stacks * 3


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("weapon-damage")
    p.add_argument("base", type=float)
    p.add_argument("score", type=int)
    p.add_argument("grade", choices=GRADE_MULTIPLIERS.keys())
    p.add_argument("--weight", choices=["light", "heavy", "charged_heavy"], default="light")

    p = sub.add_parser("limb-hit")
    p.add_argument("raw_damage", type=float)
    p.add_argument("multiplier", type=float)
    p.add_argument("stagger_threshold", type=float)
    p.add_argument("--accumulated", type=float, default=0)

    p = sub.add_parser("accuracy")
    p.add_argument("required_tolerance", type=float)
    p.add_argument("deviation", type=float)

    p = sub.add_parser("save-dc")
    p.add_argument("track", type=int)
    p.add_argument("resolve", type=int)
    p.add_argument("insight", type=int)
    p.add_argument("--situational", type=int, default=0)

    p = sub.add_parser("esv")
    p.add_argument("score", type=int)

    args = parser.parse_args()

    if args.command == "weapon-damage":
        result = weapon_damage(args.base, args.score, args.grade, args.weight)
    elif args.command == "limb-hit":
        result = limb_hit(args.raw_damage, args.multiplier, args.stagger_threshold, args.accumulated)
    elif args.command == "accuracy":
        result = accuracy_tier_multiplier(args.required_tolerance, args.deviation)
    elif args.command == "save-dc":
        result = save_dc(args.track, args.resolve, args.insight, args.situational)
    elif args.command == "esv":
        result = esv(args.score)

    print(json.dumps(result) if not isinstance(result, (int, float)) else result)
