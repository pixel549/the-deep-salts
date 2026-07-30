# THE DEEP SALTS
**Design Bible — Entity Templates**

Companion to the ruleset. **Load this plus the ruleset and character sheet when running the game.** Mechanic index/book plan/known gaps live in the dev log — do NOT load that during play.

*Version 4.5. Session attribution and change history live in the dev log, not here.*

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
- **Limbs:** standard defaults, plus non-standard: **Bell** — implement, not a limb (Ruleset §10): multiplier ×2.0, sever 40 raw. Deals full HP damage on the hit like any other strike. Breaking it permanently disables Hollow Bell for the encounter — and the Bellkeeper has no other attack, so a destroyed bell leaves it harmless.

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
- **All three parried →** Tier 1 Open. It collapses out of the spin, the weak point is Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9) — not automatic.
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
- **Limbs:** standard defaults + **The Open Throat** (weak point) — multiplier ×2.0, stagger 240, sever 400.

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
- **All three parried →** Tier 1 Open. It collapses out of the whip, the weak point is Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9) — not automatic.
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
- **All three parried →** Tier 1 Open, the weak point is Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9) — not automatic.
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
- **All three parried →** Tier 1 Open, the weak point is Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9) — not automatic.
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
- **Boss Gimmick:** Foundry Reckoning is the Marshal's real opening, same chain rule as any Flailer: **all three windows parried → Tier 1 Open on the Furnace Door**, Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9), not automatic. **Miss any window → take that beat's 40 raw + Burning and every remaining beat automatically.** Sever the Furnace Door — **300 at ×1.75 ≈ 171 raw in one hit** (per Ruleset §10's threshold ÷ multiplier) — and the fight ends regardless of remaining HP. Reachable, not trivial, at current gear. Sever never required (Ruleset §3).
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
- **Boss Gimmick:** Molten Pour follows the standard chain rule — **all three parried → Tier 1 Open on The Crack**, Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9), not automatic; **miss any window → take that beat's damage/Burning and the rest automatically.** Sever The Crack (base 350 at ×2.0 = 175 raw in one hit) to end the fight regardless of remaining HP. **Distinct twist:** every time all three Molten Pour windows land uncontested, the pour itself widens The Crack — its sever threshold **permanently drops by 50** for the rest of the fight (350 → 300 → 250 → …), an escalating vulnerability rather than a static number. Otherwise pure attrition — Founding Toll never stops, Influence climbs the whole fight, save DC rising with stack count. Sever never required (Ruleset §3).
- **Habit punished:** tanking the pour in the open instead of reading all three windows. **Dismember threat:** Moderate (no melee of its own, but Burning stacks compound if the chain lands clean). **Retreat always reachable:** Y.

## Monster 39 — Handfall

- **Archetype:** Swarm (elite) · **Level Range:** 5–20 · **HP:** 450 · **Move:** 4m, flows over any surface, never climbs so much as spreads · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A low tide of pale hands, wrist-deep and cut off clean, moving together with no body to belong to. No two are the same size. They test a surface before they cross it, the way a hand tests bathwater.
- **Limbs:** **no standard limb entries at all.** Single entry below. Precision Strike cannot be declared against Handfall — there is no anatomy to be greedy about, and any called shot resolves as a plain Mass hit.

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Mass|×1.0|—|—|—|**Yes**|

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Undertow | Light | None — unparryable, no windup | N/A | N/A | 15 raw + 1 Influence to every creature within 2m | N/A | N/A |
| Closing Fist | Heavy | "A dozen hands stack into a single column and cock back." | Target 1.30s, ±0.20s | 1 | 45 raw + 1 Blood Loss | Standard | The column collapses; it re-forms over ~2 player actions |

- **Kitable:** Y. **Assess 0–1:** "There's nothing to aim at." · **Assess 2+:** "It has no anatomy. Sever, stagger and called shots are all off the table — this one dies to raw HP damage and nothing else. Area damage is worth more than accuracy here."
- **White Salts drop:** 16. **Insight:** +1/+0. **Habit punished:** called-shot dependency. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 40 — The Salt Lung

- **Archetype:** Anchor (elite) · **Level Range:** 5–20 · **HP:** 900 · **Move:** 0m — rooted, permanently · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A wet grey organ the size of a bathing trough, sunk into a wall inside a knot of pipework it has grown into rather than been plumbed to. It inflates, holds, and lets go. The room's air changes with it.
- **Limbs:** no standard entries. Two bespoke:

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Bronchial Seam *(weak point)*|×2.0|—|—|300|N|
|Body|×1.0|—|—|—|**Yes**|

- **Severing the Seam kills the Lung outright**, regardless of remaining HP. 300 at ×2.0 = 150 raw in one hit.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Exhale | Aura | None — unparryable. Fires every other turn. | N/A | N/A | 1 Corrosion to every creature in the room | N/A | N/A |
| Draw | Aura | "The seam pulls tight and the air in the room starts moving toward it." | Target 1.60s, ±0.25s | 1 | Target pulled 3m toward the Lung and loses 2m from next turn's movement budget. No raw damage. | N/A | Deflates for a beat |

- **Kitable:** N/A — never moves, never follows. Walking out of the room is a complete counter.
- **Assess 0–1:** "It isn't fighting. It's doing something to the room." · **Assess 2+:** "It has no attack worth the name. It just makes the room cost something to stand in, and it can keep that up longer than you can. Kill the seam or leave."
- **White Salts drop:** 22. **Insight:** +1/+0. **Habit punished:** treating every encounter as a fight. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 41 — The Ambulatory Bath

- **Archetype:** Brute · **Level Range:** 10–20 · **HP:** 1600 · **Move:** 4m lurching walk on four cast-iron feet · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A clawfoot bath walking on its own feet, full to the brim and never spilling however it moves. Something is in the water. In all the time it has been walking, it has never once surfaced.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Foot ×4|×0.75|300|2 turns|400|N|
|Rim|×1.0|800|—|—|N|
|The Water *(implement)*|×2.0|—|—|250|N|

- Sever **two feet** and it is permanently grounded — Move drops to 0m for the rest of the encounter. Sever the Water (drain it, 125 raw at ×2.0) and the occupant dies with it: **the Bath dies outright regardless of HP.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Slosh | Ranged | "The surface heaves toward you without the bath having moved." | Target 1.50s, ±0.20s | 1 | 35 raw + 1 Corrosion | Standard | Refills over a beat |
| Overturn | Heavy | "It rears back onto two feet and hangs there." | Target 1.90s, ±0.20s | 2 | 85 raw, and the target is pinned beneath it — loses their next turn unless a **Strength DC 14** check is passed as a Fast Action | Standard | Long, ugly righting recovery |

- **Kitable:** Y in open ground, N in a confined room. **Assess 0–1:** "Don't let it get above you." · **Assess 2+:** "Two feet off and it stops being mobile. But the water is the real target — drain it and whatever's inside goes with it."
- **White Salts drop:** 30. **Insight:** +1/+0. **Habit punished:** fighting it in a room with no space to circle. **Dismember threat:** Very High. **Retreat always reachable:** Y.

## Monster 42 — The Gullet Run

- **Archetype:** Tide (elite) · **Level Range:** 8–20 · **HP:** 1200 · **Move:** 0m — it *is* a 12m stretch of corridor · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A passage that is wet in a way that isn't condensation. The walls are ribbed at even intervals and the ribs are not structural. Standing in it, the floor is very slightly warmer than the air.
- **Limbs:** no head, no torso, no anatomy in the usual sense.

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Ring Muscle ×6 *(spaced 2m apart along its length)*|×1.0|200|1 turn|250|N|

- **Sever any three of the six Ring Muscles and the Gullet Run dies**, regardless of remaining HP. It never leaves the corridor and the corridor never stops being it.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Swallow | Aura | None — unparryable, resolves at the end of every turn a creature is standing inside it | N/A | N/A | Target is moved 2m **deeper** into the run, involuntarily. No damage. | N/A | N/A |
| Bile Sheet | Ranged/Aura | "A wet ring travels down the passage toward you." | None — unparryable | N/A | 20 raw + 2 Corrosion to everything inside the run | N/A | N/A |

- **Kitable:** N/A. The counter is leaving — but Swallow is actively working against that, so the exit gets further away every turn spent hesitating.
- **Assess 0–1:** "The corridor is wrong. It's breathing." · **Assess 2+:** "It's one animal and you're inside it. Six rings, cut three and it dies. Or turn around now — but it's pushing you the wrong way, so decide fast."
- **White Salts drop:** 28. **Insight:** +1/+0. **Habit punished:** dithering. **Dismember threat:** None — it cannot take a limb. **Retreat always reachable:** Y, but the cost climbs each turn.

## Monster 43 — Kiln-Moth

- **Archetype:** Burster · **Level Range:** 5–20 · **HP:** 500 · **Move:** 9m flight, erratic, genuinely three-dimensional — uses ceiling height as cover · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Wings the span of a doorway on a body no bigger than a dog. The wings are dusted with something that catches the light, and then catches. It orients on heat rather than on people, which means it finds people anyway.
- **Limbs:** no head entry — it hasn't got one worth the name; head-declared shots resolve as Body.

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Wing ×2|×1.25|150|1 turn|200|N|
|Body|×1.0|800|—|—|N|

- Sever **one wing** and it is grounded: Move drops to 2m, and it loses Ignition Dive entirely.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Dustfall | Aura | None — unparryable, triggers on any creature it flies directly over during its move | N/A | N/A | 1 Burning | N/A | N/A |
| Ignition Dive | Heavy | "The wings snap flat and it simply drops out of the air at you." | Target 1.10s, ±0.15s | 2 | 55 raw + 2 Burning | Standard | Scrabbles on the floor for a beat before it can climb again |

- **Kitable:** N — it is faster than anything on foot. **Assess 0–1:** "It's fast, it's burning, and it doesn't care where you're standing." · **Assess 2+:** "The wings are the whole creature. Take one and the fight becomes trivial. It's a tight window on a fast tell, but it's a wide target."
- **White Salts drop:** 20. **Insight:** +1/+0. **Habit punished:** standing still, and letting Burning ride. **Dismember threat:** Moderate. **Retreat always reachable:** N — it follows.

## Monster 44 — The Sump Serpent

- **Archetype:** Lunger (elite) · **Level Range:** 8–20 · **HP:** 750 · **Move:** 6m in water, 2m dragging on dry ground · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Eyeless, forearm-thick, and long enough that no one has seen all of it at once. It shows two metres. It has never needed more.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Coils|×1.0|—|—|—|**Yes** — there is always more of it|
|The Shown Head|×1.5|180|1 turn|120|N|

- **The Shown Head is only a legal target on the turn immediately following one of its attacks.** Any other turn, it is submerged and the only thing available is Coils. This is the entire fight: bait a strike, then spend the one turn it gives you.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Strike-and-Sink | Heavy | "A single ripple, moving against the current." | Target 1.05s, ±0.15s | 2 | 60 raw + 1 Blood Loss | Standard | It is *out* — head exposed for the following turn |
| Constrict | Heavy — only usable if the target is standing in water | "Coils break the surface on both sides of you at once." | Target 1.70s, ±0.20s | 1 | 40 raw per turn until broken; **Strength DC 15** as an Action to escape | Standard | Releases, head exposed |

- **Kitable:** Y — on dry ground it is nearly harmless. **Assess 0–1:** "It's only dangerous while you're wet." · **Assess 2+:** "Get out of the water and it loses its best attack and most of its speed. And it only ever shows its head right after it strikes — that's your window, and it's one turn wide."
- **White Salts drop:** 24. **Insight:** +1/+0. **Habit punished:** fighting where it lives. **Dismember threat:** High (in water). **Retreat always reachable:** Y.

## Monster 45 — The Hollow Angle

- **Archetype:** Anchor (elite) · **Level Range:** 8–20 · **HP:** 600 · **Move:** none — it occupies **every corner in the room simultaneously** · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A corner where two walls meet at an angle very slightly too sharp for the room they belong to. Looked at directly, it is a corner. Looked away from, something in it has changed depth.
- **DM note (geometry rule, Ruleset §11):** the Hollow Angle does **not** alter the map. Corridors stay the length they were, exits stay where they were. What it does is occupy the corners as a single distributed body. Everything about it is legible and spatially consistent — it is strange, not broken.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|The Vertex *(implement — only exists during Reveal)*|×2.0|—|—|200|N|

- **Severing the Vertex kills it outright.** 200 at ×2.0 = 100 raw in one hit — deliberately reachable, because the window to attempt it is one turn in three.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Obtuse | Ranged | None — unparryable, no tell. Fires every turn. | N/A | N/A | 25 raw to any creature currently within **1m of a wall**. Creatures standing in open floor take nothing. | N/A | N/A |
| Reveal | Heavy — every third turn | "One corner everts. There is suddenly a *thing* where the angle was, and it has a point." | Target 1.40s, ±0.20s | 1 | 50 raw. This is also the only turn the Vertex is targetable. | Standard | Folds back into the corners |

- **Kitable:** N/A. **Assess 0–1:** "Get off the wall." · **Assess 2+:** "It can only reach you against a wall — the middle of the room is free. It surfaces every third turn and that's when it can be killed. Stand in the open and wait for it."
- **White Salts drop:** 26. **Insight:** +1/+0. **Habit punished:** back-to-the-wall kiting, the default instinct in a room full of enemies. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 46 — The Quiet

- **Archetype:** Chanter (elite) · **Level Range:** 5–20 · **HP:** 400 · **Move:** 3m drift, never hurries · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A soft, roughly person-sized absence. Not invisible — *unlistenable*. The ear refuses it the way the eye refuses a bright light, and the refusal spreads to everything standing near it.
- **Limbs:** standard humanoid defaults, no deviations. Soft, low HP, dies fast if it is actually prioritised.
- **Deafening Absence** *(passive, 6m radius, always on):*
  - Every tell inside the radius is delivered **visually only** — the DM gives no audio component in any tell description for any enemy in the bubble.
  - **Every parry and precision window inside the radius is narrowed by 0.10s** (applied to the ± tolerance, after Insight window bonus). This is a real mechanical debuff, not flavour.
  - Ends the instant the Quiet dies. It has no other trick.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Pressure | Light | None — unparryable | N/A | N/A | 20 raw + forces an Insanity save | N/A | N/A |

- **Kitable:** Y, but kiting doesn't help — the radius follows it, and it follows you.
- **Assess 0–1:** "Something's wrong with the sound in here." · **Assess 2+:** "It's the reason nothing in this room has a sound to it, and the reason your timing feels a tenth short. Kill it first. It has four hundred HP and no defence."
- **White Salts drop:** 22. **Insight:** +1/+0. **Habit punished:** ignoring support enemies to focus the biggest threat in the room. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 47 — The Thousandth Tooth

- **Archetype:** Tide (hazard-creature) · **Level Range:** 1–20 · **HP:** 800 · **Move:** 0m — it is a 6m stretch of floor · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A patch of tiling that has grown enamel. Not teeth in a mouth — teeth in a floor, every one of them pointed the same way, and the way they are pointed is at the door.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Row ×4 *(each row spans the full width)*|×1.0|—|—|200|N|

- Severing a Row **permanently opens a 1.5m-wide safe lane** through that row for the rest of the instance. Clearing all four kills it and makes the floor ordinary again.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Bite Down | Reactive | None — unparryable. Triggers on any creature that **ends its movement** on the Tooth. | N/A | N/A | 30 raw + 2 Blood Loss | N/A | N/A |

- It never attacks anything not standing on it. It has no reach, no ranged option, and infinite patience.
- **Kitable:** N/A. **Assess 0–1:** "Don't stop walking." · **Assess 2+:** "It only bites what stands still on it. Cross it in one movement and it never gets a turn — or cut lanes and make the crossing free for good."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** breaking a long movement into two turns. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 48 — The Afterimage

- **Archetype:** Effigy (elite) · **Level Range:** 10–20 · **HP:** 550 · **Move:** 5m — always arriving at where it already was · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A person-shape assembled out of the light a person leaves behind. It is doing something right now. You will find out what next turn.
- **Limbs:** standard humanoid defaults, no deviations.
- **Delay** *(defining mechanic):* every attack it makes is **declared and fully telegraphed on turn N, and resolves at the start of turn N+2.** It can have up to two Delayed Strikes in flight at once.
  - The parry stopwatch is rolled on the turn the attack **lands**, not the turn it is declared.
  - The player must **commit to parrying or not before taking their turn N+1 action** — you spend your turn knowing something is coming and having already chosen.
  - Killing the Afterimage does **not** cancel strikes already in flight. They still land.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Delayed Strike | Heavy (delayed 2 turns) | "It winds up, unhurried, and then stands there wound up." | Target 1.60s, ±0.20s, rolled on the landing turn | 2 | 70 raw | Standard | Nothing — it was never really there for the miss |

- **Kitable:** Y, and kiting is genuinely good against it. **Assess 0–1:** "It's slow. It's much too slow." · **Assess 2+:** "Everything it does is already on its way. You can't react to this one — you have to plan two turns out and mean it. And killing it doesn't stop what's already coming."
- **White Salts drop:** 26. **Insight:** +1/+0. **Habit punished:** purely reactive play. **Dismember threat:** Moderate. **Retreat always reachable:** Y — but strikes in flight still land.

## Monster 49 — The Weighing Machine

- **Archetype:** Drudge (elite) · **Level Range:** 5–20 · **HP:** 700 · **Move:** 3m, rolling on a single brass caster · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A brass fairground weighing chair, still bolted to its wheeled base, still stocked with ticket card. It rolls up beside you and waits for you to sit down. When you don't, it prints one anyway.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Chassis|×1.0|800|—|—|N|
|The Dial *(implement)*|×2.0|—|—|180|N|

- **Destroying the Dial removes Weigh entirely** for the rest of the encounter — 90 raw in one hit. It keeps the Slot Arm and becomes a very ordinary fight.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Weigh | Aura | "The dial spins up and a ticket starts feeding through the slot." Every third turn. | None — unparryable | N/A | Target takes damage equal to **their current total status-track stacks × 10** (Blood Loss + Insanity + Influence + Corrosion + Burning combined). Zero stacks = zero damage. | N/A | N/A |
| Slot Arm | Heavy | "The ticket slot swings open on its arm." | Target 1.45s, ±0.20s | 1 | 55 raw | Standard | Long mechanical reset |

- **Kitable:** Y. **Assess 0–1:** "It's counting something about you." · **Assess 2+:** "It charges you for everything you're already carrying. Clean your tracks or break the dial — either works, and one of them is a lot faster."
- **White Salts drop:** 24. **Insight:** +1/+0. **Habit punished:** letting status tracks ride because none of them are individually lethal. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 50 — The Brine Colony

- **Archetype:** Swarm (mook) · **Level Range:** 1–15 · **HP:** 350 · **Move:** 5m, a rolling grey sheet at roughly chest height along the nearest wall · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Ten thousand shelled things the size of rice grains, moving as one sheet. Individually they are nothing. The sheet has a shape and the shape has intent.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Mass|×1.0|—|—|—|**Yes**|

- **Elemental weakness — Burning ×3.** Any Burning-track damage dealt to the Brine Colony is tripled (5/turn becomes 15/turn per the standard tick). The first enemy in the manual with an explicit elemental multiplier; the shells cook.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Settle | Light | None — unparryable, no tell. Resolves at the end of the enemy block. | N/A | N/A | 10 raw + 2 Corrosion to every creature within 1m | N/A | N/A |

- **Kitable:** Y. **Assess 0–1:** "Nothing to hit and it stacks fast." · **Assess 2+:** "No anatomy, no stagger, no sever — but it burns like tinder. One fire source and this stops being a fight."
- **White Salts drop:** 14. **Insight:** +1/+0. **Habit punished:** trying to out-damage a Corrosion source instead of solving it. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 51 — The Cistern Bloom *(boss, non-humanoid)*

- **Archetype:** Anchor (boss) · **HP:** 1500 (hand-set, exempt from scaling) · **Move:** 0m — rooted through the cistern floor. Its reach, however, is the entire room.
- **Flavour:** A pale flower twelve metres across, grown up out of a drain, holding a bathing pool in its cup. Its petals are the room's ceiling. It has no face and no front — every direction is its front. It has been fed, regularly, for a long time.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Petal ×5|×1.5|200|1 turn|260|N|
|The Cup *(weak point — sealed until 3 petals are severed)*|×2.0|400|1 turn|500|N|

- **Each severed Petal permanently removes one Petal Sweep line and reduces the Bloom's reach by 3m.** At two petals remaining it can no longer reach the room's edge at all.
- **The Cup is physically inaccessible until three Petals are severed** — no called shot against it resolves before then, regardless of opening.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Petal Sweep | Heavy | "One petal peels back off the ceiling and comes down flat across the floor." | Target 1.35s, ±0.20s | 1 | 60 raw |
| Pollen | Aura | "The cup breathes out." Every other turn. | Unparryable | N/A | Forces an Insanity save + 1 Influence stack |
| Fold | Heavy (chain) | "Every remaining petal draws inward at once, closing around you in sequence." | **3 sequential windows: 0.75s · 1.25s · 1.85s, each ±0.20s** | 3 | 35 raw per unparried window (105 if all three land) |

- **Fold — the ballistic chain.** All three parried → **Tier 1 Open on the Cup, even if petals remain sealed** — the only route to the weak point that doesn't require dismemberment first. Miss any window → take that beat and every remaining beat automatically, no partial credit.
- **Kitable:** N/A — never moves, but its reach shrinks as petals come off, so *distance becomes a real strategy over the course of the fight* rather than a binary.
- **Assess 0–1:** "It's rooted. It isn't going anywhere and neither is the fight." · **Assess 2+:** "Five petals, and every one you take off shortens its reach and removes an attack. Three of them and the middle opens up. This one is built to be taken apart — grinding its HP down works, but it takes twice as long and it never gets any safer while you do."
- **White Salts drop:** 70. **Insight:** +1/+1.
- **Boss Gimmick:** **the first boss in the game where dismemberment is the intended primary route rather than an optional shortcut.** Petal sever threshold is 260 at ×1.5 = **174 raw in one hit** — genuinely reachable with a real sever weapon or an imbued opening, unlike the Singer's Open Throat. Pure HP attrition remains fully valid (Ruleset §3) and roughly doubles the fight length while the Pollen keeps climbing.
- **Habit punished:** treating every boss as an HP bar. **Dismember threat:** High. **Retreat always reachable:** Y.

## Monster 52 — The Alms Vessel

- **Archetype:** Vessel (elite) · **Level Range:** 8–20 · **HP:** 900 (shell) / 250 (occupant) · **Move:** 3m shelled, 7m spilled · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A great copper alms-urn walking on four stubby limbs of its own casting. Something soft is folded up inside it. It has folded itself very, very small.
- **Limbs (shelled phase):**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Shell|**×0.5**|—|—|400|N|

- **The ×0.5 Shell multiplier is armour** — every hit against the Vessel while shelled deals half raw. Being at or below ×1.0 it triggers **no Precision Strike stopwatch** (Ruleset §10), so it is safe to hit and slow to kill, deliberately.
- **Two routes through the shell:** grind it to 0 HP, or **sever it in one hit (400 at ×0.5 = 800 raw — effectively impossible; it is there to be a wall, not a target).** Either way, when the shell fails:
- **Spilled phase:** the occupant tips out — a separate creature, **250 HP, Move 7m, standard humanoid limbs, no armour, actively panicking.** It does not fight; it runs.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Tip *(shelled)* | Heavy | "It lifts one side and pours." | Target 1.55s, ±0.20s | 1 | 45 raw + 1 Corrosion | Standard | Rights itself slowly |
| Flail *(spilled)* | Light | None — unparryable | N/A | N/A | 25 raw, and it immediately moves its full 7m toward the nearest exit | N/A | N/A |

- If the occupant reaches an exit it **escapes** — no drop, no Insight, nothing. The second phase is a chase, not a fight.
- **Kitable:** Y shelled, N spilled (it's faster than you). **Assess 0–1:** "Your hits aren't landing properly." · **Assess 2+:** "The copper is eating half of everything. There's no clever way through it — just work. And what's inside is going to bolt the moment it opens, so be ready to be somewhere else."
- **White Salts drop:** 26 (shell) + 10 (occupant, only if caught). **Insight:** +1/+0. **Habit punished:** assuming the fight ends when the health bar does. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 53 — The Pressure

- **Archetype:** Tide (hazard-creature) · **Level Range:** any · **HP:** **none — it cannot be killed** · **Move:** N/A — it is the room
- **Flavour:** Nothing to see. The room is simply at a depth it has no business being at, and every part of you knows it.
- **Limbs:** none. No body, no target, no attack roll. It is a condition with intent.
- **Effect:** at the end of every turn any creature spends in the affected space, that creature takes **10 raw and gains 1 Corrosion.** No save, no parry, no mitigation.
- **The out:** somewhere in the room is a valve, a stopcock, a cracked gauge — a physical thing that will shut it off. **Skill DC 16**, one attempt per turn as an Action. The DM places it in plain sight but not adjacent; crossing to it is the encounter.
- **Kitable:** N/A. **Assess 0–1:** "This room is going to kill you and there's nothing in it." · **Assess 2+:** "There's a mechanism. There's always a mechanism. Find it, reach it, and stop counting turns."
- **White Salts drop:** 0 — nothing dies. **Insight:** +1 first encounter / +0 thereafter.
- **Boss Gimmick:** N/A. **Habit punished:** looking for something to hit. **Dismember threat:** None. **Retreat always reachable:** Y — leaving is always correct and always available.

## Monster 54 — The Sightless Weathervane

- **Archetype:** Drudge (elite) · **Level Range:** 8–20 · **HP:** 650 · **Move:** 0m — bolted through the floor, but constantly turning · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A wrought-iron vane driven through the floorboards, four cardinal arms ending in blades, turning slowly and without pause. It does not choose which arm reaches you. It doesn't need to.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Arm ×4|×1.0|—|—|220|N|
|Spindle|×1.0|800|—|—|**Yes**|

- Each severed Arm removes one quarter of its coverage — with two arms gone there are genuine safe arcs to stand in; with three, it is nearly harmless.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Sweep | Heavy | "The near arm is coming around — **fast / steady / slow / very slow**" (DM states the visual speed, never the number) | **Variable.** DM rolls d4 each turn: **1 → 1.00s · 2 → 1.30s · 3 → 1.60s · 4 → 1.90s.** ±0.20s in all cases. | 1 | 50 raw | Standard | Overtravels a quarter turn |

- **The variable window is the entire design.** Every other parryable enemy in the manual has one memorisable target time. This one has four, rerolled every turn, and only ever gives a qualitative hint. It is the anti-muscle-memory encounter.
- **Kitable:** N/A — but stepping out of its radius entirely is free and it cannot follow.
- **Assess 0–1:** "Its timing is never the same twice." · **Assess 2+:** "There's no number to learn here. Watch the arm, not the clock — the speed it's telling you is real, it just isn't precise. Or take the arms off and stop needing to guess."
- **White Salts drop:** 22. **Insight:** +1/+0. **Habit punished:** learning one target time and coasting on it. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 55 — The Watchwork

- **Archetype:** Crawler (elite) · **Level Range:** 10–20 · **HP:** 700 · **Move:** 8m across **ceilings and walls**, ignores all floor-based rough terrain and hazards entirely · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A clockwork centipede of brass eyelets, thirty of them, running the ceiling seam. Every eyelet has a lens and every lens is pointed down.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Segment ×8|×1.0|—|—|180|N|

- **Dismemberment is a punishment here, not a reward.** Sever any three Segments and the Watchwork **splits into two independent creatures**, each with half the remaining HP, each with its own full turn and its own Drop-Coil. They can split again. Grinding the HP down without ever severing kills it once.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Drop-Coil | Heavy | "It lets go of the ceiling directly above you." | Target 1.25s, ±0.15s | 2 | 55 raw + 1 Discombobulation | Standard | Has to climb before it can drop again — ~1 free player action |

- **Kitable:** N — it goes over everything. **Assess 0–1:** "It's using the whole room and you're only using the floor." · **Assess 2+:** "Do **not** take segments off it. Three and it becomes two of them. This is the one you kill the boring way."
- **White Salts drop:** 26 (per body — a split creature pays out twice, which is the only consolation). **Insight:** +1/+0. **Habit punished:** reflexive limb-severing on anything with limbs. **Dismember threat:** Moderate. **Retreat always reachable:** N — it is faster than you and terrain doesn't slow it.

## Monster 56 — The Steeping

- **Archetype:** Shambler (elite) · **Level Range:** 5–20 · **HP:** 600 · **Move:** 5m, and it pours through gaps rather than going around them · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A person-shaped volume of scalding water, standing upright with nothing holding it in that shape. Not a ghost. Just water, holding the outline of the last thing that sat in it long enough to leave one.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Body|×1.0|—|—|—|**Yes** — all called shots, of any kind, resolve as Body|

- **Immunities:** Burning damage deals **0** against the Steeping. Corrosion deals **0**. It is water; there is nothing to burn and nothing to eat.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Scald | Light | None — unparryable | N/A | N/A | 30 raw + 1 Burning | N/A | N/A |
| Immerse | Heavy | "It leans toward you and loses its outline on the way." | Target 1.65s, ±0.25s | 1 | 65 raw + 2 Burning. **Additionally: the target's carried powder capsules are soaked** — the next Powder Charge attempt of any kind automatically fails as a dud. No Blood Loss penalty on the dud (Ruleset §4 failure clause does not apply — nothing detonated). One capsule wasted. | Standard | Has to gather itself back upright |

- **Kitable:** Y. **Assess 0–1:** "Fire won't do anything to that." · **Assess 2+:** "No anatomy, no burn, no corrosion — plain damage only. And if it gets a full hit on you, whatever powder you're carrying is wet. Fight it dry or fight it at range."
- **White Salts drop:** 24. **Insight:** +1/+0. **Habit punished:** relying on a single damage-delivery gimmick. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 57 — The Second Sight

- **Archetype:** Chanter (elite) · **Level Range:** 10–20 · **HP:** 450 · **Move:** 6m, hovering at head height · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A loose cluster of seven lidless eyes, unattached to anything, drifting in rough formation. They do not blink and they are not all looking at the same thing.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Eye ×7|**×1.75**|—|—|**100**|N|

- **Sever all seven Eyes and it dies outright**, regardless of remaining HP. 100 at ×1.75 = **58 raw in one hit** — trivially low. The catch is the multiplier: ×1.75 sits in the **±0.09s** Precision Strike tolerance band (Ruleset §10), and a miss at 1.51–1.75 is "wide — no damage, enemy free reactive strike." Seven greedy shots in a row, each one punished if fumbled. This is the precision-build playground.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Regard | Aura | "Three of them swivel onto you at once." | Unparryable | N/A | Insanity save at **+2 DC**. On failure: **1 turn of Fugue** (Ruleset §13) — the DM delivers exactly one deliberately false tell, window, or read on the following turn. | N/A | N/A |

- **Fugue from a non-death source.** Ruleset §13 previously applied Fugue only on death. The Second Sight is the first creature that inflicts it in combat, at one-turn duration rather than until-cleared. It does not consume the next earned Insight point (the §13 clearing rule) — it simply expires.
- **Kitable:** N. **Assess 0–1:** "Every one of those is a target and every one of those is watching." · **Assess 2+:** "Seven eyes, and each one comes off in a single hit — but they're the greediest shots in the game and a miss hands it a free strike. And once it's had a proper look at you, don't trust the next tell you get."
- **White Salts drop:** 24. **Insight:** +1/+0. **Habit punished:** trusting the DM's reads unconditionally at high Insight. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 58 — The Cold Boiler

- **Archetype:** Brute · **Level Range:** 12–20 · **HP:** 2000 · **Move:** 3m, walking on the stub of its own mounting bracket · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A riveted iron boiler two men tall, walking on the broken bracket it was bolted down with. Frost on the outside, thick enough to hold a handprint. Whatever is inside it is the thing that's cold.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Plating|**×0.5**|—|—|500|N|
|Rivet Seam *(implement)*|×2.0|—|—|280|N|

- **Two-phase, and the second phase is worse.** The ×0.5 Plating halves all incoming damage (and, being ≤×1.0, triggers no Precision stopwatch). Bursting the Rivet Seam — **280 at ×2.0 = 140 raw in one hit** — does not kill it. It **vents**, and thereafter:
  - The Plating multiplier is gone permanently. All subsequent hits land at ×1.0.
  - It gains **Vent**, below.
- Winning the armour phase makes the fight faster and considerably more lethal. That trade is the encounter.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Bracket Swing | Heavy | "It hauls the broken bracket up over its shoulder." | Target 1.85s, ±0.20s | 2 | 90 raw | Standard | Very long recovery — it is enormously heavy |
| Vent | Aura *(post-seam-burst only)* | "The split in its side widens and something white comes out of it." | Unparryable. Every third turn. | N/A | **3 Burning** to every creature within 4m | N/A | N/A |

- **Kitable:** Y, and post-vent it becomes mandatory. **Assess 0–1:** "You're barely scratching it." · **Assess 2+:** "The plate is halving everything — the seam on its flank will open in one good hit and then it takes full damage. Understand that it starts venting the moment you do that, and it doesn't stop."
- **White Salts drop:** 40. **Insight:** +1/+0. **Habit punished:** rushing the obvious weak point without a plan for what comes after. **Dismember threat:** Very High. **Retreat always reachable:** Y.

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
- **Sever viability:** the game's benchmark sever weapon. Str 8 → ESV 8 → Heavy 71 (below every threshold). Str 40 → ESV 33 → Heavy ~105 (still under Head's 120). Str 99 → ESV 47 → Heavy 124, clears the Head's 120-raw line outright.

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

## Weapon 29 — The Trepanning Cradle

*The game's first **three-form** Trick weapon. Existing Trick entries toggle between two states; this one cycles.*

- **Type:** Trick (three-form) · **Stat/Grade:** compact Skill/C · splayed Skill/C · locked Strength/B · **Hands:** One compact, Two splayed, Two locked
- **Acquisition:** found — Gaslight Ward / Reliquary recipes, instance loot.
- **Base (compact, Quick):** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05. **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Base (splayed, Reach):** 24 — identical formula, Type becomes Reach. Same worked rows.
- **Base (locked, Heavy):** 30. Light = 30+ESV×0.9 · Heavy = 60+ESV×1.35. **Worked rows:** ESV 8 → 38/71 · ESV 47 → 73/124.
- **Passive:** a surgical skull-brace that never got used for that. Changing form is a Fast Action (0m) — **but only in sequence: compact → splayed → locked → compact.** There is no jumping forms. Getting from compact to locked costs two Fast Actions across two turns, and going back is another two. The weapon rewards deciding early what the fight is going to be, and punishes changing your mind halfway.
- **Insight Gate:** locked form requires **Insight Tier 3** — the deepest gate on any Trick weapon, matched to the payoff.
- **Sever viability:** compact and splayed — standard, per the general limb-model sever thresholds. Locked — Heavy clears the Head's 120-raw line at **ESV 44**, putting it in the same bracket as the Foundry Wedge.

## Weapon 30 — The Hemorrhage

- **Type:** Quick · **Stat/Grade:** Skill/D · **Hands:** One
- **Acquisition:** found — general Vault reward, no recipe tie.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75.
- **Worked rows:** ESV 8 → 26/50 · ESV 47 → 46/80.
- **Passive:** a fluted blade with a channel cut down its spine and a grip that has never been properly cleaned. **Both Light and Heavy deal +5 raw per Blood Loss stack the wielder is currently carrying.** At 9 stacks that is +45 raw on every swing — roughly doubling its output — and at 10 stacks the wielder Ruptures (25% Max HP, Ruleset §5). The weapon does nothing to cause bleeding and nothing to stop it. It simply pays better the closer you are to going over.
- **Status Applied:** none — it only reads.
- **Sever viability:** standard, per the general limb-model sever thresholds. Note the interaction: a Heavy at 9 stacks reaches **125 raw at ESV 47**, clearing the Head line on a weapon that otherwise never would. That is the whole point and it is deliberately not safe.

## Weapon 31 — The Grinning Curette

- **Type:** Quick · **Stat/Grade:** Skill/C · **Hands:** One
- **Acquisition:** found — Gaslight Ward recipe, instance loot.
- **Base:** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05.
- **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Passive:** a small looped scraping tool with a face worked into the handle, which is smiling, which it did not do when it was found. **Every Precision Strike tolerance is widened one full band per 3 points of the wielder's current Insanity track, to a maximum of two bands.** At Insanity 3 the head's ±0.13s becomes ±0.25s; at Insanity 6 an eye's ±0.09s becomes ±0.25s. Insanity 10 is a Break (Ruleset §5) — blackout, DM control, permanent Scar. The weapon is at its best four stacks from the edge and does nothing at all to keep you off it.
- **Insight Gate:** none. It doesn't need one.
- **Sever viability:** standard, per the general limb-model sever thresholds — the bonus is entirely accuracy, never raw.

## Weapon 32 — The Nursling

- **Type:** Heavy · **Stat/Grade:** Strength/C · **Hands:** Two
- **Acquisition:** found — instance loot, any recipe. It turns up. It is not clear that it is always found rather than arriving.
- **Base:** 28. Light = 28+ESV×0.7 · Heavy = 56+ESV×1.05.
- **Worked rows:** ESV 8 → 34/65 · ESV 47 → 61/106.
- **Passive:** a heavy hooked blade with a small mouth set into the inside of the guard, where a thumb would rest. **It has to be fed.**
  - Any killing blow landed with the Nursling restores **10% of the wielder's Max HP**, immediately.
  - After any encounter in which the Nursling did **not** land a killing blow, it takes **10 HP from the wielder** at the start of the next encounter. This is not preventable, is not a status track, and cannot be healed against in advance.
- A genuinely self-sustaining Strength weapon for anyone confident of finishing what they start, and a slow bleed for anyone who isn't.
- **Sever viability:** standard, per the general limb-model sever thresholds.

## Weapon 33 — The Return Post

- **Type:** Reach · **Stat/Grade:** Skill/C · **Hands:** Two
- **Acquisition:** found — general Vault reward.
- **Base:** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05.
- **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Passive:** a long iron post with a flared catch-plate, of the kind driven in to stop a door. **On a successful parry with this weapon, the incoming attack's full raw damage is stored** — one charge only, a new parry overwrites the old value. The next Heavy attack landed adds the stored raw on top of its own, then discharges. Parry a Marble Attendant's 80-raw fist and the answering Heavy carries an extra 80.
- **The charge is lost the moment the wielder takes damage from any source**, including chip, status ticks and Burning. Holding it costs nothing; holding it is also nearly impossible.
- **Sever viability:** standard, per the general limb-model sever thresholds — but a discharged Heavy against a heavy-hitting boss will clear the Head line at ESVs where the weapon has no business doing so. Legal, intended, and requires a clean parry against something that hits for 60+ to matter.

## Weapon 34 — The Halved Anchor *(paired / combining)*

*The first weapon in the game that is two weapons, and the first that combines rather than transforms.*

- **Type:** Trick (paired ↔ two-handed) · **Stat/Grade:** Strength/D separated (each half) · Strength/B combined · **Hands:** One each separated, Two combined
- **Acquisition:** found — Bellfounder's Pit / Cold Forge recipes, instance loot. Both halves are always found together; a single half is useless and cannot be wielded alone.
- **Base (separated, Quick, per half):** 20. Light = 20+ESV×0.5 · Heavy = 40+ESV×0.75. **Worked rows:** ESV 8 → 24/46 · ESV 47 → 44/76.
- **Base (combined, Heavy):** 32. Light = 32+ESV×0.9 · Heavy = 64+ESV×1.35. **Worked rows:** ESV 8 → 40/75 · ESV 47 → 75/128.
- **Passive:** a boat anchor sawn cleanly in half down the shank, each half regripped. Joining or separating is a Fast Action (0m).
  - **Separated:** one Action buys **two independent Light attacks**, which may be declared **against two different targets** — the only weapon in the game that can split a single Action across two enemies. Each resolves at full weight against its own target's meters.
  - **Combined:** a single two-handed slab of iron. Highest Heavy in the Strength/B bracket.
- **Insight Gate:** none.
- **Sever viability:** separated — standard, and low. Combined — Heavy clears the Head's 120-raw line at **ESV 41.**

## Weapon 35 — The Sentry Arm

- **Type:** Reach · **Stat/Grade:** Skill/D · **Hands:** One
- **Acquisition:** found — Loom Room / Gaslight Ward recipes, instance loot.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75.
- **Worked rows:** ESV 8 → 26/50 · ESV 47 → 46/80.
- **Passive:** a jointed mechanical arm strapped along the forearm, ending in a fixed blade, with a trigger that isn't operated by the wielder. **Set it as a Fast Action (0m) to guard a declared 2m arc.** The first enemy that enters that arc, or attacks the wielder from within it, during the enemy block takes **one automatic Light hit with no timing check.** It then goes slack and must be re-set as another Fast Action.
- **The first weapon in the game that acts during the enemy's turn.** Pure zone control — it does not improve anything the wielder does, it just makes one piece of floor cost something to walk across.
- **Sever viability:** standard, per the general limb-model sever thresholds. The automatic hit is a full Light and contributes to stagger meters normally.

## Weapon 36 — The Ward-Saw

*The game's first defensive-first Trick weapon — the missing shield row.*

- **Type:** Trick (Quick ↔ Guard) · **Stat/Grade:** Skill/C both forms · **Hands:** One saw, Two guard
- **Acquisition:** found — Paper Mill / Cold Forge recipes, instance loot.
- **Base (saw, Quick):** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05. **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Base (guard):** 24 — same formula, **Light attacks only. Heavy is unavailable in guard form entirely.**
- **Passive:** a broad-bladed pit saw with a folding brace along its spine that swings out into a full body-width shield. Switching is a Fast Action (0m).
  - **Guard form:** all incoming attacks are reduced by a flat **−10 raw**, applied before status effects, which still land in full. Losing Heavy is the price, and it is a real one — most sever routes close entirely while guarded.
  - **Saw form:** ordinary Skill/C, no bonuses.
- **Insight Gate:** none.
- **Sever viability:** saw form — standard. Guard form — none, no Heavy to sever with.

## Weapon 37 — The Debt-Iron

*The first **Grade A** weapon in the game (Ruleset §4 grade table: A ×1.1). Everything below B has been the ceiling until now.*

- **Type:** Heavy · **Stat/Grade:** Strength/A · **Hands:** Two
- **Acquisition:** found — deep instance loot only, any recipe, and never in an early room. Hand-placed, not rolled.
- **Base:** 34. Light = 34+ESV×1.1 · Heavy = 68+ESV×1.65.
- **Worked rows:** ESV 8 → 43/82 · ESV 20 → 56/101 · ESV 47 → 86/146.
- **Passive:** a debt-collector's breaking bar, tallied down one face in notches that were not cut by the same hand. It is too much weapon and it charges for itself.
  - **Every Heavy swing costs 5m of movement** rather than 3m (matching Charged Heavy, Ruleset §4). At a standard 8m budget that is most of a turn.
  - **Every Heavy inflicts 1 Blood Loss on the wielder, landed or missed.** The bar does not care whether it connected.
- **Sever viability:** best-in-class outside the Coronal. Heavy clears the Head's 120-raw line at **ESV 32** — fifteen ESV earlier than the Foundry Wedge, the previous benchmark. Arm (~308) and Leg (400) remain out of one-hit reach at any ESV, per the fixed-constant rule (Ruleset §10).

## Weapon 38 — The Hollow Coronal

*The first **Grade S** weapon in the game (Ruleset §4: S ×1.3). The ceiling, and priced like it.*

- **Type:** Heavy · **Stat/Grade:** Strength/S · **Hands:** Two
- **Acquisition:** found — boss-adjacent placement only, hand-placed, one per campaign until deliberately reintroduced. It should feel like a decision, not a drop.
- **Base:** 30. Light = 30+ESV×1.3 · Heavy = 60+ESV×1.95.
- **Worked rows:** ESV 8 → 41/76 · ESV 20 → 56/99 · ESV 47 → 92/152.
- **Passive:** a crown of fused iron on a shaft, or a shaft that ends in one — the join isn't visible. It is the heaviest thing anyone has carried down here and it is not neutral about being carried.
  - **While equipped, the wielder's Insanity and Influence save DC is +3, permanently and unconditionally.** This stacks with the Insight term and does not care about Resolve.
  - **It cannot be unequipped, stowed, or swapped away from inside an instance.** The choice is made at the hub, at the door, before anything is known about what is on the other side. It can be dropped — abandoned outright, per Abandon-All's gear rules (Ruleset §12) — but not put away.
- **Insight Gate:** none. It is not gated by sight. It is gated by nerve.
- **Sever viability:** the highest in the game. Heavy clears the Head's 120-raw line at **ESV 31.** Arm and Leg remain unreachable in one hit at any ESV — even the ceiling does not break the fixed-constant rule.

## Weapon 39 — The Weathervane Blade

- **Type:** Trick (four-form, **wielder does not choose**) · **Stat/Grade:** Skill/C in three forms, Skill/D ranged · **Hands:** varies by form
- **Acquisition:** found — general Vault reward, no recipe tie.
- **Base:** 26 in every form.
  - **Quick (Skill/C, one hand):** Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05. **ESV 8 → 32/61 · ESV 47 → 59/102.**
  - **Reach (Skill/C, two hands):** identical formula and rows.
  - **Heavy (Skill/C, two hands):** identical formula and rows.
  - **Ranged (Skill/D, two hands, single shot, no Light/Heavy split):** Shot = 26+ESV×0.5. **ESV 8 → 30 · ESV 47 → 50.** Range 8m, 1m movement cost, no timing check, no ammunition — it simply throws part of itself and gets it back.
- **Passive:** a blade with no settled shape and a set of joints that move on their own. **At the start of every encounter the DM rolls d4 and the weapon locks into one form for the duration of that encounter.** 1 → Quick · 2 → Reach · 3 → Heavy · 4 → Ranged. The wielder has no input, no reroll, and no way to change it before the encounter ends.
- Statistically identical across the melee forms, so the gamble is entirely about **fit** — the right tool for the room, or the wrong one, decided before the first turn. The ranged roll can be a gift or a disaster depending on what walked in.
- **Insight Gate:** none.
- **Sever viability:** melee forms — standard. Ranged form — none, same as the Salvage Launcher.

## Weapon 40 — The Tithe-Fork

*The first weapon in the game that consumes **Insight as ammunition** (Ruleset §11, Spending Insight).*

- **Type:** Reach · **Stat/Grade:** Skill/C · **Hands:** Two
- **Acquisition:** found — deep instance loot, any recipe. Insight-adjacent placement (behind a gated door, near a warp threshold).
- **Base:** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05.
- **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Passive:** a three-tined collection fork, of a sort used for taking things from people who were not offering them. **Spend 1 Insight as a Fast Action (0m) to prime it.** The next attack landed:
  - **Ignores all damage-reduction multipliers below ×1.0** — shells, plating, carapace, anything armoured. That hit resolves at ×1.0 minimum.
  - **Treats the target's sever threshold as 25% lower** for that hit only.
- Spending drops the wielder's Insight score immediately and can drop a tier, with everything that costs (window bonus, gates, mods). It is a real price paid for a single swing, and the swing had better matter.
- **Insight Gate:** none to wield. The passive is the gate.
- **Sever viability:** standard normally. Primed, against a standard humanoid, the Head line falls from 120 to **90 raw** — reachable by this weapon's own Heavy at **ESV 40**, and by almost anything with a good opening.

## Weapon 41 — The Cauterising Lance

- **Type:** Reach/thrust · **Stat/Grade:** Strength/C · **Hands:** Two
- **Acquisition:** found — Cold Forge / Ember Wards recipes, instance loot.
- **Base:** 28. Light = 28+ESV×0.7 · Heavy = 56+ESV×1.05.
- **Worked rows:** ESV 8 → 34/65 · ESV 47 → 61/106.
- **Passive:** a long thrusting lance with a heated collar behind the point, of the sort used to seal a wound shut rather than open one. **Every fully-landed Heavy applies 2 Burning to the target and clears 2 Blood Loss from the wielder.** The heat runs both ways along the shaft.
- The Strength answer to a bleed problem — a build that runs hot, takes Blood Loss freely, and burns it off by committing to Heavies rather than by spending item actions on Wrap.
- **Status Applied:** Burning (target), Blood Loss removal (self).
- **Sever viability:** standard, per the general limb-model sever thresholds.

## Weapon 42 — The Grafted Limb

- **Type:** Quick · **Stat/Grade:** Skill/C · **Hands:** One — it **is** the hand
- **Acquisition:** found — deep instance loot, or offered. Attaching it is a decision, not a pickup.
- **Base:** 26. Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05.
- **Worked rows:** ESV 8 → 32/61 · ESV 47 → 59/102.
- **Passive:** a forearm and hand of dark worked metal that replaces the wielder's own from the elbow down. Once attached:
  - **It cannot be unequipped, swapped, or dropped except at the hub**, where removal follows the Corrupted Regrowth regret rules (Ruleset §10) — a real cost, not a menu option.
  - **It can never be disarmed** by any effect.
  - **All self-inflicted damage from the wielder's own weapon gimmicks is halved** — Powder Charge failure, the Debt-Iron's Blood Loss, the Nursling's feeding, anything where the weapon costs you. It absorbs what it can.
  - **Severing that arm on the wielder destroys the weapon permanently.** It is a limb; limbs come off.
- **Insight Gate:** none, though below **Insight Tier 3** the wielder cannot read what it is actually doing to the arm (same threshold as full mutation stat-lines, Ruleset §10).
- **Sever viability:** standard, per the general limb-model sever thresholds.

## Weapon 43 — The Aggregate

- **Type:** Quick · **Stat/Grade:** Skill/C · **Hands:** One
- **Acquisition:** found — general Vault reward, no recipe tie.
- **Base:** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05.
- **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Passive:** a short blade of no consistent material, which is a polite way of saying it is made of pieces of other things. **After landing a killing blow, the Aggregate takes on one property of what it killed for the rest of the encounter:** the DM grants it one status application drawn from that creature's own kit — Burning, Corrosion, Influence, Blood Loss or Discombobulation — applied on its Heavy attacks at 1 stack.
- **Overwrites on every subsequent kill**, never stacks, and resets to nothing at the end of the encounter. Kill something that applies nothing and it takes nothing; the weapon is only as interesting as the room is.
- **Insight Gate:** none.
- **Sever viability:** standard, per the general limb-model sever thresholds.

## Weapon 44 — The Undertaker's Trocar

- **Type:** Reach/thrust · **Stat/Grade:** Strength/B · **Hands:** Two
- **Acquisition:** found — Reliquary / Bellfounder's Pit recipes, instance loot.
- **Base:** 26. Light = 26+ESV×0.9 · Heavy = 52+ESV×1.35.
- **Worked rows:** ESV 8 → 34/63 · ESV 20 → 44/79 · ESV 47 → 69/116.
- **Passive:** a mortuary trocar scaled up past any use it was made for — a hollow spike on a long shaft, meant to go all the way through in one push. **All or nothing:**
  - **Sever thresholds are reduced by 20% for this weapon** against every target, standard or bespoke. Standard humanoid Head becomes **96**, Arm ~246, Leg 320.
  - **It can never stagger a limb.** Its contribution to every stagger meter, on every hit, is **zero.** No stagger means no free called shots from crossing a threshold, and no limp limbs — ever.
- The most specialised weapon in the manual. It severs earlier than anything at its grade and it removes an entire subsystem from the wielder's toolkit to do it.
- **Sever viability:** Heavy clears the reduced Head line (96) at **ESV 33** — comparable to the Debt-Iron, at one grade lower and without the self-damage. Arm and Leg remain out of one-hit reach at any ESV even reduced, per the fixed-constant rule.

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

- **Role:** hub-accessible Insight trader. Trades Insight for voluntary mutations, mutation removal, and Scar removal. **Location:** hub — a fixed alcove, not signposted, not advertised. Visible only to those at Insight 15+. **No threshold gate — if Insight drops below 15, she vanishes immediately**, mid-conversation if necessary. Reappears when Insight climbs back. **Fightable:** N.
- **Fixed appearance:** ghostly, ephemeral — translucent, edges indistinct, more suggestion than person. Never fully solid. Voice arrives slightly before or after her mouth moves. Details shift if you look away and back — hair length, hand count, whether she's standing or seated. The one constant: she's always facing you.
- **On arrival:** doesn't introduce herself. Knows the player's Insight score without being told. Opens with what she can offer, not who she is. **Never** accepts Salts, items, or favours as payment. **Never** allows a clean Insight dump — every trade has a physical cost attached.
- **Never does:** raise her voice, touch anything physical, appear to anyone below Insight 15, leave the alcove. **Never says directly:** her own name (the player names her, or doesn't), what she does with the Insight she collects, or why she's in the Hydro.
- **Dialogue seeds:** measured, transactional, unbothered by refusal. "You've seen enough to find me. That's the price of admission." / "I don't sell power. I rearrange what's already yours." / "Come back when you have something to trade — or something you want taken away." / Treats a refusal as fact, not a slight.
- **Mechanical function:**
  - **Voluntary mutation (buy):** 5 Insight → player chooses a limb, DM generates a mutation (upside + downside, same Corrupted Regrowth shape as ruleset §10). The limb doesn't need to be lost first — the Vendor changes it in place. Mutation is permanent until removed. Full stat-line legible immediately (Insight threshold already met by access requirement). Always available — no prerequisite.
  - **Mutation removal:** 5 Insight → removes one existing mutation, limb reverts to human. **Requires** having at least one existing mutation or Scar — the Vendor won't accept Insight with nothing on the table.
  - **Scar removal:** only route. Scar 1 = 6 Insight, Scar 2 = 10, Scar 3+ = escalating. **Requires** having the Scar (same constraint — no phantom trades).
  - **Hard constraint:** the player must either purchase a mutation OR have an existing mutation/Scar to remove. No clean Insight dumps. The cheapest "clean" Insight reduction (buy mutation + immediately remove it) costs 10 Insight for zero lasting change. Accepting the mutation costs 5 and you keep the upside+downside. This is by design — rewards commitment over cycling.
  - **No debt system.** Hub-accessible means all trades are immediate, no cross-run payment plans.
  - **Single-conversation resolution.** All trades within one visit resolve before the Insight threshold check kicks in. The player can make multiple trades in a sitting even if intermediate Insight drops would take them below 15. Once the conversation ends and the player walks away, the threshold applies — if Insight is below 15, she's gone until it climbs back.
- **Lore:** tangled with the reception clerk's "brother" hook. Never revealed: true name, what she does with collected Insight, why she's in the Hydro, or whether she was always here.

## NPC 5 — Greta

- **Role:** hub attribute-leveling administrator — "tempering." **Location:** hub only, always found in one of the non-Salt open saunas, never anywhere else. **Fightable:** N.
- **Fixed appearance:** heavyset, old, wrapped in plain linen, steam blurring most detail past silhouette. Eyes closed more often than open — never confirmed whether she's actually looking at anything.
- **On arrival:** doesn't rise, doesn't greet first — waits to be approached, then asks what's being tempered before anything else. **Never** leaves the sauna, references the passage of time, or explains how long she's been there.
- **Never says directly:** her own history, what "tempering" costs her personally (if anything), or why it has to happen here.
- **Dialogue seeds:** "Tempering's a slow burn — no shortcuts I know of." / "Sit if you're staying. Steam does half the work." / "Which of you is changing today." (said flatly, not really a question) / "That's the price. I don't set it, I just take it."
- **Mechanical function:** administers the existing Leveling system unchanged (Ruleset §leveling — spend Vault Salts on attribute points, cost = 25 × current level, cap 100). No new formula, no discount, no markup — she's the fictional seat for a mechanic that previously had no NPC attached to it. Attribute choice is always the player's declared call, never resolved on her end.
- **Lore:** connects to nothing yet. First appearance session 8.

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
  - **Imbue Weapon** — Full Action (2m), range 5m (session 9 ruling): +12 flat damage to Lloyd's next attack, light or heavy, whichever he swings first. One charge at a time, doesn't stack with itself, does stack with the Charm (different source — hers scales off RES, the Charm is a flat item bonus).
  - **Steadying Grace** — Full Action (2m), range 5m (session 9 ruling): usable only the turn immediately after Lloyd takes a hit and doesn't land a qualifying attack that turn (his Rally window closing). Recovers 50% of whatever grey Rally HP is currently pending into real HP; the other half is lost, same as a whiffed self-Rally. Bound entirely to the existing Rally system — no new resource.
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

## Item 6 — Wrap

*Fills the default Quick Item row (Ruleset §8) — first standalone Bible entry, values already canon via the character sheet/Hub Kit.*

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** clears 2 Blood Loss stacks.
- **Status Applied:** none (removal only). **Duration:** instant. **Consumable:** Y. **Carry Limit:** 5.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** Hub Kit (2× on every arrival, free) · bought at 10 Salts beyond the kit default.

## Item 7 — Camphor

*Fills the default Quick Item row (Ruleset §8) — first standalone Bible entry.*

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** clears 2 Insanity.
- **Status Applied:** none (removal only). **Duration:** instant. **Consumable:** Y. **Carry Limit:** 5.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** Hub Kit (1× on every arrival, free) · bought at 10 Salts beyond the kit default.

## Item 8 — Tonic

*Fills the default Quick Item row (Ruleset §8) — first standalone Bible entry.*

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** heals a small flat amount — ~10% Max HP.
- **Status Applied:** none. **Duration:** instant. **Consumable:** Y. **Carry Limit:** 6.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** Hub Kit (2× on every arrival, free) · bought at 15 Salts beyond the kit default.

## Item 9 — Source-Water Flask *(standard)*

*Fills the default Action Item row (Ruleset §8) — the untreated variant the Clean Source-Water Flask (Item 4) is explicitly a rarer alternative to.*

- **Type:** Action Item · **Action Cost:** full Action, 2m
- **Effect:** heals a large amount — 50% Max HP.
- **Status Applied:** 1 Influence stack, unavoidable — drinking straight from the source always costs something.
- **Duration:** instant. **Consumable:** Y, Uses: 1 per flask. **Carry Limit:** 3.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot, most recipes. Bought at 40 Salts where a vendor stocks it.

## Item 10 — Cautery Iron

*Fills the default Action Item row (Ruleset §8) — first standalone Bible entry.*

- **Type:** Action Item · **Action Cost:** full Action, costs the entire remaining movement budget for the turn
- **Effect:** fully clears Blood Loss to 0, regardless of current stack count.
- **Status Applied:** none (removal only). **Duration:** instant. **Consumable:** N (Constant — reusable indefinitely, the cost is the movement tax, not the item).
- **Insight Gate:** none. **Limb Requirement:** a working hand and arm.
- **Acquisition:** commissioned (hub apothecary) · not found in instances. Backstory-eligible.

## Item 11 — Thrown Vial

*Fills the default Action Item row (Ruleset §8) — first standalone Bible entry.*

- **Type:** Action Item · **Action Cost:** full Action, 2m · **Range:** 6m
- **Effect:** applies 2 Corrosion stacks or 2 Burning stacks to the target (thrower's choice at time of use, fixed at throw).
- **Duration:** instant application, effect persists per the status track's own rules. **Consumable:** Y, Uses: 1 per vial. **Carry Limit:** 4.
- **Insight Gate:** none. **Limb Requirement:** a working throwing arm.
- **Acquisition:** found — general instance loot. Bought at 30 Salts where stocked.

## Item 12 — The Steadying Coin

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** clears 1 Influence stack.
- **Status Applied:** none (removal only). **Duration:** instant. **Consumable:** Y. **Carry Limit:** 5.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot. Bought at 10 Salts. **Design note:** the first dedicated Influence-clear Quick Item — closes the last gap in track-clear parity (Blood Loss/Wrap, Insanity/Camphor, Corrosion/Scour, now Influence/this).
- **Flavour:** an old coin, filed smooth on one face. Pressed to the tongue, it gives the mouth something to taste that isn't the compulsion.

## Item 13 — Cold Press

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** clears 1 Burning stack.
- **Status Applied:** none (removal only). **Duration:** instant. **Consumable:** Y. **Carry Limit:** 5.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot, common near the Ember Wards/Cold Forge recipes. Bought at 10 Salts.
- **Flavour:** a chilled cloth pouch, packed with something that never quite thaws.

## Item 14 — Sour Candy

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** heals a small flat amount — ~5% Max HP. Deliberately weaker than Tonic.
- **Duration:** instant. **Consumable:** Y. **Carry Limit:** 8 (cheap and common, carried in bulk).
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot, very common. Bought at 5 Salts. **Design note:** the budget healing option — strictly weaker and cheaper than Tonic, not a sidegrade.

## Item 15 — Loose Thread

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** grants +1m of movement, usable immediately as part of the same turn.
- **Duration:** instant. **Consumable:** Y. **Carry Limit:** 4.
- **Insight Gate:** none. **Limb Requirement:** a working hand and legs.
- **Acquisition:** found — general instance loot. Bought at 8 Salts.
- **Flavour:** pull it and something gives, just enough to get an extra step.

## Item 16 — Bitter Draught

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** the wielder's next Insanity or Influence save this turn gets +1.
- **Duration:** instant, applies to the very next save only. **Consumable:** Y. **Carry Limit:** 4.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot. Bought at 15 Salts.
- **Flavour:** foul enough that the compulsion briefly has competition for your attention.

## Item 17 — Chalk Dust

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** immediately ends the wielder's own current Off-Balance status, if active. No effect if not currently Off-Balance.
- **Duration:** instant. **Consumable:** Y. **Carry Limit:** 3.
- **Insight Gate:** none. **Limb Requirement:** a working hand and legs.
- **Acquisition:** found — general instance loot. Bought at 5 Salts (cheap — genuinely narrow use case).

## Item 18 — Hollow Reed

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** clears 1 stack from any single status track of the wielder's choice (Blood Loss, Insanity, Influence, Corrosion, or Burning).
- **Duration:** instant. **Consumable:** Y, Uses: 1, **not Hub Kit** — doesn't refill on hub return, must be found or bought fresh each time.
- **Carry Limit:** 3.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot, uncommon. Bought at 20 Salts. **Design note:** the flexible wildcard — priced and gated (no Hub Kit refill) to sit above the single-track clears without replacing them outright.

## Item 19 — Thread-Count Bandage

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** clears 1 Blood Loss stack **and** ends the wielder's current Off-Balance status, if active, in the same use.
- **Duration:** instant. **Consumable:** Y. **Carry Limit:** 2 (a combo item, deliberately rarer than plain Wrap).
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot, uncommon. Bought at 15 Salts.

## Item 20 — Bone-Set Splint

- **Type:** Action Item · **Action Cost:** full Action, costs the entire remaining movement budget for the turn (same tax as Cautery Iron)
- **Effect:** fully clears Blood Loss to 0, regardless of current stack count.
- **Duration:** instant. **Consumable:** Y, Uses: 1. **Carry Limit:** 2.
- **Insight Gate:** none. **Limb Requirement:** a working hand and arm.
- **Acquisition:** found — general instance loot, uncommon. Bought at 35 Salts. **Design note:** the disposable, found/bought counterpart to Cautery Iron's Constant hub-commissioned version — same effect, different durability tag, different economy.

## Item 21 — Distilled Calm

- **Type:** Action Item · **Action Cost:** full Action, 2m
- **Effect:** fully clears Insanity to 0, regardless of current value.
- **Duration:** instant. **Consumable:** Y, Uses: 1. **Carry Limit:** 1 (deliberately rare).
- **Insight Gate:** Tier 2. **Limb Requirement:** a working hand.
- **Acquisition:** found only — does not appear in any standard shop stock. **Design note:** an item-based version of the Resolve 60 perk *Clear Mind*, giving non-Resolve builds occasional access to the same reset — Insight-gated and capacity-capped at 1 specifically so it doesn't trivialize the Insanity Break/Scar stakes.

## Item 22 — Salt-Cured Twine

- **Type:** Action Item · **Action Cost:** full Action, 2m
- **Effect:** fully clears both Corrosion and Burning to 0 in the same use.
- **Duration:** instant. **Consumable:** Y, Uses: 1. **Carry Limit:** 2.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot, uncommon. Bought at 40 Salts.

## Item 23 — Warding Chalk Circle

- **Type:** Action Item · **Action Cost:** full Action, 2m to draw
- **Effect:** while the wielder remains standing inside the drawn circle, incoming Influence stack applications to them are halved (round down, minimum 1).
- **Duration:** until the wielder leaves the marked spot, or the encounter ends — whichever comes first. **Consumable:** N (Constant — the chalk itself doesn't run out, only the drawn circle is temporary).
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found only — not sold at any stall. **Design note:** the only defensive item in the game that trades all mobility for a standing ward, rather than a one-shot consumable effect.

## Item 24 — Signal Chime

- **Type:** Action Item · **Action Cost:** full Action, 2m · **Range:** 6m
- **Effect:** applies 1 Discombobulation to a single target at range.
- **Duration:** instant application, effect persists per Discombobulation's own rules (Ruleset §5). **Consumable:** Y, Uses: 1. **Carry Limit:** 3.
- **Insight Gate:** none. **Limb Requirement:** a working hand and arm.
- **Acquisition:** found — general instance loot. Bought at 35 Salts. **Design note:** gives non-Toller-implement, non-weapon-gimmick builds a way to apply Discombobulation at range.

## Item 25 — Bled Ledger Page

- **Type:** Action Item · **Action Cost:** full Action, 2m
- **Effect:** heals a target **other than the user** for 25% of that target's own Max HP (cross-target heal, per the standing ruling that targeted Quick/Action Item heals scale off the target's Max HP, not the user's).
- **Duration:** instant. **Consumable:** Y, Uses: 1. **Carry Limit:** 2.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot, uncommon. Bought at 40 Salts. **Design note:** the dedicated ally-support Action Item — can never target the user, by design, so it's a genuine support pickup rather than a second self-heal.

## Item 26 — Hooked Anchor Line

- **Type:** Action Item · **Action Cost:** full Action, 2m · **Range:** 5m
- **Effect:** pulls the user 5m toward a fixed surface (wall, pillar, railing) — never toward an enemy or a hazard. Pure repositioning, no damage, no called shot.
- **Duration:** instant. **Consumable:** Y, Uses: 1. **Carry Limit:** 2.
- **Insight Gate:** none. **Limb Requirement:** a working hand and arm.
- **Acquisition:** found — general instance loot. Bought at 30 Salts.

## Item 27 — Weighted Coin Stack

- **Type:** Action Item · **Action Cost:** full Action, 2m
- **Effect:** immediately banks 10% of the user's current Purse (rounded down) directly to Vault, ignoring the normal "reach the hub" requirement. If Purse is currently 0, this item does nothing and isn't consumed.
- **Duration:** instant. **Consumable:** Y, Uses: 1. **Carry Limit:** 1.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found only — never sold, for obvious reasons. **Design note:** the game's only pure-economy item; a real pickup for a build that wants to bank early against a run going bad, at the cost of an Action better spent elsewhere.

## Item 28 — Cracked Opera Glasses

- **Type:** Passive/Equip · **Action Cost:** none, worn
- **Effect:** at Assess 2+, adds one extra sentence of detail specifically about a ranged/thrown attack's actual travel path (arc, deflection points, blind spots) — informational only, no numeric bonus.
- **Consumable:** N.
- **Insight Gate:** none. **Limb Requirement:** none, worn.
- **Acquisition:** found — general instance loot, uncommon. **Design note:** deliberately fluff-first — safe to stack with anything else worn, since it changes narration, not numbers.

## Item 29 — Tarnished Cufflink

- **Type:** Passive/Equip · **Action Cost:** none, worn
- **Effect:** +1 flat to saves against Influence specifically (not Insanity).
- **Consumable:** N.
- **Insight Gate:** Tier 1. **Limb Requirement:** none, worn.
- **Acquisition:** found — general instance loot, uncommon.

## Item 30 — Chipped Molar

- **Type:** Passive/Equip · **Action Cost:** none, carried
- **Effect:** once per hub cycle, the first Blood Loss stack taken during a run is negated entirely (as if it never happened) — same cadence convention as the Vigor 40 perk *Second Wind*.
- **Consumable:** N.
- **Insight Gate:** none. **Limb Requirement:** none, carried.
- **Acquisition:** found — general instance loot, uncommon.

## Item 31 — Wax-Sealed Locket

- **Type:** Passive/Equip · **Action Cost:** none, worn
- **Effect:** the wielder's own Corrosion cap is reduced from 5 to 4 — a narrow defensive nudge against one specific track.
- **Consumable:** N.
- **Insight Gate:** none. **Limb Requirement:** none, worn.
- **Acquisition:** found — general instance loot, uncommon.

## Item 32 — Frayed Prayer Cord

- **Type:** Passive/Equip · **Action Cost:** none, carried
- **Effect:** once per instance, the first time Insanity would hit its cap of 10 and trigger a Break, it instead holds at 9 for that single trigger — a one-time buffer, not immunity. Resets available again on the next instance.
- **Consumable:** N.
- **Insight Gate:** Tier 2. **Limb Requirement:** none, carried.
- **Acquisition:** found only — genuinely rare. **Design note:** deliberately narrow — buys one more turn against a Break, once per instance, never cancels the risk outright.

## Item 33 — Bent Tuning Key

- **Type:** Passive/Equip · **Action Cost:** none, carried
- **Effect:** for Precision Strike stopwatch tolerances specifically (Ruleset §10), treat the wielder's Insight window bonus as one tier higher than actual. Does not affect parry or detonation windows.
- **Consumable:** N.
- **Insight Gate:** none. **Limb Requirement:** none, carried.
- **Acquisition:** found — general instance loot, uncommon.

## Item 34 — Censer Incense

- **Type:** Consumable · **Action Cost:** Light Action to ignite
- **Effect:** fills a ~4m radius with dense, opaque smoke for 3 rounds. Anything inside the cloud can't see out; anything outside can't see in. Breaks line of sight for all purposes — Influence auras, targeting, Assess — both ways. Placed on the ground once lit, doesn't move with the user.
- **Consumable:** Y (single use per block).
- **Insight Gate:** none. **Limb Requirement:** none.
- **Acquisition:** found — Choir Deep recipe, instance loot. Thematically tied to choir preparation rooms (the choir needed protection from its own Singer's Influence during performances).
- **Design note:** a tactical positioning tool, not a ward. Solves the Singer's LOS problem without trivializing the fight — the user trades visibility for safety, and must step out of the cloud to attack. First found session 8, robing gallery annex, ×3 stack.

## Item 34 — Threadbare Glove

- **Type:** Passive/Equip · **Action Cost:** none, worn
- **Effect:** self-initiated called shots (Ruleset §10) have their tightened tolerance eased back half a band instead of the full band.
- **Consumable:** N.
- **Insight Gate:** none. **Limb Requirement:** a working hand, worn on it.
- **Acquisition:** found — general instance loot, uncommon.

## Item 35 — Salt-Stained Ribbon

- **Type:** Passive/Equip · **Action Cost:** none, worn
- **Effect:** once per hub cycle, the next Rupture the wielder takes deals 25% less damage. Stacks additively with the Vigor 20 perk *Resist Rupture* if both are active — **combined reduction from any source caps at 50% total**, stated explicitly to prevent runaway stacking.
- **Consumable:** N.
- **Insight Gate:** none. **Limb Requirement:** none, worn.
- **Acquisition:** found — general instance loot, uncommon.

## Item 36 — Shatter-Glass Ampoule

- **Type:** Reactive/Instant (no slot, usable anytime, including outside the wielder's turn)
- **Effect:** thrown at the wielder's own feet, immediately ends their current Discombobulation early. **Deliberate, explicit exception** to Discombobulation's standing rule (Ruleset §5) that it only ever counts down automatically — framed here as a rare emergency item, not a new standing mechanic. Flagging this explicitly rather than folding it in quietly.
- **Duration:** instant. **Consumable:** Y, Uses: 1. **Carry Limit:** 1.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found only — genuinely rare, never sold. **Design note:** priced in scarcity rather than Salts specifically so it can't become routine Discombobulation-clearing.

## Item 37 — Widow's Veil

- **Type:** Reactive/Instant (no slot, usable anytime, including outside the wielder's turn)
- **Effect:** for the remainder of the current encounter, the wielder can no longer be selected as the target of an enemy-side Influence Overload redirect (Ruleset §5). Doesn't reduce the wielder's own Influence stacks — purely removes them from the redirect pool.
- **Duration:** rest of the current encounter. **Consumable:** Y, Uses: 1. **Carry Limit:** 1.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found only — genuinely rare, never sold. **Design note:** narrow by design — only relevant in Influence-heavy congregation-style fights (the Choir Deep and similar), not a general-purpose defensive tool.

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
- **Identity, confirmed:** Lloyd carries this **and, separately, the Wooden Token that belonged to "R."** (character sheet) — two distinct physical items, not one whose material drifted. This one came from the reception clerk; the wooden one didn't. Closes the old open gap on this point.

**Template fields:** Category · Risk Status · Lost on Death?/Retreat? · Acquisition (base drop / bonus conditions) · Spend Options · Flavour.

---

*Sections 8–10 (Mechanic Index, Book Plan, Known Gaps) live in the dev log.*
