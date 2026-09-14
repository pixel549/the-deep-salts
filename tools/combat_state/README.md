# Combat State Tracker (v1)

A JSON file as the single source of truth for what's happening *inside* a
fight — HP, status stacks, limb damage, round number — so it stops being
something the DM holds in its head across twenty messages.

**Status: isolated, not wired into play yet.** Same as `tools/resolver/` —
nothing in `protocols.md` or the ruleset points here. Between fights,
`deep-salts-character-sheet.md` stays the source of truth exactly as it is
now. This tool is only for the span between "combat starts" and "combat
ends," which currently has no persistent record at all — that gap is where
HP and stacks drift over a long session.

`state.example.json` is a schema demonstration, not real data — the enemy
in it is a placeholder. Never used at the table until you decide to wire it
in (at which point the real workflow is almost certainly: build the actual
encounter's `state.json` from that fight's Monster Template at the start of
combat, and fold the result back into the character sheet at the end,
exactly as protocols.md §5 already describes doing by hand).

## Schema

```
{
  "encounter": "free text",
  "round": 1,
  "combatants": {
    "<id>": {
      "id": "<id>",
      "name": "...",
      "side": "player" | "companion" | "enemy",
      "max_hp": int,
      "hp": int,
      "alive": bool,
      "status": { bleeding, burning, discombobulation, stone_skin, frenzy,
                  insanity, influence, corrosion, crust, fervour, fugue },
      "limbs": {
        "<limb_name>": { "multiplier": float, "threshold": int,
                          "accumulated": int, "severed": bool, "staggered": bool }
      }
    }
  }
}
```

`limbs` is empty for combatants that don't need per-limb tracking (Lloyd
and Maria, currently — the player-side limb rules in the ruleset are about
mutation and gating, not a stagger/sever pool). For enemies, populate it
from that encounter's actual Monster Template — `multiplier` and
`threshold` are never guessed here, same rule as `resolver.py`.

## Usage

```python
import state as combat_state

enc = combat_state.load("state.json")

combat_state.apply_limb_attack(enc, "enemy1", "arm", raw_damage=320)
combat_state.apply_status_stack(enc, "lloyd", "bleeding", +3)
combat_state.tick_start_of_turn(enc, "lloyd")   # Bleeding/Burning/Corrosion, in one call
combat_state.advance_round(enc)

combat_state.save(enc, "state.json")
```

Every mutating function returns what happened (damage dealt, whether a limb
staggered or severed, remaining HP) so the DM narrates from the return
value instead of recomputing it.

## What's implemented

- Combatant lifecycle: create, flat damage, death at 0 HP.
- Limb attacks via `resolver.limb_hit` — cumulative stagger, single-hit
  sever, and the ruleset's "severing head/torso kills regardless of
  remaining HP" rule.
- Status stacks with the ruleset's caps enforced (Discombobulation/Stone
  Skin 3, Insanity/Corrosion/Fervour 10, Crust 4; Bleeding/Burning/Frenzy/
  Influence uncapped).
- Start-of-turn ticks for Bleeding, Burning, and Corrosion in one call,
  returning a log instead of silent mutation.
- `manage_track` for the tracks that only decay when a turn was spent on
  them (Corrosion needs an action; Crust needs a whole turn with no Action
  at all — that second condition is on you to check before calling it).
- Save/load as plain JSON, so it's inspectable and diffable in git.

## What's deliberately NOT here

- Rally, Fervour's build/decay conditions (whether a turn qualifies), and
  anything else that depends on judging what happened in the fiction rather
  than a number someone hands in. Those stay DM calls; this only does the
  arithmetic once the DM has made them.
- Enemy AI, Secondary Action triggers, turn order — narrative/tactical, not
  state.
- Any connection to the character sheet. Folding an encounter's end state
  back into `deep-salts-character-sheet.md` is still a manual step, same as
  today, until that gets automated on purpose.

## Running the tests

```
python3 -m unittest discover -s tools/combat_state/tests
```
