# THE DEEP SALTS
**Design Bible — Entity Templates**

Companion to the ruleset. **Load this plus the ruleset and character sheet when running the game.** Mechanic index/book plan/known gaps live in the dev log — do NOT load that during play.

*Version 3.7. Session attribution and change history live in the dev log, not here.*

Every monster/weapon/item/NPC/status/currency gets one complete page. Copy the blank template to add an instance.

**Status effect types:** *Immediate* (lands on hit, resolves before next turn) · *Track* (builds 0–10, compounds) · *Tick* (applied at a value, counts down 1/turn automatically).

Each section leads with its **floor entry** — the weakest legal instance of that type. Nothing ships below it without a deliberate reason.

---

# 1. Monster Template

One page per monster — everything a DM needs to run that fight, nowhere else to look.

**Standard humanoid stagger durations (default, applies wherever "standard humanoid defaults" is referenced):** Head 1 turn · Arm 2 turns · Leg 2 turns · Torso n/a. Elites/bosses set bespoke durations.

## Monster 1 — Waterlogged Guest *(floor entry)*

- **Archetype:** Shambler (mook) · **Level Range:** 1–15 · **HP:** 200 · **Move:** 3m constant shuffle, no burst/recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A guest who came for the waters and never left the pool. Robe fused to grey skin. Drifts toward warmth rather than hunting.
- **Limbs:** standard defaults, no deviations. Not sever-immune.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Waterlogged Grasp | Light | None — unparryable, no windup | N/A | N/A | 0 raw; 1 Influence stack | N/A | N/A — outside 3m it just doesn't land |

- **Kitable:** Y — slowest move budget in the game.
- **Assess 0–1:** "It's slow. It won't hit hard. Watch the others behind it." · **Assess 2+:** "No damage on the grab, just Influence, no tell. Stagger a leg to ground it; head's open after."
- **Influence effect capped:** pull one step toward source (movement cost only), never an action loss, at any stack height.
- **White Salts drop:** 5 (the floor). **Insight:** +1 first sighting / +0 thereafter.

## Monster 2 — Chapel Penitent

- **Archetype:** Lunger (mook) · **Level Range:** 1–20 · **HP:** 300 · **Move:** 3m stalking pace, single 5m lunge after a short pause then a recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A pilgrim whose knees wore grooves into the stone before death. Still bows before every attack.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Penitent Rush | Heavy | "It bows deeply, then drives forward in a desperate sprint." | Target 1.2s, ±0.20s | 1 | 40 raw | Standard | Long recovery (~2 player actions before it fully re-engages, guideline not a hard count) |

- **Kitable:** Y. **Assess 0–1:** "It only becomes dangerous once it commits." · **Assess 2+:** "Wait for the bow. Dodge the charge, punish the recovery."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** panic-dodging too early. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 3 — Drowned Bellkeeper

- **Archetype:** Toller (mook) · **Level Range:** 1–20 · **HP:** 280 · **Move:** 2m slow walk, rarely closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A ruined attendant dragging a cracked handbell beneath the waterline. Every ring reaches inside the skull.
- **Limbs:** standard defaults, plus non-standard: **Bell** — implement, not a limb (Ruleset §10): multiplier ~2.0, sever ~40 raw (placeholder anchor). Deals full HP damage on the hit like any other strike. Breaking it permanently disables Hollow Bell for the encounter — and the Bellkeeper has no other attack, so a destroyed bell leaves it harmless.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Hollow Bell | Aura | "It slowly raises the bell before a dull, submerged toll." | Target 1.60s, ±0.35s total (±0.20s base + Insight window bonus) — set live session 7 | 1 | 20 raw; 1 Influence stack | Standard | Long delay before next toll |

- **Kitable:** Y. **Assess 0–1:** "That bell feels worse than it sounds." · **Assess 2+:** "Interrupt the toll by staying aggressive. Left alone it keeps building Influence."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** ignoring support enemies. **Dismember threat:** Low.

## Monster 4 — Salt-Eaten Custodian

- **Archetype:** Drudge (elite) · **Level Range:** 5–20 · **HP:** 650 · **Move:** 3m relentless walk, never sprints · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Once tasked with cleaning the baths, now drags an iron scraper large enough to serve as a coffin lid.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Iron Scrape | Heavy | "The scraper screeches across the floor before a wide sweep." | Target 1.20s, ±0.40s total (±0.25s base + Insight window bonus) — set live session 7 | 1 | 60 raw | Standard | Long recovery dragging weapon free |

- **Kitable:** Y. **Assess 0–1:** "That thing is slow, but don't stand in front of it." · **Assess 2+:** "The scrape announces everything. Dodge late, punish hard."
- **White Salts drop:** 15. **Insight:** +1/+0. **Habit punished:** greedy attacks after the tell begins. **Dismember threat:** High.

## Monster 5 — Brine Spitter

- **Archetype:** Spitter (mook) · **Level Range:** 1–20 · **HP:** 260 · **Move:** 3m retreating shuffle, keeps distance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Jaw hangs permanently open, overflowing with glittering saltwater that never runs dry.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Brine Jet | Ranged | "Its throat swells until the skin stretches taut." | Target 1.60s, ±0.20s | 1 | 30 raw | Standard | Stands exposed while coughing seawater |

- **Kitable:** N. **Assess 0–1:** "It's safer up close than far away." · **Assess 2+:** "Rush it during the inhale. The spit leaves it wide open."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** backpedalling constantly. **Dismember threat:** Low.

## Monster 6 — Bathhouse Flailer

- **Archetype:** Flailer (elite) · **Level Range:** 10–20 · **HP:** 700 · **Move:** 4m erratic, unpredictable direction changes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Wrapped in soaking towels that whip through the air like living tentacles when it panics.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Towel Lash | Light | "The dripping cloth suddenly snaps tight." | None — unparryable chip | N/A | 25 raw | Standard | N/A |
| Frenzied Whirl | Heavy (chain) | "All four towels draw back in unison, then unwind one after another." | **3 sequential windows: 0.80s · 1.30s · 1.80s, each ±0.20s base** | 3 | 30 raw per unparried window (90 if all three land) | Standard | Chain continues from the missed beat |

**Frenzied Whirl — the ballistic chain** *(set session 7, gives the Flailer archetype its defining Tier 3 opening):* three windows resolved back to back, one stopwatch each, restarting from 0 at each beat.
- **All three parried →** Tier 1 Open. It collapses out of the spin, weak point free, no second stopwatch.
- **Miss any window →** take that beat's 30 raw and every remaining beat in the chain automatically. No partial credit, no opening.
- Parried beats deal no damage and don't open it on their own — only the full three do. This is the hardest non-boss opening in the game by design.

- **Kitable:** N. **Assess 0–1:** "Stay calm. It isn't." · **Assess 2+:** "The spin isn't one attack, it's three. Read all of them or none."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** staying glued to its sides. **Dismember threat:** High.

## Monster 7 — Marble Attendant

- **Archetype:** Drudge (elite) · **Level Range:** 10–20 · **HP:** 800 · **Move:** 2m deliberate advance, pauses after every attack · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A carved attendant statue animated by centuries of absorbed prayers. Marble chips fall with every step.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Marble Fist | Heavy | "Stone cracks loudly through its arm before the punch." | Target 1.80s, ±0.20s | 2 | 80 raw | Standard | Long stationary recovery |

- **Kitable:** Y. **Assess 0–1:** "Every hit hurts. Every swing is slow." · **Assess 2+:** "Its recovery is longer than its attack. Survive one blow, answer with several."
- **White Salts drop:** 20. **Insight:** +1/+0. **Habit punished:** trading hits. **Dismember threat:** Very High.

## Monster 8 — The Singer *(boss, Choir Deep)*

- **Archetype:** Choir (boss) · **HP:** 900 (hand-set, exempt from scaling) · **Move:** 0m — fully rooted, never advances or retreats.
- **Flavour:** A pilgrim shape whose face gave way to a vertical opening that doesn't sing so much as *is* the sound. Sustains an unbroken note that draws the faithful into a ring around it, never approaching its own devotion.
- **Limbs:** standard defaults + **The Open Throat** (weak point) — multiplier ×2.0, sever 400.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Choir Pulse | Ranged/Aura | "The layered note sharpens, aims itself." | Unparryable, always lands | N/A | 2 Influence stacks/pulse |

- **Kitable:** N/A — never moves. Breaking line of sight is the counter.
- **Assess 0–1:** "It's not hunting. Whatever it's doing, it's not going to chase." · **Assess 2+:** "The note itself is the attack. The opening where its face should be is real, but boss-high, not mook-high."
- **White Salts drop:** 60. **Insight:** +1/+1.
- **Boss Gimmick:** Sever the Open Throat and the fight ends regardless of remaining HP. **Threshold 400 at ×2.0 = 200 raw in one hit** (per Ruleset §10's threshold ÷ multiplier). Deliberately above what any current weapon reaches — the Singer is an attrition fight first, and sever is never required (Ruleset §3). Otherwise pure attrition — the Singer never physically attacks; danger comes secondhand from its Penitent congregation, while Influence climbs the whole time, save DC rising with stack count.
- **Habit punished:** tanking pulses in the open, or fighting through the ring instead of around it. **Dismember threat:** Low (no melee of its own). **Retreat always reachable:** Y.

## Monster 9 — Cinderbound Attendant

- **Archetype:** Shambler (mook) · **Level Range:** 1–15 · **HP:** 220 · **Move:** 3m constant shuffle, no burst/recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A crematorium attendant whose apron fused to the firebrick during the last real burn. The wrap around its arms never fully cools. Drifts toward cold rather than hunting — the inverse of the thing that still wants its bath.
- **Limbs:** standard defaults, no deviations. Not sever-immune.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Cinder Embrace | Light | None — unparryable, no windup | N/A | N/A | 0 raw; 1 Burning stack | Standard | N/A — outside 3m it just doesn't land |

- **Kitable:** Y — slowest move budget in the game.
- **Assess 0–1:** "It's warm, not fast. Keep your distance and it can't do a thing." · **Assess 2+:** "The wrap's the fuel, not the arm. Stagger a leg — the grab still can't reach you before it drops."
- **White Salts drop:** 5 (the floor). **Insight:** +1 first sighting / +0 thereafter.

## Monster 10 — Rime-Fused Bailiff

- **Archetype:** Lunger (mook) · **Level Range:** 1–20 · **HP:** 340 · **Move:** 3m stalking pace, single 5m lunge after a short pause then a recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Once kept the cold stores at temperature. Now the cold that killed it lives under the skin, an icicle grown straight through the forearm where a blade should be.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Rime Thrust | Heavy | "Frost cracks up its arm before it drives the shard forward." | Target 1.2s, ±0.20s | 1 | 40 raw; 1 Blood Loss stack | Standard | Long recovery prying the shard free |

- **Kitable:** Y. **Assess 0–1:** "Only dangerous once it commits." · **Assess 2+:** "Wait for the crack. Dodge the thrust, punish the recovery — same rhythm as anything with one move."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** panic-dodging too early. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 11 — Wire-Strung Marionette

- **Archetype:** Burster (skirmisher) · **Level Range:** 5–25 · **HP:** 480 · **Move:** 3m twitching idle, 8m surge / ~1m recovery on the lunge · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Something that used to work the strings now wears them — cord grown straight into its own joints, drawn bowstring-tight before every leap. First of its archetype on record; nothing about it is slow.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Snap-Cord Lunge | Heavy | "The cord along its spine draws bowstring-tight." | Target 1.3s, ±0.20s | 1 | 45 raw | Standard | Long recovery, tangled in its own cord |

- **Kitable:** Partial — Y between bursts, N mid-surge (the 8m covers ground faster than a retreat). **Assess 0–1:** "It's not fast. It's a spring." · **Assess 2+:** "Everything happens on the coil. Move the instant the cord draws, not after."
- **White Salts drop:** 12. **Insight:** +1/+0. **Habit punished:** standing still after its first miss — the recovery beat is real, but short. **Dismember threat:** Moderate.

## Monster 12 — The Annotator

- **Archetype:** Chanter (caster) · **Level Range:** 1–20 · **HP:** 340 · **Move:** 3m drifting glide, always hangs back, never closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A robed archivist, mouth sewn shut decades ago. The whispering isn't coming from the mouth — it's the marginal notes crawling up its sleeves, reciting something that isn't quite words. First genuine Chanter on record.
- **Limbs:** standard defaults, no deviations — soft target, nothing to armor.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Marginal Recitation | Ranged/Aura | None — unparryable, always lands in range | N/A | N/A | 0 raw; 1 Influence stack (DM may substitute 1 Insanity stack instead, per the archetype's dual pressure) | N/A | N/A |

- **Kitable:** N/A — no melee attack to kite; correct play is closing distance and killing it fast, not keeping range.
- **Assess 0–1:** "It isn't attacking you, exactly. It's reading something onto you." · **Assess 2+:** "No tell because there's nothing to parry. Low HP, soft everywhere — kill it before the stacks matter."
- **White Salts drop:** 10. **Insight:** +1/+0. **Habit punished:** ignoring it because "it isn't attacking." **Dismember threat:** Low (dies before limbs matter).

## Monster 13 — The Dust-Choked Gardener

- **Archetype:** Spitter (controller) · **Level Range:** 1–20 · **HP:** 300 · **Move:** 3m retreating shuffle, keeps distance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A gardener's throat long since given over to a dry, papery fungus. Every cough throws spores that eat through cloth and skin alike — nothing about it is wet.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Spore Cough | Ranged | "Its chest swells, throat rattling with dust." | Target 1.6s, ±0.20s | 1 | 30 raw; 2 Corrosion stacks | Standard | Stands exposed, coughing through its own cloud |

- **Kitable:** N. **Assess 0–1:** "Closing the gap is safer than staying at range." · **Assess 2+:** "Rush it during the swell. The cloud needs the cough to actually leave its throat."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** backpedalling constantly. **Dismember threat:** Low.

## Monster 14 — The Long Cutter

- **Archetype:** Brute (heavy) · **Level Range:** 15–60 · **HP:** 1800 · **Move:** 4m slow, deliberate advance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Built from decades of fused ossuary bone, bound in rope and set pitch, wielding a cleaver the length of a door. Doesn't so much walk as arrive. First of its archetype on record — built deliberately over-levelled for now, a long-campaign fixture rather than a next-session encounter.
- **Limbs:** standard defaults, no deviations — bulk instead of speed; the legs stay the one real opening regardless of its size.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Door-Length Cleave | Heavy | "It raises the cleaver in both fists, joints grinding audibly." | Target 2.0s, ±0.20s | 2 | 90 raw | Standard | Long stationary recovery, blade stuck in the floor |

- **Kitable:** Y in principle — it's enormous, and enormous is slow. **Assess 0–1:** "It's huge. It's also slow enough to just not be there when it lands." · **Assess 2+:** "Sever a leg and the approach stops being a threat at all — the wind-up alone gives you the time."
- **White Salts drop:** 35. **Insight:** +1/+0. **Habit punished:** trading hits at melee range while under-levelled — genuine bisect threat on a fully-landed hit. **Dismember threat:** Very High. **Retreat always reachable:** Y — nothing about it is fast.

## Monster 15 — Custodian in Wax

- **Archetype:** Drudge (elite) · **Level Range:** 5–20 · **HP:** 700 · **Move:** 3m relentless walk, never sprints · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A parlour attendant recast entirely in wax mid-task, still holding the brush it died holding. Never stops. Never speeds up either.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Slow Anoint | Heavy | "The brush arm draws back with a soft, waxen creak." | Target 1.2s, ±0.25s | 1 | 55 raw | Standard | Long recovery re-settling its stance |

- **Kitable:** Y. **Assess 0–1:** "Slow, but it never stops coming." · **Assess 2+:** "Fully readable, fully punishable — the counterpoint to anything with a hidden tell."
- **White Salts drop:** 15. **Insight:** +1/+0. **Habit punished:** greedy attacks after the tell begins. **Dismember threat:** High.

## Monster 16 — The Brass-Throated Barker

- **Archetype:** Toller (mook) · **Level Range:** 1–20 · **HP:** 300 · **Move:** 2m slow walk, rarely closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Wears a barker's brass megaphone fused permanently to its jaw. Every call through it warps the mirrors around it into something worse.
- **Limbs:** standard defaults, plus non-standard: **Megaphone** — implement, not a limb (Ruleset §10): multiplier ×2.0, sever 35 raw. Deals full HP damage on hit like any other strike. Breaking it disables Warped Call for the encounter — no other attack exists.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Warped Call | Aura | "It draws breath through brass, and the glass around it starts to bend." | Target 1.5s, ±0.30s total | 1 | 20 raw; 1 Discombobulation | Standard | Long delay before the next call |

- **Kitable:** Y. **Assess 0–1:** "The call's worse than the creature." · **Assess 2+:** "Break the horn and it has nothing left at all — same rule as anything that hangs its whole kit on an implement."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** ignoring support enemies. **Dismember threat:** Low.

## Monster 17 — Reel-Torn Usher

- **Archetype:** Flailer (chaotic) · **Level Range:** 10–20 · **HP:** 750 · **Move:** 4m erratic, unpredictable direction changes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** An usher still wrapped shoulder to ankle in unspooled film stock, the reels whipping loose whenever the projector behind its ribs flickers.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Filmstrip Snap | Light | "A loose reel lashes without warning." | None — unparryable chip | N/A | 20 raw | Standard | N/A |
| Triple Unspool | Heavy (chain) | "All three reels draw taut at once, then whip out in sequence." | **3 sequential windows: 0.80s · 1.30s · 1.80s, each ±0.20s base** | 3 | 30 raw per unparried window (90 if all three land) | Standard | Chain continues from the missed beat |

**Triple Unspool — the ballistic chain** *(same archetype rule as the Bathhouse Flailer's Frenzied Whirl, reskinned)*: three windows resolved back to back, one stopwatch each, restarting from 0 at each beat.
- **All three parried →** Tier 1 Open. It collapses out of the whip, weak point free, no second stopwatch.
- **Miss any window →** take that beat's 30 raw and every remaining beat automatically. No partial credit, no opening.
- Parried beats deal no damage and don't open it on their own — only the full three do.

- **Kitable:** N. **Assess 0–1:** "Stay calm. It isn't." · **Assess 2+:** "The whip isn't one attack, it's three. Read all of them or none."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** staying glued to its sides. **Dismember threat:** High.

## Monster 18 — The Reflection *(boss, Hall of Broken Mirrors)*

- **Archetype:** Effigy (boss, duellist/mirror) · **HP:** 800 (hand-set, exempt from scaling) · **Move:** 7m — matches or slightly out-paces the player's own movement budget.
- **Flavour:** Every mirror in the hall holds it at once, but only one glass ever cracks when it steps through. Fights exactly like Lloyd does, because it's copying him, one beat behind — parry for parry, visceral for visceral, only ever a half-step from getting the timing right. First entry to actually earn the Effigy name (Ruleset §16) since Marble Attendant was reclassified away from it.
- **Limbs:** standard defaults + **The Seam** (weak point, where the reflection doesn't quite line up) — multiplier ×1.75, sever 250.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Mirrored Riposte | Heavy | "It matches your stance a half-beat late, then swings on the same line you just did." | Target 1.4s, ±0.09s | 2 | 65 raw |
| Glass Feint | Light | "It steps sideways through its own glass." | Unparryable repositioning move, no damage | N/A | 0 raw — closes or breaks distance instantly |

- **Kitable:** N — it matches movement 1:1; it will always be exactly as fast as Lloyd is.
- **Assess 0–1:** "It's not attacking first. Ever. It's waiting on you to move." · **Assess 2+:** "It's running your own kit back at you a half-beat late. The Seam is the one place its timing genuinely never lines up."
- **White Salts drop:** 55. **Insight:** +1/+1.
- **Boss Gimmick:** The Effigy parries and viscerals like a real opponent — the genuine boss-tier exception to the standing rule that standard archetypes can't (Ruleset §16/§9). It also initiates its own visceral off a missed player parry, mirroring the exact system back. Sever the Seam and the copy shatters outright, fight ends regardless of remaining HP. **Threshold 250 at ×1.75 ≈ 143 raw in one hit** (per Ruleset §10's threshold ÷ multiplier) — reachable, not trivial, at current gear. Sever is never required (Ruleset §3); pure attrition still ends it.
- **Habit punished:** leading every exchange the same way twice — it's had one rep to learn it by the second attempt. **Dismember threat:** Moderate (nothing overtly bisecting, but the parry loop punishes greed hard). **Retreat always reachable:** Y, though it will follow at exactly your own pace.

## Monster 19 — The Sackcloth Verger

- **Archetype:** Shambler (mook) · **Level Range:** 1–15 · **HP:** 240 · **Move:** 3m constant shuffle, no burst/recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A relic-keeper's under-robe, stiff with gold leaf flaking off in sheets, shuffling the same slow circuit it walked in life — venerating icons that were sold off a century ago.
- **Limbs:** standard defaults, no deviations. Not sever-immune.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Gilded Grasp | Light | None — unparryable, no windup | N/A | N/A | 0 raw; 1 Influence stack | Standard | N/A — outside 3m it just doesn't land |

- **Kitable:** Y — slowest move budget in the game.
- **Assess 0–1:** "It's slow. It won't hit hard." · **Assess 2+:** "Same shuffle as anything in this family. Stagger a leg, take the head after."
- **White Salts drop:** 5 (the floor). **Insight:** +1/+0.

## Monster 20 — Powdered Deacon

- **Archetype:** Shambler (mook) · **Level Range:** 1–15 · **HP:** 260 · **Move:** 3m constant shuffle, no burst/recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Soot-caked robes packed with decades of loose gunpowder dust. The grasp itself does nothing — the residue it leaves keeps eating long after contact ends.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Sooted Grasp | Light | None — unparryable, no windup | N/A | N/A | 0 raw; 1 Corrosion stack | Standard | N/A — outside 3m it just doesn't land |

- **Kitable:** Y. **Assess 0–1:** "Don't let the dust get on you — that's the whole fight." · **Assess 2+:** "Same floor-tier shuffle as always. The Corrosion's the only thing worth respecting."
- **White Salts drop:** 5. **Insight:** +1/+0.

## Monster 21 — Loom-Handed Weaver

- **Archetype:** Lunger (mook) · **Level Range:** 1–20 · **HP:** 360 · **Move:** 3m stalking pace, single 5m lunge after a short pause then a recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Fingers fused into a shuttle, still working threads that snapped off the loom decades ago. The lunge is the same motion its hands never stopped making.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Shuttle Strike | Heavy | "The shuttle-hand draws back with a mechanical click." | Target 1.2s, ±0.20s | 1 | 40 raw; 1 Blood Loss stack | Standard | Long recovery, re-threading itself |

- **Kitable:** Y. **Assess 0–1:** "Only dangerous once it commits." · **Assess 2+:** "Wait for the click. Dodge the strike, punish the recovery."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** panic-dodging too early. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 22 — Gaslit Orderly

- **Archetype:** Lunger (mook) · **Level Range:** 1–20 · **HP:** 380 · **Move:** 3m stalking pace, single 5m lunge after a short pause then a recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A surgical orderly still in a gaslit apron, scalpel grown straight through the palm. Steps in with the same clinical patience it once used on patients.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Clinical Thrust | Heavy | "It steadies its grip before driving the scalpel forward." | Target 1.3s, ±0.20s | 1 | 40 raw; 1 Blood Loss stack | Standard | Long recovery, blade caught on bone |

- **Kitable:** Y. **Assess 0–1:** "Only dangerous once it commits." · **Assess 2+:** "Wait for the grip, dodge the thrust, punish the recovery."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** panic-dodging too early. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 23 — Coalback Skitterer

- **Archetype:** Burster (skirmisher) · **Level Range:** 5–25 · **HP:** 500 · **Move:** 3m idle scrabble, 8m surge / ~1m recovery on the lunge · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Something that learned to move in absolute dark, coiled tight against a seam wall until the lamp swings away. Then it isn't there anymore.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Dark Surge | Heavy | "A scrape of coal, then silence — it's already coiled." | Target 1.3s, ±0.20s | 1 | 45 raw | Standard | Long recovery, scrabbling back into the dark |

- **Kitable:** Partial — Y between bursts, N mid-surge. **Assess 0–1:** "It's not fast. It's a spring." · **Assess 2+:** "It needs dark to close the gap. Keep a light on it and the surge never lines up."
- **White Salts drop:** 12. **Insight:** +1/+0. **Habit punished:** standing in full dark near a wall. **Dismember threat:** Moderate.

## Monster 24 — Reliquary Imp

- **Archetype:** Burster (skirmisher) · **Level Range:** 5–25 · **HP:** 460 · **Move:** 3m twitching idle, 8m surge / ~1m recovery on the lunge · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A gilt devotional figure, small enough to fit a shelf — until it isn't on the shelf anymore.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Gilt Lunge | Heavy | "The gold figure's joints creak taut." | Target 1.3s, ±0.20s | 1 | 45 raw | Standard | Long recovery, joints locked |

- **Kitable:** Partial — Y between bursts, N mid-surge. **Assess 0–1:** "It's not fast. It's a spring." · **Assess 2+:** "Everything happens on the coil. Move the instant the joints lock, not after."
- **White Salts drop:** 12. **Insight:** +1/+0. **Habit punished:** standing still after its first miss. **Dismember threat:** Moderate.

## Monster 25 — Sedated Whisperer

- **Archetype:** Chanter (caster) · **Level Range:** 1–20 · **HP:** 320 · **Move:** 3m drifting glide, always hangs back, never closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A patient strapped to a gurney, no longer breathing in any way that matters, still murmuring sedation-talk that was never meant for anyone conscious.
- **Limbs:** standard defaults, no deviations — soft target, nothing to armor.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Sedation Murmur | Ranged/Aura | None — unparryable, always lands in range | N/A | N/A | 0 raw; 1 Insanity stack (DM may substitute Influence, per the archetype's dual pressure) | N/A | N/A |

- **Kitable:** N/A — no melee attack to kite; correct play is closing distance and killing it fast.
- **Assess 0–1:** "It isn't attacking you, exactly." · **Assess 2+:** "No tell because there's nothing to parry. Kill it before the stacks matter."
- **White Salts drop:** 10. **Insight:** +1/+0. **Habit punished:** ignoring it because "it isn't attacking." **Dismember threat:** Low.

## Monster 26 — Static-Throated Operator

- **Archetype:** Chanter (caster) · **Level Range:** 1–20 · **HP:** 360 · **Move:** 3m drifting glide, always hangs back, never closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A switchboard operator, cord still plugged into a jack sewn straight into its throat. Every word comes out as feedback first, language second.
- **Limbs:** standard defaults, no deviations — soft target.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Feedback Whisper | Ranged/Aura | None — unparryable, always lands in range | N/A | N/A | 0 raw; 1 Influence stack | N/A | N/A |

- **Kitable:** N/A — no melee attack to kite; correct play is closing distance and killing it fast.
- **Assess 0–1:** "It isn't attacking you, exactly." · **Assess 2+:** "No tell because there's nothing to parry. Kill it before the stacks matter."
- **White Salts drop:** 10. **Insight:** +1/+0. **Habit punished:** ignoring it because "it isn't attacking." **Dismember threat:** Low.

## Monster 27 — Plume-Choked Keeper

- **Archetype:** Spitter (controller) · **Level Range:** 1–20 · **HP:** 320 · **Move:** 3m retreating shuffle, keeps distance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** An aviary-keeper's throat gone to down and hollow bone. Every cough throws a storm of feather-barbs, fine enough to work under skin.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Plume Cough | Ranged | "Its chest swells, feathers already leaking from the seams." | Target 1.6s, ±0.20s | 1 | 30 raw; 2 Corrosion stacks | Standard | Stands exposed, coughing through its own storm |

- **Kitable:** N. **Assess 0–1:** "Closing the gap is safer than staying at range." · **Assess 2+:** "Rush it during the swell."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** backpedalling constantly. **Dismember threat:** Low.

## Monster 28 — Pulp-Throated Presser

- **Archetype:** Spitter (controller) · **Level Range:** 1–20 · **HP:** 340 · **Move:** 3m retreating shuffle, keeps distance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Throat packed solid with wet pulp gone dry and papery. The cough throws shredded fiber that catches in a wound and keeps working itself deeper.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Pulp Cough | Ranged | "Its throat rattles, dry fiber already sifting loose." | Target 1.6s, ±0.20s | 1 | 30 raw; 2 Corrosion stacks | Standard | Stands exposed, coughing through the drift |

- **Kitable:** N. **Assess 0–1:** "Closing the gap is safer than staying at range." · **Assess 2+:** "Rush it during the rattle."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** backpedalling constantly. **Dismember threat:** Low.

## Monster 29 — Seam-Breaker

- **Archetype:** Brute (heavy) · **Level Range:** 20–70 · **HP:** 2200 · **Move:** 4m slow, deliberate advance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Something that used to break coal for a living, and never really clocked out. Swings a pick the length of a man.
- **Limbs:** standard defaults, no deviations — bulk instead of speed; the legs stay the one real opening.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Seam Swing | Heavy | "It plants both feet, pick raised past its own shoulder." | Target 2.0s, ±0.20s | 2 | 90 raw | Standard | Long stationary recovery, pick buried in stone |

- **Kitable:** Y in principle — it's enormous, and enormous is slow. **Assess 0–1:** "It's huge. It's also slow enough to just not be there when it lands." · **Assess 2+:** "Sever a leg and the approach stops being a threat at all."
- **White Salts drop:** 35. **Insight:** +1/+0. **Habit punished:** trading hits at melee range while under-levelled — genuine bisect threat. **Dismember threat:** Very High. **Retreat always reachable:** Y.

## Monster 30 — Frost-Iron Smith

- **Archetype:** Brute (heavy) · **Level Range:** 15–55 · **HP:** 1600 · **Move:** 4m slow, deliberate advance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A smith frozen mid-strike when the forge finally went cold for good. The hammer still glows faintly with a heat that never quite left the iron.
- **Limbs:** standard defaults, no deviations — bulk instead of speed; the legs stay the one real opening.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Cold Hammer | Heavy | "The hammer arm rises past its shoulder, trailing frost off dying heat." | Target 2.0s, ±0.20s | 2 | 90 raw; 1 Burning stack | Standard | Long stationary recovery, hammer stuck to the anvil |

- **Kitable:** Y in principle. **Assess 0–1:** "It's huge. It's also slow enough to just not be there when it lands." · **Assess 2+:** "Sever a leg and the approach stops being a threat at all."
- **White Salts drop:** 35. **Insight:** +1/+0. **Habit punished:** trading hits at melee range while under-levelled. **Dismember threat:** Very High. **Retreat always reachable:** Y.

## Monster 31 — Wire-Boned Falconer

- **Archetype:** Drudge (elite) · **Level Range:** 5–20 · **HP:** 720 · **Move:** 3m relentless walk, never sprints · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A falconer whose arm rebuilt itself in wire and feather after the bird it once carried finished the job. Never stops advancing, never speeds up either.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Wire-Boned Backhand | Heavy | "The wire arm swings wide with an audible creak." | Target 1.2s, ±0.25s | 1 | 55 raw | Standard | Long recovery re-settling its stance |

- **Kitable:** Y. **Assess 0–1:** "Slow, but it never stops coming." · **Assess 2+:** "Fully readable, fully punishable."
- **White Salts drop:** 15. **Insight:** +1/+0. **Habit punished:** greedy attacks after the tell begins. **Dismember threat:** High.

## Monster 32 — Anvil-Bound Apprentice

- **Archetype:** Drudge (elite) · **Level Range:** 10–20 · **HP:** 760 · **Move:** 2m deliberate advance, pauses after every attack · **Scale Band:** 1–20 (×1.0)
- **Flavour:** An apprentice still chained wrist-to-anvil, dragging the whole iron block behind it with every step, never once slowing to compensate.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Anvil Drag-Swing | Heavy | "The anvil scrapes stone before the whole weight comes around." | Target 1.3s, ±0.25s | 2 | 60 raw | Standard | Long recovery dragging the anvil back into line |

- **Kitable:** Y. **Assess 0–1:** "Every hit hurts. Every swing is slow." · **Assess 2+:** "Its recovery is longer than its attack — survive one, answer with several."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** trading hits. **Dismember threat:** High.

## Monster 33 — Fuse-Throated Crier

- **Archetype:** Toller (mook) · **Level Range:** 1–20 · **HP:** 280 · **Move:** 2m slow walk, rarely closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Throat packed with a slow-burning fuse instead of a voice box. Every call is timed to a sputter that never quite reaches detonation.
- **Limbs:** standard defaults, plus non-standard: **Fuse-Horn** — implement, not a limb (Ruleset §10): multiplier ×2.0, sever 30 raw. Deals full HP damage on hit like any other strike. Breaking it disables Sputtered Call for the encounter.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Sputtered Call | Aura | "The fuse in its throat catches, sputtering toward a call." | Target 1.4s, ±0.30s total | 1 | 20 raw; 1 Burning stack | Standard | Long delay before the fuse catches again |

- **Kitable:** Y. **Assess 0–1:** "The call's worse than the creature." · **Assess 2+:** "Break the horn and it has nothing left at all."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** ignoring support enemies. **Dismember threat:** Low.

## Monster 34 — The Squall Box

- **Archetype:** Toller (mook) · **Level Range:** 1–20 · **HP:** 320 · **Move:** 2m slow walk, rarely closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A cracked speaker cabinet strapped to its chest like a breastplate, still wired into whatever's left of its own throat.
- **Limbs:** standard defaults, plus non-standard: **Speaker Cabinet** — implement, not a limb (Ruleset §10): multiplier ×2.0, sever 40 raw. Deals full HP damage on hit like any other strike. Breaking it disables Feedback Squall for the encounter.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Feedback Squall | Aura | "The cabinet crackles, building toward a squall." | Target 1.5s, ±0.30s total | 1 | 20 raw; 1 Discombobulation | Standard | Long delay before the next squall |

- **Kitable:** Y. **Assess 0–1:** "The call's worse than the creature." · **Assess 2+:** "Break the cabinet and it has nothing left at all."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** ignoring support enemies. **Dismember threat:** Low.

## Monster 35 — Shuttle-Armed Weaver

- **Archetype:** Flailer (chaotic) · **Level Range:** 10–20 · **HP:** 760 · **Move:** 4m erratic, unpredictable direction changes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Four loom-shuttles grown fused to its limbs, each trailing a length of thread sharp enough to open skin. It doesn't move so much as it's operated.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Thread Snap | Light | "A loose shuttle-thread snaps without warning." | None — unparryable chip | N/A | 20 raw | Standard | N/A |
| Full Weave | Heavy (chain) | "All four shuttles draw back in unison, then fire in sequence." | **3 sequential windows: 0.80s · 1.30s · 1.80s, each ±0.20s base** | 3 | 30 raw per unparried window (90 if all three land) | Standard | Chain continues from the missed beat |

**Full Weave — the ballistic chain** *(same archetype rule as the Bathhouse Flailer's Frenzied Whirl, reskinned)*: three windows resolved back to back, one stopwatch each, restarting from 0 at each beat.
- **All three parried →** Tier 1 Open, weak point free, no second stopwatch.
- **Miss any window →** take that beat's 30 raw and every remaining beat automatically. No partial credit, no opening.
- Parried beats deal no damage and don't open it on their own — only the full three do.

- **Kitable:** N. **Assess 0–1:** "Stay calm. It isn't." · **Assess 2+:** "The weave isn't one attack, it's three. Read all of them or none."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** staying glued to its sides. **Dismember threat:** High.

## Monster 36 — Ream-Wrapped Binder

- **Archetype:** Flailer (chaotic) · **Level Range:** 10–25 · **HP:** 780 · **Move:** 4m erratic, unpredictable direction changes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Wrapped shoulder to wrist in reams of uncut paper, each sheet honed razor-sharp at the edge by decades of the same motion repeated.
- **Limbs:** standard defaults, no deviations.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Paper Cut | Light | "A loose sheet slices without warning." | None — unparryable chip | N/A | 20 raw | Standard | N/A |
| Ream Cascade | Heavy (chain) | "Both arms draw the reams taut, then release in sequence." | **3 sequential windows: 0.80s · 1.30s · 1.80s, each ±0.20s base** | 3 | 30 raw per unparried window (90 if all three land) | Standard | Chain continues from the missed beat |

**Ream Cascade — the ballistic chain** *(same archetype rule, reskinned)*: three windows resolved back to back, one stopwatch each, restarting from 0 at each beat.
- **All three parried →** Tier 1 Open, weak point free, no second stopwatch.
- **Miss any window →** take that beat's 30 raw and every remaining beat automatically. No partial credit, no opening.
- Parried beats deal no damage and don't open it on their own — only the full three do.

- **Kitable:** N. **Assess 0–1:** "Stay calm. It isn't." · **Assess 2+:** "The cascade isn't one attack, it's three. Read all of them or none."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** staying glued to its sides. **Dismember threat:** High.

## Monster 37 — The Foundry Marshal *(boss, Cold Forge)*

- **Archetype:** Foundry (boss, heavy/reach-chain) · **HP:** 1400 (hand-set, exempt from scaling) · **Move:** 3m, never sprints, never retreats — but its swing radius reaches well past where its footsteps suggest.
- **Flavour:** Once oversaw the whole forge floor. Now its ribs are the furnace, and everything it swings is still hot from the inside.
- **Limbs:** standard defaults + **The Furnace Door** (weak point, chest) — multiplier ×1.75, sever 300.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Marshal's Cross | Heavy | "It plants both feet, both arms crossing before a wide double swing." | Target 1.8s, ±0.20s | 1 | 70 raw; 1 Burning stack |
| Foundry Reckoning | Heavy (chain) | "The furnace door in its chest cracks open, venting three pulses of heat in sequence." | **3 sequential windows: 0.90s · 1.40s · 1.90s, each ±0.15s** | 3 | 40 raw per unparried window (120 if all three land), +1 Burning stack per landed window |

- **Kitable:** Partial — its footwork is slow, but the swing radius reaches further than instinct suggests; keep distance wider than it looks like you need to.
- **Assess 0–1:** "It's not fast. Its reach is the trick." · **Assess 2+:** "The chest cracks before the real attack. Read the vents, not the arms — Marshal's Cross alone never opens it."
- **White Salts drop:** 50. **Insight:** +1/+1.
- **Boss Gimmick:** Foundry Reckoning is the Marshal's real opening, same chain rule as any Flailer: **all three windows parried → Tier 1 Open on the Furnace Door**, no second stopwatch. **Miss any window → take that beat's 40 raw + Burning and every remaining beat automatically.** Sever the Furnace Door — **300 at ×1.75 ≈ 171 raw in one hit** (per Ruleset §10's threshold ÷ multiplier) — and the fight ends regardless of remaining HP. Reachable, not trivial, at current gear. Sever never required (Ruleset §3).
- **Habit punished:** judging distance by its feet instead of its reach. **Dismember threat:** High (Burning stacks compound fast off a clean chain). **Retreat always reachable:** Y.

## Monster 38 — The Bellfounder *(boss, Bellfounder's Pit)*

- **Archetype:** Bellfounder (boss, aura/attrition-chain) · **HP:** 1000 (hand-set, exempt from scaling) · **Move:** 0m — rooted at the casting pit, never advances or retreats.
- **Flavour:** Cast itself into its own bell before the bronze finished cooling. The ringing hasn't stopped since, and neither has the pouring.
- **Limbs:** standard defaults + **The Crack** (weak point, a fault line down the bell-body) — multiplier ×2.0, sever 350 (degrades, see Boss Gimmick).

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Founding Toll | Ranged/Aura | "The bell-body vibrates, tone climbing." | Unparryable, always lands | N/A | 0 raw; 2 Influence stacks/toll |
| Molten Pour | Heavy (chain) | "The Crack along its side glows, then splits into three successive pours." | **3 sequential windows: 1.00s · 1.50s · 2.00s, each ±0.20s** | 3 | 35 raw per unparried window (105 if all three land), +1 Burning stack per landed window |

- **Kitable:** N/A — never moves. Breaking line of sight is the counter, same as the Singer.
- **Assess 0–1:** "It's not hunting. It's still pouring." · **Assess 2+:** "The toll's just pressure. The pour is the real fight, and it comes in three."
- **White Salts drop:** 50. **Insight:** +1/+1.
- **Boss Gimmick:** Molten Pour follows the standard chain rule — **all three parried → Tier 1 Open on The Crack**, no second stopwatch; **miss any window → take that beat's damage/Burning and the rest automatically.** Sever The Crack (base 350 at ×2.0 = 175 raw in one hit) to end the fight regardless of remaining HP. **Distinct twist:** every time all three Molten Pour windows land uncontested, the pour itself widens The Crack — its sever threshold **permanently drops by 50** for the rest of the fight (350 → 300 → 250 → …), an escalating vulnerability rather than a static number. Otherwise pure attrition — Founding Toll never stops, Influence climbs the whole fight, save DC rising with stack count. Sever never required (Ruleset §3).
- **Habit punished:** tanking the pour in the open instead of reading all three windows. **Dismember threat:** Moderate (no melee of its own, but Burning stacks compound if the chain lands clean). **Retreat always reachable:** Y.

## Monster Template (blank)

- **Archetype:** · **Level Range:** · **HP:** · **Move Budget/Pattern:** · **Scale Band:** · **Flavour:**
- **Limbs** (standard humanoid defaults per Ruleset §10 — list only deviations/non-standard here):

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|||||||

Implements/objects (bell, shield, eye) go in this table too — see Ruleset §10 for how they resolve.

**Attacks:**

|Attack|Type|Tell|Window|Tier|Hit Effect|Status Type|Retaliation?|Miss Punish|
|-|-|-|-|-|-|-|-|-|
||||||||||

- **Kitable:** · **Assess 0–1:** · **Assess 2+:** · **White Salts drop:** · **Insight granted:**
- **Boss Gimmick (else N/A):** · **Habit Punished:** · **Falls-For-It Result:** · **Dismember Threat:** · **Retreat Reachable:**

---

# 2. Weapon Template

One page per weapon — identity, damage, passive, sever maths together.

*Damage formula, grade table and sever maths: Ruleset §4 and §10. Not restated here.*

**ESV touchpoints** (bible-only working aid): raw 8→ESV 8 · raw 20→ESV 20 · raw 40→ESV 33 · raw 99→ESV ~47.

## Weapon 1 — Paring Knife *(floor entry)*

- **Type:** Quick · **Stat/Grade:** Skill/E · **Hands:** One
- **Acquisition:** not found — the mechanical floor a backstory weapon lands at or above.
- **Base:** 20 (Damage Floor). Light = 20+ESV×0.3 · Heavy = 40+ESV×0.45.
- **Worked rows:** ESV 8 → 22/44 · ESV 47 → 34/61.
- **Passive:** none — the baseline everything else compares against. **Insight Gate:** none.
- **Sever viability:** none at any ESV — floor weapons never sever, at any Strength.

## Weapon 2 — The Salvage Launcher

- **Type:** Reach · **Stat/Grade:** Skill/D · **Hands:** Two
- **Acquisition:** commissioned (hub engineer), not found — built to fire existing Powder Charge capsules. Character-specific.
- **Base:** 30, single shot type (no Light/Heavy split). Shot = 30+ESV×0.5.
- **Worked rows:** ESV 8 → 34 · ESV 17 → 38 · ESV 47 → 53.
- **Passive — Powder Charge (ranged variant):** fires loaded only, no capsule = no shot. Loading = universal Fast Action (0m). No timing check — guaranteed detonation, traded for finite ammo. On hit: 1 Discombobulation, automatic.
- **Range:** 8m. **Movement cost to fire:** 1m (Light-tier, no Heavy variant to price separately). **Ammo:** drawn from Hub Kit capsule stock (4 standard). Empty = treat as Fists.
- **Sever viability:** none at any ESV — concussive, not bladed, not built for it.

## Weapon 3 — Metal Knuckles (paired)

Lloyd's self-made twin knuckledusters, rigged to detonate loaded Powder Charge capsules. Lost to the Singer session 3, recovered session 6, back in active use.

- **Type:** Quick · **Stat/Grade:** Skill/D · **Hands:** One
- **Acquisition:** backstory weapon, character-specific, not generally found.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75. **Worked rows:** ESV 18 → 31/58.
- **Passive — Powder Charge (melee variant):** load a capsule as a universal Fast Action (0m), same as the ranged variant. Unlike the Launcher, firing it is a **timed** detonation: target 1.00s, ±0.15s base, widened by Insight window bonus. **Confirmed effects (session 7):** success = ×1.5 damage modifier on that hit, plus 1 Discombobulation to the target. Failure = the wielder takes 2 Blood Loss stacks and the turn ends immediately with no leftover movement to spend — harsher than a whiffed self-Rally, deliberately, since the capsule is armed either way.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 4 — The Guillotine Shears

*Fills the Tideglass Cleaver row (Ruleset §4) — first Bible instance of that archetype.*

- **Type:** Quick · **Stat/Grade:** Skill/C · **Hands:** Optional
- **Acquisition:** found — Paper Mill recipe, instance loot.
- **Base:** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05.
- **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Passive:** a mounted paper-guillotine blade cut down into a dual-handled shear-sword. Light attacks close twice — the shear snapping shut — second hit at 50% of the first (rounded up). Heavy is a single full-weight cut, shears held wide.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 5 — The Foundry Wedge

*Fills the Cautery Saw row (Ruleset §4) — the canon "best raw sever weapon" archetype.*

- **Type:** Heavy · **Stat/Grade:** Strength/B · **Hands:** Two
- **Acquisition:** found — Cold Forge recipe, instance loot.
- **Base:** 30. Light = 30+ESV×0.9 · Heavy = 60+ESV×1.35.
- **Worked rows:** ESV 8 → 38/71 · ESV 47 → 73/124.
- **Passive:** an iron wedge-cleaver used to split cooling ingots off the slag. No gimmick beyond raw weight — this is the weapon you reach for specifically to sever, the same design role Cautery Saw fills.
- **Sever viability:** the game's benchmark sever weapon. Str 8 → ESV 8 → Heavy 71 (below every threshold). Str 40 → ESV 33 → Heavy ~109 (still under Head's 120). Str 99 → ESV 47 → Heavy 124, clears the Head's 120-raw line outright.

## Weapon 6 — The Retractor

*Fills the Birthing Hook row (Ruleset §4) — first Bible instance of that archetype.*

- **Type:** Reach · **Stat/Grade:** Skill/C · **Hands:** Optional
- **Acquisition:** found — Gaslight Ward recipe, instance loot.
- **Base:** 26. Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05.
- **Worked rows:** ESV 8 → 32/61 · ESV 47 → 59/102.
- **Passive:** a long surgical retractor-hook, built to hold an incision open — now opens something else. Wide sweeping arcs; a single swing (Light or Heavy) can be declared against two adjacent limbs on the same target instead of one, each resolved at full weight, at the cost of using the tighter of the two limbs' precision tolerances for both (Ruleset §10) — strong against multi-limb targets, genuinely riskier on single hard-to-hit ones.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 7 — The Brake Spike

*Fills the Funicular Spike row (Ruleset §4) — first Bible instance of that archetype. Ties back to the funicular carriage from the campaign's opening beat.*

- **Type:** Reach/thrust · **Stat/Grade:** Strength/B · **Hands:** Two
- **Acquisition:** found — deep in the Choir Deep recipe, near the original funicular housing.
- **Base:** 28. Light = 28+ESV×0.9 · Heavy = 56+ESV×1.35.
- **Worked rows:** ESV 8 → 36/67 · ESV 47 → 71/120.
- **Passive:** an iron emergency brake-spike, once driven into a funicular rail to stop runaway carriages. Any hit (Light or Heavy) against a staggered target deals +25% raw — it was built to stop something already losing momentum, and still does.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty. (At ESV 47, Heavy exactly clears the Head's 120-raw line.)

## Weapon 8 — The Toll-Press

*Fills the Brass Token Press row (Ruleset §4) — first Bible instance of that archetype.*

- **Type:** Trick (Skill↔Strength) · **Stat/Grade:** compact Skill/D · full-transform Strength/B · **Hands:** Switches (One compact, Two full-transform)
- **Acquisition:** found — hub sub-basement, tied to the toll/token economy already in play. Character-agnostic.
- **Base (compact, Quick):** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75. **Worked rows:** ESV 8 → 26/50 · ESV 47 → 46/80.
- **Base (full-transform, Heavy):** 34. Light = 34+ESV×0.9 · Heavy = 68+ESV×1.35. **Worked rows:** ESV 8 → 42/79 · ESV 47 → 77/132.
- **Passive:** a hand-press stamp for validating tolls, folded compact by default. Folding/unfolding is a Fast Action (0m), matching weapon-swap economy (Ruleset §7). **Insight Gate:** full transform requires Insight Tier 1 — below it, the press physically won't unfold; Skill governs it compact either way.
- **Sever viability:** compact — none at any ESV, it's a stamp, not a blade. Full-transform — standard per the general limb-model sever thresholds.

## Weapon 9 — The Kiln Fork

- **Type:** Heavy · **Stat/Grade:** Strength/C · **Hands:** Two
- **Acquisition:** found — Ember Wards / Cold Forge recipes, instance loot.
- **Base:** 28. Light = 28+ESV×0.7 · Heavy = 56+ESV×1.05.
- **Worked rows:** ESV 8 → 34/65 · ESV 47 → 61/106.
- **Passive:** a two-tined furnace fork, still kiln-hot at the tines. Any Heavy hit that connects applies 1 Burning stack. A Heavy landed against a Discombobulated target deals an additional +25% raw — built to finish something already reeling.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 10 — The Gravedigger's Maul

- **Type:** Heavy · **Stat/Grade:** Strength/C · **Hands:** Two
- **Acquisition:** found — general Vault reward, unlinked to a specific recipe.
- **Base:** 26. Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05.
- **Worked rows:** ESV 8 → 32/61 · ESV 47 → 59/102.
- **Passive:** a lead-headed grave-maul. Any Heavy hit that staggers a limb also knocks the target back 2m — pure crowd control, not damage. Built for a Strength build that wants space, not just numbers.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 11 — The Bell-Yoke Hammer

- **Type:** Heavy · **Stat/Grade:** Strength/C · **Hands:** Two
- **Acquisition:** found — Bellfounder's Pit recipe, instance loot.
- **Base:** 27. Light = 27+ESV×0.7 · Heavy = 54+ESV×1.05.
- **Worked rows:** ESV 8 → 33/63 · ESV 47 → 60/104.
- **Passive:** a cast bronze yoke-hammer salvaged from a dead bell-foundry. A fully-landed Heavy hit tolls once — every enemy within 3m of the target (not the target itself) takes 1 Influence stack. Melee weapon, incidental AOE support-pressure.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 12 — The Coalback Pick

- **Type:** Heavy · **Stat/Grade:** Strength/B · **Hands:** Two
- **Acquisition:** found — Coal Seam recipe, instance loot.
- **Base:** 27 (deliberately 10% below the standard Strength/B baseline — see Passive). Light = 27+ESV×0.9 · Heavy = 54+ESV×1.35.
- **Worked rows:** ESV 8 → 35/65 · ESV 47 → 70/118.
- **Passive:** a narrow-pointed mining pick. Trades raw power for a genuine sever specialization: this weapon's own sever thresholds are reduced 15% (**Head 102 · Arm 262 · Leg 340**, down from the standard 120/308/400) instead of the usual −10% Base tax buying nothing back.
- **Sever viability:** Head becomes viable noticeably earlier than a standard weapon — Heavy clears its own reduced 102-raw Head line around ESV ~40 (Str ~85+), well before a standard weapon would clear 120.

## Weapon 13 — The Twin Boning Hooks *(paired)*

- **Type:** Quick · **Stat/Grade:** Strength/D · **Hands:** One (paired)
- **Acquisition:** found — general Vault reward.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75.
- **Worked rows:** ESV 8 → 26/50 · ESV 47 → 46/80.
- **Passive:** twin dock-hooks, one per hand. A Light attack that staggers a limb lets the off-hand immediately follow with a free Light strike at the same target, 0m cost — a genuine paired-weapon combo, distinct from Metal Knuckles' timed-risk identity. Fast, Strength-governed, built for a brawler who doesn't want to go two-handed.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 14 — The Choir Needle

- **Type:** Quick · **Stat/Grade:** Skill/D · **Hands:** One
- **Acquisition:** found — Choir Deep recipe, instance loot.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75.
- **Worked rows:** ESV 8 → 26/50 · ESV 47 → 46/80.
- **Passive:** a long embroidery needle-blade. Self-initiated called shots (Ruleset §10 — an unparryable grasp, a stationary target) using this weapon have their tightened tolerance eased back one band, toward the limb's own baseline. Built specifically for ambush/precision play rather than raw output.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 15 — The Split-Tongue Dagger *(paired)*

- **Type:** Quick · **Stat/Grade:** Skill/D · **Hands:** One (paired)
- **Acquisition:** found — general Vault reward.
- **Base:** 20. Light = 20+ESV×0.5 · Heavy = 40+ESV×0.75.
- **Worked rows:** ESV 8 → 24/46 · ESV 47 → 44/76.
- **Passive:** twin narrow daggers. As one Action, both blades can strike the same limb back to back — each hit resolves independently at full weight against that limb's stagger/sever meter, rather than one hit at reduced value. Lower Base than most Skill/D options; the payoff is in the doubled meter contribution, not raw per-swing damage.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 16 — The Longhand Rapier

- **Type:** Reach · **Stat/Grade:** Skill/C · **Hands:** One
- **Acquisition:** found — general Vault reward.
- **Base:** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05.
- **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Passive:** an absurdly long, thin dueling blade. Every Precision Strike stopwatch (Ruleset §10, limb multiplier >1.0) is widened one full tolerance band while wielding this weapon — a true finesse pick, built entirely around called shots rather than raw weight.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 17 — The Cage-Wire Whip

- **Type:** Reach · **Stat/Grade:** Skill/D · **Hands:** One
- **Acquisition:** found — Hollow Aviary recipe, instance loot.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75.
- **Worked rows:** ESV 8 → 26/50 · ESV 47 → 46/80.
- **Passive:** birdcage wire, braided into a whip. Any hit costs the target 1 extra metre of movement the next time it tries to close distance on the wielder that encounter (once per landed hit, doesn't stack past a single extra metre at a time) — a genuine enemy-mobility debuff, not a player-side status.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 18 — The Bone Comb

- **Type:** Quick · **Stat/Grade:** Skill/E · **Hands:** One
- **Acquisition:** found — general Vault reward, low-tier/early pickup.
- **Base:** 20 (the floor). Light = 20+ESV×0.3 · Heavy = 40+ESV×0.45.
- **Worked rows:** ESV 8 → 23/44 · ESV 47 → 35/62.
- **Passive:** a wide-toothed carved bone comb, honed at every tine. Any Light attack costs 1m less to follow up with another action — the game's other accessible mobility-first Quick weapon alongside Paring Knife, for a build leaning on movement over raw output.
- **Sever viability:** none at any ESV — floor-tier weapon, same tradeoff as Paring Knife.

## Weapon 19 — The Censer Flail

- **Type:** Reach · **Stat/Grade:** Resolve/C · **Hands:** Two
- **Acquisition:** found — Reliquary recipe, instance loot.
- **Base:** 26. Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05.
- **Worked rows:** ESV 8 → 32/61 · ESV 47 → 59/102.
- **Passive:** a swinging censer on a heavy chain, trailing incense smoke. A fully-landed Heavy hit clears 1 stack from any single status track on an ally within 3m — a support effect delivered through an attack, not a cast. First weapon in the game to combine melee damage with ally-support, letting a Resolve build fight and hold up a companion at the same time.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 20 — The Sigil Lash

- **Type:** Quick · **Stat/Grade:** Resolve/D · **Hands:** One
- **Acquisition:** found — Choir Deep / Reliquary recipes, instance loot.
- **Base:** 20. Light = 20+ESV×0.5 · Heavy = 40+ESV×0.75.
- **Worked rows:** ESV 8 → 24/46 · ESV 47 → 44/76.
- **Passive:** a leather lash inked with warding sigils. On hit, the target's resistance to Insanity/Influence pressure drops −1 for 1 round (stacks additively with Maria's Steady Faith, a different source). A Resolve weapon built to soften enemies up for the party's status stacking rather than deal raw damage itself.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 21 — The Hymnal Truncheon

- **Type:** Heavy · **Stat/Grade:** Resolve/C · **Hands:** One
- **Acquisition:** found — Choir Deep recipe, instance loot.
- **Base:** 26. Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05.
- **Worked rows:** ESV 8 → 32/61 · ESV 47 → 59/102.
- **Passive:** a thick prayer-book bound in iron plates, swung like a club. Successful Heavy hits apply 1 Influence stack to the target on top of raw damage (Enemy-side Influence Overload, Ruleset §5) — a "battle cleric" option, one-handed despite the Heavy tag, built around a Resolve build that still wants to swing something.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 22 — The Reliquary Chime

- **Type:** Reach · **Stat/Grade:** Resolve/D · **Hands:** One
- **Acquisition:** found — Reliquary / Bellfounder's Pit recipes, instance loot.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75.
- **Worked rows:** ESV 8 → 26/50 · ESV 47 → 46/80.
- **Passive:** a hand-chime on a short rod, usable out to 6m without being a dedicated ranged weapon. On hit, applies 1 Discombobulation. Low raw output by design — this is a crowd-control pick for a Resolve build, not a damage one.
- **Sever viability:** standard, per the general limb-model sever thresholds — no weapon-specific bonus or penalty.

## Weapon 23 — The Grief-Bell

- **Type:** Quick · **Stat/Grade:** Resolve/E · **Hands:** One
- **Acquisition:** found — general Vault reward, low-tier/early pickup.
- **Base:** 20 (the floor). Light = 20+ESV×0.3 · Heavy = 40+ESV×0.45.
- **Worked rows:** ESV 8 → 23/44 · ESV 47 → 35/62.
- **Passive:** a small hand-bell. Ringing it as a Fast Action (0m) grants an ally within 5m +1 to their next Insanity/Influence save — a direct, cheap support action baked into an otherwise unremarkable Quick weapon. The floor-tier entry for the Resolve column, same role as Paring Knife/Fists fill for Skill/Strength.
- **Sever viability:** none at any ESV — floor-tier weapon, same tradeoff as Paring Knife.

## Weapon 24 — The Coil-Spring Gauntlet

- **Type:** Trick (Skill↔Strength) · **Stat/Grade:** compact Skill/D · extended Strength/C · **Hands:** Switches (One compact, Two extended)
- **Acquisition:** found — Cold Forge recipe, instance loot.
- **Base (compact, Quick):** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75. **Worked rows:** ESV 8 → 26/50 · ESV 47 → 46/80.
- **Base (extended, Heavy):** 28. Light = 28+ESV×0.7 · Heavy = 56+ESV×1.05. **Worked rows:** ESV 8 → 34/65 · ESV 47 → 61/106.
- **Passive:** a brass knuckle-gauntlet with a coiled spring core. Extending is a Fast Action (0m). Extended-form Heavy hits that stagger a limb preferentially target a leg if the wielder chooses (piston recoil knocks the stance out from under it) and knock the target back 1m. **Insight Gate:** full extension requires Insight Tier 2 — one tier past the Toll-Press, reflecting the stronger payoff.
- **Sever viability:** standard, per the general limb-model sever thresholds, in either form.

## Weapon 25 — The Furl-Blade Parasol

- **Type:** Trick (Skill↔Skill, Type switches) · **Stat/Grade:** Skill/C both forms · **Hands:** Switches (One folded, Two unfurled)
- **Acquisition:** found — Hall of Broken Mirrors recipe, instance loot.
- **Base (folded, Quick):** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05. **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Base (unfurled, Reach):** 24 — identical formula, Type changes to Reach. Same worked rows.
- **Passive:** a slim rapier built into a parasol shaft. Unfurling/folding is a Fast Action (0m), no Insight gate — same stat and grade both ways, so nothing about raw output changes, only the tradeoff. While unfurled: incoming Light attacks against the wielder are reduced by a flat −5 raw (the canopy actually blocks something), at the cost of Reach's slower repositioning compared to the folded Quick form.
- **Sever viability:** standard, per the general limb-model sever thresholds, in either form.

## Weapon 26 — The Segmented Choir-Flail

- **Type:** Trick (Strength↔Strength, Type/Hands switch) · **Stat/Grade:** Strength/D compact · Strength/C extended · **Hands:** Switches (One compact, Two extended)
- **Acquisition:** found — Loom Room recipe, instance loot.
- **Base (compact, Quick):** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75. **Worked rows:** ESV 8 → 26/50 · ESV 47 → 46/80.
- **Base (extended, Reach):** 28. Light = 28+ESV×0.7 · Heavy = 56+ESV×1.05. **Worked rows:** ESV 8 → 34/65 · ESV 47 → 61/106.
- **Passive:** compact nunchaku-style jabs, or unspooled (Fast Action, 0m) into a full chain-flail. Extended-form Heavy attacks are the first **player-side** use of the stopwatch on offense rather than defense: the swing resolves as two sequential mini-windows (0.80s, 1.30s, each ±0.20s). Both hit within their targets → full combined raw, no penalty. Miss either → that swing's total raw is halved. No Insight gate — the risk/reward is the whole point of the weapon, not a bonus layered on top.
- **Sever viability:** standard, per the general limb-model sever thresholds, in either form.

## Weapon 27 — The Twin-Reed Bow-Blade

- **Type:** Trick (Skill↔Skill, Type switches) · **Stat/Grade:** Skill/C melee · Skill/D ranged · **Hands:** Two, both forms
- **Acquisition:** found — general Vault reward, no single recipe tie.
- **Base (melee, Quick):** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05. **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Base (bow, Reach, single-shot — no Light/Heavy split):** 26. Shot = 26+ESV×0.5. **Worked rows:** ESV 8 → 30 · ESV 47 → 50.
- **Passive:** a curved short-sword that reconfigures (Fast Action, 0m) into a small recurve bow, drawing its own bolts from a built-in quiver rather than needing carried ammo. **Ammo:** 6 self-drawn bolts before requiring a hub restock (Hub Kit refill, same economy as the Salvage Launcher's capsules). Range 8m, 1m movement cost to fire, no timing check — the melee/ranged switch-hitter option for a Skill build, distinct from the Salvage Launcher's single dedicated ranged role.
- **Sever viability:** melee form — standard, per the general limb-model sever thresholds. Bow form — none at any ESV, same as the Salvage Launcher.

## Weapon 28 — The Widow's Cane

- **Type:** Trick (Skill↔Strength) · **Stat/Grade:** Skill/C compact · Strength/C extended · **Hands:** Switches (One compact, Two extended)
- **Acquisition:** found — general Vault reward, no single recipe tie — deliberately the most widely available Trick weapon.
- **Base (compact, Quick):** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05. **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Base (extended, Heavy):** 27. Light = 27+ESV×0.7 · Heavy = 54+ESV×1.05. **Worked rows:** ESV 8 → 33/63 · ESV 47 → 60/104.
- **Passive:** an elegant cane-sword that unfolds (Fast Action, 0m) into a lead-weighted cudgel-cane. No Insight gate, no bonus hook beyond the switch itself — deliberately the "plain" Trick weapon, for a build that wants to flex between finesse and power without committing to either, rather than chasing a flashy gimmick.
- **Sever viability:** standard, per the general limb-model sever thresholds, in either form.

## Weapon Template (blank)

- **Type (Quick/Heavy/Reach/Trick):** · **Stat/Grade:** · **Hands:** · **Acquisition:**
- **Base:** · **Light:** Base+ESV×grade · **Heavy:** 2×Base+ESV×grade×1.5
- **Worked rows:** ESV 8 → __/__ · ESV 47 → __/__
- **Passive:** · **Status Applied:** · **Insight Gate:**

**Sever viability:**

|Target|Min Raw|Viable at ESV|Notes|
|-|-|-|-|
|Head|120|||
|Arm|~308|||
|Leg|400|||

---

# 3. Player Character Sheet

Moved to its own live-state file — `deep-salts-character-sheet.md`. DM rewrites it after any significant change; single source of truth for HP, tracks, charges, limbs, Insight, inventory.

---

# 4. NPC Template

One page per NPC.

## NPC 1 — Robe Attendant *(floor entry)*

Zero mechanical function, zero dialogue, zero lore thread. *Not the reception clerk*, who is the recurring antagonist and always narrated as a DM moment, never a stat block.

- **Role:** background hub functionary. **Location:** hub only. **Fightable:** N.
- **Fixed appearance:** waxed-canvas apron, sleeves rolled, no eye contact. **Never changes** — the one exception to the hub's one-detail-changes rule.
- **On arrival:** hands over a towel, points once, says nothing. **Never** speaks first, answers, or acknowledges anything's wrong.
- **Dialogue:** non-verbal only — a nod, a shrug, a point at the exit, a slow head-shake. Never a spoken line.
- **Mechanical function:** robe/towel on first hub visit only, cosmetic. **Lore:** connects to nothing.

## NPC 2 — The Memory Vendor

- **Role:** deep-recess entity, not a hub fixture. Trades power for Insight, collects like a loan shark. **Location:** unconfirmed, not hub-accessible — "not a room, a depth. You get deep enough that it stops being able to avoid you." **Fightable:** N.
- **Fixed appearance:** undefined, genuinely unmet. **On arrival:** offers trades — permanent buffs or Scar removal, Insight only. **Never** accepts Salts/items/favors as payment.
- **Dialogue:** measured, transactional, unbothered by refusal · treats a missed payment as fact not threat · never raises its voice about invasion — it's just what happens next.
- **Mechanical function:**
  - **Buy-in trades:** spend Insight (score/tier/floor drop immediately) for a permanent effect, negotiated case-by-case, no fixed menu.
  - **Scar removal:** only route. Scar 1 = 6 Insight, Scar 2 = 10, Scar 3+ = higher — deliberately unpayable past the first in one sitting.
  - **Debt/toll:** larger trades can be a payment plan (e.g. "13 Insight across 2 runs"). Tracked as bookkeeping — no track, no rolls.
    - Missing a scheduled payment: flat 10% of that run's Vault banking, no escalation.
    - Refusing the toll (not just missing schedule): next reroll of that recipe comes back quietly worse (HP bump, extra body, seeded hazard).
    - Full repayment closes the debt clean regardless of missed payments along the way.
    - No interest accrues in Insight specifically (a scarce, non-renewable resource — avoids a softlock).
- **Lore:** tangled with the reception clerk's "brother" hook. Never revealed: true name, appearance, location.

## NPC Template — Persistent Companion variant

Same fields as standard, plus once recruited:
- **Recruited:** session/run + the hook that closed the deal. **Accompanies into:** which recipes (not necessarily all).
- **Stat block:** HP band, 1–2 actions, any gimmick — generated live on first accompanied run, recorded as canon.
- **Status:** Active / Held at hub / **Dead (permanent, no respawn).**

## NPC 3 — Maud

- **Role:** hub salt/item identifier and appraiser. Doesn't pry — except when something on her own personal list crosses the counter. **Location:** hub only. **Fightable:** N.
- **Fixed appearance:** undefined, never described in play. **On arrival:** IDs salts (5 Salts first ID, doubling per subsequent) or off-catalog items (8 Salts, separate scale). Has three standing salvage requests: sealed items, source-water, packing cloth.
- **Never** asks where an item came from or whose it was, as part of a standard ID. **Never says directly** why the three categories matter to her, or what a certain ring's symbol means.
- **Dialogue:** professional and unhurried on anything routine · goes still and flat the moment something personal surfaces · direct refusals, not deflection — "that's not mine to want" · asks to revisit rather than pretends it doesn't matter.
- **Mechanical function:** salt ID (5→10→20→40... doubling) · off-catalog ID (8 Salts flat) · buys sealed/found items outright, case-by-case (paid 20 for a sealed vessel unprompted) · salvage requests have no defined mechanical reward yet — relationship/lore thread, not a transaction.
- **Lore:** recognized a scratched symbol on a found ring on sight. Confirmed: she's buried someone who wore that mark, exactly once. Won't confirm/deny a connection to "Mirel" or the reception clerk's brother thread. Asked to be asked again another time — live, not closed.

## NPC 4 — Maria *(Persistent Companion)*

- **Role:** recruited support/arcane-offense companion. **Location:** recruited at the hub (Stillwell Hydro). **Accompanies into:** recipes situationally — her order's business means some places she won't set foot in; a fiction call each time, not a hard rule. **Fightable:** Y (targetable), but built to avoid melee entirely.
- **Recruited:** session 7, hub baths — approached Lloyd directly, unprompted. **Ruling (session 7):** story-initiated recruitment costs 0 — no Vault toll, no Insight spent. A future hub-bargained companion may carry a real price instead, decided per-instance when it comes up.
- **Fixed appearance:** hooded robes, sturdy boots built for trekking/fighting rather than standard habit footwear, a boot knife. Quiet, inquisitive, visibly uneasy around Lloyd's stoic/charming affect.
- **Dialogue:** soft-spoken, over-explains when nervous then catches herself · direct once committed to something · avoids talking about her order unprompted.
- **Stat block** *(generated live session 7, recorded as canon)*:
  - HP 55 · Move 8m · RES 24 (ESV 23) · Insight 0. One Action per turn, same economy as the player.
  - **Purging Flame** — AOE, RES/D, Heavy Action (3m), ranged cast up to 8m, 4m radius: 32 dmg to every enemy in the radius — and to Lloyd, if he's standing in it. No exception carved out for him.
  - **Judgment Spark** — single-target, RES/E, Light Action (1m), ranged: 27 dmg. Deliberately her weakest number; can never be used for called shots or limb targeting.
  - **Imbue Weapon** — Full Action (2m): +12 flat damage to Lloyd's next attack, light or heavy, whichever he swings first. One charge at a time, doesn't stack with itself, does stack with the Charm (different source — hers scales off RES, the Charm is a flat item bonus).
  - **Steadying Grace** — Full Action (2m): usable only the turn immediately after Lloyd takes a hit and doesn't land a qualifying attack that turn (his Rally window closing). Recovers 50% of whatever grey Rally HP is currently pending into real HP; the other half is lost, same as a whiffed self-Rally. Bound entirely to the existing Rally system — no new resource.
  - **Steady Faith** *(passive)* — within 5m of Lloyd, he gets −1 to his own Insanity/Influence save DC.
  - **Boot Knife** — Skill/E, Base 12, backup melee only, not sever-viable. Can Hold/parry like Lloyd if something closes on her, but it's not her preference — she backs off and casts before she trades hits.
- **Status:** Active.
- **Lore:** member of the Church of St Narrikon's Redemption of Mankind — a "sinister background" flagged pre-session, not yet surfaced in play. Doesn't want the Deep Salts everyone else dives for; what she actually wants is unstated. Open thread.

## NPC Template (blank)

- **Role:** · **Level Range:** · **Location(s):** · **Fightable (Y/N):**
- **Fixed appearance:** · **What changes between appearances:** · **On arrival:** · **Never does:** · **Never says directly:**
- **Dialogue seeds:** 3–5 fragments, tone not scripts.
- **Mechanical function:** services/items/gated info/behaviour shifts.
- **Lore thread:** connects to · piece together over time · never revealed.

---

# 5. Item Template

## Item 1 — Scour *(floor entry)*

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** removes exactly 1 Corrosion stack, nothing else.
- **Duration:** instant · **Consumable:** Y · **Carry Limit:** 5 (mirrors Corrosion's cap)
- **Insight Gate:** none. **Limb Requirement:** a working hand/arm.
- **Acquisition:** mineral scrapings from the source-spring terraces; cheap/free at the apothecary stall.

## Item 2 — The Beckoner

Lloyd's, recovered session 6. First item to ever push Influence onto an enemy — no prior mechanic covered this.

- **Type:** Passive-while-uncovered (session 6 redefinition — supersedes the old "Action Item, targeted" version below) · **Consumable:** N (Constant, unlimited uses)
- **Effect:** always active in lore; mechanically inert while wrapped. **Uncovered, it applies 1 Influence stack/turn to Lloyd and every enemy within an 8m radius**, no targeting needed, no Action cost to sustain — just to physically wrap or unwrap it (Fast Action, in hand). Re-wrapping stops it dead, immediately, for everyone in range.
- **Intended play pattern:** carry it uncovered near an enemy to weaken them, then re-cover it to stop affecting the area — including stepping outside the 8m radius, which has the same effect as re-wrapping for anyone who leaves it.
- **Status Type:** Track (Influence), both sides, per turn while uncovered and in range
- **Mechanical gap, now resolved (session 6):** enemy Influence overload rule now exists — see Ruleset §5. **Residual Influence on Lloyd is sticky** — see Ruleset §5, doesn't clear on wrap/distance like normal sources, only on rest or fully divesting the item.
- **Narrative hook:** while anyone (Lloyd included) is within its uncovered radius, the idol presses for a name spoken to it. He's been warned not to. Consequences unspecified — deliberately unresolved, do not invent an answer ahead of the table.

## Item 3 — The Charm

Lloyd's, recovered session 6.

- **Type:** Action Item · **Consumable:** Y, Uses: 1, destroyed on use · **Insight Gate:** Tier 3 (Insight 6+)
- **Effect (player's choice at moment of use):** either +1 bonus damage die on the next attack (sized ~base÷4, same convention as the Bloody visceral mod), or widen the next parry/precision window by +0.10s.

## Item 4 — Clean Source-Water Flask

Lloyd's, recovered session 6 alongside the rest of the gear forfeited to the Singer — the "clean variant" referenced generically in the ruleset's Action Items list, this specific instance's numbers pinned down.

- **Type:** Action Item · **Action Cost:** full Action, 2m · **Consumable:** Y, Uses: 1
- **Effect:** heals 75% of Max HP. **No Influence stack** — unlike the standard source-water flask, this is the power without the vulnerability tax. Rarer for exactly that reason.

## Item 5 — The Note-Keeper's Robe

Found session 7, Choir Deep (vestry sub-locale) — hung apart from the rest of the vestments, dry where everything else was sodden.

- **Type:** Passive/Equip · **Action Cost:** none, worn · **Consumable:** N
- **Effect:** none yet — deliberately unresolved.
- **Lore:** carries a stitched vow along the collar, legible only via Tier 4+ Insight: *"I take the note up so no other throat has to open."* Lloyd reads it as belonging to the Singer he killed (or a prior wearer of that role) — unconfirmed in-fiction. Maria (Insight 0) could not perceive any script on it at all.
- **Open design question:** is this genuine Insight-gated perception of something real, or something else entirely. Do not pre-resolve — this is meant to stay live.

## Item Template (blank)

**Type:** · **Action Cost:** · **Effect:** · **Status Applied:** · **Duration:** · **Consumable:** · **Carry Limit:** · **Insight Gate:** · **Limb Requirement:** · **Acquisition:**

---

# 6. Status Effect Template

## Status Effect 1 — Off-Balance *(floor entry, Immediate)*

- **Type:** Immediate · **Affects:** currently only produced by the player's own missed Precision Strike (band 1.26–1.50). **Resisted on application:** N.
- **Effect:** −1m movement, next turn only. **Duration:** 1 turn, expires automatically.
- **Combos:** compounds tactically with a staggered leg or Discombobulation's movement scrambling.

*Blood Loss and Rupture are fully defined in Ruleset §5 — not restated here. This section holds only effects the ruleset doesn't cover.*

## Status Effect Template (blank)

**Type (Immediate/Track/Tick):** · **Affects:** · **Resisted on application:**
**If Immediate:** effect · duration · cleared early?
**If Track:** stacks per application · effect per stack/turn · cap · overflow effect · clear condition
**If Tick:** applied value · effect while active (counts down 1/turn automatically)
**Interactions:** dangerous combos · countered by · sources

---

# 7. Currency / Collectible Template

## Currency/Collectible 1 — The Token That Isn't Yours *(floor entry)*

Not White Salts — the weakest possible Key Item, seeded and currently doing nothing on purpose.

- **Category:** Key Item (bordering Story). **Risk Status:** neither Purse nor Vault — stays with you. **Lost on death/retreat:** N/N.
- **Acquisition:** one-time only, found in the robe pocket entering the deep cure. No known second copy or way to lose the first.
- **Spend options:** none yet — fits no slot, opens nothing, deliberately.
- **Flavour:** worn brass, warm to the touch even when nothing else is. Doesn't match the clerk's own token; nobody at the hub will take it back.

**Template fields:** Category · Risk Status · Lost on Death?/Retreat? · Acquisition (base drop / bonus conditions) · Spend Options · Flavour.

---

*Sections 8–10 (Mechanic Index, Book Plan, Known Gaps) live in the dev log.*
