---
description: Run a round of Deep Salts combat with computed maths and tracked state
---

Follow `dm-only/protocols.md` §5 — RUNNING COMBAT, exactly and in order.

Non-negotiable: compute damage, limb stagger/sever, Accuracy Tier multipliers,
and save DCs with `tools/resolver/resolver.py` — never hand-derive them.
Track HP/status/limbs each round in `dm-only/combat-state.json` via
`tools/combat_state/` — never carry it in prose across messages. When the
fight ends, fold the final state back into the character sheet per §5.13
and discard the combat-state file.

$ARGUMENTS
