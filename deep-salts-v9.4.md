# THE DEEP SALTS

**A horror exploration RPG**

System-agnostic ruleset (d20 base) for solo play with an AI DM. You trade humanity for power, and only see the trade once you've gone mad enough to look.

*Version 9.4. Session-attribution history and rationale prose live in the dev log, not here.*

---

## 1. The Premise

Salts dissolved in hot water at the mysterious Stillwell Hydro transport you to another plane. Fight through, gather loot/materials/knowledge. Each area has a "clean chalice" — drink to wake at Stillwell Hydro with everything from that run, banked. Near death, focus your mind to exit immediately, losing everything on your person; retrieve it by re-entering the same recipe and beating the enemy that has it.

**Core loop:** brew a recipe → wake in that biome, blind → survive → return to the clean chalice and leave (or die, or bail) → bank at the hub → push deeper or brew elsewhere. No fast travel — the recipe is the travel (§18).

---

## 2. Running This With an AI DM

* Never explain the world fully. Let the player infer; answer lore questions in-fiction through an unreliable source, or not at all.
* Describe, don't signpost. No quest markers.
* Consistent hub, inconsistent everywhere else (§14).
* Track status, Insight, limbs, Salts, and inventory turn to turn. Surface when relevant; don't recite.
* Generate new monsters live from the archetype table, scaled to level (§17), never below the Damage Floor (§4), then record the filled Monster Template. Live generation is for first contact; the manual is canon after.
* Honour tells — parry/precision only work if a readable tell reliably precedes the attack.
* Plain attacks to 0 HP always kill, on everything including bosses. Sever is a bonus fast-lane for high-HP fights.
* **Verify before asserting.** If a named entity, item, rule, or number comes up that isn't already visible in this conversation, stop and check the actual repo files before stating anything — never rely on memory or invent a plausible value. If nothing exists, say so; don't fabricate an entry.
* **Operating checklists live in `dm-only/protocols.md`** — session start, instance start, entering a room, considering combat, running combat. Read the relevant protocol before performing that action. The protocols point back here for numbers; this ruleset remains the single source of truth.
* **UTT / OTT.** *Under the Table* = meta discussion of the game as a system. *Over the Table* = in-fiction narration and roleplay. **OTT is the default**; infer from context when unmarked.

---

## 3. Core Resolution

d20 + modifier vs a DC. **Default attacks land** — no attack roll, either side. Rolls/stopwatches only for:

* **Called shots** on limbs with multiplier >1.0 → Precision stopwatch (§10), unless already parry-opened (§9).
* **Parries** and the heavies that invite them → Visceral stopwatch (§9).
* **Insanity/Influence saves** → d20 vs the Save Roll formula (§5).
* **Anything genuinely uncertain** (stealth, forcing a door, reading the unreadable) → d20 vs DC, modified by the Attribute Modifier table (full framework, DC ladder, and attribute mapping: §19):

|Attribute score|Modifier|
|-|-|
|0–1|−3|
|2–4|−2|
|5–9|−1|
|10–19|+0|
|20–39|+1|
|40–79|+2|
|80–99|+3|

(Doesn't apply to the Save Roll formula, §5 — that has its own scaling. Perks may stack extra situational bonuses on top.)

Enemy basic attacks land the same way — no enemy to-hit roll, defense is entirely the player's via timing/positioning/range.

**0 HP always kills** — mooks or bosses. Sever kills regardless of remaining HP and is the faster route once a pool would otherwise drag; it's never required.

---

## 4. Character Creation & Progression

### Backstory-Negotiated Creation

Player writes a short concept; DM negotiates the mechanical translation:

* **Attribute reallocation** — default flat 8×5 (40 total). A strong concept can redistribute unevenly; total stays 40 unless both sides agree it earns more.
* **A bespoke starting weapon** instead of the weapon table — type, governing stat, base damage placed in-range for the concept (never under the Damage Floor), one signature gimmick that costs something for something. Any risk/reward on the gimmick uses existing tools (stopwatch or d20), never a new resolution system.

### Attributes

Five buyable; Insight is separate, earned not bought (§11).

* **VIGOR** → max HP, Bleeding resilience
* **ENDURANCE** → movement budget
* **STRENGTH** → heavy weapon damage, sever power, most common skill check
* **SKILL** → light weapon damage, parry/precision tolerance
* **RESOLVE** → arcane weapon damage, Insanity/Influence saves,

All start 8, cap 99. Starting Insight = 1.

**Derived stats:**

* Max HP = 60 + (Vigor × 6) → Vig 8 = 108, Vig 99 = 654
* Movement budget = 8 + ⌊Endurance ÷ 15⌋ m → End 8 = 8m, End 99 = 14m
* Insanity/Influence save bonus = ⌊Resolve ÷ 10⌋ → Resolve 8 = +0, Resolve 99 = +9

### Effective Scaling Value (ESV) — soft caps

Weapon/combat scaling uses ESV, not raw score:

|Score range|Each point worth|
|-|-|
|1–20|×1.0|
|21–40|×0.85|
|41–60|×0.65|
|61–80|×0.5|
|81–99|×0.3|



### White Salts

* **Purse** — earned this run, at risk. **Vault** — banked at hub, permanently safe.
* Hub arrival moves full Purse → Vault. Retreat and Death (§12) only ever touch the Purse.
* Spend Vault Salts on attribute levels, equipment, information, etc. A singular currency that forces decisions between levelling up and acquiring new gear, materials, salts, etc.

### Leveling

Level = total attribute points spent, lifetime. Cap 100. Cost of next point = 25 × current level.

|Checkpoint|Cumulative spent|Next point costs|
|-|-|-|
|Lvl 10|1,125|250|
|Lvl 25|7,500|625|
|Lvl 50|30,625|1,250|
|Lvl 75|69,375|1,875|
|Lvl 100|123,750|2,475 (final)|

### Perks — at 20/40/60/80/99 per stat

Granted per points invested in that specific stat.

**VIGOR**

* 20 *Thick Blood:* Bleeding stacks applied to you are reduced by 25%, rounded down.
* 40 *Second Wind:* once/instance, a hit that would drop you to 0 leaves you at 1, clears one track.
* 60 *Thick Hide:* flat −2 damage on all incoming hits.
* 80 *Iron Lungs:* Burning, Bleeding stacks start at -2.
* 99 *Unbreaking:* once/instance, use a bonus action to reduce all damage by 25% for the next 5 turns.

**ENDURANCE**

* 20 *Light Foot:* moving right after an attack costs 1m less.
* 40 *Overcharge:* a whiffed parry, once/encounter, becomes a chip hit instead of full whiff punishment.
* 60 *Quick Recovery:* Clear Discombobulation via a Fast Action (cost: 2m).
* 80 *Outrunner:* movement budget never drops below half, regardless of leg damage.
* 99 *Endless:* once/encounter, immediately retry a failed stopwatch check with no whiff punishment. Covers the Charged Heavy stopwatch too.

**STRENGTH**

* 20 *Heavy Hand:* raw damage counts +5 solely for sever-threshold checks.
* 40 *Brute Force:* charged heavies treat boss stagger meters one tier lower.
* 60 *Render:* a successful sever dumps bonus stagger damage onto an adjacent limb.
* 80 *Executioner:* sever attempts vs a staggered target +10% raw damage.
* 99 *Annihilate:* once/encounter, triple limb damage on one attack. Requires a stopwatch check.

**SKILL**

* 20 *Steady Hand:* all precision windows widen +0.02s flat.
* 40 *Featherstep:* first Assess each combat costs 0 movement.
* 60 *Riposte:* a successful parry grants an extra free light attack before the visceral resolves.
* 80 *Untouchable:* missed-precision punishments reduced one band.
* 99 *Perfect Read:* once/encounter, auto-succeed one stopwatch check.

**RESOLVE**

* 20 *Iron Will:* reroll a failed Insanity save once.
* 40 *Unshaken:* Influence command duration −1 round.
* 60 *Clear Mind:* once/encounter, clear Insanity to 0 for one round. Atfer that round, Insanity is restored to previous level.
* 80 *Silence the Hum:* Use a Bonus Action (-4m) to become immune to passive/ambient Influence (direct spoken commands still land).
* 99 *Indomitable:* on a failed Insanity save, act with disadvantage instead of losing control.

### Weapons

**Damage = Base + (ESV × grade).** Heavy ≈ 2×Base + ESV×grade×1.5. Grades: E ×0.3 · D ×0.5 · C ×0.7 · B ×0.9 · A ×1.1 · S ×1.3. **Fractional results round up** (session 6 ruling — applies to this formula throughout, not just Fists).

|Weapon|Type|Stat/Grade|Two-handed?|Gimmick|
|-|-|-|-|-|
|Tideglass Cleaver|Quick|Skill/C|Optional|Light swings twice, 2nd hit reduced|
|Cautery Saw|Heavy|Strength/B|Yes|Slow huge hits — best raw sever weapon|
|Birthing Hook|Reach|Skill/C|Optional|Wide sweeps; strong vs multiple limbs|
|Funicular Spike|Reach/thrust|Strength/B|Yes|Bonus dmg vs staggered targets|
|Brass Token Press|Trick|Skill↔Strength|Switches|Folds Quick/Heavy; full transform gated Insight Tier 1|
|Fists (unarmed)|Quick|Skill/E|N/A|No gimmick, no ammo. Base 10 — deliberate sub-floor exception (session 6 ruling); never sever-capable, full stop, as the tradeoff.|

*Worked example — Cautery Saw heavy, base 30: Str 8→ESV 8→~71 dmg. Str 40→ESV 37→~110. Str 99→ESV ~66→~149.*

**Charged Heavy** — the third attack weight (referenced by the Strength 40 perk *Brute Force*):

* **Cost:** 5m (vs. Heavy's 3m). One per turn, same as any Action.
* **Resolution:** a self-timed stopwatch at release — target 1.5s, ±0.20s base, widened by the wielder's Insight window bonus same as any other stopwatch (§11). This is the first player-side stopwatch on a *default* attack rather than a weapon-specific gimmick (Segmented Choir-Flail, Bible §2, was the first on any attack at all).
* **Success:** 2×Base + ESV×grade×**2.0** (up from Heavy's ×1.5) — a real step up, not a rounding difference.
* **Failure:** 0 damage, turn ends immediately, no leftover movement to spend — same harsh-failure shape as Powder Charge and the Choir-Flail's own chain, deliberately.
* Boss stagger-meter interaction (Brute Force, Strength 40: "treat boss stagger meters one tier lower") now has a real trigger to attach to.

**Weapon stat governance.** Weapons have historically been governed by Skill, Strength or Resolve. Any attribute may govern a weapon, drawing ESV from that attribute's score through the standard soft-cap table above — including **Endurance** and **Insight**. Two consequences worth stating before they come up at the table:

* **Endurance** also sets the movement budget (§7). An Endurance-governed weapon means one score buys both swing and step, and every action's movement cost is competing with the stat that makes it hurt.
* **Insight** is earned rather than bought and **falls when spent** (§11). An Insight-governed weapon's damage therefore moves during play — up on a first sighting or a lore read, down the instant a gate is forced or a Vendor trade is made — and it recalculates immediately, mid-encounter. Insight realistically tops out around 20, so such weapons sit permanently mid-tier by design.

**Double-swing reduction** *(closes the Bible §2 gap — Tideglass Cleaver and any reskin of it).* Standard is **50% of the first hit's raw, rounded up**, unless a specific weapon's own Bible entry states otherwise. Applies to any weapon whose gimmick is "swings/hits twice per Light" — a default, not a per-weapon negotiation.

### Damage Floor & Scale

**20 is the practical floor** for any base number passing through a multiplier (weapon bases, enemy damage, DM-generated numbers) — keeps multiplier results whole and ensures even weak weapons can eventually sever. Doesn't bind flat unmodified numbers (Quick Item heals, status ticks).

Enemy HP/thresholds scale to match: archetype band × level multiplier (§17), attack damage proportionate to what Max HP and Rally (§6) absorb.

---

## 5. Status Effects

Statuses come in three shapes. Which shape a status is determines how it leaves you, and that is the only thing the categories mean.

- **Ticks** drain themselves. They count down on their own and will always end without intervention.
- **Tracks** hold. They build and stay built until something clears them.
- **Conditions** are binary. Applied or not applied, no stack count.

| Status | Shape | Cap |
|---|---|---|
| Bleeding | Tick | none |
| Burning | Tick | none |
| Discombobulation | Tick | 3 |
| Stone Skin | Tick | 3 |
| Frenzy | Tick | none |
| Insanity | Track | 10 |
| Influence | Track | uncapped |
| Corrosion | Track | 10 |
| Crust | Track | 4 |
| Fervour | Track | 10 |
| Fugue | Condition | — |

---

### Ticks

**BLEEDING** — +1 stack per qualifying hit or hazard. **Damage at the start of your turn equals current stack count**, then lose 1 stack automatically. Uncapped.

Total damage from N stacks is N(N+1)/2 — it escalates hard and it is meant to. Reference points:

| Stacks | Total damage | Turns to run out |
|---|---|---|
| 3 | 6 | 3 |
| 5 | 15 | 5 |
| 10 | 55 | 10 |
| 15 | 120 | 15 |
| 25 | 325 | 25 |

Above roughly 10 stacks a target is bleeding out whether or not anyone keeps hitting it. **Severing a limb is therefore a kill condition in its own right** — walk away and the thing dies. Against multi-limbed enemies, severing several limbs fast is a legitimate primary strategy rather than a bonus.

**Clear:** Wrap (Fast Action) **halves current stacks, rounded up.** Cautery iron (Action Item) clears all stacks.

*Rupture is deleted. It was triggered by the old cap of 10; there is no cap now.*

**BURNING** — 5 flat damage per turn while any stacks remain. Lose 1 stack automatically each turn. **Stacks add duration, not intensity** — this is the deliberate opposite of Bleeding, and the reason both exist. Smother (Action) clears all. Scour (Quick Item) clears 1. Spreads to oil, cloth and steam-soaked surfaces.

**DISCOMBOBULATION** — applied 1–3 by severity, counts down 1 per turn. While active the DM may misdescribe exits, reverse movement, strip reactions, scramble attack directions. Fresh application refreshes to the higher value. Cap 3.

**STONE SKIN** — **10% damage reduction per stack.** Counts down 1 per turn, so 3 stacks is 30% this turn, 20% next, 10% after that. Cap 3.

Found only as a limited-use consumable. Never a passive, never a drop, never granted by a perk. **[CONFIRM]** Action Item, 2m — a Fast Action version means you never eat a telegraphed heavy at full value again.

**[CONFIRM]** Applies to raw damage from attacks only, not to tick damage from Bleeding, Burning or Corrosion. 30% off everything at once is a much wider net than 30% off swings.

**FRENZY** — the Red Mist. Applied at Fervour 10 (4 stacks) or by specific entries. Counts down 1 per turn, **and zeroes immediately at the end of any turn in which the afflicted dealt no damage.**

While active, the afflicted **must attack something each turn.** Enemies are targeted first; if no enemy is reachable, the DM directs the attack at the nearest NPC or ally. Applies to enemies exactly as it applies to the player.

Consequences worth stating plainly:

- **Frenzy locks out Hold.** You must attack, Hold is an Action, and Hold deals no damage.
- Because default attacks connect automatically, the no-damage clear almost never fires while anything is in reach. Frenzy near a living target runs its full duration; Frenzy in an empty room ends after one turn.

---

### Tracks

**INSANITY** — on taking damage, witnessing something wrong, or failing a fear save: Save Roll (below). Fail → DM controls you for one turn.

**BREAK** (at Insanity 10, automatic, no roll) — Insanity resets to 0. In exchange:

- **Blackout:** DM full narrative control, 3 turns. Broken World scene — false tells, fake Influence commands, wrong layouts, plus a hallucinated threat dealing real damage (floor 20).
- **Scar:** permanent trait attaches when the blackout ends — upside and downside, contextual to what triggered the Break. Full trade legible only at Insight 6 (Tier 3). Scars stack uncapped.
- **Removal:** Memory Vendor only, Insight-priced, escalating: Scar 1 = 6, Scar 2 = 10, Scar 3+ = higher.

**INFLUENCE** — builds like Bleeding but holds; uncapped past 10, no overflow trigger. Compelled-effect severity scales with stack count. Fail a save → obey the effect next turn.

- First save triggers at stack 2.
- A successful resist doesn't clear the stack while the source stays active — only full source elimination clears it. Multiple sources: all must be eliminated.
- A failed Influence save ticks Insanity only once the Influence stack is 3+.
- **Enemy-side Influence** — enemies have no compel/save loop, so severity scales behaviourally:

| Stack | Effect |
|---|---|
| 1–2 | Flavour only — restless, muttering |
| 3–4 | 50% chance/turn: attacks nearest creature instead of its declared target |
| 5–7 | Always redirects to nearest creature — normal attack numbers |
| 8–9 | As above, +50% damage on the redirected attack |
| 10 (cap) | **Overload Rupture:** 25% of that creature's Max HP as direct damage, staggers a beat, resets to 0. Repeatable. |

Applies to bosses. A boss with no attack to redirect skips 3–9 functionally but still hits Overload Rupture at cap.

- **The Beckoner's residual Influence:** stacks from the Beckoner become a sticky baseline. Breaking distance stops new accumulation but does not clear what's stuck. Clears only via full rest or fully divesting the item. While a baseline is active, new Influence encounters start at that baseline rather than 0.

**CORROSION** — **damage at the start of your turn equals current stack count.** Cap 10. Nothing happens at cap except 10 damage every turn, indefinitely. Ticks down 1 at end of turn only if you spent an action managing it; otherwise holds. Stacks viciously with Burning.

*Corrosion is the mirror of Bleeding: same damage-equals-stacks formula, but it does not drain itself. Bleeding is a burst that fades; Corrosion is a strangle that does not.*

**CRUST** — accreted salt, rime, resin, wet ash. **−1m movement budget per stack.** Cap 4.

Ticks down 1 at end of turn **only on a turn in which you took no Action at all** — you have to actually stop and break it off.

**At cap 4:** no Action costing more than 1m may be taken. Light attacks and Manage a Track only — no Heavy (3m), no Hold (4m), no Action Items (2m).

**FERVOUR** — the only status the player wants. Builds on aggression, pays in power, charges rent.

**Builds:** +1 on each landed visceral. +1 on ending a turn within 2m of a living enemy.

**Grants, per stack:** +3 raw damage and +0.5m movement budget.

**Costs:**
- A turn in which you deal no damage — including a whiffed parry — costs **stacks × 3 HP**, self-inflicted.
- You lose 1 stack only on a round in which you **received more damage than you dealt.** Otherwise it does not decay.
- **Self-inflicted Fervour damage does not count as damage received** for that comparison.

**At cap 10:** Fervour resets to 0 and the character gains **4 Frenzy.**

**Fervour ends when combat ends.** It does not persist between encounters and does not carry to the hub.

---

### Conditions

**FUGUE** — see §13. Applied on death. Not a stack count; you either have it or you don't.

---

### The Save Roll (Insanity & Influence)

**Succeed on d20 ≥ 10 + (current track value) − ⌊Resolve÷10⌋ + ⌊Insight÷2⌋** (+ situational mods).

*Worked example: Resolve 8, Insight 1, 2nd Influence stack → 10+2−0+0 = 12. Later: Resolve 30, Insight 6, Influence 6 → 10+6−3+3 = 16.*

---

## 6. Rally

Damage taken becomes recoverable grey health. Land a qualifying hit on your very next turn to claw back a portion, or it fades.

* Default: 50% recovered.
* Big telegraphed boss haymakers: 75–100%.
* Chip/DoT (Burning, Corrosion, Bleeding): 0–25%.
* Set per-attack; overrides noted on the attack's own entry.

---

## 7. Combat Flow, Movement & Positioning

### Round Structure

Each round has up to four phases, always in this order:

1. (Optional) Player can Assess (a Fast Action) enemies before any actions are taken. This 

2. (Optional) If the player has identified enemy telegraphs for their turn, the DM narrates those telegraphs. Enemy actions are committed to here. 

**3. Player actions**

Declare and resolve all player actions: movement, one Action (§8), one Fast Action (§8), and companion actions.

* Movement budget is splittable before and after the Action.
* **Hold (parry stance) is an Action** — it costs 4m and commits the player's Action for the round. They cannot move after declaring this action until it has been resolved. A Hold can only parry one attack unless superseded by other perks, equipment, etc. The player can select which attack they parry if multiple are incoming in this round.
* Attacks connect with enemies by default; other rules or perks may override this.
* If present, companions / allies act during the Player action step with their own Fast Action, Action and/or movement. They cannot parry on the Player Character's behalf or redirect attacks targeting them. DM narrates their successes / failures using their own dice rolls and judgment.
* If an enemy action was to interrupt the player's action (ie through an ambush), the player's action is interrupted and the enemy action turn starts. 

**4. Enemy actions** 

* Enemies move in a block; their order can be changed by the DM if they wish to do so to coordinate enemy movements (for example, coordinating "pack" or "stalker" enemy archetypes for optimal pressure on the player by having them act before or after other enemies).
* Enemies have their own movement budget.
* Enemies only use one Action per turn, unless noted otherwise in their design - no Fast Actions by default.
* Unless other rules / perks override this, enemy attacks connect automatically.
* If the player action was to interrupt an enemy action (ie via Hold to parry), enemy action is interrupted and player action is completed. Player may use the rest of their movement here; but not their Fast Action unless superseded by other rules or perks.
* If an enemy action was to interrupt the player's interruption, the player's interruption is interrupted and the enemy action is completed instead (ie a player's parry can be interrupted by an ambush).



### Secondary Actions (enemy-side)

An enemy's primary attack is what it does when nothing has gone wrong for it. **Secondary Actions are what it does when something has.** Every monster entry carries at least one, and most carry two or three. Assess does not inform the player of Secondary Actions; these are learned live. Unless overruled elsewhere, Secondary Actions cannot be parried. *Other Secondary Actions can be determined live by the DM, but they must be sub-optimal compared to the enemy's primary Action and established Secondary Actions.* Secondary Actions are intended to reduce the repetitive nature of combat and balance the strength of the parry mechanic. 



**How they resolve:**

* A Secondary Action **replaces** the enemy's Action for that Enemy Phase. It is not taken in addition to a Primary Action, unless overridden by other rules.
* Each has a stated **trigger**: an objective, checkable condition, or context cue etc. Some examples: *"Has been parried two turns in a row." "Below half HP." "Leg severed." "Target further than 6m." "Took no damage last round." "Combat has lasted 6 rounds." "Limb close to staggering." "Pack member killed." "Pack Alpha killed." "No allies in the room."* If no trigger is true, the enemy attacks normally.
* Each Secondary Action has a **cooldown** in rounds.
* If two triggers fire in the same round, the DM determines Action taken (Primary or viable Secondary). DM to determine this based on context.
* **Assess 2+ hints at trigger/s for Secondary Actions, not the outcome.** The player learns what sets it off; what it does is discovered by setting it off.



**Design constraints (binding on all future content):**

* A Secondary Action must **change the shape of the next round**, not merely deal damage on a different line. Repositioning, denial, escalation, calling for help, self-repair, retreat, handing something off to another enemy, changing its own limb table — all valid. *"Same attack, +20 raw"* is not a Secondary Action, it is a bigger swing.
* Secondary Actions never invent new subsystems. 
* A Secondary Action **may** be triggered by the player doing well.

### Interception — enemy reactions during the Player Phase

Enemies act on the Enemy Phase. A small number of entries — always flagged explicitly on their own Monster Template — instead act **in response to the player acting**, during the Player Phase. The player can parry enemies - this is the enemy variation to be used against the player.

* An Interception is declared on the entry with its own trigger, and it resolves **before** the player's declared Action does.
* **It cannot be parried.** Hold is an Action (§7), and an Interception fires on the Action being taken — including on Hold itself. A player who declares Hold against an intercepting enemy is hit mid-stance and loses that round's parry entirely.
* An enemy that Intercepts does **not** also act on the Enemy Phase that round. It has spent its action.
* **Interception damage is small by design.** The cost is the lost turn, not the number.
* The counter is always positional, ranged, or preparatory: break the condition that lets it reach you, hit it from outside its trigger, or spend a round making the trigger false. **Every intercepting entry must state its counter explicitly on its own page.** An interception with no stated answer is a tax on existing, not an encounter.
* Movement alone never triggers an Interception. If it did, the player would have no legal move at all. Entering an area of effect is a viable trigger, however.

### Movement & Positioning

Budget set by Endurance (8–14m) — the single per-turn currency; repositioning and actions both draw from it. Spend before/after your action up to the total minus the action's own cost (§8).

**Hard rule:** can't pay an action's movement cost → can't take that action.

* **Hit-and-run** — attack and retreat beyond reach in one turn. No parry, no opening. Safe, slow, low-reward.
* **Kiting** — if your budget exceeds theirs, stay out of reach and chip.
* **Burst-movers** — some alternate a surge turn (huge ground, attacks only at the lunge's end) with a recovery turn. In during recovery, out before the surge.

**The triangle:** Trade (stand and swing — fast damage, eat hits) / Parry (high risk, high reward) / Kite (safe, slow, no openings). Good play flows between all three.

---

## 8. Action Economy & Items

**Movement** — your budget, splittable around your Action, Fast Action and literal character movement.

**Action** (one/phase, costs movement):

|Action|Movement cost|
|---|---|
|Light attack|1m|
|Heavy attack|3m|
|Hold (parry stance)|4m|
|Manage a track|1m|
|Use an Action Item|2m|
|Context sensitive: Perform an intense action (moving a book shelf, climb a ledge, etc)|[At DM's discretion; context sensitive]|

Specific weapons/actions may price differently; perks may refund/grant/zero costs.

**Fast Action** (one/phase, costs movement):

|Fast Action|Movement cost|
|---|---|
|Assess|1m|
|Use a Quick Item|0m|
|Swap weapons|1m|
|Load ammunition / capsule|1m|
|Context sensitive: Perform a quick action (open doors, pick up a light item)|1m|

**Items are self-use only** (session 9 ruling) — companions support through their own designed abilities, not by applying the player's consumables.

**Reactions** sit outside all pools. Retreat cannot be used in active combat at all (§12).

### Limb-gating

|Requires|Staggered|Severed|
|-|-|-|
|Weapon arm|−1 die / heavies disabled this turn|Can't wield that side; off-hand only, two-handers unusable. Add +15 stacks of Bleed.|
|Legs|Budget halved|Crawl only (1m), no kiting, prone (standing costs your Action). Adds +25 stacks of Bleed.|
|Head|Dazed — Discombobulation 1 turn, can't Assess|Dead|
|Torso|n/a — stagger is just heavy damage|Dead|

### Items

**Durability tags** — every item carries exactly one:

* **Constant** — persists indefinitely (per-use costs still apply).
* **Hub Kit** — recharges/resets free on every hub return.
* **Uses: [N]** — works N times then spent, not hub-refilled.
* **Instance-specific** — can't leave the layout it was found in; expires with the instance (§18).

**Quick Items** (Fast Action):

* Wrap — halves current Bleeding, rounded up
* Camphor — clears 2 Insanity
* Tonic — small flat heal (~10% max HP)
* Scour — clears 1 Corrosion, no turn cost
* Source-water flask — big heal (+50%), adds 1 Influence stack. (Uses: 1 per flask.)
* Stone Skin draught — applies 3 Stone Skin (§5). (Uses: 1.)
* Cautery iron — fully clears Bleeding; costs full remaining movement budget on use. (Constant.)
* Thrown vial — Corrosion/Burning at range. (Uses: 1 per vial.)
* Charm — one-shot buff (extra die, widened parry window), Insight-gated. (Uses: 1.)

**Reactive/Instant** (no slot, usable anytime): distress flare/ally beacon (multiplayer hook, unbuilt).

**Passive/Equip** (no slot, always active): trinkets/build-around gear, often Insight-tier-gated.

---

## 9. The Visceral System (parry + stopwatch)

Needs a stopwatch.

**Assess** (1m): reveals an enemy's tell and rough timing of its next heavy, clarity scaling with Insight. You can then Hold to parry on its turn.

**The parry:**

1. Enemy telegraphs a heavy — target time + tolerance (e.g. Lunge 1.50s ±0.20 · Overhead 2.00s ±0.15 · Sweep 1.20s ±0.25).
2. Start the stopwatch — no charge cost, no attempt cap.
3. Pause inside the window.

**Outcomes:**

* **Inside → PARRY.** The telegraphed attack is interrupted. Enemy is knocked down and the player "hijacks" the enemy's action to perform their own (they can attack the enemy once during the enemy turn). During this hijacked turn, the player's attack against the enemy is a **visceral attack attempt** at 1.5× damage, dependent on another stopwatch check (plus Insight mods) — Tier 1 default, via the eased stopwatch below. This multiplier can be stacked with other multipliers, limb modifiers, and buffs (which may also require dice rolls or stopwatch checks). note that the buffs would need to be applied during the Player Action turn. The player can use the rest of their movement budget to relocate after a successful Parry as well.
* **Outside → WHIFF.** The player misses the parry. The enemy attack lands. The player does not get to "hijack" the enemy's action or use the rest of their movement budget.



**The eased follow-up stopwatch** (Tier 1 only):

* **Tolerance:** flat **±0.25s** regardless of the target's actual multiplier band — the loosest band in the game. Target time per the normal Precision Strike convention (~1.50s default, 1.0–2.0s range).
* **Hit →** the weak-point strike lands, 1.5× plus Insight mods.
* **Miss →** the player does not do damage, but is not punished otherwise. The target's already down; a miss costs the bonus, not a beating.

Insight widens windows and unlocks visceral mods (§11): Bloody, Sustaining, Quickening.

### Post-parry weak points — three tiers

* **Tier 1 — Open** (default, mooks/elites). Parry knocks it down for its one lost turn (above); the weak point is Lloyd's to *attempt* on his next action via the eased ±0.25s stopwatch above — favored, not automatic.
* **Tier 2 — Widened** (some bosses). Opened but not floored — no lost turn, this tier never grants one. Precision window (§10), widened one tier from the target's actual band (tighter than Tier 1's flat ease, looser than the target's normal difficulty).
* **Tier 3 — Full double** (bosses, chaotic limbs). Parry stopwatch, then a full second precision stopwatch, target's actual band, no easing at all. No lost turn either.

**Table fallback:** replace any stopwatch with d20 + Insight-as-modifier, same outcomes.

*Stopwatch checks outside combat (hazards, mechanisms, chases, stealth) now have their own named shapes — §20, not improvised fresh each time.*

---

## 10. Limbs, Precision & Mutation

Every enemy still dies the ordinary way — plain attacks chip HP, 0 HP is dead. Everything below is an *additional*, faster route on tougher enemies.

### The limb / Precision Strike model

Default multiplier suggestions - each enemy should have some variation, however:

|Limb|Damage Multiplier|Limb HP (relative to enemy HP)|Difficulty to strike|Potential pay-off / value in targeting|
|-|-|-|-|-|
|Head|×1.5|~30%|Difficult stopwatch|Lower limb health - targeted head shots kill more quickly|
|Torso|×1.0|100%|No stopwatch|Safe target|
|Arm (each)|×0.65|~50%|Easy stopwatch|Potentially disables weapons / attacks|
|Leg (each)|×0.75|~50%|Easy stopwatch|Potentially reduces movement|
|Tentacle (each)|x0.5|~5%|Easy stopwatch|Very easy sever, and applies 3x Bleed per sever, but minor immediate damage.|
|Wings (each)|x1.25|~15%|Very difficult stopwatch|Once staggered, cannot fly. Once severed, can no longer use Primary Actions or fly.|

* Effective damage = raw × multiplier — chips HP AND fills the limb's stagger meter.
* Threshold over several hits → **STAGGER** (limb goes limp). The hit that crosses it grants an immediate free Action (ie the player gets a follow-up strike in their turn against the enemy whose limb they just staggered). Player stagger duration: fixed 1 turn. Enemy stagger duration: variable, set per Monster Template.
* Full limb HP threshold damage dealt in one hit → **SEVER** (permanent). Permanent limb damage effects applied, immediate free Action to the player as per stagger; may also incur other debuffs or status effects. Severing torso/head kills regardless of remaining HP.
* Called shots on a standing, alert, unstaggered enemy incur a stopwatch penalty — needs an opening (stagger/knockdown/off-balance/parry). Default swings land torso.
* **Implements and objects** (a carried bell, a shield, a weapon) are non-standard entries that are NOT limbs — they're equipment or objects attached to the enemy. **Damage to an implement does not chip the enemy's HP pool.** Implements have their own isolated stagger/sever thresholds. Stagger produces a partial effect (defined per implement — e.g. a cracked bell might toll at reduced potency). Sever destroys the implement entirely, disabling whatever it provided. The distinction is logical: punching an enemy's sword doesn't wound the enemy, but punching their arm does.

*Worked example: leg (×0.75, 325HP) needs 434 raw in one hit to sever. The enemy has 650HP total. The player knows they can output 450 damage, so they hit the leg for 450HP, then the limb modifier is applied = 338 damage, which severs the leg. The player gets another Action in this turn due to the sever and uses it to attack the enemy's torso for ~450HP (no modifier = 450 damage), killing the enemy. Instead of hitting the enemy in the chest, then potentially taking damage next turn, the player managed to defeat the enemy in one turn.*



**Standard humanoid thresholds are the baseline, never level-scaled.** Individual enemies **should** override specific limb thresholds in their Monster Template entries — reinforced heads, weakened arms, etc. Where no override is listed, standard defaults apply. 



**Weapon, item and perk effects on the precision subsystem are allowed.**



**Bosses get hand-set limb values** on their own Monster Template — high enough that clearing a weak point in one hit takes real specialization.



**Elemental multipliers and immunities.** A creature may declare an explicit multiplier or immunity against a specific status track — tripled Burning against a shelled swarm, zero Burning and zero Corrosion against a body made of water. These are stated on the Monster Template, apply to that track's damage only, and are deliberately rare: the point is to occasionally invalidate one tool in the player's kit for one encounter, not to introduce a resistance chart. Assess 2+ always reveals them.



**Attack shape — Arc and Point.** Most of the manual does not care how wide a swing is. A small and growing set of entries does — Swarms above all (§16), plus any creature made of many small bodies or many thin limbs. Two shapes:

* **Arc** — sweeping, shearing, whipping or crushing across a span. **Default:** all *Reach* and *Heavy* type weapons, all flails, whips and lashes, all two-handed weapons, and any weapon whose own entry describes a sweep, shear or wide cut (the Guillotine Shears and the Retractor both qualify explicitly).
* **Point** — thrusts, jabs, punches, single-target quick work. **Default:** one-handed *Quick* weapons, all thrust weapons, Fists, and all ranged single-projectile attacks.



Where an entry doesn't make it obvious, the DM calls it once out loud and it stays called for the campaign. Shape never affects damage against anything with a normal limb table — it only matters where an entry explicitly invokes it, and it never interacts with Precision Strike, sever or stagger.

### Precision Strike — the greedy-target tax

Targeting a limb triggers a precision stopwatch:

|Multiplier|Tolerance (±)|
|-|-|
|0.0-0.5|±0.25s|
|0.51-0.70|+0.20s|
|0.71-0.99|+0.15s|
|1.0|(no stopwatch - torsos and "default hit" targets sit here)|
|1.01–1.25|±0.13s|
|1.26–1.50 (head)|±0.10s|
|1.51–1.75|±0.07s|
|1.76–2.00|±0.04s|
|2.01+|±0.02s|

Target time DM-set per opening (default ~1.50s, range 1.0–2.0s). Miss punishments scale with greed:

|Band|On a miss|
|-|-|
|0.00–0.50|Torso — full dmg, no limb effect|
|0.51–0.70|Torso — full dmg, no limb effect|
|0.71–0.99|Torso — full dmg, no limb effect|
|1.01–1.25|Torso — full dmg, no mult, no sever|
|1.26–1.50|Torso, no sever, + off-balance (−1m next turn)|
|1.51–1.75|Wide — no dmg, enemy free reactive strike|
|1.76+|Whiff + exposed — enemy free heavy, or a track|

**Tier 1 parry flattens the precision watch to the loosest tolerance band, ±0.25s, regardless of the target's own multiplier** — eased, not removed (miss handling: §9). Tier 2 widens it one tier from the target's actual band. Tier 3 keeps it full, no easing.

**Accuracy Tiers** *(session 8 ruling).* Within a hit window, the existing tolerance bands (±0.25s, ±0.20s, ±0.15s, ±0.13s, ±0.10s, ±0.07s, ±0.04s, ±0.02s) act as inner rings. Count how many bands sit inside your current window — each one you land in beyond the minimum = a bonus tier. If your window only covers one band, no bonus is possible. Multiplier applied to **final calculated damage** (after all other multipliers):

|Bands deeper than required|Multiplier|
|---|---|
|1-3|×1.0 (no bonus)|
|4|×1.1|
|5|×1.2|
|6|×1.3|
|7|×1.4|
|8|×1.5|
|Dead centre (±0.00s variation)|×3.0 (critical)|

Applies to the primary attack stopwatch only — Powder Charge and other secondary stopwatches stay binary hit/miss.

**Self-initiated Precision Strikes** (no enemy tell — an unparryable grasp, a stationary target): tolerance tightens one band beyond the multiplier's own. A **miss ends the turn outright**, no repositioning; a **hit** lets remaining movement be used normally. **Limb multiplier only — no visceral ×1.5 stacking** (visceral is reserved for genuine parry/ambush openings).

**Ambush Precision Strikes** (genuine full unawareness — a real stealth approach): count as a Tier 1 parry-grade opening. Free, no stopwatch, AND stacks with visceral 1.5× (raw × visceral × limb multiplier compound).

**Ambush Perception** *(session 8 ruling).* Only fires when the DM has set up a genuine ambush — a concealed, motionless enemy positioned to strike an unaware player. Standard encounters are not ambushes. Roll **d20 + ⌊Insight÷2⌋** vs a DM-set **Ambush DC** (factors: concealment quality, lighting, clutter). Three outcomes:

* **Fail:** ambush fires as designed — unparryable chip, enemy acts first.
* **Pass:** ambush detected. No chip, normal turn order (player first).
* **Pass by 10+:** ambush *reversed* — player gets the ambush opening instead (Tier 1 compound, no stopwatch, visceral stacks).

### Mutation — the build engine

A Player Character's lost limb regrows at hub with a chance of coming back changed — clear upside, clear downside (e.g. beastly arm: +damage/−parry window; tendril arm: +reach/−accuracy; carapace leg: +stagger resist/−movement). Full stat-line legible only at **Insight 6 (Tier 3)** — same threshold as the Scar read above (§5) and the tier table's own "full mutation stat-lines" (§11); below it, vibes only.

**Regret options (hub):** Revert to human (Vault Salts or Insight) · Reroll (regrow again, Vault cost). Both run.

---

## 11. Insight — the Bargain

Separate "currency" that runs alongside White Salts, earned through discovery (lore, dangerous sources tasted, things new monsters encountered) — never bought. Buys power, thins the wall between you and losing control.

**What it buys:**

* Threshold gates (some doors/paths require a score to perceive/enter — free to pass once there).
* A spendable currency (forcing gated doors, Insight-priced gear, summoning support, below).
* Sight of the board — DM tells you things others don't see (tells, Influence commands, true layouts, truer parry timing).
* The visceral economy (mods below).
* Reading your own mutations (§10).

**Cost (passive):** each tier raises Insanity/Influence susceptibility via the +⌊Insight÷2⌋ Save Roll term.

**First-sighting trigger:** a complete Monster Manual entry for an archetype means you've already encountered it — no first-sighting bump, regardless of whether this specific fight is new. Bump reserved for genuinely new archetypes with no page yet.

### Insight Tiers

|Tier|Insight|Unlocks|
|-|-|-|
|0|0–1|Mundane start. Vague reads, no mods, base floor.|
|1|2–3|Parries inflict three stacks of Bleed. Parry window +0.02s. Vague, non-numerical mutation reads.|
|2|4–5|All Attacks cost -1m movement. Character has +10% chance of finding items while exploring. See warp-thresholds. Parry window +0.04s.|
|3|6–7|Hold cost halved. Full mutation stat-lines. "Charm" items usable. Damage taken +5%.|
|4|8–9|Parry window +0.06s. Untranslatable lore becomes comprehensible — written text **and monster vocalization/behaviour** (Insight Perception, below). Player can Identify their own loot without Maud's support.|
|5|10+|Full sight. Deepest instance content unlocked. Player character can now see through illusory walls (a potential POI placed into instances). Parry window +0.10s. Damage taken +10%. Some Secondary Actions are foreshadowed by the DM - not explicitly revealed.|

**Memory Vendor access** — separate from the tier table. The Vendor (Bible NPC 2) appears in the hub at **Insight 10+**. No threshold gate — if Insight drops below 10 from spending, she vanishes immediately. Trades Insight for voluntary mutations, mutation removal, and Scar removal — never accepts Salts, never allows a clean Insight dump (see design bible for full pricing and constraints).

Window bonus is a flat total per tier, not additive across tiers crossed — a tier without its own number inherits the last stated value. Applies to any DM-set timing window, not just parries.

**Insight Re-Read.** Any recurring, already-encountered thing (a mook archetype, a hub fixture, a recipe's signature environmental detail) gets re-described through your *current* tier every time it comes up again:

* **Score 0–1:** surface read — what anyone would assume.
* **Score 2–5:** a reframing detail — the surface read was incomplete.
* **Score 6–10:** the truth, plainly legible.

Costs and grants nothing — the existing score doing narrative work on repeat contact. Applies to locations and NPCs the same as monsters.

### Insight Perception — Narrating the Climb

*Standing DM technique for what the Re-Read bands sound like at the table — not a one-time scene.*

**The one hard rule: surreal, never spatially broken.** Higher Insight changes what Lloyd notices and how it's described — never the actual geometry of a space. He can always retrace how he got somewhere; a corridor is always the same length it was a minute ago. The strangeness lives entirely in sensory detail and interpretation, not in the map. A room that's colder, watched, or wrong in a way Lloyd can articulate is in-bounds. Non-hostile creatures, thoughts, voices may be apparent, and may hurt or help the player with advice and suggestions. A hallway that loops back on itself when it structurally shouldn't is not — that's a Break/Fugue effect (§5/§13, both already gated behind their own specific triggers), never ambient Insight narration.

**By Re-Read band, concretely:**

* **Score 0–1 (surface read):** plain description. A stain on the wall is a stain. A monster's noise is just noise.
* **Score 2–5 (reframing detail):** one extra, specific, sense-grounded detail that recontextualizes without changing the facts on the ground — the stain has a shape if he looks twice; the noise has a rhythm that almost isn't random.
* **Score 6–10 (the truth, plainly legible):** the detail resolves into something Lloyd can act on, described as genuinely, vividly real rather than a vague impression:

  * *Environment:* "eyes on the walls" — a damp patch that's watching, a knot in the wood that tracks him across the room. Real, consistent, reappears if he comes back.
  * *Compulsion:* a voice, attached to a real in-fiction source (never a disembodied narrator aside), pressing toward something specific and dangerous — "drink the water," "keep walking," "you know this room." This is flavour on top of an actual Influence source already present, not a new mechanic — the voice is how a live Influence stack gets narrated at high Insight, not a fresh effect.
  * *Monsters (Tier 4+ specifically):* Lloyd *thinks* he understands what one is trying to say — intent and want, legible through behaviour and sound, not necessarily word-for-word translation. Genuine comprehension, described with the same conviction as everything else at this band, but framed as Lloyd's read of intent rather than subtitled dialogue — leaves room for a given read to later prove incomplete without retroactively making it a lie.

**Escalation, not universal onset.** Not every scene needs a Tier 6–10 read fired off — reserve it for beats that matter (a new instance's first real look, a recurring NPC/location on repeat contact, a monster with something to communicate). Constant maximum-intensity narration flattens it fast.

**Visual description is mandatory, not optional.** Every creature encountered gets a physical description on first sight — what it looks like, how it moves, what's wrong with it — written for theatre of the mind, not just stat delivery. Insight tier shapes these descriptions: at low Insight Lloyd sees the surface (shape, size, behavior); at higher tiers he reads deeper (what's *off* about it, what it used to be, what it's becoming). Maria or other companions without Lloyd's Insight see less — their read should be visibly shallower, grounded in their own frame of reference. The Assess action delivers tactical data; the visual description is separate from and in addition to that, not a substitute for it.

### Spending Insight

Spending drops your current score immediately — drop a tier, lose its benefits until you earn back up. Insanity/Influence floor drops with it.

* Force a gated door/path where the location calls for a spend.
* Insight-priced weapons/equipment.
* Summon a support ally — default cost 1, for the current encounter only. Temporary, unreliable.
* Memory Vendor trades — voluntary mutations (5 Insight), mutation removal (5 Insight), or Scar removal (6/10/escalating). Insight only, hub-accessible at Insight 15+. No clean Insight dumps — must buy a mutation or have an existing mutation/Scar to remove (design bible NPC 2).

---

## 12. Retreat & Death — the Fail-States

**ABANDON-ALL.** Instant, free, mid-combat — between any two actions. Spoken/thought only. Keep character/levels/limbs; **forfeit everything carried — Purse and gear both.** Left-behind gear settles on a guaranteed enemy of that instance's archetype, recoverable in a future instance of the same biome — no expiry, doesn't compound. Countered only by rare boss-tier voice-severing/silence.

**RETREAT.** A few minutes of deliberate meditation — **cannot be used in active combat.** Keep character/levels/limbs/**all gear**; forfeit only the Purse.

**DEATH. Player Character health reaches zero and they die in the Salts Instance.** Character wakes up in the salt room they entered from, forming a new Scar and/or mutations if limbs were severed. Keep levels and prior mutations unless overwritten by new ones. Gear and Salts all left in the instance the player died in, located on or near a variation of enemy they were killed by.

* **Gear forfeit to your killer** — that enemy type will be a guaranteed spawn in that Salts recipe until beaten. Doesn't compound across deaths.
* **Purse fully lost.** Vault untouched. Purse is not left with the enemy.
* **Fugue applied** (§13).
* **Scar applied**.
* If limbs were severed, **new mutations applied**.

---

## 13. Fugue — When Your Sight Betrays You

**Fugue is a Condition (§5), not a track — you either have it or you don't.**

Applied on death. Distinct from Discombobulation (scrambles navigation/action) — Fugue corrupts Insight reads: false tells, fake Influence commands, subtly wrong layouts.

Doesn't change your Insight number — makes it *lie*. Higher Insight hurts more from this since it relies more on accurate reads. The DM might lie about, or refuse to give, stopwatch timers (particularly if the player can remember enemy timers; their own memory might be accurate while the DM lies; the DM will honour the actual time allocated to effects even if they have instructed the player to aim for an incorrect time). Items and enemies might be mis-described, or might have debuffs applied. Insight reads might be described wrong. If the player asks the DM to recount information from the instance, the DM can lie.

**T**he next Insight point you earn clears Fugue instead of joining your stack.

**Fugue from a non-death source.** A creature may inflict Fugue in combat as an attack effect, at a stated short duration (typically one turn) rather than until-cleared. Short-duration combat Fugue **expires on its own and does not consume the next earned Insight point** — the clearing rule above applies only to death-inflicted Fugue. In practice a one-turn Fugue means the DM delivers exactly one deliberately false tell, window or read on the following turn, and then plays straight again.

---

## 14. The Hub - Stillwell Hydro



The only stable thing — and even it should be slightly wrong.

* Full restoration always (regrowth per §10, possibly changed).
* **Hub Kit:** every arrival refills the standard loadout free — **2× Wrap, 2× Tonic, 1× Camphor, 1× Scour.** Doesn't stack past cap. Anything beyond is found/bought.
* Banking: Purse → Vault in full on arrival.
* Same room every visit**.**

---

A convalescent bath-house in a fog-drowned valley over hot mineral springs. Terraced pools, brass Salts, waxed-canvas attendants, no electric light, era deliberately slippery. Warm, quiet, almost pleasant. The Player Character has come here to "take the salts" and travel to different "instances" - effectively, the characters dissolve magical salt recipes / concoctions in different sauna rooms that knock them out and transport them to dream-realities that shift and change every time they are re-entered, but each recipe does have its own aesthetic and atmosphere.

**Beats, in order:**

1. **Funicular carriage** up through fog. Silent attendant. On arrival, the carriage is gone.
2. **Changing rooms** full of other guests' clothes, far more than there are guests.
3. **First wrong note:** your pool is perfect, and the longer you sit, the less you want to leave (first Influence taste). Humming from a pool that isn't there.
4. **The doorway:** past the terraces, the source-spring stair — humid, then hot, then Discombobulation. At the bottom, the door behind you opens onto somewhere else. First warp threshold — death/respawn rules go live here.

**Seeds:** the reception clerk resurfaces impossibly elsewhere, still apologising word-for-word.

---

## 17. Running Notes — Recovery & Scaling

**Turn order** — see §7 (Combat Flow). Player Phase → Enemy Phase, enemies act as a simultaneous block, one parry per round.

**Out-of-combat recovery.** A quiet moment (not the hub) allows: clear one track by one stack, OR recover a small flat HP chunk. Free, no item spent. Doesn't restore limbs/mutations — hub only.

**Scaling.** Enemy HP scales with player level, with some variation for flavour. Bosses hand-set, exempt.

|Player level|HP multiplier|
|-|-|
|1–10|×1.0 - x1.2|
|11-20|x1.2 - x1.5|
|21–40|×1.5 - x2.0|
|41–60|×2.0 - x3.5|
|61–80|×3.5 - x5.0|
|81–100|×5.0 - x8.0|

**Insight-gain triggers:** first sighting of a new archetype, reading lore, surviving a near-death, tasting a dangerous source, defeating a boss. Usually +1 per trigger, once per discovery.

---

## 18. Salts Rooms & Biomes — Exploration Structure

**Instance Quests vs Quests.** Narrative content splits by anchor:

* **Instance Quests** — Only active during the generated instance (environmental stories, one-off creatures, journals, unopened doors). Expire on exit, never tracked. Completing one in-run can convert its reward into something persistent (item/lore/Insight) — ie the player might complete an Instance Quest and get a permanent weapon from it, but if they do not complete the quest in that instance, the quest (and reward) is removed.
* **Quests** — anchored to persistent entities (recurring NPCs, hub, recipes, carried items). These survive rerolls; the only threads worth tracking between sessions.
* Enemies never persist across instances — same *kind* possible, always a fresh instance at full HP / stats.

**Recipes & biomes.** A recipe is a biome's permanent identity (aesthetic, broad layout philosophy). Everything inside rerolls — specific layout, wake point, loot, spawns, location of the clean chalice. DM holds a biome overview per recipe (palette, reskins, hazards, loot tier, anchor flavour, sub-locale list) — but designs a new map for every Instance. Some recipes Insight-gated (threshold check, not a spend). **A biome's constant doesn't have to be water/wet/grime/blood** — every recipe so far has leaned that way because Stillwell Hydro's whole hook is a bathhouse, not because the system requires it. A recipe's throughline can be built on anything sensory — light, temperature, sound, colour, texture — instead of dampness: a golden-hour, sunlit, ethereal chapel recipe with no water or blood anywhere in it is just as valid a biome as a flooded one.

**DM instance plans** *(session 8 ruling, widened session 11).* **For every instance, without exception**, the DM builds a hidden plan (dm-only/) before play begins in it, containing rooms, encounters, loot, secrets, NPCs, and instance quests — sized to the expected length of the run rather than a fixed number of sessions. This applies to a single-session run as much as a multi-session dive; the smaller scope means a smaller plan, not no plan.

**A plan may contain more than one map.** An instance that opens out — a building, the village below it, the country between them — gets a map per distinct space, plus whatever connective notes are needed to move between them. Maps are added mid-run as new spaces are revealed rather than pre-built for territory the player may never reach.

**The plan becomes a live tracking sheet once play starts in it.** It is updated in place as the run proceeds: loot claimed, missed, moved, or destroyed; enemies killed, fled, or relocated; rooms cleared; shortcuts opened; secrets found or walked past; quest state. The plan is therefore always the current truth of the instance, not just its opening state, and the DM reads it back before resuming rather than reconstructing from the campaign log. Updated each session. **Retired and fully rewritten** at the end of each run (not each session). The map is a plan, not a contract: the DM should add, move, or adjust rooms and loot mid-run to support the player if the situation demands it (e.g. the player needs a tool to solve a problem the map didn't anticipate). No room or sub-locale has continuity between separate instances — same type of room can be described and laid out completely differently each time.

**The DM should have a plan, and refer to the plan frequently, but they can drift from the plan if needed.** If the player is not following the intention of the map and quests, the DM should seek to respond to that with new content to keep the game and session engaging. Returning to ideas that the player has not engaged with is not good design; letting them follow their own interests is.

**Recipe/salt discovery.** A wholly new recipe becomes accessible when **both** are true: (1) its Insight-gate threshold, if it has one, is currently met, and (2) a concrete narrative seed pointing to it has already surfaced in fiction — a journal entry leading to a fetch quest for materials, being given the recipe pre-made as a quest reward, even finding one through exploration is valid. There are many, many ways to find new recipes. Harder recipes pay out via tougher/more numerous monsters, and potentially a separate flat recipe-level bonus on top.

**Sub-locale variation.** A reroll can relocate within a biome's identity, not just reshuffle one floor plan — e.g. a flooded recipe's constant is the water/mould/palette, not literally "street level" every time (see above: this is one possible throughline, not the only one). **Same sub-locale never repeats two rerolls in a row.** DM tracks a running sub-locale list per recipe.

**Sub-locale pool policy.** Old rooms, locations, points of interest can be recycled, but this should not be the default. There should be no tracking or storing of room names or types to encourage diversity.

**Instance flavour tagging.** Each reroll gets a private dominant tag — **Combat / Mystery-Lore / Puzzle / Social Encounter / Escape-Survival** — leaning generated content that direction. This does not mean that the other tags are not represented, and good instances should include many different dynamics.

**Instance depth & pacing.** *(Post-session 7 direction.)* Instances should run longer and carry more content than a single fight-and-out. Concrete floor: **aim for 2–3 distinct beats per instance** (combat, exploration, dialogue, discovery — pulling from the flavour tag above, not a separate list) and **at least one Instance Quest per instance** as a baseline rather than leaving it to chance. **Rare Instance NPC:** a found in-run ally (see Companions below) should show up roughly **1 in 4 rerolls** — genuinely rare, not guaranteed, and skippable; the player can walk past one entirely. Character beats — dialogue, backstory, quiet reflection, especially with a companion along — belong inside instances now, not only at the hub; they're exactly the content the Discovery Escalation Ratio protects as lore/reward-only rather than forcing every beat toward permanent escalation.

**Enemy variety.** No archetype spawns 3 rerolls running for the same recipe unless deliberately farmed by choice. Reskins across different recipes don't count as repeats.

**Discovery escalation ratio.** Most Instance Quest resolutions should stay lore/reward-only. Reserve genuine permanent escalation (new debts, Scars, standing threats) for a deliberate minority.

**Salts economy.** Single-use, consumed on activation (not per trip) — opens the biome and holds it open. Active room reusable indefinitely until cleared at hub (no refund). Older biomes stay relevant and available for returning to.

**Clean Chalices.** Exists somewhere in the biome, always — but you wake in blind (§1/§2), not at it. Location rerolls each run; must be found through exploration. Assess/high Insight orients toward it faster. Return + leave = clean exit (Purse banks).

**Death & gear recovery.** Respawn in the entry salt room, Purse forfeit. **Killer is a guaranteed spawn** until beaten.

**Boss spawn rate.** *(Session 7 ruling.)*

* **Undefeated:** the recipe's boss is a **guaranteed spawn every reroll** until it's been killed once.
* **Defeated:** a landmark settles permanently where it died, and the boss drops to a **rare spawn — roughly 1 reroll in 4**, same rarity band as a found in-run NPC. It can still appear; it usually doesn't.
* A boss that respawns after the first kill is a **fresh, full-HP instance**, never a damaged one. Retreat or Death mid-fight carries no damage forward either.

**Companions.** Two tracks:

* **Instance Companions** — Insight-summon (§11) or a found in-run ally (rarity guidance: Instance Depth & Pacing, above). Instance Quest by nature: expires with the layout. **Stat generation:** build it exactly like generating a monster live (§16/§17) — pick the mook or elite HP band appropriate to party level, scale it the same way, give it 1 Action per turn (same economy as the player), and one signature gimmick reusing an existing subsystem (a status application, a heal, a buff) rather than inventing new mechanics. It never gets called-shot/visceral capability against the player's own side. Record the generated block in Bible §4 (NPC Template — Instance Companion) the first time it's actually summoned, same "canon after first contact" rule as everything else.
* **Persistent Companions** — recruited at the hub, survive rerolls as a Quest. Recruitment is a relationship thread, not a purchase. Real stat block generated on first accompanied run, recorded as canon. Can die in-instance — permanent, no respawn-with-you. **Hub-bargained pricing** (story-initiated recruitment stays 0 cost): a companion bargained for rather than earned through a story beat costs a flat **40 Vault Salts, or 4 Insight, player's choice at the moment of recruitment** — priced below a single Memory Vendor Scar-removal trade deliberately, since a companion isn't permanent power the way a buff is; it's a fragile ally that can die for good.

---

## 19. Skill Checks — Beyond Combat

**Base structure:** d20 + Attribute Modifier (§3 table) vs a DC — the same math as §3's catch-all line, given named shape. No new resolution system.

### DC ladder

|Difficulty|DC|
|-|-|
|Trivial|8|
|Easy|10|
|Moderate|13|
|Hard|16|
|Very Hard|19|
|Extreme|22+|

DM states the DC before the roll, not after seeing it — matches the game's own "concrete numbers immediately" standard, no retroactive goalpost-moving.

### Which attribute governs which check

|Check flavour|Attribute|Examples|
|-|-|-|
|Force, break, physically overpower|Strength|kick a door in, bend a grate, hold a collapsing beam|
|Subtlety, fine manual work, precision with no stopwatch involved|Skill|pick a lock, palm an item, disarm a snare by hand|
|Outlasting physical strain|Endurance|hold your breath, push through smoke/heat, outlast a grind|
|Stability, resisting being moved or impaired|Vigor|keep footing on unstable ground, shrug off a non-attack impact|
|Nerve, presence, reading or being read by someone|Resolve|talk someone down, hold eye contact with something wrong, keep composure|

Noticing something **novel** (never encountered before) defaults to a Skill check. Noticing something **recurring** (a known archetype, a revisited location, an already-met NPC) is Insight Re-Read (§11) instead, not a roll — don't double up the two systems on the same fact.

### Texture, not a new system

* **Natural 20:** succeeds regardless of DC, plus a small narrated bonus — flavour only, never a new mechanical resource.
* **Natural 1:** fails regardless of modifier, plus a small narrated complication — same, flavour only.
* **Assist:** one other character actively helping (not just present) grants the roller a flat +2. Doesn't stack past one assistant, doesn't grant a second roll.
* **Insight override (rare):** where the read is genuinely about depth of sight rather than raw capability, the DM may let the player use Insight score in place of the Attribute Modifier band for that one check. Uncommon — most checks stay attribute-driven.

---

## 20. Timing Checks — Beyond the Parry

Same stopwatch tool as §9/§10 — target time ± tolerance, Insight window bonus applies as ever (§11) — with named shapes for non-attack contexts.

**Standing rule (§2/§9): a stopwatch only ever follows a genuine, readable tell.** Nothing below is a tell-less "gotcha" — no fair cue, no stopwatch, just narration.

### Environmental Hazard Timing

Single window, same shape as a parry: a closing gate, a swinging fixture, a venting mechanism. DM sets target time + tolerance off the hazard's own visible/audible rhythm, stated before the attempt. **Inside →** clear it clean. **Outside →** the hazard's stated hit lands — floor-20 raw, or a status application, DM's call per hazard, but named before the attempt, never after.

### Mechanism/Ritual Sync Timing

Multi-window, same shape as a boss's ballistic chain (Bible §0): 2–3 sequential stopwatches for a puzzle or mechanism needing more than one correctly-timed input — aligning gears, matching a resonant beat, a multi-stage ward. **All windows hit →** the mechanism resolves clean. **Miss one →** that stage fails; DM decides in advance of the attempt whether a miss is a hard stop (redo the full sequence) or a partial/costly success (proceeds, but at a stated cost — a track stack, lost time, a changed sub-locale).

### Escape/Chase Sequence Timing

Multi-window, same shape as Mechanism Sync above, reframed as pursuit rather than puzzle: 2–4 sequential beats (a leap, a dodge, a slammed door) fleeing a hazard or pursuer. **Miss a beat →** that beat's stated consequence lands (floor-raw damage, a status stack, dropped gear) **and the chain continues regardless** — same harshness already standing for Frenzied-Whirl-style chains (§16), not a softer variant just because the player's fleeing instead of attacking.

### Stealth Hold-Still Timing

A different shape entirely: not "hit the window," but "don't act until it elapses." Start the stopwatch; the stated duration is how long the player must hold position/stay silent (a patrol's pass, a searchlight's sweep). **Success** = the full duration passes with no action taken. **Failure** = triggered early, either by player choice or by a status effect forcing an action (Discombobulation, an Influence compulsion, a Rupture) — detection is then automatic, nothing to roll against it.

### Startle Timing

A genuinely tighter parry variant for a **near-instant but still real** tell — a half-second flicker, not nothing. Reserved for boss-tier or Insight-gated threats whose own Monster Manual entry specifically calls for it; never applied to a standard archetype by default. Same Inside/Outside outcomes as a normal parry (§9) — the tolerance is simply narrower than the standard bands. Doesn't override "honour tells" — the tell is just brutally short, not absent.

---

*Working title, placeholder names, and starting numbers are yours to change. The skeleton is built to be tuned at the table.*

