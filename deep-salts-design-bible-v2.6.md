# THE DEEP SALTS

**Design Bible — Entity Templates**

Companion to the core ruleset and monster manual. **Load this document (plus the ruleset and the character sheet) when running the game.** Project-management material — mechanic index, book plan, known gaps (§8–10) — lives in the separate dev log and should NOT be in context during play.

*Version 2.6 — session zero updates: Monster Template limb table gains a Stagger Duration column; standard humanoid stagger durations proposed; small high-value called-shot targets documented as non-standard limb entries (Sever mechanic, no new category); Drowned Bellkeeper's bell documented as a worked example. Rules flagged **(untested)** are proposed rulings awaiting playtest.*

Every monster, weapon, item, NPC, status effect, and currency gets ONE complete page here — every field about that one thing, in one place. Copy the blank template to add an instance. Nothing about a single entity should require flipping to another page; if you're cross-referencing three tables to know how one weapon works, the template has failed — flag it.

**Status effect types:** *Immediate* (lands on hit, resolves before the next turn) · *Track* (builds 0–10, compounds) · *Tick* (applied at a set value, counts down 1 per turn automatically — e.g. Discombobulation at 3 → 2 → 1 → clear, no action needed).

Each section leads with its **floor entry** — the weakest legal instance of that entity type. Nothing else in the game should ship below it without a deliberate reason. Use floors as rulers.

\---

# 1\. Monster Template

One page per monster. A completed page is everything a DM needs to run that fight without looking anywhere else.

## Monster 1 — Waterlogged Guest *(floor entry)*

* **Archetype:** Shambler (mook)
* **Level Range:** 1–15
* **HP (base):** 200 — playtest ruling (two runs confirmed 400 made a no-threat mook a slog). Sits below the Shambler band's written floor; band revision logged in the dev log gaps.
* **Move Budget / Pattern:** 3m constant shuffle. No burst, no recovery beat — never changes pace.
* **Scale Band:** 1–20 (×1.0, Ruleset §17)
* **Flavour:** A guest who came for the waters and never left the pool. Robe fused to grey skin. It doesn't hunt so much as drift toward warmth.

**Limbs:** standard humanoid defaults, no deviations (Head ×1.5/180 · Torso ×1.0/800 · Arm ×0.65/200 · Leg ×0.75/300). Not sever-immune.

**Standard humanoid stagger durations (PROPOSED — untested, applies wherever "standard humanoid defaults" is referenced across this document):** Head 1 turn · Arm 2 turns · Leg 2 turns · Torso n/a (torso stagger is just heavy damage, mirroring the player-side table). Elites and bosses set bespoke durations on their own template rather than inheriting this default.

**Triggering a stagger** (single hit or cumulative, meeting the threshold) grants an immediate free called shot on that same action, no precision stopwatch — same as a Tier 1 parry opening (Ruleset §10, session zero ruling).

**Attacks:**

|Attack|Type|Tell|Window|Tier|Hit Effect|Retaliation on Visceral|Miss/Whiff Punish|
|-|-|-|-|-|-|-|-|
|Waterlogged Grasp|Light|None — unparryable by design; it doesn't wind up, it just reaches|N/A|N/A (no heavy exists on this creature)|0 raw damage; applies 1 Influence stack (Track)|N/A — no visceral possible|N/A — outside its 3m reach the grasp simply doesn't land (Ruleset §3)|

**Behaviour:**

* **Ballistic trigger / chain:** none
* **Kitable:** Y — slowest move budget in the game; any Endurance investment outpaces it outright
* **Assess (Insight 0–1):** "It's slow. It won't hit hard. Watch the others behind it."
* **Assess (Insight 2+):** "No damage on the grab, just Influence. No tell because there's no windup — no parry exists here, so just hit it till it drops. Want it faster? Stagger a leg to ground it; the head's an open called shot after."
* **Influence effect, capped (session 4 ruling):** on a failed save, the compelled effect is a pull one step toward the source — a movement cost only, never a lost action, regardless of stack height. This creature never escalates further no matter how long a fight against it runs.
* **White Salts Drop (base):** 5 — the floor value for the White Salts economy; nothing drops less without a specific reason **(untested)**
* **Insight Granted:** +1 on first sighting only (Ruleset §17 trigger list); +0 thereafter
* **Boss Gimmick:** N/A



Monster 2 — Chapel Penitent



Archetype: Lunger (mook)

Level Range: 1–20

HP (base): 300 (untested)

Move Budget / Pattern: 3m stalking pace. Performs a single 5m lunge after a short pause, then requires a recovery beat before lunging again.

Scale Band: 1–20 (×1.0, Ruleset §17)

Flavour (1–2 sentences): A pilgrim whose knees wore grooves into the stone before death finally claimed them. It still bows before every attack.



Limbs — standard humanoid defaults apply (Head ×1.5/180 · Torso ×1.0/800 · Arm ×0.65/200 · Leg ×0.75/300). List only deviations and non-standard limbs (tentacles, cores, etc.):



Limb	Multiplier	Stagger Threshold	Sever Threshold	Sever Immune?

None	—	—	—	—



Attacks



Attack	Type	Tell (exact narration)	Window (target/±)	Tier	Hit Effect + Stacks	Status Type (Imm/Track/Tick)	Retaliation on Visceral?	Miss/Whiff Punish

Penitent Rush	Heavy	"It bows deeply, then drives forward in a desperate sprint."	Target	Heavy	40 raw damage	None	Standard	Long recovery while regaining footing



Behaviour:

Ballistic Trigger: None.

Ballistic Chain Sequence: None.

Kitable (Y/N): Y



Assess Result — Insight 0–1: "It only becomes dangerous once it commits."

Assess Result — Insight 2+: "Wait for the bow. Dodge the charge and punish the recovery."



White Salts Drop (base): 8

Insight Granted (first sighting/defeat): +1 / +0



Boss Gimmick (bosses only, else N/A): N/A



Habit Punished: Panic dodging too early.

What Happens if the Player Falls For It: The lunge catches the end of the dodge.

Dismember/Bisect Threat: Moderate.

Retreat Always Reachable? (Y/N): Y



Monster 3 — Drowned Bellkeeper



Archetype: Chanter (mook)

Level Range: 1–20

HP (base): 280 (untested)

Move Budget / Pattern: 2m slow walk. Rarely closes distance voluntarily.

Scale Band: 1–20 (×1.0, Ruleset §17)

Flavour (1–2 sentences): A ruined attendant dragging a cracked handbell beneath the waterline. Every ring sounds muffled, yet somehow reaches inside the skull.



Limbs: Standard humanoid defaults, plus one non-standard entry:

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Bell (held object)|~2.0 (proposed)|N/A|N/A|~40 raw (untested — proposed placeholder; session zero resolved this as a pure timing check without computing an exact raw-damage figure, so the number here is a best-guess anchor, not a confirmed one)|N/A|

Breaking the bell permanently disables Hollow Bell for the rest of the encounter (Sever mechanic — no partial/temporary state). Worked example from session zero: precision stopwatch at 1.20s target, ±0.25s tolerance; hit landed, bell shattered, no further tolls that fight.

Attacks



Attack	Type	Tell (exact narration)	Window	Tier	Hit Effect + Stacks	Status Type	Retaliation on Visceral?	Miss/Whiff Punish

Hollow Bell	Aura	"It slowly raises the bell before a dull, submerged toll."	Target	Light	20 raw damage; applies 1 Influence stack	Track	Standard	Long delay before next toll



Behaviour:

Ballistic Trigger: None.

Ballistic Chain Sequence: None.

Kitable: Y



Assess Result — Insight 0–1: "That bell feels worse than it sounds."

Assess Result — Insight 2+: "Interrupt the toll by staying aggressive. Left alone, it'll keep building Influence."



White Salts Drop (base): 8

Insight Granted (first sighting/defeat): +1 / +0



Boss Gimmick: N/A



Habit Punished: Ignoring support enemies.

What Happens if the Player Falls For It: Influence accumulates while other monsters pressure them.

Dismember/Bisect Threat: Low.

Retreat Always Reachable? (Y/N): Y



Monster 4 — Salt-Eaten Custodian



Archetype: Shambler (elite)

Level Range: 5–20

HP (base): 650 (untested)

Move Budget / Pattern: 3m relentless walk. Never sprints.

Scale Band: 1–20 (×1.0, Ruleset §17)

Flavour (1–2 sentences): Once tasked with cleaning the baths, it now drags an iron scraper large enough to serve as a coffin lid.



Limbs: Standard humanoid defaults. No deviations.



Attacks



Attack	Type	Tell	Window	Tier	Hit Effect + Stacks	Status Type	Retaliation on Visceral?	Miss/Whiff Punish

Iron Scrape	Heavy	"The scraper screeches across the floor before a wide sweep."	Target	Heavy	60 raw damage	None	Standard	Long recovery while dragging weapon free



Behaviour:

Ballistic Trigger: None.

Ballistic Chain Sequence: None.

Kitable: Y



Assess Result — Insight 0–1: "That thing is slow, but don't stand in front of it."

Assess Result — Insight 2+: "The scrape announces everything. Dodge late and punish hard."



White Salts Drop (base): 15

Insight Granted (first sighting/defeat): +1 / +0



Boss Gimmick: N/A



Habit Punished: Greedy attacks after the tell begins.

What Happens if the Player Falls For It: They eat the full sweep.

Dismember/Bisect Threat: High.

Retreat Always Reachable? (Y/N): Y



Monster 5 — Brine Spitter



Archetype: Spitter (mook)

Level Range: 1–20

HP (base): 260 (untested)

Move Budget / Pattern: 3m retreating shuffle. Prefers maintaining distance.

Scale Band: 1–20 (×1.0, Ruleset §17)

Flavour (1–2 sentences): Its jaw hangs permanently open, overflowing with glittering saltwater that never runs dry.



Limbs: Standard humanoid defaults. No deviations.



Attacks



Attack	Type	Tell	Window	Tier	Hit Effect + Stacks	Status Type	Retaliation on Visceral?	Miss/Whiff Punish

Brine Jet	Ranged	"Its throat swells until the skin stretches taut."	Target	Light	30 raw damage	None	Standard	Stands exposed while coughing seawater



Behaviour:

Ballistic Trigger: None.

Ballistic Chain Sequence: None.

Kitable: N



Assess Result — Insight 0–1: "It's safer up close than far away."

Assess Result — Insight 2+: "Rush it during the inhale. The spit leaves it wide open."



White Salts Drop (base): 8

Insight Granted (first sighting/defeat): +1 / +0



Boss Gimmick: N/A



Habit Punished: Backpedalling constantly.

What Happens if the Player Falls For It: Repeated ranged hits while retreating.

Dismember/Bisect Threat: Low.

Retreat Always Reachable? (Y/N): Y



Monster 6 — Bathhouse Flailer



Archetype: Flailer (elite)

Level Range: 10–20

HP (base): 700 (untested)

Move Budget / Pattern: 4m erratic movement with unpredictable direction changes.

Scale Band: 1–20 (×1.0, Ruleset §17)

Flavour (1–2 sentences): Wrapped in soaking towels that whip through the air like living tentacles whenever it panics.



Limbs: Standard humanoid defaults. No deviations.



Attacks



Attack	Type	Tell	Window	Tier	Hit Effect + Stacks	Status Type	Retaliation on Visceral?	Miss/Whiff Punish

Towel Lash	Light	"The dripping cloth suddenly snaps tight."	Target	Light	25 raw damage	None	Standard	Brief stumble

Frenzied Whirl	Heavy	"It throws both arms wide before spinning violently."	Target	Heavy	70 raw damage	None	Standard	Extended dizzy recovery



Behaviour:

Ballistic Trigger: None.

Ballistic Chain Sequence: None.

Kitable: N



Assess Result — Insight 0–1: "Stay calm. It isn't."

Assess Result — Insight 2+: "The spin has the real threat. Let it commit, then strike."



White Salts Drop (base): 18

Insight Granted (first sighting/defeat): +1 / +0



Boss Gimmick: N/A



Habit Punished: Staying glued to its sides.

What Happens if the Player Falls For It: Gets clipped by the spinning attack.

Dismember/Bisect Threat: High.

Retreat Always Reachable? (Y/N): Y



Monster 7 — Marble Effigy



Archetype: Effigy (elite)

Level Range: 10–20

HP (base): 800 (untested)

Move Budget / Pattern: 2m deliberate advance. Pauses after every attack.

Scale Band: 1–20 (×1.0, Ruleset §17)

Flavour (1–2 sentences): A carved attendant statue animated by centuries of absorbed prayers. Chips of marble fall away with every step.



Limbs: Standard humanoid defaults. No deviations.



Attacks



Attack	Type	Tell	Window	Tier	Hit Effect + Stacks	Status Type	Retaliation on Visceral?	Miss/Whiff Punish

Marble Fist	Heavy	"Stone cracks loudly through its arm before the punch."	Target	Heavy	80 raw damage	None	Standard	Long stationary recovery



Behaviour:

Ballistic Trigger: None.

Ballistic Chain Sequence: None.

Kitable: Y



Assess Result — Insight 0–1: "Every hit hurts. Every swing is slow."

Assess Result — Insight 2+: "Its recovery is longer than its attack. Survive one blow and answer with several."



White Salts Drop (base): 20

Insight Granted (first sighting/defeat): +1 / +0



Boss Gimmick: N/A



Habit Punished: Trading hits.

What Happens if the Player Falls For It: Loses every damage race.

Dismember/Bisect Threat: Very High.

Retreat Always Reachable? (Y/N): Y





Monster 8 — The Singer *(boss, Choir Deep)*



Archetype: Choir (boss)

Level Range: 1–20 (first Choir Deep boss; hand-set, exempt from the scaling table per Ruleset §17)

HP (base): 900 (hand-set)

Move Budget / Pattern: 0m — fully rooted, never advances, never retreats.

Scale Band: N/A — bosses hand-set per §17.

Flavour (1–2 sentences): A pilgrim shape whose face gave way to a vertical opening that doesn't sing so much as simply *is* the sound. It sustains an unbroken, layered note that draws the faithful into an unmoving ring around it and never once approaches the source of its own devotion.



Limbs — standard humanoid defaults apply, plus one non-standard entry:

Limb	Multiplier	Stagger Threshold	Stagger Duration	Sever Threshold	Sever Immune?
The Open Throat (weak point)	×2.0	N/A	N/A	400	No



Attacks

Attack	Type	Tell (exact narration)	Window (target/±)	Tier	Hit Effect + Stacks	Status Type (Imm/Track/Tick)	Retaliation on Visceral?	Miss/Whiff Punish
Choir Pulse	Ranged/Aura	"The layered note sharpens, aims itself."	N/A — unparryable, no attack roll, always lands	N/A	2 Influence stacks per pulse	Track (Influence)	N/A	N/A



Behaviour:

Ballistic Trigger: None.

Ballistic Chain Sequence: None.

Kitable (Y/N): N/A — it never moves at all. Breaking line of sight (distance, a wall, leaving the room) is the counter, not outrunning it.



Assess Result — Insight 0–1: "It's not hunting. Whatever it's doing, it's not going to chase."

Assess Result — Insight 2+: "The note itself is the attack — every beat near it costs you, whether or not it ever lays a hand on you. The opening where its face should be is a real weak point, but it's set boss-high, not mook-high."



White Salts Drop (base): 60

Insight Granted (first sighting/defeat): +1 / +1



Boss Gimmick (bosses only, else N/A): The Open Throat is the only way to end this fight quickly — sever it (400 raw-equivalent in one hit) and it's over regardless of remaining HP. Otherwise this is a pure attrition fight: the Singer itself never physically attacks, all direct danger comes from the Penitent congregation it's gathered, while Influence quietly climbs the whole time you're in the room, save DC rising with the stack count until a flat d20 can no longer clear it.



Habit Punished: Standing in the open tanking pulses to save time, or fighting through the Penitent ring instead of around it.

What Happens if the Player Falls For It: Influence climbs past the point saves can reasonably clear; compelled effects escalate in severity and there's no walking it back except breaking line of sight entirely.

Dismember/Bisect Threat: Low (no melee attack of its own — all physical danger is secondhand, via the Penitents).

Retreat Always Reachable? (Y/N): Y — it never chases, so distance is always available as an out.

---

## Monster Template (blank)

* **Archetype:** · **Level Range:** · **HP (base):** · **Move Budget / Pattern:** · **Scale Band:** · **Flavour (1–2 sentences):**

**Limbs** — standard humanoid defaults apply (Head ×1.5/180 · Torso ×1.0/800 · Arm ×0.65/200 · Leg ×0.75/300). List only deviations and non-standard limbs (tentacles, cores, etc.):

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|||||||

**Small/high-value called-shot targets** (a bell, a crack in scale, an eye) go in this same table as non-standard limb entries — not a separate system. Give them an appropriately high multiplier (the existing Precision Strike tolerance table already tightens as multiplier climbs) and use the **Sever** mechanic only (permanent disable on a single qualifying hit) — there's no meaningful partial "stagger" state for an object like this. Leave Stagger Threshold/Duration blank or N/A for these entries.

**Attacks** — one row per attack (light, heavy, ranged, aura, or ballistic chain step):

|Attack|Type|Tell (exact narration)|Window (target/±)|Tier|Hit Effect + Stacks|Status Type (Imm/Track/Tick)|Retaliation on Visceral?|Miss/Whiff Punish|
|-|-|-|-|-|-|-|-|-|
||||||||||

**Behaviour:**

* **Ballistic Trigger:** · **Ballistic Chain Sequence:** · **Kitable (Y/N):**
* **Assess Result — Insight 0–1:** · **Assess Result — Insight 2+:**
* **White Salts Drop (base):** · **Insight Granted (first sighting/defeat):**

**Boss Gimmick** (bosses only, else N/A):

* **Habit Punished:** · **What Happens if the Player Falls For It:** · **Dismember/Bisect Threat:** · **Retreat Always Reachable? (Y/N):**

\---

# 2\. Weapon Template

One page per weapon — identity, damage, passive, sever maths together.

**Damage formula reference:** Damage = Base + (ESV × grade multiplier). E ×0.3 · D ×0.5 · C ×0.7 · B ×0.9 · A ×1.1 · S ×1.3. Heavy = 2×Base + (ESV × grade × 1.5). Charged Heavy = same maths as Heavy (placeholder — see dev log gaps). Double-swing second hit = 50% of first **(untested)**.

**Sever reference:** min raw = threshold ÷ multiplier. Head 180 → 120 raw · Arm 200 → \~308 raw · Leg 300 → 400 raw.

**ESV touchpoints for worked rows:** raw 8 → ESV 8 · raw 20 → ESV 20 · raw 40 → ESV 33 · raw 99 → ESV \~47.

## Weapon 1 — Paring Knife *(floor entry)*

* **Type:** Quick · **Stat/Grade:** Skill / E · **Hands:** One
* **Acquisition:** not found in the world — this is the mechanical floor a backstory-negotiated starting weapon (Ruleset §4) lands at or above. The ruler, not the drop.
* **Base Damage:** 20 (the Damage Floor — lowest legal base in the system)
* **Light** = 20 + ESV×0.3 · **Heavy** = 40 + ESV×0.45
* **Worked rows:** ESV 8 → Light 22 / Heavy 44 · ESV 47 (maxed) → Light 34 / Heavy 61
* **Two-Handed Modifier:** N/A
* **Passive:** none — the "nothing extra" baseline every other weapon's passive is compared against
* **Insight Gate:** none — usable from Insight 0

**Sever viability:** not viable against any limb at any ESV (best case Heavy at ESV 47 = 61 raw, under half the head's 120). Correct and intended — a floor weapon never severs, at any Strength (Ruleset §10).

## Weapon Template (blank)

* **Type (Quick/Heavy/Reach/Trick):** · **Governing Stat / Grade (E–S):** · **One or Two-Handed:** · **Acquisition:**
* **Base Damage:**
* **Light formula:** Base + ESV×grade · **Heavy formula:** 2×Base + ESV×grade×1.5
* **Worked rows** (compute once at ESV 8 and ESV 47 so the DM never does arithmetic mid-fight): ESV 8 → Light \_\_ / Heavy \_\_ · ESV 47 → Light \_\_ / Heavy \_\_
* **Two-Handed Modifier:** · **Passive Effect:** · **Stack Amount (if Track/Tick):** · **Status Type Applied:** · **Special Mechanic (Trick weapons — transform conditions, forms):** · **Insight Gate:**

**Sever viability:**

|Target|Min Raw Needed|Viable at ESV|Notes|
|-|-|-|-|
|Head|120|||
|Arm|\~308|||
|Leg|400|||

\---

# 3\. Player Character Sheet

**Moved to its own live-state file — `deep-salts-character-sheet.md`.** Live state doesn't belong inside a static reference document. The DM keeps the sheet file current (rewriting it after any significant change) and treats it as the single source of truth for HP, tracks, charges, limbs, Insight, and inventory mid-fight. Section number retained here so cross-references stay valid.

\---

# 4\. NPC Template

One page per NPC.

## NPC 1 — Robe Attendant *(floor entry)*

Zero mechanical function, zero dialogue, zero lore thread — the least an NPC can be while still occupying space. *Not the reception clerk*, who is the recurring antagonist and is always narrated as a DM moment, never a stat block.

* **Role:** background hub functionary — hands out robes and towels, gestures toward the changing rooms
* **Level Range:** N/A — not a combat entity · **Location(s):** hub only (reception corridor, changing rooms) · **Fightable:** N

**Appearance \& Behaviour:**

* **Fixed appearance:** waxed-canvas apron, sleeves rolled, never makes eye contact
* **What changes between appearances:** nothing — the one deliberate exception to the hub's "one detail changes each time" rule (Ruleset §14)
* **On player arrival:** hands over a folded towel, points once toward the pools, says nothing
* **Never does:** speak first, answer a question, acknowledge that anything is wrong
* **Never says directly:** anything. Genuinely mute in play.

**Dialogue seeds** (non-verbal only — silence is the whole bit): a nod toward the terraces · a shrug, if asked something with no answer · a single point at the exit if the player lingers · a slow head-shake, no more · never a spoken line.

**Mechanical function:** no hub services, no gated information, no behaviour shifts. Provides a robe and towel automatically on the first hub visit only — cosmetic.

**Lore thread:** connects to nothing. Player can piece together: nothing. Never revealed: whether it's a person at all.

## NPC Template (blank)

* **Role:** · **Level Range:** · **Location(s):** · **Fightable? (Y/N — if Y, attach Monster Template):**

**Appearance \& Behaviour:** Fixed Appearance · What Changes Between Appearances · What They Do on Player Arrival · What They Never Do · What They Never Say Directly

**Dialogue Seeds:** 3–5 fragments — tone and register, not scripts.

**Mechanical Function:** Hub Services Offered · Items Provided + Conditions · Information Gated · Behaviour Shift Conditions

**Lore Thread:** Connects To · Player Can Piece Together Over Time · Never Revealed

\---

# 5\. Item Template

One block per item; all fields fit one table.

## Item 1 — Scour *(floor entry)*

The weakest, most narrowly-scoped Quick Item on file (Ruleset §8: "redundant with the manage-track Action, but doesn't cost your whole turn").

* **Type:** Quick · **Action Cost:** Fast Action (Ruleset §8)
* **Effect:** removes exactly 1 Corrosion stack. No other effect — no healing, no interaction with any other track.
* **Status Type:** Track (reduces Corrosion by 1; applies nothing new) · **Duration:** instant · **Consumable:** Y
* **Carry Limit:** 5 **(untested — proposed default, mirrors Corrosion's 5-stack cap so one full satchel zeroes one full buildup)**
* **Insight Gate:** none — Tier 0
* **Limb Requirement:** a working hand/arm — the general default for Quick/Action items. Abandon-All (Ruleset §8) is the one stated exception requiring no limbs.
* **Acquisition:** mineral scrapings from the source-spring terraces; sold cheap or free at the hub apothecary stall
* **Flavour:** a handful of chalky salts, the same stuff crusted on every basin in the baths. Rub it into the burn and it stops eating.

## Item Template (blank — copy per item)

**Type (Quick/Action/Reactive/Passive):** · **Action Cost (which slot):** · **Effect (fully quantified — no vague wording):** · **Status Type Applied (Imm/Track/Tick):** · **Duration:** · **Consumable? (Y/N):** · **Carry Limit:** · **Insight Gate:** · **Limb Requirement:** · **Acquisition:** · **Flavour (1 line):**

\---

# 6\. Status Effect Template

One block per effect. Fill only the sub-section matching the effect's Type.

## Status Effect 1 — Off-Balance *(floor entry, Immediate)*

Referenced in the Precision Strike miss-punishment table (Ruleset §10, band 1.26–1.50); formalised here. Smallest possible footprint: one turn, one small penalty, nothing to manage.

* **Type:** Immediate · **Affects:** Both (currently only produced by a player's own missed Precision Strike) · **Resisted on application:** N — a flat miss-punishment consequence, not an attack that gets saved against
* **Effect on application:** −1m to movement budget, next turn only
* **Duration:** 1 turn — expires automatically · **Cleared early:** N — it expires; nothing removes it because it's already the shortest duration in the system
* **Dangerous combinations:** compounds tactically (not mechanically) with a staggered leg (§8 limb-gating) or Discombobulation's movement scrambling — several small movement penalties adding up to a genuinely bad turn
* **Countered by:** nothing — too small to need a cure
* **Enemy / weapon sources:** none on file yet; open for a future enemy to apply directly as a light debuff

## Status Effect 2 — Blood Loss *(Track)*

* **Type:** Track (0–10) · **Affects:** Both · **Resisted on application:** N
* **Stacks per application:** +1 per qualifying hit (slashing/piercing) or hazard
* **Effect per stack:** each *new* stack deals immediate bonus damage equal to the new stack total (1st cut +1, 2nd +2 … 5th +5 = 15 cumulative across those five hits). No per-turn drain — nothing happens between hits. This is what distinguishes it from Corrosion, which ticks every turn regardless.
* **Cap:** 10 · **Overflow:** reaching 10 triggers **Rupture** (below) and resets this track to 0
* **Clear:** bandage, cautery, or a pressure action; a Wrap Quick Item clears 2 stacks (Ruleset §8)
* **Dangerous combinations:** stacks fastest against multi-hit sources (Tideglass Cleaver double-swing, Flailer ballistic chain) — each landed hit is a fresh, bigger bonus
* **Sources:** slashing/piercing attacks generally; specific weapons can apply extra stacks as a passive (none defined yet)

## Status Effect 3 — Rupture *(Immediate, triggered)*

* **Type:** Immediate · **Affects:** Both · **Resisted:** N — a mechanical trigger, not an attack
* **Effect on application:** 25% of Max HP as direct damage, plus staggered for a beat. Scales with the character so it stays a real threat at any Vigor level. **(untested)**
* **Duration:** instant — resolves once, fully, on trigger. Nothing to clear.
* **Dangerous combinations:** landing near your remaining-HP threshold when Blood Loss hits 10 — a genuine "you should have managed this" spike, not a guaranteed kill, but close at low Max HP
* **Countered by:** nothing once triggered — the only counter is managing Blood Loss before 10
* **Sources:** currently only the player's own Blood Loss reaching cap; open for a future enemy or hazard to apply directly

## Status Effect Template (blank)

* **Type (Immediate/Track/Tick):** · **Affects (Player/Enemy/Both):** · **Resisted on Application? (Y/N):** · **Resistance Mechanic:**
* **If Immediate:** Effect on Application · Duration · Cleared Early? (Y/N) / Condition
* **If Track (0–10):** Stacks per Application · Effect per Stack / per Turn · Cap · Rupture/Overflow Effect · Clear Condition + Cost
* **If Tick:** Applied Value · Effect While Active · (counts down 1/turn automatically)
* **Interactions \& Sources:** Dangerous Combinations · Countered By · Enemy Sources · Weapon/Item Sources

\---

# 7\. Currency / Collectible Template

## Currency/Collectible 1 — The Token That Isn't Yours *(floor entry)*

Not White Salts (fully defined in Ruleset §4/§19) — the weakest possible Key Item: seeded in the world (Ruleset §15) and currently doing nothing, on purpose.

* **Category:** Key Item (bordering on Story)
* **Risk Status:** neither Purse nor Vault — it just stays with you · **Lost on death:** N · **Lost on retreat:** N
* **Acquisition — drops:** none. **Bonus condition:** one-time only, found in the robe pocket on the way into the deep cure (Ruleset §15). No known way to get a second, or lose the first.
* **Spend options:** none yet. Fits no slot, opens no listed door, buys nothing — deliberately, because it isn't supposed to mean anything yet.
* **Flavour:** worn brass, warm to the touch even when nothing else is. It doesn't match the token the reception clerk hands out, and nobody at the hub will take it back.

**Template fields** (copy per entry): Category (Spendable/Story/Cosmetic/Key Item) · Risk Status (Purse/Vault/Neither) · Lost on Death? · Lost on Retreat? · Acquisition — Base Drop by Archetype · Acquisition — Bonus Conditions · Spend Options (what it buys / cost / where) · Flavour (1–2 lines)

\---

*Sections 8–10 (Mechanic Index, Book Plan, Known Gaps) live in the dev log — `deep-salts-dev-log-v1.md`. Section numbering is preserved across both files so ruleset cross-references (e.g. "design bible §10") remain valid.*

