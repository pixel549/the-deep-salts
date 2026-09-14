# Combat Resolver (v1)

Deterministic arithmetic for The Deep Salts, pulled out of the DM's head and
into code. Covers the parts of ruleset v9.4 that are pure maths, not
judgment calls — the stuff that actually drifts over a long chat session.

**Status: isolated, not wired into play yet.** Nothing in `dm-only/`,
`protocols.md`, or the character sheet references this folder. It doesn't
change how any session runs until you decide to point the DM at it. Lives
under `tools/` specifically so it can sit in the repo, sync to any device
via git, and not interfere with the current setup.

## What's implemented

- ESV soft-cap conversion and weapon damage (Light / Heavy / Charged Heavy),
  including the double-swing reduction — §4.
- Accuracy Tier multiplier from a stopwatch deviation — §10.
- Limb hits: effective damage, cumulative stagger, single-hit sever — §10.
  (Standard humanoid thresholds are included as a documented fallback only —
  see "On limb thresholds" below.)
- Insight tier lookup and window bonus — §11.
- The Insanity/Influence Save Roll DC — §5.
- Status tick/track maths: Bleeding (including the N(N+1)/2 total), Corrosion,
  Stone Skin reduction, Crust movement penalty, Fervour bonus/whiff cost — §5.

Every function is checked against a worked example already stated in the
ruleset or the dev log where one exists (see `tests/`), not just against my
own reading of the rule.

## What's deliberately NOT here

- Round flow, turn order, whose action it is — that's judgment, not maths.
- Rally (the 50/75/100% recovery bands are set per-attack, not formulaic).
- Any live game state (HP totals, current stacks, current Insight). This is
  a calculator, not a tracker — that's the next piece (`state.json`), not
  this one.
- Per-monster overrides. Bosses and elites get hand-set limb tables on their
  own Monster Template; this script never guesses those for you.

## Usage

As a library:

```python
from resolver import weapon_damage, limb_hit, accuracy_tier_multiplier

weapon_damage(30, 40, "B", weight="heavy")   # -> 110
limb_hit(450, 0.75, 325)                      # -> severs, per the §10 worked example
```

As a CLI, for a quick check mid-session without writing a script:

```
python3 resolver.py weapon-damage 30 40 B --weight heavy
python3 resolver.py limb-hit 450 0.75 325
python3 resolver.py accuracy 0.10 0.02
python3 resolver.py save-dc 6 30 6
```

## Running the tests

Stdlib `unittest` only — no `pip install` needed, so it runs the same on
any device this repo is cloned to:

```
python3 -m unittest discover -s tools/resolver/tests
```

## On limb thresholds

`STANDARD_HUMANOID_LIMBS` in `resolver.py` is the fallback table from
`monster-pass-instructions.md` (Head 180 / Torso 800 / Arm 200 / Leg 300).
**Real fights should pass the specific monster's own numbers** — the
ruleset is explicit that bosses and repeat-encounter enemies get hand-set
thresholds on their own template, and using the generic fallback against
one of those would silently give a wrong answer with total confidence,
which is worse than the problem this tool exists to fix.

## Maintenance rule

If a ruleset version bump changes a formula, grade multiplier, tolerance
band, threshold, or tier breakpoint referenced here, **update this file in
the same commit.** A resolver script that isn't updated goes stale in a way
an LLM DM doesn't — the LLM at least re-reads the current ruleset file each
time; a stale constant here will confidently give the old answer forever.
Section numbers in the docstrings (§4, §5, §9, §10, §11) point at
`deep-salts-v9.4.md` as of this commit.
