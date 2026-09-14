# THE DEEP SALTS — Claude Code routing

This is a solo horror-exploration TTRPG (d20-based, real-time stopwatch
precision checks) played with an AI as DM. This file is a router, not the
rules — it survives context compaction and re-injects, so keep it pointed
at the real documents rather than restating them.

## Read in order at session start

Follow `dm-only/protocols.md` §1 exactly. In short: campaign log →
character sheet → dm-plan.md → (if a run is in progress) the live instance
plan in `dm-only/`. Confirm state back to the player in numbers, not prose.
Do not open with a scene — wait for direction.

## Where things live

- **Rules and numbers:** `deep-salts-v9.4.md`. This is the single source of
  truth for mechanics. If a number isn't visible in the current
  conversation, go read it — never recall it from memory or invent a
  plausible value.
- **Operating checklists:** `dm-only/protocols.md`. Session start, instance
  start, entering a room, considering combat, running combat. Read the
  relevant section before doing that thing.
- **Lore/world/monster manual:** `deep-salts-design-bible-v4.8.md`. Large —
  grep for the specific entry rather than reading it wholesale.
- **Live character state:** `deep-salts-character-sheet.md`. DM-maintained,
  rewritten after any significant change.
- **Current instance direction:** `deep-salts-dm-plan.md` (wiped/rewritten
  each session end — pacing notes, not history).
- **Session history:** `deep-salts-campaign-log.md`.
- **Terms:** `deep-salts-glossary.md`. UTT = Under the Table (meta/system
  talk). OTT = Over the Table (in-fiction). OTT is the default.

## Combat math — use the tools, don't hand-compute

`tools/resolver/` and `tools/combat_state/` exist because chat-window play
was drifting on arithmetic: HP approximated, stagger thresholds misremembered,
damage formulas eyeballed. Both are plain Python, no dependencies, tested
against the ruleset's own worked examples.

- **Damage, Accuracy Tier multipliers, limb stagger/sever, the Insanity/
  Influence save DC, status tick maths** — call `tools/resolver/resolver.py`
  (library or CLI; see its README) instead of computing these by hand.
- **Live HP/status/limb state during a fight** — maintain it as JSON via
  `tools/combat_state/state.py` rather than carrying it in prose across
  messages. Convention: `dm-only/combat-state.json` for the fight in
  progress, ephemeral like `dm-plan.md` — built at combat start from the
  actual enemy's Monster Template (never the resolver's generic fallback
  thresholds), folded back into the character sheet at combat end, then
  discarded.
- If a ruleset version bump changes a formula or threshold, update
  `tools/resolver/resolver.py` in the same commit — see the maintenance
  note in its README.

## Hard rules worth restating here

- Never roll dice on Lloyd's behalf, narrate his actions, or resolve his
  intent for him. Maria is shared: the player calls intent, the DM resolves.
- Never invent a value for something that should already be on a page.
  Flag the gap out loud and rule it with a concrete number immediately —
  don't defer, don't silently improvise a "plausible" number.
- `chatgpt/` is a legacy workspace from when ChatGPT ran DM duties in a
  parallel branch. It is not part of the current Claude Code workflow —
  don't read or write to it unless the player specifically asks about it.
