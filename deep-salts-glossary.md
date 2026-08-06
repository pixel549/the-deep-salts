# THE DEEP SALTS
**Glossary — Canonical Terminology**

*Version 1.0. Current as of Ruleset v9.4 / Design Bible v4.8.*

The naming authority for the project. Where any other document disagrees with this one, this one is wrong and needs updating — but the disagreement is a bug, and should be fixed rather than tolerated.

**Section 1** is the live vocabulary. **Section 2** is the retirement list: what a term used to be called, and what it is now. Check Section 2 first when reading anything written before v9.4.

---

# 1. Live Vocabulary

## Damage & resolution

**Raw** — damage before any limb multiplier, visceral bonus, or accuracy bonus. The number a weapon or attack generates on its own.

**Effective damage** — raw × limb multiplier. What actually chips HP and fills a limb's stagger meter.

**ESV (Effective Scaling Value)** — soft-capped attribute score used for weapon scaling. Distinct from the Attribute Modifier. A score of 99 yields ESV ~66.

**Attribute Modifier** — the −3 to +3 band used for d20 checks. Not the same as ESV and never interchangeable with it.

**Damage Floor** — 20. The practical minimum for any base number passing through a multiplier. Does not bind flat unmodified numbers such as item heals or status ticks.

**Tell** — the DM's description of an enemy's wind-up. Doubles as flavour and as mechanical signal: it carries the parry timing where timing is available, and hints at what the enemy is committing to this round.

## The parry loop

**Assess** — a Fast Action (1m) revealing an enemy's tell and rough timing. Clarity scales with Insight. Reveals Secondary Action *triggers* at Assess 2+, never their outcomes.

**Hold** — parry stance. An Action costing 4m. You cannot move after declaring it until it resolves.

**Parry** — stopping the stopwatch inside the window. Interrupts the telegraphed attack and knocks the enemy down.

**Hijack** — what a successful parry buys: the player takes over the enemy's action and strikes during the enemy's turn. Leftover movement may be spent afterward.

**Visceral** — the 1.5× strike a hijack opens. An *attempt*, resolved on its own stopwatch. Stacks with limb multipliers and buffs.

**Whiff** — stopping the stopwatch outside the window. The enemy's attack lands and no hijack occurs.

**Open (Tier 1 / 2 / 3)** — how generous the post-parry weak point is. Tier 1 flattens the follow-up watch to the loosest band; Tier 3 gives no easing at all.

**Accuracy Tiers** — landing deeper inside a window than required. Counted in tolerance bands: 4 bands deep pays ×1.1, rising to ×1.5 at 8. Dead centre pays ×3.0.

## Anatomy

**Precision Strike** — declaring a specific limb rather than taking a default swing. The single term for this; "called shot" is retired. Triggers a stopwatch at every multiplier except exactly ×1.0.

**Limb HP** — a limb's own pool, expressed as a percentage of the enemy's total HP rather than a fixed constant.

**Stagger** — a limb's threshold crossed cumulatively. The limb goes limp and the crossing hit grants an immediate free Action.

**Sever** — a limb's full HP dealt in one hit. Permanent. Head or torso severed kills regardless of remaining HP.

**Implement** — equipment or an object attached to an enemy (a bell, a shield, a carried weapon). Damage to an implement does **not** chip the enemy's HP. Isolated stagger and sever thresholds. The test: would ripping it off leave a wound, or leave them holding nothing?

**Arc / Point** — attack shape. Matters against Swarms and a small number of other entries.

## Combat flow

**Round** — four phases in fixed order: optional Assess, optional DM telegraph narration (enemies commit here), player actions, enemy actions.

**Action** — one per phase, priced in movement. Light 1m · Heavy 3m · Hold 4m · Manage a track 1m · Action Item 2m.

**Fast Action** — one per phase, also priced in movement. Assess 1m · Quick Item 0m · Swap weapons 1m.

**Movement budget** — 8 + ⌊Endurance ÷ 15⌋ metres. The single per-turn currency; repositioning and actions both draw from it. Cannot pay an action's cost, cannot take that action.

**Secondary Action** — what an enemy does when something has gone wrong for it. Replaces its attack; carries a stated trigger and cooldown. Unparryable unless its entry says otherwise. Learned live — Assess hints at triggers only.

**Interception** — the rare enemy that acts *in response to the player acting*, during the player's phase. Cannot be parried. Damage is small by design; the cost is the lost turn.

**Rally** — grey health. Land a qualifying hit on your next turn to claw back a portion, or it fades. 50% default, 75–100% off big boss haymakers, 0–25% off chip and tick damage.

## Statuses

Three shapes, and the shape determines only one thing: how it leaves you.

**Tick** — drains itself, counting down without intervention. *Bleeding · Burning · Discombobulation · Stone Skin · Frenzy.*

**Track** — builds and holds until something clears it. *Insanity · Influence · Corrosion · Crust · Fervour.*

**Condition** — binary, no stack count. *Fugue.*

**Bleeding** — uncapped Tick. Damage at start of turn equals current stack count, then loses 1. Total from N stacks is N(N+1)/2, so it escalates hard. Above ~10 stacks a target bleeds out unattended. Wrap halves it; cautery iron clears it.

**Burning** — Tick, 5 flat damage per turn, loses 1 stack per turn. Stacks add **duration, not intensity** — the deliberate opposite of Bleeding.

**Discombobulation** — Tick, cap 3. The DM may misdescribe exits, reverse movement, strip reactions, scramble attack directions.

**Stone Skin** — Tick, cap 3. 10% damage reduction per stack. Consumable-only; never a passive, drop or perk.

**Frenzy** — Tick. The afflicted must attack something each turn, enemies first, allies if nothing else is reachable. Zeroes at the end of any turn dealing no damage. Locks out Hold.

**Insanity** — Track, cap 10. Failed saves hand your turn to the DM. Cap triggers a **Break**.

**Break** — Insanity at 10. Resets the track and buys a 3-turn **Blackout** plus a permanent **Scar**.

**Blackout** — the DM-controlled scene a Break triggers. False tells, fake commands, wrong layouts, and a hallucinated threat dealing real damage.

**Scar** — the permanent trait a Break leaves. Upside and downside. Removable only via the Memory Vendor, at escalating Insight cost.

**Influence** — Track, uncapped past 10. Compulsion on a failed save. Only full elimination of the source clears it. Enemy-side, severity scales behaviourally rather than by save.

**Overload Rupture** — Influence at 10, on any creature. 25% of that creature's Max HP as direct damage, resets to 0, repeatable. The only surviving "Rupture" in the game.

**Corrosion** — Track, cap 10. Damage at start of turn equals stack count. Ticks down only if you spend an action managing it; otherwise holds indefinitely. The mirror of Bleeding — same formula, but it does not drain itself.

**Crust** — Track, cap 4. Accreted salt, rime, resin, wet ash. −1m movement budget per stack. Ticks down only on a turn where you took no Action at all. At cap, no Action over 1m — which locks out Hold.

**Fervour** — Track, cap 10. The only status the player wants. Builds on aggression, grants +3 raw and +0.5m per stack, charges stacks × 3 HP for any turn dealing no damage. Cap converts to 4 Frenzy and resets. Ends when combat ends.

**Fugue** — Condition. Applied on death. Doesn't change your Insight number, makes it *lie*. The DM may misreport timings, misdescribe items and enemies, and lie about recounted information. Cleared by the next Insight point earned.

**Save Roll** — d20 ≥ 10 + current track value − ⌊Resolve ÷ 10⌋ + ⌊Insight ÷ 2⌋. Insanity and Influence only.

## Progression & economy

**White Salts** — the single currency. Buys attribute levels, equipment, information — deliberately forcing a choice between levelling and acquiring.

**Purse** — salts carried and at risk on the current run. **Vault** — salts banked at the hub, permanently safe.

**Insight** — the sixth dial, earned through discovery and never bought. Buys sight and access; raises save DCs and, at higher tiers, damage taken. Falls when spent.

**Insight Tier** — 0 to 5, mapped to Insight 0–1 / 2–3 / 4–5 / 6–7 / 8–9 / 10.

**Insight Re-Read** — recurring things get re-described through the player's current tier. Costs nothing.

**Insight Perception** — untranslatable lore becoming comprehensible at Tier 4, in written text and in monster vocalisation and behaviour alike.

**Mutation** — a severed limb regrowing changed at the hub. Clear upside, clear downside. Full stat-line legible only at Insight 6.

**Memory Vendor** — hub NPC, visible at Insight 10+. Vanishes immediately if Insight drops below the threshold. Trades Insight for voluntary mutations, mutation removal and Scar removal. Never accepts Salts.

**Perk** — granted at 20/40/60/80/99 points invested in a single attribute.

## Exploration

**Recipe** — a biome's permanent identity: aesthetic and broad layout philosophy. Fixed. Everything inside it rerolls.

**Instance** — one generated run of a recipe. **Reroll** — generating a fresh one.

**Sub-locale** — where within the biome you land.

**Salt room** — the entry point, and where you respawn on death.

**Clean Chalice** — the exit. Exists somewhere in every instance, never where you woke up, must be found. Drinking from it banks the run.

**Instance Quest** — active only during the generated instance. Expires on exit, never tracked. Completing one can convert its reward into something permanent.

**Quest** — anchored to a persistent entity (recurring NPC, hub, recipe, carried item). Survives rerolls and is worth tracking.

**Hub** — Stillwell Hydro. The only stable place, and still slightly wrong.

**Flavour tag** — a private per-reroll skew: Combat · Mystery-Lore · Puzzle · Social Encounter · Escape-Survival.

**Warp threshold** — the point past which death and respawn rules go live.

## Fail-states

**Death** — HP reaches 0 inside an instance. Respawn at the salt room. Levels and prior mutations kept. Gear left on a variation of the enemy that killed you, which becomes a guaranteed spawn in that recipe until beaten. Purse lost entirely. A Scar is applied, and new mutations if limbs were severed.

**Retreat** — out of combat only. Currently unsettled; do not build against it.

## Enemy archetypes

Defined in Design Bible §0. Referenced by name in every monster entry's Archetype field.

**Humanoid:** Shambler · Lunger · Burster · Chanter · Spitter · Brute · Flailer · Drudge · Toller

**Non-humanoid:** Swarm · Anchor · Vessel · Crawler · Tide

**Atypical:** Pack · Leech · Snare · Stalker · Rite · Passenger

**Boss:** Effigy, plus bespoke entries.

*Note: **Anchor** is an archetype — a Move-0m elite that threatens a whole room. It has nothing to do with the Clean Chalice, which was formerly called an anchor. See Section 2.*

---

# 2. Retired & Renamed

Anything written before Ruleset v9.4 may use the left column.

| Retired term | Current term | Notes |
|---|---|---|
| Blood Loss | **Bleeding** | Also completely rebuilt: was a front-loaded 0–10 Track, now an uncapped self-draining Tick |
| Rupture | *(deleted)* | Existed only as Blood Loss's cap-10 trigger. **Overload Rupture** on the Influence track is unrelated and still live |
| Called shot | **Precision Strike** | One term now. The stopwatch is a property of the target's multiplier, not a separate species of action |
| Anchor *(the exit)* | **Clean Chalice** | Renamed to resolve the collision with the Anchor archetype, which keeps its name |
| Corrupted Regrowth | **Mutation** | |
| Abandon-All | *(deleted)* | Mid-combat bail-out removed entirely |
| Visceral Mods (Bloody / Sustaining / Quickening) | *(deleted)* | Insight tiers grant their effects directly now |
| Ruleset §16, Default Monster Table | **Design Bible §0** | Archetypes moved out of the ruleset |
| Ruleset §15, Starter Location | **Ruleset §14** | Folded into The Hub |
| Monster Template | **Monster Sheet Template** | |
| Resist Rupture *(Vigor 20 perk)* | **Thick Blood** | Bleeding stacks applied to you reduced 25%, rounded down |
| *Immediate* *(status shape)* | *(deleted)* | The three shapes are Tick, Track and Condition |
| Fugue as a Track | **Fugue as a Condition** | Never had stacks |
| Sub-1.0 multipliers as armour | *(deleted)* | Every limb triggers a stopwatch now except exactly ×1.0 |

---

# 3. Known Gaps

Recorded so they don't get rediscovered every few sessions.

- **Retreat is unsettled.** Referenced in Ruleset §12 and named in the fail-states, but its cost and trigger are undefined. Nothing should be built against it until it is.
- **Off-Balance has no shape.** Design Bible §6 lists it as an *Immediate*, a category that no longer exists. It is a 1-turn effect from a missed Precision Strike in the 1.26–1.50 band, and needs classifying or demoting to a plain effect.
- **The Monster Manual predates v9.4's limb model.** Every entry states fixed limb thresholds where the ruleset now defines Limb HP as a percentage of enemy HP.
- **Pack's premise is softer than its text.** Its threat model assumes strictly simultaneous enemy action and one parry per round; v9.4 lets the DM reorder enemies and lets Hold choose its target. Acknowledged and accepted.
