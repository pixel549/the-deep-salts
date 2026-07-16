# THE DEEP SALTS
**Dev Log — Mechanic Index, Book Plan & Known Gaps**

Split out of the Design Bible (v2.5) so table-time context stays lean. **This file is project management — do NOT load it when running the game.** Sections keep their original design-bible numbers (§8–10) so ruleset cross-references remain valid.

---

# 8. Mechanic Template

**Rule of use:** mechanic pages exist ONLY for rulings the ruleset doesn't cover. Never write a mechanic page that duplicates ruleset content — a second copy of the parry rules is how two subtly divergent versions end up in play. The Open gaps list (§10) is the queue of mechanics that actually need pages; everything already Defined below is a pointer, not a rewrite.

## Mechanic Index

**Defined** (rules live in the ruleset — pointers only):

| Mechanic | Where | Note |
|---|---|---|
| Limb Targeting, Stagger & Sever | Ruleset §10 | Standard thresholds are fixed constants, never level-scaled; sever viable vs ordinary enemies ~raw Str 60–80 with a real sever weapon. Bosses: bespoke, deliberately-high hand-set thresholds. |
| Blood Loss | Ruleset §5 · bible §6 | Escalating per-hit bonus; Rupture split out as its own Immediate at cap 10 |
| Insanity / Influence saves | Ruleset §5 | Shared Save Roll: d20 ≥ 10 + track − ⌊Resolve÷10⌋ + ⌊Insight÷2⌋ |
| Discombobulation | Ruleset §5 | Tick, applied 1–3, −1/turn automatic |
| Attack Resolution | Ruleset §3 | Default attacks auto-land both sides; rolls/stopwatches for called shots, parries, saves, genuine uncertainty |
| Damage Floor & Scale | Ruleset §4 | 20 minimum base for anything passing through a multiplier |
| Backstory-Negotiated Character Creation | Ruleset §4 | Session-zero negotiation |
| Salts Rooms & Biomes | Ruleset §18 | Recipe→biome constant; interiors reroll; killer guaranteed spawn; boss kills persist |
| Hub Services & Pricing | Hub doc | Fixtures own existing mechanics: Pool Warden (leveling), Hydrotherapist (mutation revert/reroll), Maud (items, salt ID). Numbers **(untested)** — see §10. |

**Partially defined:**

| Mechanic | Where | Still needed |
|---|---|---|
| Rally | Ruleset §6 | Default 50% / next-turn window set; per-attack overrides need real numbers as monsters/weapons get built |
| Insight | Ruleset §11 | Spend menu, tier trade-offs, mods numbered; per-encounter award sizing still DM discretion |

**TBD** (need their own mechanic pages — see rule of use above; only where the ruleset is genuinely silent): Assess (unparryable enemies) · Immediate Status Resolution · Tick Status Resolution · White Salts economy drop rates · Double-Swing Reduction · Fugue edge cases

*(Removed from TBD this session — now fully specified in the ruleset, per the rule of use: Stagger → Free Called Shot and Staggered Enemy Limb Effects. Both resolved via session zero play — see ruleset §10, design bible §1.)*

*(Removed from the old TBD list as ruleset duplicates, per the rule of use: Parry + Visceral, Precision Strike, Burning, Corrosion, Action Economy, Movement & the Triangle, Leveling & ESV, Death & Retreat, Corrupted Regrowth, Turn Order, Short Rest, Abandon-All, Rupture damage page. All fully specified in the ruleset already — if play exposes a genuine gap in any of them, add it to §10 and it re-enters the queue.)*

## Mechanic Template (blank — copy per entry)

**One-Line Summary:** · **Full Procedure (numbered steps — every case covered):** · **Edge Cases (what happens when X meets Y):** · **Interactions with Other Mechanics:** · **DM Notes (what the DM must track/narrate/decide):** · **Player Notes (what the player must know to engage honestly):** · **Worked Example (one complete resolution):** · **Known Gaps / Open Questions:**

---

# 9. Ruleset Structure — Book Plan

Five books. Filled entity pages from bible §1–7 feed the relevant book. Status: **(✓)** floor entry filled, otherwise TBD.

- **Book 1 — Player's Guide:** character creation/leveling/White Salts/perks · weapons (✓ Paring Knife) · items (✓ Scour) · action economy/movement/triangle · parry/visceral/precision/assess/limbs · status effects (✓ Off-Balance) · Insight · Death & Retreat · Mutation · Abandon-All
- **Book 2 — DM's Guide:** running the world (dream-logic principles) · hub management · Insight award triggers · scaling · encounter design · NPC behaviour (✓ Robe Attendant) · lore threading · turn order/short rest/save mechanics
- **Book 3 — Monster Manual:** all monster pages (✓ Waterlogged Guest) · index by level range · archetype summary
- **Book 4 — World Book:** Stillwell Hydro full writeup · depth tiers · future locations · warp threshold rules
- **Book 5 — Index:** alphabetical indices · quick reference card

---

# 10. Known Gaps — Issues from Playtesting

## Open

| Gap | Description | Lives in |
|---|---|---|
| Influence → Insanity threshold | Stack number at which failed Influence saves also tick Insanity is undefined. Inconsistent in play (2+) vs manual (3+). **Note (session zero):** a related but distinct question — the stack at which Influence's own save is first *triggered at all* — was resolved this session at stack 2 (Ruleset §5). Flagging that this may or may not be the same axis as the Insanity-tick question below; not silently merged. | Status effect page |
| Chanter HP vs archetype text | Archetype note says low HP; Hummer entry has 900 HP. Contradiction caused a 13-turn fight. | Monster page |
| Assess on unparryable enemies | Assess is written only around parry tells. Undefined for Chanters. | Mechanic page |
| Double-swing reduction | No fixed percentage. Proposed: 50%. | Weapon page |
| White Salts drop rates | No base drops per archetype defined (Waterlogged Guest's 5 is the proposed floor). | Currency page |
| Insight not awarded Session 01 | Two new archetypes met, no Insight granted. Trigger threshold unclear. | Mechanic page |
| Turn order bypassed in play | d20 roll-off was skipped; DM narrated initiative instead. | Mechanic page |
| Charged Heavy tier | Weapon Template asks for three damage tiers; ruleset §4 defines two (light, heavy/charged combined). Placeholder in use: Charged Heavy = same maths as Heavy, until a real third tier is defined — if one's wanted at all. | Ruleset §4 / weapon page |
| Salt drop rates | Salts are single-use recipe fuel (Ruleset §18) but no per-biome or per-archetype drop guidance exists. DM discretion until playtested. | Item/Currency page |
| Recipe discovery triggers | How new recipes are learned — lore finds, experimentation, NPC purchase, Insight reveals — has no written procedure. | Ruleset §18 |
| Standard humanoid stagger durations | Proposed this session (Head 1 turn / Arm 2 / Leg 2, design bible §1) but genuinely untested — needs playtest confirmation like any other proposed number. | Design bible §1 |
| Bell sever threshold (Drowned Bellkeeper) | ~40 raw is a placeholder anchor, not a computed figure — session zero resolved the bell as a pure timing check without ever calculating raw damage against a threshold. | Design bible §1 (Bellkeeper page) |
| Endurance 40/99 perk replacements | *Overcharge* and *Endless* both referenced visceral charges directly; charges are now removed. Ruleset v7.1 has provisional placeholder text at both slots, explicitly marked needs-sign-off — not a real design decision yet. | Ruleset §4 |

## Resolved — proposed numbers not yet in the ruleset **(all untested)**

| Gap | Resolution |
|---|---|
| Mutation revert/reroll costs | Reroll = 10 × character level per limb. Revert = 25 × level (equal to the next attribute point — going human costs one level of progress) or flat 2 Insight. |
| Item prices | Scour 5 · Wrap 10 · Salts 10 · Tonic 15 (anchored to the floor mook's 5 White Salts drop). Action Items: rotating stock, 1–2 per hub visit, 3–5× Quick prices. |
| Recruit cap & Gallery | 10 recruits max (Gallery rooms 2–11); found/resolved/willing gate; one function + one drift behaviour each; recruits can be lost. |
| Maud's salt-ID pricing | 5 White Salts for a first identification, doubling per subsequent ID (5 → 10 → 20 → 40...). Confirmed by design intent this session — scales with progression rather than staying flat. |

## Resolved — now canon in the ruleset (log only)

Save Roll formula (Ruleset §5) · Blood Loss/Rupture split and quantification (Ruleset §5, bible §6) · sever thresholds reframed as fixed constants with Str 60–80 viability window (Ruleset §10; Cautery Saw base bumped 20→30) · Immediate-type effects populated (Off-Balance, bible §6) · enemy damage generated live per encounter, level-scaled, floor 20 (Ruleset §2/§4/§16) · attack resolution / no to-hit rolls (Ruleset §3) · character sheet split into its own live-state file (`deep-salts-character-sheet.md`) · Shambler HP band lowered 800–1200 → 200–1200 to match playtest (Ruleset §16) · **sever-as-only-kill-route drift** — prior sessions had the AI DM treating stagger/sever as mandatory for every kill, turning basic mooks into attrition wars. Fixed with an explicit standing instruction (Ruleset §2) plus reworded HP notes at §3, §10, §16, §19 and the Shambler/Waterlogged Guest entries: plain attacks to 0 HP always kill everything; sever is an optional fast lane reserved for high-HP fights, never a requirement.

**Session 2 — Hub Kit + Camphor (§8/§14):** consumable acquisition was a genuine gap — chargen grants a weapon but no items, "restocked at hub" existed only for Lloyd's capsules, and nothing defined how anyone gets Wraps/Tonics. Fix: the Hub Kit — every hub arrival refills a standard free loadout (2× Wrap, 2× Tonic, 1× Camphor, 1× Scour), capped, non-stacking; everything beyond it is found or bought with White Salts. Also renamed the "Salts" Quick Item to **Camphor** (currency name-clash) and defined its effect properly: clears 2 Insanity stacks — Insanity is a build-only track, so items are its main downward pressure. The stale "(starter gear pending — hub intake)" placeholder on the character sheet is resolved and deleted.

**Session 2 — Instance Quests vs Quests (§18):** narrative threads split by anchor. Layout-anchored content (environmental stories, one-off creatures, journals, unexplored doors) = Instance Quests — expire on exit, never tracked, lost to the reroll by design; completing one in-run can convert its reward into something persistent (item/lore/Insight), the only escape route. Persistent-entity-anchored content (recurring NPCs, hub, recipes, carried items) = Quests — the only threads logged between sessions. Corollary: enemies never persist across instances — same *kind* possible, always a fresh instance at full pool. Prompted by session 2's dragger (damage dealt now officially discarded), "R." (expired with its layout; only the token escaped), and the Beckoner (the completed-and-extracted exemplar).

**Session 2 — movement-as-action-fuel rework (§7/§8):** base movement 5→8m (formula now 8 + ⌊End÷15⌋, range 8–14m); Actions now cost movement on use (Light 1m, Heavy 3m, Hold 2m, manage track 1m, Action Item 2m, Assess 1m); Fast Actions always 0m. Hard rule: can't pay the cost, can't take the action. Cautery iron's "no movement" special case reworded as "costs full remaining budget." Weapon-specific costs and movement-refund/bonus perks are declared design space, unpopulated. Knock-on: staggered/severed legs now bite much harder (4m budget = Heavy + 1m total) — intentional, on-theme.

**Session 2 — enemy parry restriction (§16):** standard archetypes can no longer parry/visceral the player; that loop is reserved for bosses and hand-flagged elites. Effigy reclassified from standard archetype #8 to a named boss archetype — it keeps its full mirror kit, and being able to parry you is now definitionally boss-tier.

**Session 2:** generic uncertain-action clause (Ruleset §3) moved off flat `d20 + Attribute` onto a scaled **Attribute Modifier table** (0–1: −3 · 2–4: −2 · 5–9: −1 · 10–19: +0 · 20–39: +1 · 40–79: +2 · 80–99: +3). Flat addition let a single high stat (Skill 17+) auto-clear most reasonable DCs well before the attribute range's 99 cap; the scaled table keeps the d20 the dominant swing at every tier while still rewarding investment. Does not touch the Save Roll formula (§5), which already had its own scaling and wasn't the problem. Passive perks may still stack additional situational bonuses on top. Not retroactive — checks already resolved this session under the old math stand as rolled.

**Session zero (Ruleset v7.1 / design bible v2.6):** visceral charges removed as a resource entirely — parries gated by timing accuracy + a genuine telegraphed opening only, no charge pool (Ruleset §4/§9/§19; orphaned two Endurance perks, see Open) · enemy limb stagger fully specified — triggering a stagger grants an immediate free called shot same-action, and enemy stagger duration is variable per Monster Template rather than the player-side fixed one turn (Ruleset §10; design bible §1 gains a Stagger Duration column) · small/high-value called-shot targets (bells, cracks, eyes) formally folded into the limb system as non-standard entries using the Sever mechanic — no new category needed (Ruleset §10; design bible §1, Drowned Bellkeeper worked example) · self-initiated called shots (no enemy tell to time against) use one tolerance band tighter, and a miss ends the turn outright with no repositioning movement (Ruleset §9/§10) · Influence uncapped past 10 with no Rupture-equivalent overflow — instead, compelled-effect severity scales with stack count at DM discretion; first save triggers at stack 2; source-elimination fully clears the stack, and with multiple simultaneous sources all must be eliminated first (Ruleset §5) · currency terminology standardised to White Salts throughout the design bible and dev log (mechanical references only — flavour/proper-noun uses like "The Token That Isn't Yours" and the reception clerk's brass token are deliberately unchanged, since both are meant to look like coins in-fiction).
