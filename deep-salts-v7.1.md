# THE DEEP SALTS
**A horror exploration RPG**

System-agnostic ruleset (d20 base) for solo play with an AI DM or a small table. One idea: you trade your humanity for power, and you can only see the trade once you've gone mad enough to look.

*Version 7.1 — session zero rulings folded in: visceral charges removed as a resource, enemy limb stagger duration + free-shot-on-trigger, Influence uncapped with DM-discretion severity scaling, self-initiated called-shot tightening. Rules flagged **(untested)** are proposed rulings awaiting playtest.*

---

## 1. The Premise

You take the salts — magical materials dissolved in hot water that transport you to another plane. Fight through, gathering loot, materials, experience and knowledge. Each area contains a clean chalice (the anchor) — drink from it to wake in Stillwell Hydro with everything from that run, banked. If you're close to death you can focus your mind and exit immediately, but you lose all equipment and materials on your person. Retrieve them by re-entering the same salts recipe and finding the same enemy you were facing when you bailed.

**Core loop:** brew a recipe in a salts room → wake in that biome, blind → survive (or don't) → return to the anchor and leave (or die, or bail) → restore and bank at the hub → push deeper or brew somewhere new. There is no fast travel — the recipe is the travel (§18). You become stronger, and less human, the further you go.

---

## 2. Running This With an AI DM

Hand the AI this document plus these standing instructions:

- **Never explain the world fully.** Let the player infer. Answer direct lore questions in-fiction through an unreliable source, or not at all.
- **Describe, don't signpost.** No quest markers. Telegraph danger through sensory tells, not labels.
- **Consistent hub, inconsistent everything else** (§14).
- **Track** the player's status tracks, Insight, limbs, White Salts, and inventory turn to turn. Surface when relevant; don't recite constantly.
- **Generate monsters live, then record them.** The monster table (§16) gives archetypes — HP bands, tells, movement — not fixed numbers. When a monster first appears, build its exact HP, attack damage, and stagger/sever thresholds on the spot using the Monster Template (separate document): start from the archetype's HP band, scale by player level (§17), never below the Damage Floor (§4). Then record the filled template in the monster manual — from that point on, those are the creature's canonical numbers whenever it or its kind reappears. Live generation is for first contact; the manual is the source of truth thereafter.
- **Honour the tells.** Parry and precision only work if you reliably narrate a readable tell before a heavy attack or weak-point opening. This is a promise to the player.
- **Run one recurring antagonist NPC** — reappears across warped locations, always slightly changed, never helpful (§14).
- **Don't gate kills behind sever.** Plain attacks reducing an enemy to 0 HP always kill it — full stop, on every enemy including bosses (§3, §10). Sever is a bonus fast-lane for enemies with enough HP that grinding would drag, not a requirement for killing anything. Reserve encouraging stagger/parry/sever play for fights where a plain slugfest would genuinely be a slog (elites, brutes, bosses); a basic mook should just die to a few solid hits.

Solo play suits the real-time stopwatch mechanics. At a table, see the d20 fallback in §9.

---

## 3. Core Resolution

Any d20-style base: d20 + modifier vs a difficulty number. The custom systems below sit on top.

**Default attacks land.** A light or heavy attack against an in-range target that isn't actively contesting it just hits — no attack roll, either side of the table. Tension lives in choices, not coin-flips. Rolls and stopwatches enter only when someone reaches for real risk:

- **Called shots** on limbs with a multiplier above 1.0 → the Precision stopwatch (§10), unless a parry already opened the target (§9).
- **Parries** and the enemy heavies that invite them → the Visceral stopwatch (§9).
- **Insanity and Influence saves** (a "fear save" is just an Insanity roll triggered by witnessing something dreadful) → d20 vs the Save Roll formula (§5).
- **Anything else genuinely uncertain** — stealth, forcing a door, reading something that shouldn't parse — straight d20 vs a DM-set DC, modified by the **Attribute Modifier** table below for whichever attribute applies. Light-touch.

**Attribute Modifier table** (for the generic uncertain-action clause only — does *not* apply to the Save Roll formula in §5, which has its own scaling):

| Attribute score | Modifier |
|---|---|
| 0–1 | −3 |
| 2–4 | −2 |
| 5–9 | −1 |
| 10–19 | +0 |
| 20–39 | +1 |
| 40–79 | +2 |
| 80–99 | +3 |

Keeps a flat, high stat (e.g. Skill 17+) from trivializing every DC in the 8–99 attribute range; investment still matters, but the d20 stays the dominant swing at every tier. Passive perks may grant additional situational bonuses on top of this table under specific conditions — those stack normally.

Same logic for enemies: a basic enemy attack lands automatically unless the player contests it — parries (§9) or is out of its move range (§7). No enemy to-hit roll; defense is entirely the player's, through timing and positioning.

**HP note:** reaching 0 HP always kills — that baseline never goes away, on any enemy, mooks or bosses alike. Enemy HP pools are just large on tougher things, so grinding a big pool down one swing at a time can turn into a slog. Severing a vital limb kills regardless of remaining HP (§10) — it's a *faster* route on enemies where the HP pool is the problem, not a requirement for killing anything. A basic mook with a small pool is meant to just die to a few plain hits; save the stagger/sever push for fights where attrition alone would actually drag.

---

## 4. Character Creation & Progression

### Backstory-Negotiated Creation

Before numbers, the player writes a short backstory and concept. The DM negotiates the mechanical translation:

- **Attribute reallocation.** Default spread is flat (8 in all five). A strong concept can redistribute the same 40-point pool unevenly. Total stays at 40 unless DM and player agree the concept earns more — always a two-way trade, never a freebie.
- **A bespoke starting weapon.** Instead of the Weapon table: type, governing stat, base damage placed in the existing range for the character's fictional strength (never under the Damage Floor), and one signature gimmick. A gimmick costs something (movement, setup, a self-applied track) for something (bonus damage, a status, positioning) — and any risk-for-reward uses the existing tools (stopwatch or d20 check), not a new resolution system.
- **A negotiation, not a wishlist.** The DM pushes back on anything that breaks the Damage Floor, ignores ESV, or gives something for nothing.

*Worked example on file: a young, pregnant guest with a kitchen knife. Result — low Vigor, knife at the floor, signature two-swipe-then-plunge: plunge deals double swipe damage, costs extra movement to set up, stopwatch check for bonus damage on the plunge.*

### Attributes

Five buyable attributes; Insight is a separate sixth dial (§11), earned not bought.

- **VIGOR** → max HP, Blood Loss resilience
- **ENDURANCE** → movement budget, visceral charges
- **STRENGTH** → heavy weapon damage, limb-sever power
- **SKILL** → light weapon damage, parry/precision tolerance
- **RESOLVE** → Insanity/Influence saves

All start at 8. Cap 99. Starting Insight = 1.

**Derived stats** (linear, from raw score):

- Max HP = 60 + (Vigor × 6) → Vigor 8 = 108, Vigor 99 = 654
- Movement budget = 8 + ⌊Endurance ÷ 15⌋ metres → End 8 = 8m, End 99 = 14m
- Insanity/Influence save bonus = ⌊Resolve ÷ 10⌋ → Resolve 8 = +0, Resolve 99 = +9

*(Visceral charges removed as a derived stat — session zero ruling. Parries are now gated entirely by timing accuracy and a genuine telegraphed opening, not a resource pool; see §9.)*

### Effective Scaling Value (ESV) — soft caps

Each point's contribution shrinks by band. Weapon/combat scaling uses ESV; derived stats above use raw score.

| Score range | Each point worth |
|---|---|
| 1–20 | ×1.0 |
| 21–40 | ×0.65 |
| 41–60 | ×0.4 |
| 61–80 | ×0.2 |
| 81–99 | ×0.1 |

A stat at 99 has an ESV of ~47. The back 19 points buy almost nothing — 99 is a statement, not a requirement. The smart stop is usually 40–60.

### White Salts — currency

Brass, same motif as the reception token. Earned from kills, exploration, discovery.

- **Purse** — earned this run. At risk.
- **Vault** — banked at the hub. Permanently safe.

Reaching the hub moves the full Purse into the Vault. Abandon-All, Retreat, and Death (§12) only ever touch the Purse — the Vault is never at risk, no matter which fail-state ends the run. Spend Vault White Salts on attribute levels.

### Leveling

Level = total points spent across the five attributes, lifetime. One point in any attribute = +1 level. Cap: level 100. Cost of the next point = 25 × current level.

| Checkpoint | Cumulative spent | Next level costs |
|---|---|---|
| Level 10 | 1,125 | 250 |
| Level 25 | 7,500 | 625 |
| Level 50 | 30,625 | 1,250 |
| Level 75 | 69,375 | 1,875 |
| Level 100 | 123,750 | — (final purchase: 2,475) |

### Perks — at 20/40/60/80/99 in each stat

Granted per points invested in that stat specifically, not character level.

**VIGOR**
- 20 — *Resist Rupture:* rupture damage reduced 25%.
- 40 — *Second Wind:* once per hub cycle, a hit that would drop you to 0 HP leaves you at 1 and clears one track of your choice.
- 60 — *Thick Hide:* flat −2 damage reduction on all incoming hits.
- 80 — *Iron Lungs:* immune to Burning spreading from nearby sources (direct Burning still applies).
- 99 — *Unbreaking:* once per encounter, a rupture leaves you at 1 HP instead of resolving in full.

**ENDURANCE**
- 20 — *Light Foot:* moving immediately after an attack costs 1m less.
- 40 — *Overcharge (PROVISIONAL — needs sign-off):* a whiffed parry, once per encounter, is treated as a chip hit instead of the full whiff punishment. *(Original wording referenced visceral charges, now removed — placeholder pending a real replacement.)*
- 60 — *Quick Recovery:* track management becomes a Fast Action instead of an Action.
- 80 — *Outrunner:* movement budget can never drop below half, regardless of leg stagger/severance.
- 99 — *Endless (PROVISIONAL — needs sign-off):* once per encounter, immediately retry a failed precision/visceral stopwatch check with no whiff punishment. *(Same note as above — orphaned by charge removal.)*

**STRENGTH**
- 20 — *Heavy Hand:* raw damage counts +5 solely when checking sever thresholds.
- 40 — *Brute Force:* charged heavies treat boss stagger meters as one tier lower.
- 60 — *Render:* a successful sever also dumps bonus stagger damage onto an adjacent limb.
- 80 — *Executioner:* sever/decapitation attempts against a staggered target deal +10% raw damage.
- 99 — *Annihilate:* once per encounter, declare a heavy attack an automatic sever if it meets the effective damage threshold — no precision check.

**SKILL**
- 20 — *Steady Hand:* all precision windows widen a flat +0.02s.
- 40 — *Featherstep:* first Assess each turn costs 0 movement.
- 60 — *Riposte:* a successful parry grants a free light attack before you resolve the visceral.
- 80 — *Untouchable:* missed-precision punishments reduced one band.
- 99 — *Perfect Read:* once per encounter, automatically succeed one stopwatch check of your choice.

**RESOLVE**
- 20 — *Iron Will:* reroll a failed Insanity save once.
- 40 — *Unshaken:* Influence command duration reduced one round.
- 60 — *Clear Mind:* once per encounter, clear Insanity to 0.
- 80 — *Silence the Hum:* immune to passive/ambient Influence; direct spoken commands still land.
- 99 — *Indomitable:* on a failed Insanity save, act with disadvantage instead of losing control — the DM never fully takes you.

### Weapons

**Damage = Weapon Base + (ESV of governing attribute × letter-grade multiplier).** Heavy/charged attacks roughly double the base and apply ×1.5 to the scaling term. Grades: E ×0.3 · D ×0.5 · C ×0.7 · B ×0.9 · A ×1.1 · S ×1.3.

| Weapon | Type | Stat / Scaling | Two-handed? | Gimmick |
|---|---|---|---|---|
| Tideglass Cleaver | Quick | Skill / C | Optional | Light attack swings twice per action, second hit at reduced damage |
| Cautery Saw | Heavy | Strength / B | Yes | Slow, huge single hits — best raw weapon for sever thresholds |
| Birthing Hook | Reach | Skill / C | Optional | Wide sweeps; strong vs multiple limbs or grouped adds |
| Funicular Spike | Reach/thrust | Strength / B | Yes | Bonus damage vs already-staggered targets |
| Brass Token Press | Trick | Skill ↔ Strength | Switches | Folds between Quick and Heavy mid-fight; full transform gated behind Insight Tier 1 |

*Worked example — Cautery Saw heavy attack, base 30 (anchored so the sever claim holds): Str 8 → ESV 8 → 2×30 + (8×0.9×1.5) ≈ 71. Str 40 → ESV 33 → ≈ 105. Str 99 → ESV ~47 → ≈ 123 — just past the head's 120-raw sever line (§10). Other bases in the table are placeholders.*

### Damage Floor & Scale

Numbers run high, not d20-fantasy-modest — the ESV and multiplier maths only stays clean at scale. **20 is the practical floor for any base number that passes through a multiplier** (weapon bases, enemy attack damage, DM-generated numbers). 20 keeps results whole across the multipliers that actually come up (×0.65 = 13, ×0.75 = 15, ×1.5 = 30), and anything lower makes weak weapons unable to sever, ever — not the intent (a kitchen knife is still a knife). The floor doesn't bind flat, unmodified numbers (a Quick Item heal, a status tick).

Enemy HP (§16) and thresholds (§10) scale to match: archetype HP band × level multiplier (§17), attack damage proportionate to what Max HP and Rally (§6) can absorb — a mook stings, a boss's telegraphed haymaker is a real chunk that Rally can partially forgive.

---

## 5. Status Tracks

Most conditions are tracks — counters that build (0–10) rather than switches. Defaults below; tune to taste.

**BLOOD LOSS** — 1 stack per qualifying slashing/piercing hit or hazard. Each new stack deals immediate bonus damage equal to the new stack total (0→1: +1; 1→2: +2; five consecutive cuts = 15 bonus total). No passive drain between hits. Cap 10 → triggers Rupture, resets to 0. Clear: bandage, cautery, or a pressure action (a Wrap clears 2 stacks, §8).

**RUPTURE** (triggered only, at Blood Loss 10) — 25% of Max HP direct damage, staggers you a beat, resets Blood Loss to 0. Low Rally recovery — ten unmanaged stacks are meant to stick. **(untested)**

**INSANITY** — the "character acts without you" meter. On taking damage, witnessing something wrong, or failing a fear save: Save Roll (below). Fail → DM controls you one turn (freeze, flee, strike the nearest body, speak to something that isn't there). High Insight raises this. *Not the same as Insight.*

**BURNING** — ticking damage each turn. Spreads to oil, cloth, steam-soaked surfaces. Action to smother. Heat sources can re-ignite you.

**DISCOMBOBULATION** — a Tick, not a track. Applied at 1–3 (DM's call by severity: scrambled sign = 1, the source-spring stair = 3), counts down 1 at end of each of your turns automatically. While active the DM may misdescribe exits, reverse movement, strip reactions, or scramble attack directions — pick what fits. A fresh application refreshes to the new value if higher. Cap 3. (Long-term cousin: Fugue, §13 — a Track, not a Tick.)

**INFLUENCE** — some enemies suggest rather than strike, verbally or otherwise — a spoken command, or just a pull, an ache, a wordless want. Builds as a Track like Blood Loss, but **uncapped past 10** — no fixed overflow trigger, no Rupture-equivalent. Instead, **the severity of compelled effects available to the DM scales with stack count**: low stacks might mean lingering near a source or a minor compulsion; higher stacks can escalate to dropping a weapon, fleeing, self-harm, or striking an ally. This is deliberately open-ended DM discretion, not a fixed table — calibrate severity to stack count and use judgment so it doesn't wreck pacing. On a failed save, obey the effect (or the enemy's spoken command, if it has one) on your next turn. Susceptibility rises with Insanity and Insight.

- **First save trigger:** a source's stacks don't force a save until the 2nd stack lands. *(Session zero ruling.)*
- **Clear conditions:** a successful resist alone does not clear the stack while the source remains active — it only avoids that turn's compulsion. Full clear happens once the source is eliminated (line of sight fully broken). **With multiple simultaneous sources, full clear requires ALL active sources gone** — killing one of several just stops that one from adding further stacks. *(Session zero ruling.)*
- **Insanity tick threshold:** a failed Influence save also ticks Insanity, but only once the stack is at **3 or higher** — not at the 2-stack mark where the save itself first triggers. The save-trigger stack (2) and the Insanity-tick stack (3) are deliberately different numbers, not a copy-paste of each other. *(Session 3 ruling — resolves prior inconsistency between 2+ and 3+ seen in play.)*

**CORROSION** — stacking decay. Damage at start of your turn = stacks × 2. Cap 5 (10/turn). Stacks tick down 1 at end of turn ONLY IF you spent an action managing them (douse, scrape, neutralise); otherwise they hold. Sources: acid, spores, fouled water, coatings. Stacks viciously with Burning.

### The Save Roll (Insanity & Influence)

One formula, both saves. Roll 1d20; succeed on:

**≥ 10 + (current track value) − ⌊Resolve ÷ 10⌋ + ⌊Insight ÷ 2⌋** (+ situational mods from gear or the enemy). **(untested)**

*Worked example: level 1, Resolve 8, Insight 1, second Influence stack → 10 + 2 − 0 + 0 = 12. Later: Resolve 30, Insight 6, Influence 6 → 10 + 6 − 3 + 3 = 16 — Resolve pulls its weight, Insight spends it right back.*

---

## 6. Rally

Damage taken becomes recoverable grey health for a short window. Land a hit before it closes and claw back a portion. The core risk engine — it rewards pushing into danger.

**Window:** your very next turn only. Land a qualifying hit before that turn ends or it fades.

**Recovery is per-attack, default 50%** of damage taken. Overrides (noted in the attack's Hit Effect field once templated):

- Big telegraphed commit-everything hits (boss haymakers) skew high: 75–100%.
- Chip and DoT (Burning, Corrosion, rupture) skew low: 0–25%. Attrition should attrite.
- Passive gear can shift a source's percentage per its listing.

---

## 7. Movement & Positioning

Movement is combat's third axis.

**Budget** set by Endurance (8–14m). Movement is the single per-turn currency: repositioning *and* actions both draw from it. Spend before and after your action — in, strike, out — up to the total, minus whatever your action itself costs (§8).

**The hard rule:** if you can't pay an action's movement cost, you can't take it. Sprint the full budget and you've got no attack left in you this turn. Every metre run is a metre you can't fight with.

**Hit-and-run.** Attack and retreat beyond the enemy's reach in one turn. No parry = no visceral opening — chipping, not opening. Safe, slow, low-reward. Good when hurt, out of charges, or whittling something you can't yet open.

**Kiting.** Enemies have move budgets too. If yours exceeds theirs, stay out of reach and chip. A slow enemy in open space is manageable; a slow enemy that has cornered you is not.

**Burst-movers.** Some alternate a surge turn (huge ground, often attacking only at the lunge's end) with a recovery turn (barely moving). Read the rhythm: in during recovery, out before the surge. Assess (§9) can reveal movement patterns, not just tells.

**The triangle:**
- **Trade** — stand and swing. Fast damage, eat hits.
- **Parry** — high risk, high reward. Viscerals and weak points; a whiff hurts.
- **Kite** — move and chip. Safe, slow, no openings, useless against anything as fast as you.

Good play flows between all three as health, charges, and tempo shift.

---

## 8. Action Economy & Items

Three pools per turn, plus one category outside them all.

**Movement** — your budget, splittable around your Action. Actions cost movement (below); Fast Actions never do.

**Action** (one per turn — each costs movement from the budget, paid on use):

| Action | Movement cost | Fiction |
|---|---|---|
| Light attack | 1m | Plant feet, jab, keep moving |
| Heavy attack | 3m | Full stop, wind-up, commit |
| Hold (parry stance) | 2m | Set stance, weight down, wait |
| Manage a track (smother, scrape, pressure) | 1m | A pause, not a production |
| Use an Action Item | 2m | Hands busy, attention split |
| Assess | 1m | Reading, not acting |

Costs above are the defaults — specific weapons and actions may price differently, and perks may refund movement after an action, grant bonus movement before one, or zero a cost under conditions. (Perk design space, not yet populated.)

**Fast Action** (one per turn, always 0m):
- Use a Quick Item, load a capsule — anything done on the move. That's the whole point of the category.

Heal-and-attack is real: Quick Items are Fast Actions, so vial-and-swing works. The lever is potency — Quick Items are deliberately weak; anything strong costs a full Action, competing with attacking. Big heal OR attack; small heal AND attack.

**Reactions** sit outside all pools — things that happen on someone else's turn. Abandon-All (below) lives here; Retreat (§12) does not — it can't be invoked in active combat at all, only between fights.

### Limb-gating

| Requires | Staggered | Severed |
|---|---|---|
| Weapon arm (attacks, holds, item use) | −1 die / heavies disabled this turn | Can't wield that side; off-hand only, reduced damage, two-handers unusable |
| Legs (movement) | Budget halved | Crawl only (1m), can't kite, prone (standing costs your Action) |
| Head | Dazed — Discombobulation 1 turn, can't Assess | Dead (head severance always lethal) |
| Torso | n/a — torso stagger is just heavy damage | Dead |

A staggered leg takes kiting off the table — the triangle narrows by one option, yours or theirs.

### Items

**Durability tags (Session 2 ruling).** Every item carries exactly one tag answering "what happens to this over time":

- **Constant** — persists indefinitely, unlimited uses. Equipment, keepsakes, the Beckoner. Any per-use *cost* (like the Beckoner's Influence stack) still applies; the tag only means the item itself never runs out.
- **Hub Kit** — recharges/resets free on every return to the hub. The standard consumable kit (§14) and signature-weapon ammo (e.g. powder capsules).
- **Uses: [N]** — works N times, then it's spent. NOT refilled by the hub; may be rechargeable by other in-world means if one is ever found. The Charm is Uses: 1 — destroyed on use.
- **Instance-specific** — cannot leave the layout it was found in; expires with the instance (see §18). Journals, keys, environmental tools that only mean something where they lie.

When an item enters play, the DM assigns its tag on the spot.

**Quick Items** (Fast Action — weak, frequent):
- **Wrap** — clears 2 Blood Loss stacks
- **Camphor** — clears 2 Insanity stacks (a vial of sharp resin; one hard breath and the walls stop moving — grounding, not curing). *(Renamed from "Salts," session 2 — killed the currency name-clash and defined the effect properly; Insanity is a build-only track, so items are its main downward pressure alongside Resolve 60's once-per-encounter clear.)*
- **Tonic** — small flat heal (~10% max HP)
- **Scour** — clears 1 Corrosion stack without costing your turn

**Action Items** (full Action — strong, situational):
- **Source-water flask** — big heal, but adds an Influence stack. Power for vulnerability. *(Uses: 1 per flask — found or bought, never hub-refilled.)*
- **Cautery iron** — fully clears Blood Loss; stationary and exposed while using (costs your full remaining movement budget on use, not the standard 2m). *(Constant — it's a tool, not a consumable.)*
- **Thrown vial** — applies Corrosion/Burning at range. *(Uses: 1 per vial.)*
- **Charm** — one-shot buff (extra die, widened parry window); Insight-gated to use (§11). *(Uses: 1 — destroyed on use, session 2 ruling.)*

**Reactive / Instant** (usable anytime, even mid-enemy-turn, no slot):
- **Abandon-All** — the panic word, the psychic tether home. Spoken or thought — needs only a working mind and voice, no limbs. Mechanically (§12): instant, free, usable between any two actions including mid-resolution of an attack — but forfeits everything carried in that instance, gear included, not just the Purse. Left-behind gear is recoverable later from a guaranteed enemy in a future instance of the same biome. The only counter — a gag/silence effect or an enemy that severed your voice — is rare, boss-tier, always telegraphed. **Retreat (§12) is the cheaper, slower cousin — Purse-only cost, but can't be used mid-combat.**
- **Distress flare / ally beacon** — same category; multiplayer hook for later.

**Passive / Equip** (no slot, always active) — trinkets and build-around gear. Modifies numbers only; often Insight-tier-gated to equip.

---

## 9. The Visceral System (parry + stopwatch)

The signature mechanic. You need a stopwatch (phone is fine).

**Assess.** Spend 1m of movement: the DM reveals an enemy's tell and rough timing of its next heavy (and, if relevant, its movement pattern). Clarity scales with Insight — low gives a ballpark ("about a second and a half"), high gives a tighter, truer call. You can then hold your action to parry on the enemy's turn.

**The parry:**
1. Enemy telegraphs a heavy. Attack type maps to a window — target time and tolerance. Examples: Lunge 1.50s ±0.20 · Overhead 2.00s ±0.15 · Sweep 1.20s ±0.25. Faster, tighter = more dangerous.
2. Start the stopwatch — no charge cost, no cap on attempts. *(Session zero ruling: charges removed; parries are gated by timing and a real opening only, to stop players hoarding attempts for bosses instead of playing the system.)*
3. Pause inside the window.

**Outcomes:**
- **Inside → PARRY.** Enemy opened. Visceral: your next strike deals 1.5× damage (plus Insight mods), knocks the enemy down, ends its turn, costs it movement next turn. Some enemies retaliate when viscerald (§16).
- **Outside → WHIFF.** Eat the heavy in full plus a punish (DM's pick: crit back, apply a track, or stagger you a turn). A whiff hurts more than blocking — that's the gamble. Don't reuse a tell: a second, different heavy on the last one's timing gets you killed.

Insight widens windows and unlocks visceral mods (§11): Bloody, Sustaining, Quickening.

### Post-parry weak points — three tiers

DM assigns per enemy on a simple read: does a parry reliably floor this thing?

- **Tier 1 — Open** (default). Parry floors them; the weak point is yours, no second stopwatch. The parry was the skill check. (Mooks, elites.)
- **Tier 2 — Widened** (some bosses). Opened but not floored. Precision window (§10), widened one tier.
- **Tier 3 — Full double** (bosses, chaotic limbs). Parry stopwatch, then a second precision stopwatch at normal tightness. The ceiling, not the norm.

**Table fallback:** if real-time timing bogs down, replace any stopwatch with a d20 reflex roll using Insight as the modifier, same outcomes. Solo AI play uses the stopwatch.

---

## 10. Limbs, Precision & Mutation

The character-build system. You and your enemies have targetable limbs; losing them is how you become something else.

**Baseline first:** every enemy still dies the ordinary way — plain attacks against its torso chip its HP, and 0 HP is dead, same as any d20 game. Everything below is an *additional*, faster route available on tougher enemies, not a replacement for that baseline.

### The limb model

Each limb has a (damage multiplier / stagger threshold). Standard humanoid:

| Limb | Multiplier | Stagger threshold |
|---|---|---|
| Head | ×1.5 | 180 |
| Torso | ×1.0 | 800 |
| Arm (each) | ×0.65 | 200 |
| Leg (each) | ×0.75 | 300 |

- **Effective damage = raw × multiplier.** Chips the HP pool AND fills the limb's stagger meter.
- Threshold reached **over several hits → STAGGER.** Limb goes limp. **The hit that crosses the threshold grants an immediate free called shot that same action** — no precision stopwatch, same as a Tier 1 parry opening. Player-side stagger duration is fixed at one turn (§8). **Enemy-side stagger duration is variable**, set per creature and per limb on that monster's own Monster Template entry (design bible §1) — some enemies limp one turn, others three or five, author's call. *(Session zero ruling.)*
- Threshold reached **in a single blow → SEVER.** Limb destroyed, permanently.
- **Severing a vital limb kills regardless of HP.** Torso or head off = dead. Arms/legs cripple but don't kill.
- **No free called shots** on a standing, alert, unstaggered enemy. A specific-limb shot (especially the head) needs an opening — stagger, knockdown, off-balance, parry — or takes a called-shot penalty. Default swings land torso.
- **Small/high-value called-shot targets (a bell, a crack in scale, an eye) are mechanically limbs** — no separate system needed. Author them as a non-standard limb entry (the Monster Template already reserves space for these alongside tentacles/cores) with an appropriately high multiplier; the existing Precision Strike tolerance table already tightens automatically as the multiplier climbs. They use the **Sever** mechanic (single hit meets threshold → permanent disable) rather than Stagger — there's no meaningful "temporarily cracked bell" state. *(Session zero ruling.)*

*Worked example: a leg (×0.75, 300) needs 400 raw in one hit to sever. The head (×1.5, 180) needs 120 raw — a charged heavy clears it, a light swing doesn't.*

**Sever is a mid-level payoff, not a requirement.** Plain damage to 0 HP kills anything on its own — sever just skips the rest of the pool when it's available. The standard humanoid thresholds above are **fixed constants — they never scale with level band (§17).** Only HP scales. Your raw damage climbs while thresholds hold still, so solidly mid-level with a sever-capable weapon, one-hit decapitations on standard enemies open up. Reference: with the Cautery Saw and real investment, one-hit head sever starts around raw Strength 60–80 depending on perks. Arms (~308 raw) and legs (400 raw) stay out of one-hit reach even at 99 with current numbers — they're staggered, not severed. The head is deliberately the one glamour target.

**Bosses don't use these numbers.** Every boss gets hand-set limb values on its own Monster Template. Set the key weak-point threshold high enough that clearing it in one hit takes a heavily specialised build — DM judgment per boss; a generous weak point can be a boss's whole gimmick, but most shouldn't have one.

### Precision Strike — the greedy-target tax

Targeting any limb with a multiplier **above 1.0** triggers a precision stopwatch. At or below 1.0 (torso, arms, legs) — never affected.

| Multiplier | Tolerance (±) | Feel |
|---|---|---|
| 1.01–1.25 | ±0.25s | generous |
| 1.26–1.50 (head) | ±0.13s | tight |
| 1.51–1.75 | ±0.09s | very tight |
| 1.76–2.00 | ±0.06s | savage |
| 2.01+ | ±0.04s | frame-perfect |

Target time set by the DM per opening (default ~1.50s, range ~1.0–2.0s). Miss punishments scale with greed:

| Band | On a miss |
|---|---|
| 1.01–1.25 | Lands on torso — full damage, no multiplier, no sever |
| 1.26–1.50 | Torso, no sever, + off-balance (−1m move next turn) |
| 1.51–1.75 | Goes wide — no damage, enemy gets a free reactive strike |
| 1.76+ | Whiff + exposed — enemy free heavy, or you take a track (DM's pick) |

**Parry interaction (the key relief):** the precision watch only appears when going for a >1.0 limb *without* a parry, or against Tier 2/3 enemies. Tier 1 parry removes it entirely (free placed shot); Tier 2 widens it one tier; Tier 3 keeps it full. The standard loop — assess → parry → free weak point — stays clean; execution pressure appears only when earned.

**Self-initiated called shots (no enemy tell to anchor timing on).** Some called shots aren't reacting to a telegraphed enemy heavy at all — going for the head or weak point of something that never winds up (an unparryable grasp, a stationary target). There's nothing external to time against, so the DM tightens the tolerance **one band beyond what the multiplier alone would indicate**, reflecting the added difficulty of a blind attempt. Critically: **a miss on a self-initiated called shot ends the turn outright** — no remaining movement can be spent repositioning or kiting away. A **hit** lets the remaining movement budget be used normally. This asymmetry, not an invented visual/audio cue, is what makes a blind shot a real risk. *(Session zero ruling.)*

**Ambush called shots (full unawareness).** A target that is genuinely unaware — a successful stealth approach, not just a stationary/unparryable one — counts as at least a **Tier 1 parry-grade opening**: the called shot lands free, no precision stopwatch at all, same as a real parry. And because the ambush itself is the "opening," it stacks with the standard **visceral 1.5×** the way a Tier 1 parry's free weak point always has — the two multipliers were never meant to be interchangeable substitutes for each other, they compound (raw × visceral 1.5× × limb multiplier). *(Session 3 ruling — this is what let a Skill-build ambush headshot clear a standard humanoid's sever threshold in one hit.)*

### Corrupted Regrowth — the build engine

A lost limb regrows at the hub with a chance of coming back changed. A wrong-grown limb carries a trade — clear upside, clear downside:

- **Beastly arm** — +X damage / −X ms parry window
- **Tendril arm** — +reach & grapple / −accuracy
- **Carapace leg** — +stagger resistance / −movement

You can only read the trade at sufficient Insight. Below the threshold the limb just feels wrong — the DM gives vibes, not numbers. High Insight reveals the full stat line.

By endgame you're curating monstrosity — deliberately farming limb loss to reroll for better mutations. The horror is that you chose this, one sensible trade at a time.

**Regret options (hub):** **Revert** to human — costs Vault White Salts, or Insight itself (forgetting what you've become). **Reroll** — regrow and gamble again, also a Vault cost. Both run.

---

## 11. Insight — the Bargain

The spine of progression, separate from the five buyable attributes. Never purchased — earned through discovery: lore uncovered, dangerous sources tasted, things defeated that grant sight. A Faustian dial: it buys power and quietly thins the wall between you and losing control.

**What it buys:**
- **Threshold gates** — some doors, paths, and warp-thresholds require your Insight score to perceive or enter. Free to pass once there — a check on who you've become, not a purchase.
- **A spendable currency** — separately, Insight can be spent (drawing down your score): forcing certain gated doors, buying Insight-priced weapons/equipment, summoning support (below).
- **Sight of the board** — higher Insight = the DM tells you things others never learn: a tell before it strikes, an Influence command before you must save, the true layout of a discombobulating room, truer parry timing on an Assess.
- **The visceral economy** — unlock and load visceral mods, stronger ones gated behind higher tiers.
- **Reading your own mutations** (§10).

**The cost (passive):** each tier raises your Insanity/Influence susceptibility — formalised as the +⌊Insight ÷ 2⌋ term in the Save Roll (§5). More powerful and more fragile, simultaneously.

### Insight Tiers

| Tier | Insight | Unlocks |
|---|---|---|
| 0 | 0–1 | Mundane start. Vague reads, no mods, base floor. |
| 1 | 2–3 | Bloody mod. Parry window +0.05s. Low-grade mutation reads. |
| 2 | 4–5 | Sustaining mod. See warp-thresholds. Window +0.10s. |
| 3 | 6–7 | Quickening mod. Full mutation stat-lines. Charm items usable. |
| 4 | 8–9 | Window +0.15s. Untranslatable lore becomes comprehensible. |
| 5 | 10 | Full sight. Deepest hub content unlocked. |

**Window bonus is a flat total per tier, not additive across tiers crossed.** A tier that doesn't list its own number (Tier 3 above) simply inherits the last stated value rather than adding nothing — Tier 3 carries Tier 2's +0.10s forward until Tier 4 explicitly raises it to +0.15s. Applies to any DM-set timing window (parry, precision, or otherwise), not just parries specifically. *(Session 3 ruling.)*

**Tier trade-offs cut both ways** (DM's discretion on crossing a tier):
- New enemy tells and attacks visible on an Assess that a dimmer character wouldn't perceive.
- Occasionally an enemy gains something it didn't have — your Insight woke it up.
- Extra parry-window widening on specific high-tier enemies or locations, stacking with the flat bonus.
- Free, no-roll perception reveals — a shape in the fog, a word under the humming, a door that wasn't a door a floor ago.

### Spending Insight

Spending immediately reduces your current score. Drop into a lower tier and you lose its benefits — mods, window bonuses, sight — until you earn back up. The upside: your Insanity/Influence floor drops with it.

Spendable on:
- Forcing a gated door/path where the location calls for a spend rather than a threshold (DM states which, per location).
- Weapons/equipment priced in Insight (noted on the item's template).
- **Summoning a support ally** — spend Insight (default 2) to call something to your side for the current encounter: a fellow patient, something that owes you, a piece of the Hydro that likes you today. Temporary, unreliable, never explained. **(untested — cost, duration, and capability are DM calls until run.)**

### Visceral Mods **(untested numbers)**

- **Bloody** — on a landed visceral, roll one bonus damage die, sized ~base ÷ 4 rounded to the nearest standard die (base 20 → d6).
- **Sustaining** — while slotted, restore 15% of damage dealt as HP. Applies to any hit, not just viscerals.
- **Quickening** — while slotted, movement budget +2m for the encounter.

---

## 12. Abandon-All, Retreat & Death — the Fail-States

Two ways out under your own power — one instant and costly, one slow and cheap — plus the one you don't get to choose.

**ABANDON-ALL (the panic button).** Instant, free, usable mid-combat — between any two actions, including mid-resolution of an attack. Spoken or thought — needs only a working mind and voice, no limbs. Declare → yanked to the hub. Keep character, levels, limbs/mutations; **forfeit everything carried in that instance — Purse and gear both.** Left-behind gear isn't destroyed: it settles on/with a guaranteed enemy of that instance's archetype, recoverable by finding and beating that archetype in a future instance of the same biome — same logic as a killer holding a dead character's gear (below), no expiry, doesn't compound. Can be a same-session errand or a long-burn goal, player's call. The only counter — a gag/silence effect or an enemy that's severed your voice — is rare, boss-tier, always telegraphed. *(Session 3 ruling — previously this WAS "Retreat," Purse-only; split out as the expensive, any-time option once actual play showed a mid-fight escape needed a real cost.)*

**RETREAT (the calm way out).** Takes a few real minutes of deliberate meditation — **cannot be invoked in active combat**, only between fights or in a genuinely safe moment. Declare → yanked to the hub. Keep character, levels, limbs/mutations, **and all carried gear**; forfeit only the run's Purse. The controlled version of walking away: disengage first, then leave clean, rather than panic-wording out mid-swing. *(Session 3 ruling — split from Abandon-All.)*

**DEATH (you didn't make it).** Respawn in the salt room you entered from (§18). Keep character, levels, mutations. But:

- **Gear is forfeit to your killer.** Everything carried stays on the corpse — or inside the thing that ate you. Take it back, usually by killing what's now wearing it. Lost gear does NOT compound — die on the recovery run and the first death's gear is still where it was. Chip away, level elsewhere, return when ready.
- **Purse fully lost.** No floor pickup, no run-back recovery. The Vault is never touched. Bank often.
- **Fugue applied** (§13).

---

## 13. Fugue — When Your Sight Betrays You

Applied on death. Keep it distinct from Discombobulation: Discombobulation scrambles navigation and action ("I don't know where I am"); Fugue corrupts Insight reads — false tells, fake Influence commands, subtly wrong layouts ("I can't trust what I think I know").

Death doesn't change your Insight number — no farming it by dying, no dumping it to shed your floor — it makes your existing Insight *lie*. Higher Insight relies more on accurate reads, so corrupted sight hurts the eldritch build more. Death scales its sting to how far you've ascended.

**Clearing:** spend the next Insight point you earn — it clears your head instead of joining your stack. Death quietly costs forward progress a second way; high-Insight players clear it fast, low-Insight players can let it ride.

---

## 14. The Hub

The only stable thing — and even it should be slightly wrong.

- **Full restoration, always.** Whatever was torn off, home fixes it (regrowth per §10 — possibly changed).
- **Hub Kit (Session 2 ruling).** On every hub arrival, the consumable kit refills to its standard loadout, free — same logic as HP and signature-weapon ammo. Default kit: **2× Wrap, 2× Tonic, 1× Camphor, 1× Scour.** Unused items don't stack past the kit cap. Anything beyond the kit (Source-water flasks, thrown vials, cautery irons, found items) is acquired in runs or bought at the hub with White Salts — the item economy sits on top of a guaranteed floor, so a run is never lost to bad shopping.
- **Banking.** Purse moves fully into Vault on arrival. Spend Vault White Salts on attribute levels (§4), mutation revert/reroll (§10), and other hub services.
- Same room every visit, **one detail changed each time** — a clock never showing the same time twice, an NPC recalling a conversation you haven't had yet. Safe and faintly unnerving.
- **The recurring antagonist:** one NPC reappearing across warped locations — always slightly different, always unhelpful or hostile, never explained. (In the starter location: the reception clerk.)

---

## 15. Starter Location — STILLWELL HYDRO

*(Placeholder name. Deliberately NOT a Victorian blood-hunt city.)*

A convalescent bath-house in a fog-drowned valley, built over hot mineral springs meant to cure. Terraced pools, brass White Salts, attendants in waxed-canvas aprons, no electric light. The era is intentionally slippery. It is warm, quiet, and almost pleasant. That is the trap.

**Your mundane goal.** You came to take the waters — for an ailment, or to collect a relative who checked in weeks ago and stopped writing. The front desk has your name. Everything is in order.

**The calm threshold (start here).**
- A funicular carriage carries you up through the fog. The attendant doesn't speak. On arrival, you can't see the carriage behind you anymore.
- Reception. A clerk hands you a token, a robe, and a key. He apologises that your relative "is taking the deep cure and can't be disturbed." Ask again and he repeats it word for word.
- Changing rooms full of other guests' clothes — folded neatly, layered with dust. Far more than there are guests.

**The first wrong note.** Your private pool is the perfect temperature, and the longer you sit, the more you don't want to leave (first taste of Influence — soft, pleasant). Through the steam, someone in the next pool hums a tune you half-know. There is no one in the next pool. There is no next pool — that wall is solid.

**The doorway into the nightmare.** Past the soaking terraces lies the deep cure — the source spring, where the "long-term patients" go. The stair down is humid, then hot, then thick enough to bring on Discombobulation. At the bottom, the door behind you opens onto somewhere that is not the stair you came down. Your first warp threshold and the point of no return — death/respawn rules go live.

**Seeds.**
- Recurring antagonist: the reception clerk, met again somewhere impossible, apron on now, still apologising, still word for word.
- Inventory oddity: a brass token in your robe pocket that isn't yours — worn smooth, warm, fitting no slot anywhere. Yet.
- The relative: still "taking the deep cure." You will learn what that means. You will wish you hadn't.

---

## 16. Default Monster Table

Archetypes, not fixed creatures — reskin per location. Plain attacks to 0 HP always kill; limbs and openings (stagger, sever) are the *faster* route on anything with enough HP that grinding it down would drag — mooks with small pools are meant to just die to a few hits, no called shots required. Attack damage isn't listed — generate live (§2), scaled to level (§17), never below the Damage Floor.

1. **SHAMBLER** (mook) — HP ~200–1200, low end for zero-threat teaching mooks (playtest note: a mook with no real offence and no visceral path shouldn't out-tank the fights that follow it) · Move slow (3m). The basic body. Lights only, no parryable heavy — a soft tell-less grab applying Influence or a track. Comes in 2s–4s and swarms. Kiteable. Unparryable, so there's no visceral loop on this thing at all — it just dies to plain attacks like anything else. Staggering a leg then taking the head (§10) is a faster option once the player's learned the limb system, never the required route. The teaching enemy for limbs.
2. **LUNGER** (elite) — HP ~500–700 · Move medium (5m). One telegraphed heavy + Blood Loss. Tell: raises blade to eye-line, steps in (~1.4s). Tier 1 — parry, free head. Teaches assess → hold → parry, and the reuse-a-tell trap if it has a second, faster jab.
3. **BURSTER** (skirmisher) — HP ~400–600 · Move burst (8m surge / ~1m recover). Surges across the room, striking only at the lunge's end, then must recover. Tell: coils before the leap. Tier 1–2. The §7 dance enemy.
4. **CHANTER** (caster) — HP ~300–500 · Move slow (3m), hangs back. No melee; ranged Influence + Insanity pressure each turn. Unparryable. Ignore it and the room gets worse — close and kill first. Low HP, soft limbs. The priority target.
5. **SPITTER** (controller) — HP ~400–600 · Move medium (4m), keeps distance. Ranged Corrosion, stacks fast. Tell: swells, draws back (~1.6s — dodge or interrupt). Tier 1. The track-clock — close fast or get cornered and ticked to death. Pairs evilly with a Burster or Brute.
6. **BRUTE** (heavy) — HP ~1500–2500 · Move slow (4m). Huge, slow heavies. Can amputate or bisect an under-levelled player on a fully-landed combo — telegraphed catastrophe, never random. Tell: overhead wind-up (~2.0s). Tier 2. Retreat is a valid answer. Sever a leg to neutralise its approach.
7. **FLAILER** (chaotic) — HP ~600–900 · Move medium, erratic. Multiple whipping limbs, multi-track (Corrosion + Blood Loss). Tell: limbs draw back in unison — multiple windows in sequence (a ballistic chain). Tier 3. The precision-strike showcase; hardest non-boss to open.
**Enemy parry restriction (Session 2 ruling):** standard archetypes CANNOT parry or visceral the player — the visceral loop belongs to the player. Standard enemies still punish whiffs and telegraph their own heavies, but the parry-you-back mirror match is reserved for bosses and hand-flagged bespoke elites. Keeps ordinary fights readable; anything that can turn your own system against you announces itself by being a boss.

**Bosses** are bespoke, built on three pillars:
1. A gimmick punishing a default habit. (The Conjoined Twins punish centre-mass viscerals: low-HP trunk, and severing it splits them into two faster enemies.)
2. A multi-parry ballistic chain (Tier 3) as the route to a real opening.
3. A dismember/bisect threat for the under-levelled — with a retreat threshold always reachable, so a lost fight is an escape, not a feel-bad death.

**EFFIGY** (boss archetype — duellist/mirror) — HP hand-set · Move fast (7m+). Uses your toolkit: parries you, viscerals you, hit-and-runs, can out-move you. Fast, tight windows; reads your tells too. The fight that tests whether you've learned the system or just bullied mooks. *(Reclassified from standard archetype, Session 2 — it's the sole legitimate wielder of player-style parries, which makes it boss-tier by definition under the parry restriction above.)*

---

## 17. Running Notes — Turn Order, Recovery & Scaling

**Turn order.** The Player Character always acts first, every round — no roll-off, no standing initiative. Enemies act as a block afterward. *(Session 3 ruling — replaces the old d20 roll-off.)* This exists specifically so Assess/Hold decisions always happen before the enemies that turn's tell would apply to; the old roll-off could strand a freshly-set Hold on the wrong side of the enemy's action if the player rolled low, which isn't a real choice, it's a coin-flip nullifying a deliberate one. Practical effect on monster design: a tell and its payoff attack no longer need to be split across two separate rounds to give the player a fair reactive window — since the player's own turn always lands before the enemy block, a single enemy turn can narrate a full tell-then-strike (bow, then lunge) as one continuous beat, timed via the normal stopwatch, without requiring an artificial recovery-round structure just to make room for a parry.

**Out-of-combat recovery.** A quiet moment between fights (not the hub) allows a short rest: clear one track by a single stack, OR recover a small flat chunk of HP (~Quick Item tier). Free, no item spent. Does not restore visceral charges, limbs, or mutations — hub-exclusive.

**Scaling.** Enemy HP scales with player *level* (total points spent), not single-stat investment. Standard humanoid limb thresholds do NOT scale (§10). Bosses: HP and thresholds hand-set, exempt from the table. Rough HP multiplier on base table values — a rule of thumb, eyeball per encounter:

| Player level | Multiplier |
|---|---|
| 1–20 | ×1.0 |
| 21–40 | ×1.5 |
| 41–60 | ×2.25 |
| 61–80 | ×3.5 |
| 81–100 | ×5.0 |

**Insight-gain triggers.** Awarded at narratively significant moments, not on a checklist: first sighting of a new archetype, reading lore, surviving a near-death, tasting a dangerous source, defeating a boss. Usually +1 per trigger, once per discovery.

---

## 18. Salts Rooms & Biomes — Exploration Structure

**Instance Quests vs Quests (Session 2 ruling).** Narrative content in a run splits cleanly in two:

- **Instance Quests** — threads that live inside one layout: environmental stories, corpses, journals, one-off creatures, unexplored doors. They expire the moment the player exits (anchor, retreat, or death → reroll). Unfinished instance content is lost to the shifting reality — permanently, no tracking, no guilt. Completing one during the run can convert its reward into something persistent (an item carried out, lore learned, Insight gained) — that's the only way instance content escapes the reroll.
- **Quests** — threads anchored to persistent entities: recurring NPCs, the hub and its people, known recipes, carried items. These survive rerolls and are the only narrative threads worth tracking between sessions.
- **Corollary:** enemies do not persist across instances. A new run may contain the same *kind* of creature, but it's a fresh instance at full pool — no carrying over damage dealt in a previous layout.

**DM triage rule:** if a thread is anchored to the layout, it dies with the layout. Only log what's anchored to something persistent.

Stillwell Hydro holds ~6 salts rooms — sauna chambers where measured doses trigger the out-of-body crossings. The structural spine of the world outside the hub.

**Recipes & biomes**
- **A recipe is a biome's identity.** A specific combination and quantity always leads to the same kind of place — 2 ounces of Jade Salts is always the deserted streets. Recipe→biome mappings are permanent world constants.
- **Everything inside rerolls.** Layout, wake-in point, loot placement, enemy spawns regenerate every entry. The DM holds a biome overview per recipe — palette, archetype reskins, hazards, loot tier, anchor flavour — never a map.
- **Recipe discovery happens in the world:** salts as loot, proportions from lore, NPC hints. Some recipes are Insight-gated — below the tier, the combination doesn't take; the room fills with ordinary steam. A threshold check, not a spend.

**Salts & the room economy**
- Salts are **single-use, consumed on activation** — not per trip. Burning a recipe opens that biome and holds it open.
- An active room is **reusable indefinitely until deliberately cleared** at the hub. Clearing frees the slot, refunds nothing. With ~6 rooms, every active recipe is a standing commitment.
- Salts carry no death risk in the usual sense — they can be lost with your gear (§12) precisely because the room stays open: wake in the salt room, walk straight back in for free.
- Older biomes stay relevant as **salt farms** — expanding your recipe list may mean returning to cleared low-level zones hunting salts you've already spent.

**Anchors — how a run ends well**
- You always wake at an **anchor** — a biome-flavoured fixture (a brazier in the streets, a font in the church). Its location rerolls each trip; it always exists.
- Return to it and choose to leave → **clean exit.** Wake in the salt room, Purse banks. The push-your-luck engine: deeper loot vs a longer walk back.
- Assess or high Insight can orient you toward the anchor — direction and rough distance, clarity scaling per §9.
- Retreat and Abandon-All (§12) both work as written. The anchor is the free, clean exit; Retreat is the cheap-but-slow one (Purse only, no mid-combat); Abandon-All is the expensive, any-time panic word (Purse and gear both).

**Death, gear recovery & persistence**
- Death respawns you in the salt room you entered from. Purse forfeit; re-entry free while the room is active.
- **Your killer is a guaranteed spawn.** The creature carrying your gear always exists somewhere in that biome until killed, even as everything rerolls around it. Assess or high Insight can point toward it. (Without this, rerolling layouts make gear findable in theory and lost in practice.)
- **Boss kills are permanent per biome.** A slain boss never respawns; the biome "settles" — one fixed landmark appears where it died and persists across rerolls. The one mark you leave on a world that otherwise forgets you.

**Open questions (untested):** salt drop rates per biome/archetype; exact recipe-discovery triggers (lore vs experimentation vs NPC purchase). DM discretion until playtested.

---

## 19. Quick Reference

**RESOLUTION** — Default attacks land automatically, both sides. Rolls/stopwatches only for called shots, parries, saves, and genuine uncertainty (§3).

**ATTRIBUTES** — Vigor / Endurance / Strength / Skill / Resolve. Start 8, cap 99 (negotiable via backstory, §4). ESV soft-caps each point above 20 (×0.65 / ×0.4 / ×0.2 / ×0.1 per band). Damage floor: 20 minimum base for anything passing through a multiplier. Insight separate — earned, 0–10 tiers.

**WHITE SALTS** — Purse (at risk) → Vault (safe) on hub arrival. Level = total points spent, cap 100. Next level = 25 × current level. Perks at 20/40/60/80/99 per stat.

**RALLY** — Damage taken → grey health, recoverable by landing a hit on your very next turn only. Default 50%; big telegraphed hits 75–100%, chip/DoT 0–25% — set per attack (§6).

**TRACKS** (0–10 unless noted)

| Track | Effect | Clears by |
|---|---|---|
| Blood Loss | Each new stack: +damage = new stack total. No passive drain. Cap 10 → Rupture | Bandage / cautery / pressure |
| Rupture (triggered @ 10) | 25% Max HP damage + stagger + Blood Loss resets | Resolves once |
| Insanity | Fail Save Roll → DM controls you 1 turn. ↑ with Insight | Camphor (−2) / calm / Resolve 60 perk |
| Burning | Damage/turn, spreads to flammables | Smother (action) |
| Discombobulation (Tick, 1–3) | Bad exits, reversed move, lost reactions | −1/turn, automatic |
| Influence | Fail Save Roll → obey/compelled effect next turn, severity scales with stacks (DM discretion), uncapped past 10. ↑ Insanity & Insight | Full source elimination (ALL active sources if multiple) |
| Corrosion | stacks × 2 dmg/turn, cap 5 | Manage action → −1/turn; else holds |
| Fugue (on death) | Insight reads become false | Spend next Insight earned (not banked) |

**SAVE ROLL** — d20 ≥ 10 + track value − ⌊Resolve ÷ 10⌋ + ⌊Insight ÷ 2⌋ (+ mods). One formula, both saves (§5).

**MOVEMENT** — Budget 8–14m (Endurance), the single per-turn currency: repositioning AND actions draw from it. Splittable around your action. Can't pay an action's cost = can't take it. Trade / Parry / Kite triangle. Out-speed slow enemies; dance burst-movers (in on recovery, out before surge). Hit-and-run = strike + retreat, no parry, no opening.

**ACTION ECONOMY** — Action (one/turn, costs movement: Light 1m · Heavy 3m · Hold 2m · manage track 1m · Action Item 2m · Assess 1m) + Fast Action (one/turn, always 0m: Quick Item, load a capsule) + Movement. Quick Items weak but free alongside an attack; Action Items strong but cost the turn. Limb-gating table in §8. Abandon-All = instant panic escape, voice/mind only, exempt from the economy, forfeits Purse + gear — stoppable only by rare, telegraphed boss-tier silence. Retreat = meditative, Purse-only, cannot be used mid-combat (§12).

**PARRY/VISCERAL** — Assess (1m) reads tell + timing (clarity scales with Insight). Hold (2m) → stopwatch in window, no charge cost, no cap on attempts. In = visceral (1.5× + knockdown + enemy loses move) ± mods. Out = eat heavy + punish. Don't reuse a tell. Only bosses and hand-flagged elites can parry/visceral YOU — standard enemies never do (§16).

**POST-PARRY TIERS** — T1: free weak point, no watch. T2: widened precision watch. T3: parry watch + full precision watch.

**LIMBS** — (multiplier / threshold). Effective dmg = raw × mult, fills meter + chips HP. Threshold over several hits = stagger (the triggering hit grants an immediate free called shot; enemy stagger duration is variable, set per Monster Template); in one hit = sever (permanent). Small high-value targets (bells, cracks, eyes) are just limbs with a high multiplier — no separate system. Torso or head severed = dead — but so is 0 HP from plain attacks, always. Specific-limb shots need an opening; default = torso. Self-initiated blind shots (no enemy tell) use one tolerance band tighter and end the turn on a miss.

**PRECISION** (limbs >1.0 only) — tighter window for higher multiplier (head ±0.13s). Miss → progressively worse (chip / off-balance / wide + reactive / exposed). Removed by T1 parry, widened by T2.

**MUTATION** — Lost limbs regrow at hub, chance of coming back changed (+power / −something). Read trades only at high Insight. Revert or reroll at hub, Vault White Salts.

**ABANDON-ALL** — Instant, free, mid-combat, any time. Keep character/limbs, forfeit Purse AND gear (recoverable off a guaranteed enemy in a future instance, no expiry). §12.

**RETREAT** — A few minutes' meditation, cannot be used in active combat. Keep character/limbs/gear, forfeit Purse only. Free. §12.

**DEATH** — Respawn in the salt room you entered from. Keep character/levels/mutations. Gear forfeit to killer (a guaranteed spawn until killed; doesn't compound). Purse lost, Vault safe. Fugue applied.

**SALTS ROOMS** — ~6 rooms. Recipe = biome (permanent constant); layout/loot/spawns reroll per entry. Salts single-use on activation; active room free to reuse until deliberately cleared (no refund). Clean exit via anchor (rerolls position, always exists) → Purse banks. Some recipes Insight-gated. Boss kills permanent; one landmark settles.

**INSIGHT** — Earned, 0–10, five tiers. Sight + visceral mods + mutation-reading. ↑ power, ↑ Insanity/Influence floor. Spendable (doors, Insight-priced gear, ally summon at default 2) — spending drops score, tier, and floor together.

---

*Working title, placeholder names, and starting numbers are yours to change. The skeleton is built to be tuned at the table.*
