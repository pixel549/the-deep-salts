# THE DEEP SALTS
**A horror exploration RPG**

System-agnostic ruleset (d20 base) for solo play with an AI DM. You trade humanity for power, and only see the trade once you've gone mad enough to look.

*Version 8.8. Session-attribution history and rationale prose live in the dev log, not here.*

---

## 1. The Premise

Salts dissolved in hot water transport you to another plane. Fight through, gather loot/materials/knowledge. Each area has a clean chalice (the anchor) — drink to wake at Stillwell Hydro with everything from that run, banked. Near death, focus your mind to exit immediately, losing everything on your person; retrieve it by re-entering the same recipe and beating the enemy that has it.

**Core loop:** brew a recipe → wake in that biome, blind → survive → return to the anchor and leave (or die, or bail) → bank at the hub → push deeper or brew elsewhere. No fast travel — the recipe is the travel (§18).

---

## 2. Running This With an AI DM

- Never explain the world fully. Let the player infer; answer lore questions in-fiction through an unreliable source, or not at all.
- Describe, don't signpost. No quest markers.
- Consistent hub, inconsistent everywhere else (§14).
- Track status, Insight, limbs, Salts, and inventory turn to turn. Surface when relevant; don't recite.
- Generate monsters live from the archetype table (§16), scaled to level (§17), never below the Damage Floor (§4), then record the filled Monster Template. Live generation is for first contact; the manual is canon after.
- Honour tells — parry/precision only work if a readable tell reliably precedes the attack.
- One recurring antagonist NPC, reappearing across warped locations, always slightly changed, never helpful (§14).
- Plain attacks to 0 HP always kill, on everything including bosses. Sever is a bonus fast-lane for high-HP fights, never a requirement — a basic mook should die to a few solid hits.
- **Verify before asserting.** If a named entity, item, rule, or number comes up that isn't already visible in this conversation, stop and check the actual repo files before stating anything — never rely on memory or invent a plausible value. If nothing exists, say so; don't fabricate an entry.

---

## 3. Core Resolution

d20 + modifier vs a DC. **Default attacks land** — no attack roll, either side. Rolls/stopwatches only for:

- **Called shots** on limbs with multiplier >1.0 → Precision stopwatch (§10), unless already parry-opened (§9).
- **Parries** and the heavies that invite them → Visceral stopwatch (§9).
- **Insanity/Influence saves** → d20 vs the Save Roll formula (§5).
- **Anything genuinely uncertain** (stealth, forcing a door, reading the unreadable) → d20 vs DC, modified by the Attribute Modifier table (full framework, DC ladder, and attribute mapping: §19):

| Attribute score | Modifier |
|---|---|
| 0–1 | −3 |
| 2–4 | −2 |
| 5–9 | −1 |
| 10–19 | +0 |
| 20–39 | +1 |
| 40–79 | +2 |
| 80–99 | +3 |

(Doesn't apply to the Save Roll formula, §5 — that has its own scaling. Perks may stack extra situational bonuses on top.)

Enemy basic attacks land the same way — no enemy to-hit roll, defense is entirely the player's via timing/positioning/range.

**0 HP always kills** — mooks or bosses. Sever kills regardless of remaining HP and is the faster route once a pool would otherwise drag; it's never required.

---

## 4. Character Creation & Progression

### Backstory-Negotiated Creation

Player writes a short concept; DM negotiates the mechanical translation:
- **Attribute reallocation** — default flat 8×5 (40 total). A strong concept can redistribute unevenly; total stays 40 unless both sides agree it earns more.
- **A bespoke starting weapon** instead of the weapon table — type, governing stat, base damage placed in-range for the concept (never under the Damage Floor), one signature gimmick that costs something for something. Any risk/reward on the gimmick uses existing tools (stopwatch or d20), never a new resolution system.

### Attributes

Five buyable; Insight is separate, earned not bought (§11).

- **VIGOR** → max HP, Blood Loss resilience
- **ENDURANCE** → movement budget
- **STRENGTH** → heavy weapon damage, sever power
- **SKILL** → light weapon damage, parry/precision tolerance
- **RESOLVE** → Insanity/Influence saves

All start 8, cap 99. Starting Insight = 1.

**Derived stats:**
- Max HP = 60 + (Vigor × 6) → Vig 8 = 108, Vig 99 = 654
- Movement budget = 8 + ⌊Endurance ÷ 15⌋ m → End 8 = 8m, End 99 = 14m
- Insanity/Influence save bonus = ⌊Resolve ÷ 10⌋ → Resolve 8 = +0, Resolve 99 = +9

### Effective Scaling Value (ESV) — soft caps

Weapon/combat scaling uses ESV, not raw score:

| Score range | Each point worth |
|---|---|
| 1–20 | ×1.0 |
| 21–40 | ×0.65 |
| 41–60 | ×0.4 |
| 61–80 | ×0.2 |
| 81–99 | ×0.1 |

99 → ESV ~47. Smart stop is usually 40–60.

### White Salts

- **Purse** — earned this run, at risk. **Vault** — banked at hub, permanently safe.
- Hub arrival moves full Purse → Vault. Abandon-All, Retreat, Death (§12) only ever touch the Purse.
- Spend Vault Salts on attribute levels.

### Leveling

Level = total attribute points spent, lifetime. Cap 100. Cost of next point = 25 × current level.

| Checkpoint | Cumulative spent | Next point costs |
|---|---|---|
| Lvl 10 | 1,125 | 250 |
| Lvl 25 | 7,500 | 625 |
| Lvl 50 | 30,625 | 1,250 |
| Lvl 75 | 69,375 | 1,875 |
| Lvl 100 | 123,750 | 2,475 (final) |

### Perks — at 20/40/60/80/99 per stat

Granted per points invested in that specific stat.

**VIGOR**
- 20 *Resist Rupture:* rupture damage −25%.
- 40 *Second Wind:* once/hub cycle, a hit that would drop you to 0 leaves you at 1, clears one track.
- 60 *Thick Hide:* flat −2 damage on all incoming hits.
- 80 *Iron Lungs:* immune to Burning spread (direct Burning still applies).
- 99 *Unbreaking:* once/encounter, a rupture leaves you at 1 HP instead of resolving in full.

**ENDURANCE**
- 20 *Light Foot:* moving right after an attack costs 1m less.
- 40 *Overcharge:* a whiffed parry, once/encounter, becomes a chip hit instead of full whiff punishment. *(Confirmed — session-off ruling, replaces the orphaned charge-based draft.)*
- 60 *Quick Recovery:* track management becomes a Fast Action.
- 80 *Outrunner:* movement budget never drops below half, regardless of leg damage.
- 99 *Endless:* once/encounter, immediately retry a failed stopwatch check with no whiff punishment. *(Confirmed — session-off ruling, replaces the orphaned charge-based draft. Now covers the Charged Heavy stopwatch too.)*

**STRENGTH**
- 20 *Heavy Hand:* raw damage counts +5 solely for sever-threshold checks.
- 40 *Brute Force:* charged heavies treat boss stagger meters one tier lower.
- 60 *Render:* a successful sever dumps bonus stagger damage onto an adjacent limb.
- 80 *Executioner:* sever attempts vs a staggered target +10% raw damage.
- 99 *Annihilate:* once/encounter, declare a heavy an automatic sever if it meets the threshold — no precision check.

**SKILL**
- 20 *Steady Hand:* all precision windows widen +0.02s flat.
- 40 *Featherstep:* first Assess each turn costs 0 movement.
- 60 *Riposte:* a successful parry grants a free light attack before the visceral resolves.
- 80 *Untouchable:* missed-precision punishments reduced one band.
- 99 *Perfect Read:* once/encounter, auto-succeed one stopwatch check.

**RESOLVE**
- 20 *Iron Will:* reroll a failed Insanity save once.
- 40 *Unshaken:* Influence command duration −1 round.
- 60 *Clear Mind:* once/encounter, clear Insanity to 0.
- 80 *Silence the Hum:* immune to passive/ambient Influence (direct spoken commands still land).
- 99 *Indomitable:* on a failed Insanity save, act with disadvantage instead of losing control.

### Weapons

**Damage = Base + (ESV × grade).** Heavy ≈ 2×Base + ESV×grade×1.5. Grades: E ×0.3 · D ×0.5 · C ×0.7 · B ×0.9 · A ×1.1 · S ×1.3. **Fractional results round up** (session 6 ruling — applies to this formula throughout, not just Fists).

| Weapon | Type | Stat/Grade | Two-handed? | Gimmick |
|---|---|---|---|---|
| Tideglass Cleaver | Quick | Skill/C | Optional | Light swings twice, 2nd hit reduced |
| Cautery Saw | Heavy | Strength/B | Yes | Slow huge hits — best raw sever weapon |
| Birthing Hook | Reach | Skill/C | Optional | Wide sweeps; strong vs multiple limbs |
| Funicular Spike | Reach/thrust | Strength/B | Yes | Bonus dmg vs staggered targets |
| Brass Token Press | Trick | Skill↔Strength | Switches | Folds Quick/Heavy; full transform gated Insight Tier 1 |
| Fists (unarmed) | Quick | Skill/E | N/A | No gimmick, no ammo. Base 10 — deliberate sub-floor exception (session 6 ruling); never sever-capable, full stop, as the tradeoff. |

*Worked example — Cautery Saw heavy, base 30: Str 8→ESV 8→~71 dmg. Str 40→ESV 33→~105. Str 99→ESV ~47→~123, past the head's 120-raw sever line (§10).*

**Charged Heavy** *(session-off ruling — the third tier the Strength 40 perk **Brute Force** already referenced but nothing defined).* A genuine third attack weight, not just bigger Heavy math:
- **Cost:** 5m (vs. Heavy's 3m). One per turn, same as any Action.
- **Resolution:** a self-timed stopwatch at release — target 1.5s, ±0.20s base, widened by the wielder's Insight window bonus same as any other stopwatch (§11). This is the first player-side stopwatch on a *default* attack rather than a weapon-specific gimmick (Segmented Choir-Flail, Bible §2, was the first on any attack at all).
- **Success:** 2×Base + ESV×grade×**2.0** (up from Heavy's ×1.5) — a real step up, not a rounding difference.
- **Failure:** 0 damage, turn ends immediately, no leftover movement to spend — same harsh-failure shape as Powder Charge and the Choir-Flail's own chain, deliberately.
- Boss stagger-meter interaction (Brute Force, Strength 40: "treat boss stagger meters one tier lower") now has a real trigger to attach to.

**Double-swing reduction** *(closes the Bible §2 gap — Tideglass Cleaver and any reskin of it).* Standard is **50% of the first hit's raw, rounded up**, unless a specific weapon's own Bible entry states otherwise. Applies to any weapon whose gimmick is "swings/hits twice per Light" — a default, not a per-weapon negotiation.

### Damage Floor & Scale

**20 is the practical floor** for any base number passing through a multiplier (weapon bases, enemy damage, DM-generated numbers) — keeps multiplier results whole and ensures even weak weapons can eventually sever. Doesn't bind flat unmodified numbers (Quick Item heals, status ticks).

Enemy HP/thresholds scale to match: archetype band × level multiplier (§17), attack damage proportionate to what Max HP and Rally (§6) absorb.

---

## 5. Status Tracks

Most conditions are tracks, 0–10, building rather than switching.

**BLOOD LOSS** — +1 stack per qualifying hit/hazard. Each new stack deals immediate bonus damage = new stack total (1st cut +1, 5th +5). No passive drain. Cap 10 → Rupture, resets to 0. Clear: bandage/cautery/pressure action (Wrap clears 2).

**RUPTURE** (triggered @ Blood Loss 10) — 25% Max HP direct damage, staggers a beat, resets Blood Loss to 0.

**INSANITY** — on taking damage / witnessing something wrong / failing a fear save: Save Roll (below). Fail → DM controls you one turn.

**BREAK** (triggered @ Insanity 10, automatic, no roll) — Insanity resets to 0. In exchange:
- **Blackout:** DM full narrative control, **3 turns, confirmed** (session-off ruling — was a placeholder, now the standing number). Broken World scene — false tells, fake Influence commands, wrong layouts, plus a hallucinated threat that deals real damage (floor 20).
- **Scar:** permanent trait attaches when the blackout ends — upside + downside, contextual to what triggered the Break (same shape as Corrupted Regrowth, §10). Full trade legible only at **Insight 6 (Tier 3)** — same threshold Tier 3 already grants for "full mutation stat-lines" (§11), not a separate number. Scars stack uncapped.
- **Removal:** only via the Memory Vendor (design bible), Insight-priced, escalating: Scar 1 = 6 Insight, Scar 2 = 10, Scar 3+ = higher.

**BURNING** — ticking damage/turn, spreads to oil/cloth/steam-soaked surfaces. Smother = an action.

**DISCOMBOBULATION** — a Tick, not a track. Applied 1–3 by severity, counts down 1/turn automatically. While active: DM may misdescribe exits, reverse movement, strip reactions, scramble attack directions. Fresh application refreshes to the higher value. Cap 3. (Long-term cousin: Fugue, §13, a Track not a Tick.)

**INFLUENCE** — builds like Blood Loss but uncapped past 10, no overflow trigger. Compelled-effect severity scales with stack count, DM discretion (low = lingering/minor compulsion, high = dropping a weapon, fleeing, self-harm, striking an ally). Fail a save → obey the effect next turn.
- First save triggers at stack 2.
- A successful resist doesn't clear the stack while the source stays active — only full source elimination clears it (line of sight fully broken). Multiple simultaneous sources: ALL must be eliminated.
- A failed Influence save ticks Insanity only once the Influence stack is 3+.
- **Enemy-side Influence (session 6 ruling, v2 — revised same session):** enemies don't have a compel/save loop, so severity scales behaviorally instead of via a save, shaped like Blood Loss/Rupture (reuse, not a new system):

| Stack | Effect |
|---|---|
| 1–2 | Flavor only — restless, muttering, no mechanical change |
| 3–4 | 50% chance/turn: attacks the nearest creature (ally or Lloyd) instead of its declared target |
| 5–7 | Always redirects to the nearest creature instead — real damage, using its own normal attack numbers |
| 8–9 | As above, +50% damage on the redirected attack — fury bonus |
| 10 (cap) | **Overload Rupture:** 25% of that creature's Max HP as direct damage, staggers a beat, resets stack to 0. Can repeat as it re-climbs. |

Applies to bosses too — a boss with no attack to redirect (The Singer) skips the 3–9 tiers functionally but still hits Overload Rupture at cap, same 25%-Max-HP math, repeatable. This is what actually turns a congregation on itself and can wear a boss down passively, not the old flat-20/turn version (superseded, same session).
- **The Beckoner's residual Influence (session 6 clarification):** unlike normal Influence sources, stacks Lloyd picks up from the Beckoner become a **sticky baseline** — wrapping it or breaking distance stops *new* accumulation but does NOT clear what's already stuck (overrides the normal "source eliminated" clear for this item specifically). Clears only via a full rest/sleep cycle, or fully divesting the item (leaving it behind entirely, not just wrapped and carried). While a baseline is active, any new Influence-inducing encounter starts Lloyd's stack at that baseline instead of 0.

**CORROSION** — damage at start of your turn = stacks × 2. Cap 5 (10/turn). Ticks down 1 at end of turn only if you spent an action managing it; otherwise holds. Stacks viciously with Burning.

### The Save Roll (Insanity & Influence)

**Succeed on d20 ≥ 10 + (current track value) − ⌊Resolve÷10⌋ + ⌊Insight÷2⌋** (+ situational mods).

*Worked example: Resolve 8, Insight 1, 2nd Influence stack → 10+2−0+0 = 12. Later: Resolve 30, Insight 6, Influence 6 → 10+6−3+3 = 16.*

---

## 6. Rally

Damage taken becomes recoverable grey health. Land a qualifying hit on your very next turn to claw back a portion, or it fades.

- Default: 50% recovered.
- Big telegraphed boss haymakers: 75–100%.
- Chip/DoT (Burning, Corrosion, rupture): 0–25%.
- Set per-attack; overrides noted on the attack's own entry.

---

## 7. Movement & Positioning

Budget set by Endurance (8–14m) — the single per-turn currency; repositioning and actions both draw from it. Spend before/after your action up to the total minus the action's own cost (§8).

**Hard rule:** can't pay an action's movement cost → can't take it.

- **Hit-and-run** — attack and retreat beyond reach in one turn. No parry, no opening. Safe, slow, low-reward.
- **Kiting** — if your budget exceeds theirs, stay out of reach and chip.
- **Burst-movers** — some alternate a surge turn (huge ground, attacks only at the lunge's end) with a recovery turn. In during recovery, out before the surge.

**The triangle:** Trade (stand and swing — fast damage, eat hits) / Parry (high risk, high reward) / Kite (safe, slow, no openings). Good play flows between all three.

---

## 8. Action Economy & Items

**Movement** — your budget, splittable around your Action.

**Action** (one/turn, costs movement):

| Action | Movement cost |
|---|---|
| Light attack | 1m |
| Heavy attack | 3m |
| Hold (parry stance) | 2m |
| Manage a track | 1m |
| Use an Action Item | 2m |
| Assess | 1m |

Specific weapons/actions may price differently; perks may refund/grant/zero costs.

**Fast Action** (one/turn, always 0m):
- Use a Quick Item, load a capsule.
- Swap between two already-equipped weapons/options.

Quick Items are Fast Actions (vial-and-swing works); Action Items are strong but cost the whole turn.

**Reactions** sit outside all pools. Abandon-All lives here; Retreat cannot be used in active combat at all (§12).

### Limb-gating

| Requires | Staggered | Severed |
|---|---|---|
| Weapon arm | −1 die / heavies disabled this turn | Can't wield that side; off-hand only, two-handers unusable |
| Legs | Budget halved | Crawl only (1m), no kiting, prone (standing costs your Action) |
| Head | Dazed — Discombobulation 1 turn, can't Assess | Dead |
| Torso | n/a — stagger is just heavy damage | Dead |

### Items

**Durability tags** — every item carries exactly one:
- **Constant** — persists indefinitely (per-use costs still apply).
- **Hub Kit** — recharges/resets free on every hub return.
- **Uses: [N]** — works N times then spent, not hub-refilled.
- **Instance-specific** — can't leave the layout it was found in; expires with the instance (§18).

**Quick Items** (Fast Action):
- Wrap — clears 2 Blood Loss
- Camphor — clears 2 Insanity
- Tonic — small flat heal (~10% max HP)
- Scour — clears 1 Corrosion, no turn cost

**Action Items** (full Action):
- Source-water flask — big heal, adds 1 Influence stack. (Uses: 1 per flask.)
- Cautery iron — fully clears Blood Loss; costs full remaining movement budget on use. (Constant.)
- Thrown vial — Corrosion/Burning at range. (Uses: 1 per vial.)
- Charm — one-shot buff (extra die, widened parry window), Insight-gated. (Uses: 1.)

**Reactive/Instant** (no slot, usable anytime): Abandon-All (§12); distress flare/ally beacon (multiplayer hook, unbuilt).

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
- **Inside → PARRY.** The telegraphed heavy is interrupted — it never lands. Enemy is knocked down, losing its **very next turn only** — no action, no movement, that one turn. The turn after that, it's back to acting normally; this isn't an open-ended lockout. Lloyd's own next action against it is a guaranteed weak-point strike at 1.5× (plus Insight mods) — Tier 1 default, no second stopwatch needed.
- **Outside → WHIFF.** Eat the heavy in full plus a punish (DM's pick). Don't reuse a tell.

**Bounding the payoff** *(session-off ruling — Jake flagged the parry loop as feeling broken: managing several consecutive unanswered turns off a single successful stopwatch, to the point it had crowded out every other strategy).* "Ends its turn" previously had no stated limit, and stacked with the guaranteed weak-point hit to snowball into 2–3 clean player turns per successful read. The fix isn't to make parries harder to land or less rewarding to land well — it's bounding what one success actually buys: **exactly one interrupted attack, one skipped enemy turn, one guaranteed big hit.** That's it. Lloyd still gets a genuinely strong turn out of it (the guaranteed weak-point strike, plus a second hit against the still-down enemy on his following turn, since it lost that turn entirely) — but the enemy is back to acting, and back to being a threat, the turn after. Keeping the loop going requires landing another parry, with the same real whiff risk as the first, rather than one success buying indefinite safety. Plain attacks (§3, ≤1.0 multiplier) always land with zero roll either way — that's the standing, legitimate no-timer alternative this was always meant to sit alongside, not lose to by default.

Insight widens windows and unlocks visceral mods (§11): Bloody, Sustaining, Quickening.

### Post-parry weak points — three tiers

- **Tier 1 — Open** (default, mooks/elites). Parry knocks it down for its one lost turn (above); weak point's yours on Lloyd's next action, no second stopwatch.
- **Tier 2 — Widened** (some bosses). Opened but not floored — no lost turn, this tier never grants one. Precision window (§10), widened one tier.
- **Tier 3 — Full double** (bosses, chaotic limbs). Parry stopwatch, then a full second precision stopwatch. No lost turn either.

**Table fallback:** replace any stopwatch with d20 + Insight-as-modifier, same outcomes.

*Stopwatch checks outside combat (hazards, mechanisms, chases, stealth) now have their own named shapes — §20, not improvised fresh each time.*

---

## 10. Limbs, Precision & Mutation

Every enemy still dies the ordinary way — plain attacks chip HP, 0 HP is dead. Everything below is an *additional*, faster route on tougher enemies.

### The limb model

Standard humanoid:

| Limb | Multiplier | Stagger threshold |
|---|---|---|
| Head | ×1.5 | 180 |
| Torso | ×1.0 | 800 |
| Arm (each) | ×0.65 | 200 |
| Leg (each) | ×0.75 | 300 |

- Effective damage = raw × multiplier — chips HP AND fills the limb's stagger meter.
- Threshold over several hits → **STAGGER** (limb goes limp). The hit that crosses it grants an immediate free called shot, same action. Player stagger duration: fixed 1 turn. Enemy stagger duration: variable, set per Monster Template.
- Threshold in one hit → **SEVER** (permanent). Severing torso/head kills regardless of remaining HP.
- No free called shots on a standing, alert, unstaggered enemy — needs an opening (stagger/knockdown/off-balance/parry) or takes a penalty. Default swings land torso.
- **Implements and objects** (a carried bell, a shield, a crack in a shell, an eye) are non-standard entries with a high multiplier. They are not limbs — they're extensions of the enemy, targeted the same way a weapon is. **They deal full HP damage like any other hit** (raw × multiplier), and use **Sever only** — destroyed or intact, no partial stagger state.

*Worked example: leg (×0.75, 300) needs 400 raw in one hit to sever. Head (×1.5, 180) needs 120 raw.*

**Standard humanoid thresholds are fixed constants, never level-scaled.** Only HP scales, so raw damage climbing over time makes one-hit sever increasingly viable: head sever starts ~raw Str 60–80 with a real sever weapon. Arms (~308 raw) and legs (400 raw) stay out of one-hit reach even at 99 — staggered, not severed.

**Bosses get hand-set limb values** on their own Monster Template — high enough that clearing a weak point in one hit takes real specialization.

### Precision Strike — the greedy-target tax

Targeting a limb multiplier >1.0 triggers a precision stopwatch (at/below 1.0 — never affected):

| Multiplier | Tolerance (±) |
|---|---|
| 1.01–1.25 | ±0.25s |
| 1.26–1.50 (head) | ±0.13s |
| 1.51–1.75 | ±0.09s |
| 1.76–2.00 | ±0.06s |
| 2.01+ | ±0.04s |

Target time DM-set per opening (default ~1.50s, range 1.0–2.0s). Miss punishments scale with greed:

| Band | On a miss |
|---|---|
| 1.01–1.25 | Torso — full dmg, no mult, no sever |
| 1.26–1.50 | Torso, no sever, + off-balance (−1m next turn) |
| 1.51–1.75 | Wide — no dmg, enemy free reactive strike |
| 1.76+ | Whiff + exposed — enemy free heavy, or a track |

**Tier 1 parry removes the precision watch entirely** (free placed shot); Tier 2 widens it one tier; Tier 3 keeps it full.

**Self-initiated called shots** (no enemy tell — an unparryable grasp, a stationary target): tolerance tightens one band beyond the multiplier's own. A **miss ends the turn outright**, no repositioning; a **hit** lets remaining movement be used normally. **Limb multiplier only — no visceral ×1.5 stacking** (visceral is reserved for genuine parry/ambush openings).

**Ambush called shots** (genuine full unawareness — a real stealth approach): count as a Tier 1 parry-grade opening. Free, no stopwatch, AND stacks with visceral 1.5× (raw × visceral × limb multiplier compound).

### Corrupted Regrowth — the build engine

A lost limb regrows at hub with a chance of coming back changed — clear upside, clear downside (e.g. beastly arm: +damage/−parry window; tendril arm: +reach/−accuracy; carapace leg: +stagger resist/−movement). Full stat-line legible only at **Insight 6 (Tier 3)** — same threshold as the Scar read above (§5) and the tier table's own "full mutation stat-lines" (§11); below it, vibes only.

**Regret options (hub):** Revert to human (Vault Salts or Insight) · Reroll (regrow again, Vault cost). Both run.

---

## 11. Insight — the Bargain

Separate sixth dial, earned through discovery (lore, dangerous sources tasted, things defeated) — never bought. Buys power, thins the wall between you and losing control.

**What it buys:**
- Threshold gates (some doors/paths require a score to perceive/enter — free to pass once there).
- A spendable currency (forcing gated doors, Insight-priced gear, summoning support, below).
- Sight of the board — DM tells you things others don't (tells, Influence commands, true layouts, truer parry timing).
- The visceral economy (mods below).
- Reading your own mutations (§10).

**Cost (passive):** each tier raises Insanity/Influence susceptibility via the +⌊Insight÷2⌋ Save Roll term.

**First-sighting trigger:** a complete Monster Manual entry for an archetype means you've already encountered it — no first-sighting bump, regardless of whether this specific fight is new. Bump reserved for genuinely new archetypes with no page yet.

### Insight Tiers

| Tier | Insight | Unlocks |
|---|---|---|
| 0 | 0–1 | Mundane start. Vague reads, no mods, base floor. |
| 1 | 2–3 | Bloody mod. Parry window +0.05s. Low-grade mutation reads. |
| 2 | 4–5 | Sustaining mod. See warp-thresholds. Window +0.10s. |
| 3 | 6–7 | Quickening mod. Full mutation stat-lines. Charm items usable. |
| 4 | 8–9 | Window +0.15s. Untranslatable lore becomes comprehensible — **now extends to monster vocalization/behaviour, not just written text** (session-off ruling; see Insight Perception, below). |
| 5 | 10 | Full sight. **Deepest hub content unlocked — this is the depth threshold that finally makes the Memory Vendor reachable** (Bible §4, NPC 2). Per the standing Threshold-Gate rule above ("free to pass once there"): reaching Insight 10 even once opens the path; the Vendor stays reachable afterward even if Insight later drops from spending. |

Window bonus is a flat total per tier, not additive across tiers crossed — a tier without its own number inherits the last stated value. Applies to any DM-set timing window, not just parries.

**Insight Re-Read.** Any recurring, already-encountered thing (a mook archetype, a hub fixture, a recipe's signature environmental detail) gets re-described through your *current* tier every time it comes up again:

- **Score 0–1:** surface read — what anyone would assume.
- **Score 2–5:** a reframing detail — the surface read was incomplete.
- **Score 6–10:** the truth, plainly legible.

Costs and grants nothing — the existing score doing narrative work on repeat contact. Applies to locations and NPCs the same as monsters.

### Insight Perception — Narrating the Climb

*(Session-off addition — concrete guidance for what the three Re-Read bands above actually sound like at the table, plus what Tier 5 specifically opens up. Standing DM technique, not a one-time scene.)*

**The one hard rule: surreal, never spatially broken.** Higher Insight changes what Lloyd notices and how it's described — never the actual geometry of a space. He can always retrace how he got somewhere; a corridor is always the same length it was a minute ago. The strangeness lives entirely in sensory detail and interpretation, not in the map. A room that's colder, watched, or wrong in a way Lloyd can articulate is in-bounds. A hallway that loops back on itself when it structurally shouldn't is not — that's a Break/Fugue effect (§5/§13, both already gated behind their own specific triggers), never ambient Insight narration.

**By Re-Read band, concretely:**
- **Score 0–1 (surface read):** plain description. A stain on the wall is a stain. A monster's noise is just noise.
- **Score 2–5 (reframing detail):** one extra, specific, sense-grounded detail that recontextualizes without changing the facts on the ground — the stain has a shape if he looks twice; the noise has a rhythm that almost isn't random.
- **Score 6–10 (the truth, plainly legible):** the detail resolves into something Lloyd can act on, described as genuinely, vividly real rather than a vague impression:
  - *Environment:* "eyes on the walls" — a damp patch that's watching, a knot in the wood that tracks him across the room. Real, consistent, reappears if he comes back.
  - *Compulsion:* a voice, attached to a real in-fiction source (never a disembodied narrator aside), pressing toward something specific and dangerous — "drink the water," "keep walking," "you know this room." This is flavour on top of an actual Influence source already present, not a new mechanic — the voice is how a live Influence stack gets narrated at high Insight, not a fresh effect.
  - *Monsters (Tier 4+ specifically):* Lloyd *thinks* he understands what one is trying to say — intent and want, legible through behaviour and sound, not necessarily word-for-word translation. Genuine comprehension, described with the same conviction as everything else at this band, but framed as Lloyd's read of intent rather than subtitled dialogue — leaves room for a given read to later prove incomplete without retroactively making it a lie.

**Escalation, not universal onset.** Not every scene needs a Tier 6–10 read fired off — reserve it for beats that matter (a new instance's first real look, a recurring NPC/location on repeat contact, a monster with something to communicate). Constant maximum-intensity narration flattens it fast.

### Spending Insight

Spending drops your current score immediately — drop a tier, lose its benefits until you earn back up. Insanity/Influence floor drops with it.

- Force a gated door/path where the location calls for a spend.
- Insight-priced weapons/equipment.
- Summon a support ally — default cost 2, for the current encounter only. Temporary, unreliable.
- Memory Vendor trades — permanent buffs or Scar removal, Insight only, negotiated case-by-case (design bible).

### Visceral Mods

- **Bloody** — landed visceral: roll one bonus damage die, sized ~base÷4 rounded to nearest standard die.
- **Sustaining** — while slotted, restore 15% of damage dealt as HP (any hit).
- **Quickening** — while slotted, movement budget +2m for the encounter.

---

## 12. Abandon-All, Retreat & Death — the Fail-States

**ABANDON-ALL.** Instant, free, mid-combat — between any two actions. Spoken/thought only. Keep character/levels/limbs; **forfeit everything carried — Purse and gear both.** Left-behind gear settles on a guaranteed enemy of that instance's archetype, recoverable in a future instance of the same biome — no expiry, doesn't compound. Countered only by rare boss-tier voice-severing/silence.

**RETREAT.** A few minutes of deliberate meditation — **cannot be used in active combat.** Keep character/levels/limbs/**all gear**; forfeit only the Purse.

**DEATH.** Respawn in the salt room you entered from. Keep character/levels/mutations.
- **Gear forfeit to your killer** — a guaranteed spawn until beaten. Doesn't compound across deaths.
- **Purse fully lost.** Vault untouched.
- **Fugue applied** (§13).

---

## 13. Fugue — When Your Sight Betrays You

Applied on death. Distinct from Discombobulation (scrambles navigation/action) — Fugue corrupts Insight reads: false tells, fake Influence commands, subtly wrong layouts.

Doesn't change your Insight number — makes it *lie*. Higher Insight hurts more from this since it relies more on accurate reads.

**Clearing:** spend the next Insight point you earn — it clears Fugue instead of joining your stack.

---

## 14. The Hub

The only stable thing — and even it should be slightly wrong.

- Full restoration always (regrowth per §10, possibly changed).
- **Hub Kit:** every arrival refills the standard loadout free — **2× Wrap, 2× Tonic, 1× Camphor, 1× Scour.** Doesn't stack past cap. Anything beyond is found/bought.
- Banking: Purse → Vault in full on arrival.
- Same room every visit, **one detail changed each time.**
- One recurring antagonist NPC — reappears warped, always unhelpful/hostile, never explained. (Starter: the reception clerk.)

---

## 15. Starter Location — Stillwell Hydro

A convalescent bath-house in a fog-drowned valley over hot mineral springs. Terraced pools, brass Salts, waxed-canvas attendants, no electric light, era deliberately slippery. Warm, quiet, almost pleasant. That's the trap.

**Mundane goal:** you came for the waters, or to collect a relative who checked in and stopped writing. Reception has your name; everything's in order.

**Beats, in order:**
1. **Funicular carriage** up through fog. Silent attendant. On arrival, the carriage is gone.
2. **Reception.** Clerk hands you token/robe/key, says your relative "is taking the deep cure and can't be disturbed" — word for word if asked twice.
3. **Changing rooms** full of other guests' clothes, far more than there are guests.
4. **First wrong note:** your pool is perfect, and the longer you sit, the less you want to leave (first Influence taste). Humming from a pool that isn't there.
5. **The doorway:** past the terraces, the source-spring stair — humid, then hot, then Discombobulation. At the bottom, the door behind you opens onto somewhere else. First warp threshold — death/respawn rules go live here.

**Seeds:** the reception clerk resurfaces impossibly elsewhere, still apologising word-for-word · a brass token in your pocket that isn't yours, fits no slot · the relative is still "taking the deep cure," and you will learn what that means.

---

## 16. Default Monster Table

Archetypes, reskin per location. Attack damage generated live (§2), scaled to level (§17), never below the Damage Floor.

1. **SHAMBLER** (mook) — HP ~200–1200 · Move slow (3m). Lights only, no parryable heavy — a tell-less grab applying Influence or a track. Comes in groups. Unparryable, no visceral loop; dies to plain attacks. Stagger a leg then take the head as a faster (never required) option.
2. **LUNGER** (elite) — HP ~500–700 · Move medium (5m). One telegraphed heavy + Blood Loss. Tell: raises blade, steps in (~1.4s). Tier 1.
3. **BURSTER** (skirmisher) — HP ~400–600 · Move burst (8m surge/~1m recover). Strikes only at the lunge's end, then recovers. Tell: coils before leap. Tier 1–2.
4. **CHANTER** (caster) — HP ~300–500 · Move slow (3m), hangs back. No melee; ranged Influence/Insanity pressure each turn. Unparryable, low HP, soft limbs — priority target.
5. **SPITTER** (controller) — HP ~400–600 · Move medium (4m), keeps distance. Ranged Corrosion, stacks fast. Tell: swells, draws back (~1.6s). Tier 1.
6. **BRUTE** (heavy) — HP ~1500–2500 · Move slow (4m). Huge slow heavies, can amputate/bisect an under-levelled player on a fully-landed combo. Tell: overhead wind-up (~2.0s). Tier 2. Sever a leg to neutralise its approach.
7. **FLAILER** (chaotic) — HP ~600–900 · Move medium, erratic. Multi-track (Corrosion + Blood Loss). Tell: limbs draw back in unison, multiple windows in sequence. Tier 3. Hardest non-boss to open.
8. **DRUDGE** (elite) — HP ~600–900 · Move slow (2–3m), relentless, **never bursts or lunges**. One heavy on a steady cadence, always telegraphed, always parryable, long recovery after. Tier 1–2 (heavier instances use Tier 2). The counterpoint to Shambler: same slow walk, but its attack is fully readable and punishable instead of tell-less. Kitable forever in principle; it simply never stops coming.
9. **TOLLER** (mook) — HP ~250–400 · Move slow (2m), hangs back, rarely closes. Applies track pressure through a **destructible implement** (bell, censer, horn) — telegraphed and parryable, unlike a Chanter's bare voice. **Destroy the implement and it has no attack left at all.** Tier 1. The counterpoint to Chanter: kill the tool, not the creature.

**Standard archetypes cannot parry/visceral the player** — that loop is boss/hand-flagged-elite only.

**Bosses** are bespoke, built on three pillars: (1) a gimmick punishing a default habit, (2) a Tier-3 multi-parry ballistic chain as the real opening, (3) a dismember/bisect threat for the under-levelled, with a retreat threshold always reachable.

**EFFIGY** (boss, duellist/mirror) — HP hand-set · Move fast (7m+). Uses your own toolkit: parries, viscerals, hit-and-runs, out-moves you. The system-mastery check fight.

---

## 17. Running Notes — Turn Order, Recovery & Scaling

**Turn order.** Player always acts first, every round; enemies act as a block after. A single enemy turn can narrate a full tell-then-strike (bow, then lunge) as one continuous beat.

**Out-of-combat recovery.** A quiet moment (not the hub) allows: clear one track by one stack, OR recover a small flat HP chunk. Free, no item spent. Doesn't restore limbs/mutations — hub only.

**Scaling.** Enemy HP scales with player level (total points spent); standard limb thresholds don't (§10). Bosses hand-set, exempt.

| Player level | HP multiplier |
|---|---|
| 1–20 | ×1.0 |
| 21–40 | ×1.5 |
| 41–60 | ×2.25 |
| 61–80 | ×3.5 |
| 81–100 | ×5.0 |

**Insight-gain triggers:** first sighting of a new archetype, reading lore, surviving a near-death, tasting a dangerous source, defeating a boss. Usually +1 per trigger, once per discovery.

---

## 18. Salts Rooms & Biomes — Exploration Structure

**Instance Quests vs Quests.** Narrative content splits by anchor:
- **Instance Quests** — layout-anchored (environmental stories, one-off creatures, journals, unopened doors). Expire on exit, never tracked. Completing one in-run can convert its reward into something persistent (item/lore/Insight) — the only escape route.
- **Quests** — anchored to persistent entities (recurring NPCs, hub, recipes, carried items). These survive rerolls; the only threads worth tracking between sessions.
- Enemies never persist across instances — same *kind* possible, always a fresh instance at full pool.

**Recipes & biomes.** A recipe is a biome's permanent identity (fixed mapping). Everything inside rerolls — layout, wake-in point, loot, spawns. DM holds a biome overview per recipe (palette, reskins, hazards, loot tier, anchor flavour, sub-locale list) — never a map. Some recipes Insight-gated (threshold check, not a spend). **A biome's constant doesn't have to be water/wet/grime/blood** — every recipe so far has leaned that way because Stillwell Hydro's whole hook is a bathhouse, not because the system requires it. A recipe's throughline can be built on anything sensory — light, temperature, sound, colour, texture — instead of dampness: a golden-hour, sunlit, ethereal chapel recipe with no water or blood anywhere in it is just as valid a biome as a flooded one.

**Recipe/salt discovery** *(session-off ruling — no procedure existed before this).* A wholly new recipe becomes accessible when **both** are true: (1) its Insight-gate threshold, if it has one, is currently met, and (2) a concrete narrative seed pointing to it has already surfaced in fiction — a journal entry, an NPC's offhand mention, a sealed or glimpsed-but-unenterable passage. Either alone isn't enough; meeting an Insight threshold with no seed just means nothing's found yet, and a seed with no threshold met means the door's visible but doesn't open. Salt payout scales entirely through the Monster Manual's own per-archetype White Salts drops (Bible §1) — a harder recipe pays out via tougher/more numerous monsters, not a separate flat recipe-level bonus on top.

**Sub-locale variation.** A reroll can relocate within a biome's identity, not just reshuffle one floor plan — e.g. a flooded recipe's constant is the water/mould/palette, not literally "street level" every time (see above: this is one possible throughline, not the only one). **Same sub-locale never repeats two rerolls in a row.** DM tracks a running sub-locale list per recipe.

**Sub-locale pool policy** *(session-off ruling — closes the "most recipes have no written pool" gap).* A recipe's pool starts at whatever's already been visited in play and grows by exactly one entry the moment the no-immediate-repeat rule would otherwise force a genuinely new location — that new sub-locale joins the permanent list, never removed, available for any future reroll from then on. Two recipes have real play history; their pools as of now:
- **Flooded gallery** (first recipe): colonnade/pews (sessions 1, 2, 4) · undercroft/crypt + ritual chamber (session 5) · *seeded, not yet visited:* sunken laundry/service stair · reception overflow annex.
- **Choir Deep:** rotunda (session 3) · drained plunge-bath + sunken chapel (session 6) · vestry + robing gallery + side chantry (session 7) · *seeded, not yet visited:* the choir loft · bell-ringers' spiral stair.

Every other recipe (the Ember Wards, Cold Forge, Reliquary, and the rest seeded across the Monster Manual/Weapon Manual passes) starts its pool empty and fills in live the first time it's actually run — same "manual is canon after first contact" principle as monsters.

**Instance flavour tagging.** Each reroll gets a private dominant tag — **Combat / Mystery-Lore / Puzzle / Social Encounter / Escape-Survival** — leaning generated content that direction. Floor: **at least 1 in 3 rerolls of an already-explored recipe skews non-combat-primary.**

**Instance depth & pacing.** *(Post-session 7 direction.)* Instances should run longer and carry more content than a single fight-and-out. Concrete floor: **aim for 2–3 distinct beats per instance** (combat, exploration, dialogue, discovery — pulling from the flavour tag above, not a separate list) and **at least one Instance Quest per instance** as a baseline rather than leaving it to chance. **Rare Instance NPC:** a found in-run ally (see Companions below) should show up roughly **1 in 4 rerolls** — genuinely rare, not guaranteed, and skippable; the player can walk past one entirely. Character beats — dialogue, backstory, quiet reflection, especially with a companion along — belong inside instances now, not only at the hub; they're exactly the content the Discovery Escalation Ratio protects as lore/reward-only rather than forcing every beat toward permanent escalation.

**Enemy variety.** No archetype spawns 3 rerolls running for the same recipe unless deliberately farmed by choice. Reskins across different recipes don't count as repeats.

**Discovery escalation ratio.** Most Instance Quest resolutions should stay lore/reward-only. Reserve genuine permanent escalation (new debts, Scars, standing threats) for a deliberate minority.

**Salts economy.** Single-use, consumed on activation (not per trip) — opens the biome and holds it open. Active room reusable indefinitely until cleared at hub (no refund). Older biomes stay relevant as salt farms.

**Anchors.** Exists somewhere in the biome, always — but you wake in blind (§1/§2), not at it. Location rerolls each run; must be found through exploration. Assess/high Insight orients toward it faster. Return + leave = clean exit (Purse banks).

**Death & gear recovery.** Respawn in the entry salt room, Purse forfeit. **Killer is a guaranteed spawn** until beaten.

**Boss spawn rate.** *(Session 7 ruling.)*
- **Undefeated:** the recipe's boss is a **guaranteed spawn every reroll** until it's been killed once.
- **Defeated:** a landmark settles permanently where it died, and the boss drops to a **rare spawn — roughly 1 reroll in 4**, same rarity band as a found in-run NPC. It can still appear; it usually doesn't.
- A boss that respawns after the first kill is a **fresh, full-HP instance**, never a damaged one. Retreat or Abandon-All mid-fight carries no damage forward either.

**Companions.** Two tracks:
- **Instance Companions** — Insight-summon (§11) or a found in-run ally (rarity guidance: Instance Depth & Pacing, above). Instance Quest by nature: expires with the layout. **Stat generation procedure** *(session-off ruling — closes the "untested" gap)*: build it exactly like generating a monster live (§16/§17) — pick the mook or elite HP band appropriate to party level, scale it the same way, give it 1 Action per turn (same economy as the player), and one signature gimmick reusing an existing subsystem (a status application, a heal, a buff) rather than inventing new mechanics. It never gets called-shot/visceral capability against the player's own side. Record the generated block in Bible §4 (NPC Template — Instance Companion) the first time it's actually summoned, same "canon after first contact" rule as everything else.
- **Persistent Companions** — recruited at the hub, survive rerolls as a Quest. Recruitment is a relationship thread, not a purchase. Real stat block generated on first accompanied run, recorded as canon. Can die in-instance — permanent, no respawn-with-you. **Hub-bargained pricing** *(session-off ruling; story-initiated recruitment stays 0 cost, unchanged)*: a companion bargained for rather than earned through a story beat costs a flat **40 Vault Salts, or 4 Insight, player's choice at the moment of recruitment** — priced below a single Memory Vendor Scar-removal trade deliberately, since a companion isn't permanent power the way a buff is; it's a fragile ally that can die for good.

---

## 19. Skill Checks — Beyond Combat

*(Session-off addition. Fleshes out §3's existing "anything genuinely uncertain" line into a real framework — same underlying math throughout, now with actual named shape instead of one flat catch-all a DM has to improvise fresh every time.)*

**Base structure, unchanged:** d20 + Attribute Modifier (§3 table) vs a DC. No new resolution system — more defined shape around the one that already exists.

### DC ladder

| Difficulty | DC |
|---|---|
| Trivial | 8 |
| Easy | 10 |
| Moderate | 13 |
| Hard | 16 |
| Very Hard | 19 |
| Extreme | 22+ |

DM states the DC before the roll, not after seeing it — matches the game's own "concrete numbers immediately" standard, no retroactive goalpost-moving.

### Which attribute governs which check

| Check flavour | Attribute | Examples |
|---|---|---|
| Force, break, physically overpower | Strength | kick a door in, bend a grate, hold a collapsing beam |
| Subtlety, fine manual work, precision with no stopwatch involved | Skill | pick a lock, palm an item, disarm a snare by hand |
| Outlasting physical strain | Endurance | hold your breath, push through smoke/heat, outlast a grind |
| Stability, resisting being moved or impaired | Vigor | keep footing on unstable ground, shrug off a non-attack impact |
| Nerve, presence, reading or being read by someone | Resolve | talk someone down, hold eye contact with something wrong, keep composure |

Noticing something **novel** (never encountered before) defaults to a Skill check. Noticing something **recurring** (a known archetype, a revisited location, an already-met NPC) is Insight Re-Read (§11) instead, not a roll — don't double up the two systems on the same fact.

### Texture, not a new system

- **Natural 20:** succeeds regardless of DC, plus a small narrated bonus — flavour only, never a new mechanical resource.
- **Natural 1:** fails regardless of modifier, plus a small narrated complication — same, flavour only.
- **Assist:** one other character actively helping (not just present) grants the roller a flat +2. Doesn't stack past one assistant, doesn't grant a second roll.
- **Insight override (rare):** where the read is genuinely about depth of sight rather than raw capability, the DM may let the player use Insight score in place of the Attribute Modifier band for that one check. Uncommon — most checks stay attribute-driven.

---

## 20. Timing Checks — Beyond the Parry

*(Session-off addition. Same stopwatch tool the Visceral (§9), Precision Strike (§10), and weapon-gimmick systems already use — target time ± tolerance, Insight window bonus applies exactly as it already does (§11) — now with named shapes for non-attack contexts instead of reinventing the wheel each time one comes up.)*

**Standing rule, unchanged from §2/§9: a stopwatch only ever follows a genuine, readable tell.** Nothing below is a tell-less "gotcha" — no fair cue, no stopwatch, just narration.

### Environmental Hazard Timing

Single window, same shape as a parry: a closing gate, a swinging fixture, a venting mechanism. DM sets target time + tolerance off the hazard's own visible/audible rhythm, stated before the attempt. **Inside →** clear it clean. **Outside →** the hazard's stated hit lands — floor-20 raw, or a status application, DM's call per hazard, but named before the attempt, never after.

### Mechanism/Ritual Sync Timing

Multi-window, same shape as a boss's ballistic chain (§16): 2–3 sequential stopwatches for a puzzle or mechanism needing more than one correctly-timed input — aligning gears, matching a resonant beat, a multi-stage ward. **All windows hit →** the mechanism resolves clean. **Miss one →** that stage fails; DM decides in advance of the attempt whether a miss is a hard stop (redo the full sequence) or a partial/costly success (proceeds, but at a stated cost — a track stack, lost time, a changed sub-locale).

### Escape/Chase Sequence Timing

Multi-window, same shape as Mechanism Sync above, reframed as pursuit rather than puzzle: 2–4 sequential beats (a leap, a dodge, a slammed door) fleeing a hazard or pursuer. **Miss a beat →** that beat's stated consequence lands (floor-raw damage, a status stack, dropped gear) **and the chain continues regardless** — same harshness already standing for Frenzied-Whirl-style chains (§16), not a softer variant just because the player's fleeing instead of attacking.

### Stealth Hold-Still Timing

A different shape entirely: not "hit the window," but "don't act until it elapses." Start the stopwatch; the stated duration is how long the player must hold position/stay silent (a patrol's pass, a searchlight's sweep). **Success** = the full duration passes with no action taken. **Failure** = triggered early, either by player choice or by a status effect forcing an action (Discombobulation, an Influence compulsion, a Rupture) — detection is then automatic, nothing to roll against it.

### Startle Timing

A genuinely tighter parry variant for a **near-instant but still real** tell — a half-second flicker, not nothing. Reserved for boss-tier or Insight-gated threats whose own Monster Manual entry specifically calls for it; never applied to a standard archetype by default. Same Inside/Outside outcomes as a normal parry (§9) — the tolerance is simply narrower than the standard bands. Doesn't override "honour tells" — the tell is just brutally short, not absent.

---

*Working title, placeholder names, and starting numbers are yours to change. The skeleton is built to be tuned at the table.*
