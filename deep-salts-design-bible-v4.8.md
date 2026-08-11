# THE DEEP SALTS
**Design Bible — Entity Templates**

Companion to the ruleset. **Load this plus the ruleset and character sheet when running the game.** Mechanic index/book plan/known gaps live in the dev log — do NOT load that during play.

*Version 4.8. Session attribution and change history live in the dev log, not here.*

Every monster/weapon/item/NPC/status/currency gets one complete page. Copy the blank template to add an instance.

**Status effect shapes** (ruleset §5): *Tick* (drains itself, counts down 1/turn) · *Track* (builds and holds until cleared) · *Condition* (binary, no stack count).

Each section leads with its **floor entry** — the weakest legal instance of that type. Nothing ships below it without a deliberate reason.

---

# 0. Enemy Archetypes

Redesign per location, adding new quirks and challenges. Attack damage generated live (§2), scaled to level (ruleset §17), never below the Damage Floor.

1. **SHAMBLER** (mook) — HP ~200–1200 · Move slow (3m). Lights only, no parryable heavy — a tell-less grab applying Influence or a track. Comes in groups. Unparryable, no visceral loop; dies to plain attacks. Stagger a leg then take the head as a faster (never required) option.
2. **LUNGER** (elite) — HP ~500–700 · Move medium (5m). One telegraphed heavy + Bleeding. Tell: raises blade, steps in (~1.4s). Tier 1.
3. **BURSTER** (skirmisher) — HP ~400–600 · Move burst (8m surge/~1m recover). Strikes only at the lunge's end, then recovers. Tell: coils before leap. Tier 1–2.
4. **CHANTER** (caster) — HP ~300–500 · Move slow (3m), hangs back. No melee; ranged Influence/Insanity pressure each turn. Unparryable, low HP, soft limbs — priority target.
5. **SPITTER** (controller) — HP ~400–600 · Move medium (4m), keeps distance. Ranged Corrosion, stacks fast. Tell: swells, draws back (~1.6s). Tier 1.
6. **BRUTE** (heavy) — HP ~1500–2500 · Move slow (4m). Huge slow heavies, can amputate/bisect an under-levelled player on a fully-landed combo. Tell: overhead wind-up (~2.0s). Tier 2. Sever a leg to neutralise its approach.
7. **FLAILER** (chaotic) — HP ~600–900 · Move medium, erratic. Multi-status (Corrosion + Bleeding). Tell: limbs draw back in unison, multiple windows in sequence. Tier 3. Hardest non-boss to open.
8. **DRUDGE** (elite) — HP ~600–900 · Move slow (2–3m), relentless, **never bursts or lunges**. One heavy on a steady cadence, always telegraphed, always parryable, long recovery after. Tier 1–2 (heavier instances use Tier 2). The counterpoint to Shambler: same slow walk, but its attack is fully readable and punishable instead of tell-less. Kitable forever in principle; it simply never stops coming.
9. **TOLLER** (mook) — HP ~250–400 · Move slow (2m), hangs back, rarely closes. Applies track pressure through a **destructible implement** (bell, censer, horn) — telegraphed and parryable, unlike a Chanter's bare voice. **Destroy the implement and it has no attack left at all.** Tier 1. The counterpoint to Chanter: kill the tool, not the creature.

**Non-humanoid archetypes.** The nine above all assume a roughly person-shaped enemy with a head, a torso and four limbs — which is what the standard limb model (§10) is built for. The five below deliberately do not, and each one breaks a different assumption the player has learned to rely on. They exist so that a room can pose a problem that isn't "the same fight with more HP."

10. **SWARM / AMBIENT HAZARD** (mook–elite) — HP ~350–600 · Move medium, flows rather than walks; occupies a stated volume (e.g. 3m×3m) rather than a point. **No limb entries at all** — a single sever-immune Mass row. Precision Strike cannot be declared, stagger never fires, limb-targeted shots resolve as plain hits, and every sever check simply does not apply. Dies only to raw HP damage. The direct counter to a precision build, and the reason HP attrition stays a first-class kill method (§3).
    - **Dispersion (attack shape matters).** A Swarm's HP represents distributed bodies, not a target. **Arc attacks deal full raw. Point attacks deal half, rounded up** (see *Attack shape* in §10). A Swarm is the one place in the game where a slow wide weapon strictly outperforms a fast precise one, and where the correct answer may be a torch rather than a blade.
    - **Escalating contact.** A Swarm's damage is designed to grow with time spent inside it rather than with the strength of its hits. Standing in one is the mistake; the archetype exists to price the player's position rather than to threaten a burst.
    - Swarms are the natural home for elemental multipliers and immunities (§10) — a shelled swarm cooks, a swarm of vapour ignores bleed entirely.
11. **ANCHOR** (elite–boss) — HP ~600–1500 · **Move 0m, permanently.** Never chases, never follows, cannot be kited because it never needed to close. Threatens through room-wide auras, reach, or a hazard it imposes on the space. Leaving is usually a complete counter — which makes "is this fight worth having" a real question rather than a rhetorical one.
12. **VESSEL** (elite) — a shell and an occupant, two separate creatures in sequence. The shell carries a **sub-1.0 damage multiplier as armour** (see §10) and no interesting attacks; the occupant is fast, fragile, and usually trying to leave. The health bar emptying is the middle of the fight, not the end of it.
13. **CRAWLER / CEILING AMBUSHER** (elite) — HP ~600–900 · Move fast (8m+) across **walls and ceilings**, ignoring floor terrain, hazards and chokepoints entirely. Cannot be funnelled, cannot be outrun, and the player's usual positional tools all quietly stop working.
    - **It holds with half its limbs and strikes with the other half**, so a Crawler that attacks from the ceiling *stays on the ceiling*. Attacking it in melee requires that its striking limbs be long enough to have brought it into reach — and many variants' aren't. Reach is stated per entry; some Crawlers are simply not meltable with a melee weapon while overhead.
    - **Interception is the archetype's signature** (§7): while overhead and unspotted, a Crawler answers the player *taking an Action* rather than acting on its own phase. The mirror-image of the player's own parry loop — it punishes committing first, exactly as the parry punishes the enemy for committing first.
    - **Legs are the whole limb table.** A 6- or 8-leg cluster; **severing half of them ends wall and ceiling movement permanently**, converting the Crawler to a slow ground crawl for the rest of the encounter. **Staggering any single leg drops it to the floor immediately** for the stagger's duration. Getting it down is the fight; killing it once it is down usually is not.
    - The archetype is built to make ranged tools, thrown items and knockdown effects load-bearing rather than optional. A player with no answer to *height* has no answer to a Crawler.
14. **TIDE** (hazard-creature) — occupies a stretch of floor, corridor or room. Often has no attack the player can react to and sometimes **no HP at all** — it is resolved by crossing it, cutting a lane through it, or shutting it off, not by killing it. The archetype that makes an encounter a problem rather than a fight.

15. **PACK** (mook, group-only) — HP ~150–320 per member · Move fast (6–8m). **Never appears alone.** A Pack is 3–6 members plus one **Alpha** carrying roughly triple a member's HP and one command or buff ability. Every member has **three or more attack options** rather than one. **While the Alpha lives, the whole pack takes the same action in unison** — five Bleeding applications landing in a single Enemy Phase, or five bodies of flat raw, chosen fresh each round. Individually each member is parryable and unthreatening; collectively they are unparryable, because §7 grants one parry per round against five simultaneous strikes. **Kill the Alpha and coherence breaks:** surviving members roll independently from then on, each picking its own attack, and the round stops arriving as a single stacked blow even though not one statline changed. The archetype that makes the simultaneous Enemy Phase bite, and the first where target priority *is* the fight.

16. **LEECH** (parasite/controller) — HP ~200–450 · Move variable, frequently concealed, sometimes short-range blink. **Deals no physical damage whatsoever.** It drains the player's *economy* instead: White Salts out of the Purse, Insight, item charges, ammunition, pending Rally, or an attribute temporarily — a fixed amount per round, beginning the round after it establishes and continuing until it dies, loses line of sight, or the player leaves its stated range. Trivially killable and never worth the turn while anything else in the room is swinging, which is precisely the trap: ignore it and it eats the run's profit, answer it and you turn your back on whatever is walking up behind it. **Drained resources are gone, not held** — killing a Leech never refunds what it took unless its own entry says so.

17. **SNARE** (terrain/anchor hybrid) — HP deliberately excessive (~1200–2500) · Move 0m, or a crawl measured in metres per encounter. A living hazard fused into the room, threatening through tendrils, roots, wires or lines reaching stated distances from a fixed anchor. **HP attrition is deliberately not the route** — the intended kill is limb destruction, and each limb destroyed permanently removes one zone of threat and shrinks the room's dangerous footprint. Converts a kitable space into a spatial puzzle where standing position relative to the anchor decides which incoming attacks can be escaped at all, including those of *other* enemies in the room. Distinct from Anchor (threatens the whole room; answered by leaving) and Tide (crossed rather than fought): a Snare can be dismantled, and dismantling it is the encounter.

18. **STALKER** (pursuit/unkillable) — HP hand-set and deliberately excessive, or none at all · Move relentless, pointedly just under the player's own budget. **Not built to be beaten in a stand-up fight, and often not beatable at all in a given instance.** Limbs split into two grades: **soft joints** that stagger in a round or two and buy 2–4 rounds of distance, and a **true weak point** — a core, a gem, a heart-seam — with a threshold no current weapon reaches and reduced incoming damage on top. Alerting one converts the rest of the instance into a chase; it crosses rooms, it does not lose interest, and it does not heal what has been staggered off it for the duration of the run. **The instance must contain at least one environmental answer**, decided when the layout is generated rather than improvised when the player asks for one: a drop, a hazard, a sealable door, a flooding chamber, a rival creature that will aggro it. If a given roll genuinely has none, then finding the clean chalice and leaving is the correct play and the DM must let that read cleanly rather than dangling a solution that does not exist.

19. **RITE** (puzzle/rule-bound) — HP variable · Move variable. Operates under a **strict, discoverable, absolutely consistent rule** governing when, whether and whom it attacks: it strikes only armed targets, or only what moved last round, or only whoever spoke, or it repeats the player's own previous action back at them. **The rule is never stated outright.** It is deduced from behaviour; Assess 2+ gives a strong directional hint rather than the answer. **The rule never bends — not once, not for tension, not because the fight has gone long.** An enemy that cheats its own rule is a random number generator with extra steps and destroys every Rite that comes after it. Obeying the rule is usually a complete counter and usually costs the player something they did not want to give up. The archetype for a room that is a problem rather than a fight.

20. **PASSENGER** (occupant/target-denial) — HP ~150–250 for the passenger itself, plus whatever it is currently riding · Move via its host. Something small living inside something larger. **Killing the host does not kill it.** On the host's death it transfers to the nearest available body within a stated range — other enemies, corpses on the floor, and where the entry explicitly says so, a companion. It is exposed and targetable **only during the transfer, for exactly one round.** The whole fight is engineering a moment where the host dies with nothing else in reach. Distinct from Vessel (a shell and an occupant resolved in sequence): a Passenger has no fixed number of phases and will keep going as long as the room keeps offering it bodies.

**Shared HP pools.** A creature may present as several bodies drawing on one pool. Damage to any body drains the shared total; individual bodies are not separately killable unless the entry says so. This is a Vessel or Swarm variant, not a new archetype, and it exists to make target selection and positioning matter in fights that would otherwise be a single health bar with extra steps. Two shapes have precedent: **bleed-back** (an undamaged body restores to the pool each round, so splitting attention is mandatory) and **terminal burst** (the bodies detonate together when the pool empties, so where they stand at the end is the real fight).

**Standard archetypes cannot parry/visceral the player** — that loop is boss/hand-flagged-elite only.

**Bosses** are bespoke, built on three pillars: (1) a gimmick punishing a default habit, (2) a Tier-3 multi-parry ballistic chain as the real opening, (3) a dismember/bisect threat for the under-levelled, with a disengage threshold always reachable.

**EFFIGY** (boss, duellist/mirror) — HP hand-set · Move fast (7m+). Uses your own toolkit: parries, viscerals, hit-and-runs, out-moves you. The system-mastery check fight.

---

# 1. Monster Sheet Template

One page per monster — everything a DM needs to run that fight, nowhere else to look.

**Standard humanoid stagger durations (default, applies wherever "standard humanoid defaults" is referenced):** Head 1 turn · Arm 2 turns · Leg 2 turns · Torso n/a. Elites/bosses set bespoke durations.

## Monster 1 — Waterlogged Guest *(floor entry)*

- **Archetype:** Shambler (mook) · **Level Range:** 1–15 · **HP:** 200 · **Move:** 3m constant shuffle, no burst/recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A guest who came for the waters and never left the pool. Robe fused to grey skin. Drifts toward warmth rather than hunting.
- **Limbs:** custom. **Head: guarded** — hunches forward, arms outstretched. Not targetable until at least one arm is staggered or severed (recoils, exposing head). Once exposed: standard (stagger 180, ×1.5). **Arms: stagger 100, ×1.0** (waterlogged, swollen, barely holding together). Arm sever → Grasp disabled on that side; both severed = harmless. **Legs:** standard (300, ×0.75). Not sever-immune.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Waterlogged Grasp | Light | None — unparryable, no windup | N/A | N/A | 0 raw; 1 Influence stack | N/A | N/A — outside 3m it just doesn't land |

- **Secondary Actions:**
  - **Drift to Warmth** — *Trigger:* a Burning stack is active on any creature within 8m (including the player). *Cooldown:* 2 rounds. It loses interest in the player entirely, moves its full budget toward the burning creature and Grasps that instead. Fire in the room redirects every Guest in it — which makes Maria's Purging Flame a lure as much as a weapon.
  - **Cling** — *Trigger:* the Guest has been within 1m of the player at the start of two consecutive rounds. *Cooldown:* 3 rounds. No Grasp. It simply takes hold: the player's movement budget is reduced by 3m next turn. No damage, no Influence, no save. Standing next to a Shambler is not free.
- **Kitable:** Y — slowest move budget in the game.
- **Assess 0–1:** "It's slow. It won't hit hard. Watch the others behind it." · **Assess 2+:** "No damage on the grab, just Influence, no tell. Stagger a leg to ground it; head's open after."
- **Influence effect capped:** pull one step toward source (movement cost only), never an action loss, at any stack height.
- **White Salts drop:** 5 (the floor). **Insight:** +1 first sighting / +0 thereafter.

## Monster 2 — Chapel Penitent

- **Archetype:** Lunger (mook) · **Level Range:** 1–20 · **HP:** 300 · **Move:** 3m stalking pace, single 5m lunge after a short pause then a recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A pilgrim whose knees wore grooves into the stone before death. Still bows before every attack.
- **Limbs:** custom. **Head:** standard (stagger 180). **Arms:** standard (stagger 200). **Legs: stagger 150** (knees worn to grooves from centuries of kneeling — structurally compromised). Leg sever → Penitent Rush permanently disabled (no lunge without legs).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Penitent Rush | Heavy | "It bows deeply, then drives forward in a desperate sprint." | Target 1.2s, ±0.20s | 1 | 40 raw | Standard | Long recovery (~2 player actions before it fully re-engages, guideline not a hard count) |

- **Secondary Actions:**
  - **False Bow** — *Trigger:* Penitent Rush was parried in the previous round. *Cooldown:* 2 rounds. It bows — identically, no tell difference, no way to distinguish it — and does not come. No attack and no damage, and a player who declared Hold has spent their Action on nothing. The manual's cleanest anti-parry feint.
  - **Prostrate Crawl** — *Trigger:* a leg is severed. *Cooldown:* 2 rounds. No lunge. It hauls itself 2m and grabs at ankles: any creature it reaches loses 3m from next turn's movement budget. Unparryable, no damage.
- **Kitable:** Y. **Assess 0–1:** "It only becomes dangerous once it commits." · **Assess 2+:** "Wait for the bow. Dodge the charge, punish the recovery."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** panic-dodging too early. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 3 — Drowned Bellkeeper

- **Archetype:** Toller (mook) · **Level Range:** 1–20 · **HP:** 280 · **Move:** 2m slow walk, rarely closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A ruined attendant dragging a cracked handbell beneath the waterline. Every ring reaches inside the skull.
- **Limbs:** standard defaults, plus non-standard: **Bell** — implement, not a limb (Ruleset §10): isolated HP pool, multiplier ×2.0, sever threshold 40. Damage to the bell does NOT chip the Bellkeeper's main HP. Breaking it permanently disables Hollow Bell for the encounter — and the Bellkeeper has no other attack, so a destroyed bell leaves it harmless.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Hollow Bell | Aura | "It slowly raises the bell before a dull, submerged toll." | Target 1.60s, ±0.35s total (±0.20s base + Insight window bonus) — set live session 7 | 1 | 20 raw; 1 Influence stack | Standard | Long delay before next toll |

- **Secondary Actions:**
  - **Muffled Toll** — *Trigger:* the Bell implement is staggered. *Cooldown:* 2 rounds. It clamps the cracked bell against its own ribs and rings it inward. No Influence — instead every **enemy** within 6m recovers 20 HP. Half-destroying the bell is worse than leaving it alone.
  - **Call the Ring** — *Trigger:* Hollow Bell is parried. *Cooldown:* 3 rounds. No toll. It rings a summons instead: every enemy in the room gains 3m of movement on this Enemy Phase, resolved before their own actions.
- **Kitable:** Y. **Assess 0–1:** "That bell feels worse than it sounds." · **Assess 2+:** "Interrupt the toll by staying aggressive. Left alone it keeps building Influence."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** ignoring support enemies. **Dismember threat:** Low.

## Monster 4 — Salt-Eaten Custodian

- **Archetype:** Drudge (elite) · **Level Range:** 5–20 · **HP:** 650 · **Move:** 3m relentless walk, never sprints · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Once tasked with cleaning the baths, now drags an iron scraper large enough to serve as a coffin lid.
- **Limbs:** custom. **Head: stagger 250, ×1.5** (salt-crusted skull and neck — reinforced, much harder than standard). **Scraper arm: stagger 120, ×1.2** (salt-eaten elbow joint — exposed, damage transfers efficiently). Arm sever → Iron Scrape permanently disabled, scraper drops. Optimal target — lower threshold AND higher multiplier than head. **Off arm:** standard (200, ×0.65). **Legs:** standard (300, ×0.75).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Iron Scrape | Heavy | "The scraper screeches across the floor before a wide sweep." | Target 1.20s, ±0.40s total (±0.25s base + Insight window bonus) — set live session 7 | 1 | 60 raw | Standard | Long recovery dragging weapon free |

- **Secondary Actions:**
  - **Barricade** — *Trigger:* Iron Scrape has been parried twice this encounter. *Cooldown:* 3 rounds. It drives the scraper into the floor edge-on and braces behind it. No attack; the scraper is a 3m barrier the player cannot cross this round, and the Custodian's head and scraper arm are both untargetable behind it.
  - **Scrape the Salt** — *Trigger:* below 50% HP. *Cooldown:* 4 rounds. No attack. It drags the scraper across its own crusted skull and shoulders: **all accumulated stagger progress on every limb resets to zero.** Sever thresholds are unaffected — chip damage is undone, commitment is not.
- **Kitable:** Y. **Assess 0–1:** "That thing is slow, but don't stand in front of it." · **Assess 2+:** "The scrape announces everything. Dodge late, punish hard."
- **White Salts drop:** 15. **Insight:** +1/+0. **Habit punished:** greedy attacks after the tell begins. **Dismember threat:** High.

## Monster 5 — Brine Spitter

- **Archetype:** Spitter (mook) · **Level Range:** 1–20 · **HP:** 260 · **Move:** 3m retreating shuffle, keeps distance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Jaw hangs permanently open, overflowing with glittering saltwater that never runs dry.
- **Limbs:** custom. **Head: stagger 180, ×1.5** (standard). **Jaw** — implement, isolated HP pool: stagger threshold 60 (×1.5). Jaw stagger → Brine Jet interrupted, 1 round cooldown before it can spit again. Jaw sever → Brine Jet permanently disabled (mouth destroyed). The jaw hangs loose — it's the obvious weak point. **Arms:** standard (200, ×0.65). **Legs:** standard (300, ×0.75).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Brine Jet | Ranged | "Its throat swells until the skin stretches taut." | Target 1.60s, ±0.20s | 1 | 30 raw | Standard | Stands exposed while coughing seawater |

- **Secondary Actions:**
  - **Backwash** — *Trigger:* the player is within 2m at the start of the Enemy Phase. *Cooldown:* 2 rounds. It swallows instead of spitting and retreats its full budget. No damage; it heals 30 HP and the Jaw's stagger meter resets to zero.
  - **Prime the Ring** — *Trigger:* the Jaw is staggered. *Cooldown:* once per encounter. Unable to spit, it hoses the floor at its feet: a 2m puddle costing 2m extra to cross and applying 1 Corrosion per round to anything standing in it, lasting the encounter.
- **Kitable:** N. **Assess 0–1:** "It's safer up close than far away." · **Assess 2+:** "Rush it during the inhale. The spit leaves it wide open."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** backpedalling constantly. **Dismember threat:** Low.

## Monster 6 — Bathhouse Flailer

- **Archetype:** Flailer (elite) · **Level Range:** 10–20 · **HP:** 700 · **Move:** 4m erratic, unpredictable direction changes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Wrapped in soaking towels that whip through the air like living tentacles when it panics.
- **Limbs:** custom. **Head: stagger 240, ×1.5** (wrapped in layers of soaking towels — padded, harder than standard). **Each arm: stagger 140, ×1.0** (towel-wrapped, less structural than bone — damage transfers cleanly). Arm sever → Frenzied Whirl permanently drops 1 beat from chain (3→2→1). Both arms severed = single-beat chain. Optimal targets — lower threshold, decent multiplier, and each sever degrades its best attack. **Legs:** standard (300, ×0.75).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Towel Lash | None — unparryable chip | N/A | 25 raw | Standard | N/A |
| Frenzied Whirl | Heavy (chain) | "All four towels draw back in unison, then unwind one after another." | **3 sequential windows: 0.80s · 1.30s · 1.80s, each ±0.20s base** | 3 | 30 raw per unparried window (90 if all three land) | Standard | Chain continues from the missed beat |

**Frenzied Whirl — the ballistic chain** *(set session 7, gives the Flailer archetype its defining Tier 3 opening):* three windows resolved back to back, one stopwatch each, restarting from 0 at each beat.
- **All three parried →** Tier 1 Open. It collapses out of the spin, the weak point is Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9) — not automatic.
- **Miss any window →** take that beat's 30 raw and every remaining beat in the chain automatically. No partial credit, no opening.
- Parried beats deal no damage and don't open it on their own — only the full three do. This is the hardest non-boss opening in the game by design.

- **Secondary Actions:**
  - **Soak** — *Trigger:* any Burning stack lands on it. *Cooldown:* 2 rounds. It wrings the sodden towels over itself. All Burning cleared, and it gains 2m of movement this round. Fire is the obvious answer to a cloth enemy and this is why it isn't.
  - **Snap Dry** — *Trigger:* both arms severed. *Cooldown:* 3 rounds. With no towels left it grabs and squeezes instead: unparryable, 20 raw + 1 Bleeding to a creature within 1m, every round. Taking its arms off makes it worse at range and no safer up close.
- **Kitable:** N. **Assess 0–1:** "Stay calm. It isn't." · **Assess 2+:** "The spin isn't one attack, it's three. Read all of them or none."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** staying glued to its sides. **Dismember threat:** High.

## Monster 7 — Marble Attendant

- **Archetype:** Drudge (elite) · **Level Range:** 10–20 · **HP:** 800 · **Move:** 2m deliberate advance, pauses after every attack · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A carved attendant statue animated by centuries of absorbed prayers. Marble chips fall with every step.
- **Limbs:** custom. **Head: stagger 350, ×1.5** (solid marble — near-impossible to sever at current raw; this is deliberate). **Arms: stagger 160, ×1.0** (stress fractures from centuries of punching stone — clean break point). Arm sever → Marble Fist permanently disabled. Optimal target for ending the fight's threat. **Legs: stagger 200, ×1.0** (weight-bearing pillars under constant stress). Leg sever → grounded (1m crawl), but still punches in range. Useful for kiting, not for finishing.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Marble Fist | Target 1.80s, ±0.20s | 2 | 80 raw | Standard | Long stationary recovery |

- **Secondary Actions:**
  - **Settle** — *Trigger:* it took no damage in the previous round. *Cooldown:* 3 rounds. No attack. It stands still and lets the marble knit: one staggered limb recovers immediately and that limb's stagger meter resets to zero. Kiting a Marble Attendant undoes the work.
  - **Shed** — *Trigger:* below 40% HP. *Cooldown:* once per encounter. Once per encounter, permanent. It sloughs its outer marble in sheets: **Head stagger drops 350 → 200**, but Move rises 2m → 4m and Marble Fist's target time tightens to 1.40s. The head finally becomes viable exactly when standing near it stops being safe.
- **Kitable:** Y. **Assess 0–1:** "Every hit hurts. Every swing is slow." · **Assess 2+:** "Its recovery is longer than its attack. Survive one blow, answer with several."
- **White Salts drop:** 20. **Insight:** +1/+0. **Habit punished:** trading hits. **Dismember threat:** Very High.

## Monster 8 — The Singer *(boss, Choir Deep)*

- **Archetype:** Choir (boss) · **HP:** 900 (hand-set, exempt from scaling) · **Move:** 0m — fully rooted, never advances or retreats.
- **Flavour:** A pilgrim shape whose face gave way to a vertical opening that doesn't sing so much as *is* the sound. Sustains an unbroken note that draws the faithful into a ring around it, never approaching its own devotion.
- **Limbs:** standard defaults + **The Open Throat** (weak point) — multiplier ×2.0, stagger 240, sever 400.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Choir Pulse | Ranged/Aura | "The layered note sharpens, aims itself." | Unparryable, always lands | N/A | 2 Influence stacks/pulse |

- **Secondary Actions:**
  - **Descant** — *Trigger:* the player has broken line of sight to it for a full round. *Cooldown:* 2 rounds. No pulse. The note changes register and every congregation member in the room immediately moves its full budget to re-establish line of sight **for** the Singer, gaining +10 raw on its next attack. Hiding from the Singer costs the room.
  - **Swallow the Note** — *Trigger:* the Open Throat takes any damage. *Cooldown:* 3 rounds. The throat closes. No Choir Pulse this round, the Open Throat is untargetable next round, and the Singer regains 40 HP. The weak point is real; it is also not patient.
- **Kitable:** N/A — never moves. Breaking line of sight is the counter.
- **Assess 0–1:** "It's not hunting. Whatever it's doing, it's not going to chase." · **Assess 2+:** "The note itself is the attack. The opening where its face should be is real, but boss-high, not mook-high."
- **White Salts drop:** 60. **Insight:** +1/+1.
- **Boss Gimmick:** Sever the Open Throat and the fight ends regardless of remaining HP. **Threshold 400 at ×2.0 = 200 raw in one hit** (per Ruleset §10's threshold ÷ multiplier). Deliberately above what any current weapon reaches — the Singer is an attrition fight first, and sever is never required (Ruleset §3). Otherwise pure attrition — the Singer never physically attacks; danger comes secondhand from its Penitent congregation, while Influence climbs the whole time, save DC rising with stack count.
- **Habit punished:** tanking pulses in the open, or fighting through the ring instead of around it. **Dismember threat:** Low (no melee of its own). **Retreat always reachable:** Y.

## Monster 9 — Cinderbound Attendant

- **Archetype:** Shambler (mook) · **Level Range:** 1–15 · **HP:** 220 · **Move:** 3m constant shuffle, no burst/recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A crematorium attendant whose apron fused to the firebrick during the last real burn. The wrap around its arms never fully cools. Drifts toward cold rather than hunting — the inverse of the thing that still wants its bath.
- **Limbs:** custom. **Head: guarded** — the firebrick apron covers its face and chest like a cowl. Not targetable until torso stagger (apron cracks, head exposed). Once exposed: standard (stagger 180, ×1.5). **Arms: stagger 120, ×1.0** (wrapped in smouldering cloth — brittle underneath). Arm sever → Cinder Grasp disabled on that side; 1 Burning applied to attacker from the severed stump's final flare. **Legs:** standard (300, ×0.75). Not sever-immune.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Cinder Embrace | Light | None — unparryable, no windup | N/A | N/A | 0 raw; 1 Burning stack | Standard | N/A — outside 3m it just doesn't land |

- **Secondary Actions:**
  - **Bank the Coals** — *Trigger:* a Burning stack was cleared by any creature within 6m in the previous round. *Cooldown:* 2 rounds. It draws the loose heat back in: heals 25 HP, and its next Cinder Embrace applies 2 Burning instead of 1.
  - **Drift to Cold** — *Trigger:* a creature within 8m has zero Burning stacks while the player has one or more. *Cooldown:* 2 rounds. It ignores the player and moves its full budget toward the coldest thing in the room. The exact inverse of the Waterlogged Guest's lure, and the two can be played against each other in the same room.
- **Kitable:** Y — slowest move budget in the game.
- **Assess 0–1:** "It's warm, not fast. Keep your distance and it can't do a thing." · **Assess 2+:** "The wrap's the fuel, not the arm. Stagger a leg — the grab still can't reach you before it drops."
- **White Salts drop:** 5 (the floor). **Insight:** +1 first sighting / +0 thereafter.

## Monster 10 — Rime-Fused Bailiff

- **Archetype:** Lunger (mook) · **Level Range:** 1–20 · **HP:** 340 · **Move:** 3m stalking pace, single 5m lunge after a short pause then a recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Once kept the cold stores at temperature. Now the cold that killed it lives under the skin, an icicle grown straight through the forearm where a blade should be.
- **Limbs:** custom. **Head:** standard (180). **Rime arm (ice shard): stagger 160** (frozen, brittle). Arm sever → Rime Thrust permanently disabled. **Off arm:** standard (200). **Legs:** standard (300).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Rime Thrust | Target 1.2s, ±0.20s | 1 | 40 raw; 1 Bleeding stack | Standard | Long recovery prying the shard free |

- **Secondary Actions:**
  - **Rime Sheath** — *Trigger:* the Rime arm is staggered. *Cooldown:* 3 rounds. No thrust. It plunges the arm into the floor and regrows the shard: the stagger clears and the arm's stagger meter resets to zero. Sever it or commit properly — half measures are undone every time.
  - **Frost Ground** — *Trigger:* Rime Thrust is parried. *Cooldown:* 2 rounds. It slams the shard down instead of recovering. A 3m circle of ice for 3 rounds: any creature spending 4m or more of movement inside it takes 15 raw and loses 2m from next turn's budget.
- **Kitable:** Y. **Assess 0–1:** "Only dangerous once it commits." · **Assess 2+:** "Wait for the crack. Dodge the thrust, punish the recovery — same rhythm as anything with one move."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** panic-dodging too early. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 11 — Wire-Strung Marionette

- **Archetype:** Burster (skirmisher) · **Level Range:** 5–25 · **HP:** 480 · **Move:** 3m twitching idle, 8m surge / ~1m recovery on the lunge · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Something that used to work the strings now wears them — cord grown straight into its own joints, drawn bowstring-tight before every leap. First of its archetype on record; nothing about it is slow.
- **Limbs:** custom. **Head:** standard (180). **Arms: stagger 140** (wire-strung, taut but snappable). **Legs: stagger 150** (wire joints under tension). Leg sever → 8m surge disabled, grounded. The Marionette's danger is its surge — removing the legs removes the threat.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Snap-Cord Lunge | Heavy | "The cord along its spine draws bowstring-tight." | Target 1.3s, ±0.20s | 1 | 45 raw | Standard | Long recovery, tangled in its own cord |

- **Secondary Actions:**
  - **Restring** — *Trigger:* a leg is severed. *Cooldown:* 4 rounds. No attack. It hauls slack cord out of its own torso and splices the stump: the leg is restored as a wire strut, Move drops permanently by 2m, and Snap-Cord Lunge returns. Once per leg.
  - **Draw and Hold** — *Trigger:* the player is more than 6m away at the start of the Enemy Phase. *Cooldown:* 2 rounds. It winds the spine-cord and does not release. No attack this round; next round's Snap-Cord Lunge has 11m reach and its window tightens to ±0.13s.
- **Kitable:** Partial — Y between bursts, N mid-surge (the 8m covers ground faster than a retreat). **Assess 0–1:** "It's not fast. It's a spring." · **Assess 2+:** "Everything happens on the coil. Move the instant the cord draws, not after."
- **White Salts drop:** 12. **Insight:** +1/+0. **Habit punished:** standing still after its first miss — the recovery beat is real, but short. **Dismember threat:** Moderate.

## Monster 12 — The Annotator

- **Archetype:** Chanter (caster) · **Level Range:** 1–20 · **HP:** 340 · **Move:** 3m drifting glide, always hangs back, never closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A robed archivist, mouth sewn shut decades ago. The whispering isn't coming from the mouth — it's the marginal notes crawling up its sleeves, reciting something that isn't quite words. First genuine Chanter on record.
- **Limbs:** standard defaults, no deviations — soft target, nothing to armor.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Marginal Recitation | Ranged/Aura | None — unparryable, always lands in range | N/A | N/A | 0 raw; 1 Influence stack (DM may substitute 1 Insanity stack instead, per the archetype's dual pressure) | N/A | N/A |

- **Secondary Actions:**
  - **Cross-Reference** — *Trigger:* two or more other enemies are in the room. *Cooldown:* 3 rounds. No recitation. It reads across: every other enemy's next attack gains +10 raw for one round. The Chanter's support role made explicit rather than implied.
  - **Erratum** — *Trigger:* it takes damage from a Precision Strike or Precision Strike. *Cooldown:* 2 rounds. The marginal notes rewrite themselves. The player's next Precision Strike this encounter resolves one tolerance band tighter. Stacks with itself up to twice.
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

- **Secondary Actions:**
  - **Seed the Floor** — *Trigger:* the player closes to within 2m. *Cooldown:* 3 rounds. No cough. It retreats its full budget and lays a 3m dust bed behind it: 1 Corrosion per round to anything standing in it, 4 rounds, blocks nothing and stops nobody.
  - **Dry Heave** — *Trigger:* below 40% HP. *Cooldown:* 3 rounds. No attack. It doubles over and every Corrosion stack on every creature within 5m ticks a second time this round.
- **Kitable:** N. **Assess 0–1:** "Closing the gap is safer than staying at range." · **Assess 2+:** "Rush it during the swell. The cloud needs the cough to actually leave its throat."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** backpedalling constantly. **Dismember threat:** Low.

## Monster 14 — The Long Cutter

- **Archetype:** Brute (heavy) · **Level Range:** 15–60 · **HP:** 1800 · **Move:** 4m slow, deliberate advance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Built from decades of fused ossuary bone, bound in rope and set pitch, wielding a cleaver the length of a door. Doesn't so much walk as arrive. First of its archetype on record — built deliberately over-levelled for now, a long-campaign fixture rather than a next-session encounter.
- **Limbs:** custom. **Head: stagger 320, ×1.5** (a fused knot of skulls bound in rope and set pitch — there is no single skull in there to break). **Cleaver arms, both: stagger 260, ×0.9** (bone laid over bone, tough and worth very little on its own). Severing one → Door-Length Cleave drops to a one-handed 55 raw at target 1.50s ±0.20s. Severing both → the cleaver is dropped and **becomes claimable on the floor.** **The Pitch Seam: stagger 200, ×1.4** — a rope-bound join across the lower back where the pitch never fully set. **Only targetable from behind**, and it does not turn quickly. Seam sever → the Long Cutter comes apart at the waist and the fight ends regardless of remaining HP. **Legs: stagger 200, ×1.0** (bearing an absurd load). Leg sever → grounded to a 1m drag, and the cleave stays lethal to anything still in reach.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Door-Length Cleave | Heavy | "It raises the cleaver in both fists, joints grinding audibly." | Target 2.0s, ±0.20s | 2 | 90 raw | Standard | Long stationary recovery, blade stuck in the floor |

- **Secondary Actions:**
  - **Set the Line** — *Trigger:* Door-Length Cleave is parried. *Cooldown:* 3 rounds. It does not recover — it plants the cleaver and shifts its stance. No attack this round; next round's Cleave becomes a two-window chain (2.00s then 1.20s, ±0.20s each) and **both** must be parried for any opening at all.
  - **Arrive** — *Trigger:* the player has been more than 8m away for two consecutive rounds. *Cooldown:* 4 rounds. No attack. It covers 12m in a single stride and ends adjacent. Kiting the Long Cutter works and it has a hard ceiling.
- **Kitable:** Y in principle — it's enormous, and enormous is slow. **Assess 0–1:** "It's huge. It's also slow enough to just not be there when it lands." · **Assess 2+:** "Sever a leg and the approach stops being a threat at all — the wind-up alone gives you the time."
- **White Salts drop:** 35. **Insight:** +1/+0. **Habit punished:** trading hits at melee range while under-levelled — genuine bisect threat on a fully-landed hit. **Dismember threat:** Very High. **Retreat always reachable:** Y — nothing about it is fast.

## Monster 15 — Custodian in Wax

- **Archetype:** Drudge (elite) · **Level Range:** 5–20 · **HP:** 700 · **Move:** 3m relentless walk, never sprints · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A parlour attendant recast entirely in wax mid-task, still holding the brush it died holding. Never stops. Never speeds up either.
- **Limbs:** custom. **Head: stagger 300, ×1.5** (recast solid in wax over bone — dense, and there is no skull-shaped void in it). **Brush arm: stagger 110, ×1.2** (the wax never set properly around the wrist it died working with — the join is visibly soft). Arm sever → Slow Anoint permanently disabled. Optimal target: lower threshold and higher multiplier than the head. **Off arm:** standard (200, ×0.65). **Legs: stagger 260, ×0.9** (poured into columns; heavy, unhurried, hard to break). Leg sever → 1m crawl, and it still anoints anything that comes into reach.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Slow Anoint | Heavy | "The brush arm draws back with a soft, waxen creak." | Target 1.2s, ±0.25s | 1 | 55 raw | Standard | Long recovery re-settling its stance |

- **Secondary Actions:**
  - **Anoint the Room** — *Trigger:* Slow Anoint is parried. *Cooldown:* 3 rounds. It paints the floor instead of the player: a 4m band of wax costing double movement to cross, lasting until burned. Burning it clears the band instantly **and** applies 2 Burning to the Custodian.
  - **Re-Cast** — *Trigger:* a limb is severed. *Cooldown:* 4 rounds. No attack. It stands still and the wax runs: the severed limb reforms at half its original stagger threshold. Twice per encounter maximum.
- **Kitable:** Y. **Assess 0–1:** "Slow, but it never stops coming." · **Assess 2+:** "Fully readable, fully punishable — the counterpoint to anything with a hidden tell."
- **White Salts drop:** 15. **Insight:** +1/+0. **Habit punished:** greedy attacks after the tell begins. **Dismember threat:** High.

## Monster 16 — The Brass-Throated Barker

- **Archetype:** Toller (mook) · **Level Range:** 1–20 · **HP:** 300 · **Move:** 2m slow walk, rarely closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Wears a barker's brass megaphone fused permanently to its jaw. Every call through it warps the mirrors around it into something worse.
- **Limbs:** standard defaults, plus non-standard: **Megaphone** — implement, not a limb (Ruleset §10): isolated HP pool, multiplier ×2.0, sever threshold 35. Damage to the megaphone does NOT chip the Barker's main HP. Breaking it disables Warped Call for the encounter — no other attack exists.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Warped Call | Aura | "It draws breath through brass, and the glass around it starts to bend." | Target 1.5s, ±0.30s total | 1 | 20 raw; 1 Discombobulation | Standard | Long delay before the next call |

- **Secondary Actions:**
  - **Feedback Loop** — *Trigger:* the Megaphone implement is staggered. *Cooldown:* 2 rounds. It screams through the damaged brass. Unparryable, 0 raw, **1 Discombobulation to every creature in the room** — its own allies included. Breaking the megaphone halfway is a genuinely bad idea.
  - **Announce** — *Trigger:* a new enemy enters the room, or Warped Call is parried. *Cooldown:* 3 rounds. No call. Every enemy in the room immediately moves its full budget toward the player, resolved before their own actions.
- **Kitable:** Y. **Assess 0–1:** "The call's worse than the creature." · **Assess 2+:** "Break the horn and it has nothing left at all — same rule as anything that hangs its whole kit on an implement."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** ignoring support enemies. **Dismember threat:** Low.

## Monster 17 — Reel-Torn Usher

- **Archetype:** Flailer (chaotic) · **Level Range:** 10–20 · **HP:** 750 · **Move:** 4m erratic, unpredictable direction changes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** An usher still wrapped shoulder to ankle in unspooled film stock, the reels whipping loose whenever the projector behind its ribs flickers.
- **Limbs:** custom. **Head: stagger 230, ×1.5** (wound to the jaw in film stock — padded, harder than standard). **Each arm: stagger 130, ×1.0** (film rather than muscle; damage transfers cleanly). Arm sever → Triple Unspool permanently loses one beat (3→2→1). Both severed = single-beat chain. **The Projector** — implement, **isolated HP pool** (damage to it does NOT chip the Usher's main HP): ×1.5, stagger 90, sever 150. Housed in the ribs and visible through the gap. Projector stagger → Project disabled for 2 rounds. Projector sever → Project permanently disabled and Filmstrip Snap drops to 10 raw. **Legs:** standard (300, ×0.75).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Filmstrip Snap | Light | "A loose reel lashes without warning." | None — unparryable chip | N/A | 20 raw | Standard | N/A |
| Triple Unspool | Heavy (chain) | "All three reels draw taut at once, then whip out in sequence." | **3 sequential windows: 0.80s · 1.30s · 1.80s, each ±0.20s base** | 3 | 30 raw per unparried window (90 if all three land) | Standard | Chain continues from the missed beat |

**Triple Unspool — the ballistic chain** *(same archetype rule as the Bathhouse Flailer's Frenzied Whirl, reskinned)*: three windows resolved back to back, one stopwatch each, restarting from 0 at each beat.
- **All three parried →** Tier 1 Open. It collapses out of the whip, the weak point is Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9) — not automatic.
- **Miss any window →** take that beat's 30 raw and every remaining beat automatically. No partial credit, no opening.
- Parried beats deal no damage and don't open it on their own — only the full three do.

- **Secondary Actions:**
  - **Splice** — *Trigger:* an arm is severed. *Cooldown:* 3 rounds. No attack. It knots loose film into the stump: the arm is restored and Triple Unspool returns to three beats. Twice per encounter maximum.
  - **Project** — *Trigger:* the player successfully parried anything in the previous round. *Cooldown:* 3 rounds. No attack. The projector behind its ribs throws a life-size duplicate of the Usher onto the wall. For 2 rounds the DM narrates **two** Filmstrip Snap tells per round; one is false, and parrying the false one wastes the round's Hold. Assess 2+ states plainly that this is happening; it never states which is which.
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

- **Secondary Actions:**
  - **Learn** — *Trigger:* the player takes the same Action type (attack / Hold / item) two rounds running. *Cooldown:* 2 rounds. No attack — it copies that Action instead. If the player Held, the Reflection Holds: the player's next attack against it must land outside a ±0.13s parry window or be parried outright, costing the attack and granting the Reflection a free Mirrored Riposte.
  - **Shatter Out** — *Trigger:* below 30% HP. *Cooldown:* once per encounter. Once. It steps back into the glass and every mirror in the hall cracks at once: 30 raw to everything in the room, itself included. It re-emerges anywhere in the room at full movement, with The Seam untargetable for one round.
- **Kitable:** N — it matches movement 1:1; it will always be exactly as fast as Lloyd is.
- **Assess 0–1:** "It's not attacking first. Ever. It's waiting on you to move." · **Assess 2+:** "It's running your own kit back at you a half-beat late. The Seam is the one place its timing genuinely never lines up."
- **White Salts drop:** 55. **Insight:** +1/+1.
- **Boss Gimmick:** The Effigy parries and viscerals like a real opponent — the genuine boss-tier exception to the standing rule that standard archetypes can't (Ruleset §16/§9). It also initiates its own visceral off a missed player parry, mirroring the exact system back. Sever the Seam and the copy shatters outright, fight ends regardless of remaining HP. **Threshold 250 at ×1.75 ≈ 143 raw in one hit** (per Ruleset §10's threshold ÷ multiplier) — reachable, not trivial, at current gear. Sever is never required (Ruleset §3); pure attrition still ends it.
- **Habit punished:** leading every exchange the same way twice — it's had one rep to learn it by the second attempt. **Dismember threat:** Moderate (nothing overtly bisecting, but the parry loop punishes greed hard). **Retreat always reachable:** Y, though it will follow at exactly your own pace.

## Monster 19 — The Sackcloth Verger

- **Archetype:** Shambler (mook) · **Level Range:** 1–15 · **HP:** 240 · **Move:** 3m constant shuffle, no burst/recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A relic-keeper's under-robe, stiff with gold leaf flaking off in sheets, shuffling the same slow circuit it walked in life — venerating icons that were sold off a century ago.
- **Limbs:** standard defaults, no deviations. Not sever-immune. Soft target — it dies before the headshot loop matters, and the interesting decision here is positional, not anatomical.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Gilded Grasp | Light | None — unparryable, no windup | N/A | N/A | 0 raw; 1 Influence stack | Standard | N/A — outside 3m it just doesn't land |

- **Secondary Actions:**
  - **Venerate** — *Trigger:* it has taken no damage for two consecutive rounds. *Cooldown:* 3 rounds. No attack. It kneels before an icon-niche that has been empty for a century and the gold leaf comes off it in sheets: 1 Influence, no save, to every creature within 4m, and the Verger heals 20 HP.
  - **Break Circuit** — *Trigger:* the player is physically standing between the Verger and the niche it is walking toward. *Cooldown:* 2 rounds. It abandons the shuffle. Unparryable, 20 raw + 2 Influence with both arms. Standing in its way is the only thing that makes it dangerous, and it is the only thing that stops it healing.
- **Kitable:** Y — slowest move budget in the game.
- **Assess 0–1:** "It's slow. It won't hit hard." · **Assess 2+:** "Same shuffle as anything in this family. Stagger a leg, take the head after."
- **White Salts drop:** 5 (the floor). **Insight:** +1/+0.

## Monster 20 — Powdered Deacon

- **Archetype:** Shambler (mook) · **Level Range:** 1–15 · **HP:** 260 · **Move:** 3m constant shuffle, no burst/recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Soot-caked robes packed with decades of loose gunpowder dust. The grasp itself does nothing — the residue it leaves keeps eating long after contact ends.
- **Limbs:** standard defaults, no deviations. Soft target — it dies before the headshot loop matters. **Note what it is packed with before choosing a damage type** (see Secondary Actions).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Sooted Grasp | Light | None — unparryable, no windup | N/A | N/A | 0 raw; 1 Corrosion stack | Standard | N/A — outside 3m it just doesn't land |

- **Secondary Actions:**
  - **Touch Off** — *Trigger:* any Burning stack lands on it. *Cooldown:* once per encounter. Once, and terminally. The packed powder goes up: **45 raw + 3 Corrosion to everything within 3m**, the Deacon included, which kills it outright. The manual's cleanest argument for looking at a robe before reaching for fire.
  - **Shed Dust** — *Trigger:* the player is more than 4m away. *Cooldown:* 2 rounds. No grasp. It beats its robes out: a 3m cloud settles where it stands, applying 1 Corrosion per round to anything inside it for 3 rounds.
- **Kitable:** Y. **Assess 0–1:** "Don't let the dust get on you — that's the whole fight." · **Assess 2+:** "Same floor-tier shuffle as always. The Corrosion's the only thing worth respecting."
- **White Salts drop:** 5. **Insight:** +1/+0.

## Monster 21 — Loom-Handed Weaver

- **Archetype:** Lunger (mook) · **Level Range:** 1–20 · **HP:** 360 · **Move:** 3m stalking pace, single 5m lunge after a short pause then a recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Fingers fused into a shuttle, still working threads that snapped off the loom decades ago. The lunge is the same motion its hands never stopped making.
- **Limbs:** custom. **Head:** standard (180, ×1.5). **Shuttle hand: stagger 120, ×1.2** (fingers fused into a wooden shuttle; the wood-to-bone join never healed and never will). Sever → Shuttle Strike, Warp the Floor and Draw Tight all permanently disabled. Threads already laid remain. **Off arm:** standard (200, ×0.65). **Legs:** standard (300, ×0.75).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Shuttle Strike | Heavy | "The shuttle-hand draws back with a mechanical click." | Target 1.2s, ±0.20s | 1 | 40 raw; 1 Bleeding stack | Standard | Long recovery, re-threading itself |

- **Secondary Actions:**
  - **Warp the Floor** — *Trigger:* Shuttle Strike is parried. *Cooldown:* 3 rounds. It runs thread across the room instead of recovering: two 4m lines drawn between fixed points. Crossing one costs 2m and 1 Bleeding. They last the encounter and **cannot be cut by Point attacks** (§10) — an Arc attack declared against a line destroys it.
  - **Draw Tight** — *Trigger:* the player is standing on or across one of its threads. *Cooldown:* 2 rounds. No attack. It hauls: the player is dragged 3m along the thread toward the Weaver. No save, no damage, no way to decline.
- **Kitable:** Y. **Assess 0–1:** "Only dangerous once it commits." · **Assess 2+:** "Wait for the click. Dodge the strike, punish the recovery."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** panic-dodging too early. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 22 — Gaslit Orderly

- **Archetype:** Lunger (mook) · **Level Range:** 1–20 · **HP:** 380 · **Move:** 3m stalking pace, single 5m lunge after a short pause then a recovery beat · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A surgical orderly still in a gaslit apron, scalpel grown straight through the palm. Steps in with the same clinical patience it once used on patients.
- **Limbs:** custom. **Head:** standard (180, ×1.5). **Scalpel hand: stagger 110, ×1.2** (the blade grew straight through the palm and the palm never closed around it). Sever → Clinical Thrust and Triage both permanently disabled — the Orderly can neither cut nor mend. **Off arm:** standard (200, ×0.65). **Legs:** standard (300, ×0.75).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Clinical Thrust | Heavy | "It steadies its grip before driving the scalpel forward." | Target 1.3s, ±0.20s | 1 | 40 raw; 1 Bleeding stack | Standard | Long recovery, blade caught on bone |

- **Secondary Actions:**
  - **Triage** — *Trigger:* another enemy within 4m is below half HP. *Cooldown:* 3 rounds. No attack. It works on the ally instead: 60 HP restored and one staggered limb cleared. Clinical, unhurried, and the reason it should never be left for last.
  - **Dose** — *Trigger:* the player has 3 or more Bleeding stacks. *Cooldown:* 3 rounds. Unparryable, 0 raw. Forces an Insanity save at +2 DC. It is not trying to kill anyone. It believes it is helping.
- **Kitable:** Y. **Assess 0–1:** "Only dangerous once it commits." · **Assess 2+:** "Wait for the grip, dodge the thrust, punish the recovery."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** panic-dodging too early. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 23 — Coalback Skitterer

- **Archetype:** Burster (skirmisher) · **Level Range:** 5–25 · **HP:** 500 · **Move:** 3m idle scrabble, 8m surge / ~1m recovery on the lunge · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Something that learned to move in absolute dark, coiled tight against a seam wall until the lamp swings away. Then it isn't there anymore.
- **Limbs:** custom. **Head: stagger 220, ×1.5** (low, plated, and carried behind the forelimbs). **Forelimbs, each: stagger 130, ×1.0.** Sever one → Dark Surge's reach drops from 8m to 4m. Sever both → Dark Surge permanently disabled. **Legs: stagger 180, ×0.9.** Sever → reduced to a 2m crawl, no surge, and it can no longer re-enter concealment.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Dark Surge | Heavy | "A scrape of coal, then silence — it's already coiled." | Target 1.3s, ±0.20s | 1 | 45 raw | Standard | Long recovery, scrabbling back into the dark |

- **Secondary Actions:**
  - **Douse** — *Trigger:* it has been struck twice this encounter. *Cooldown:* 4 rounds. No attack. It smothers the nearest light source: for 3 rounds every Ambush DC in the room rises by 4, and the Skitterer re-enters concealment as part of this action.
  - **Coil** — *Trigger:* Dark Surge is parried. *Cooldown:* 2 rounds. No attack. It retreats its full budget to a seam in the wall and coils. Next round's Dark Surge resolves as an **ambush** (Ruleset §10, Ambush Perception) rather than a telegraphed attack.
- **Kitable:** Partial — Y between bursts, N mid-surge. **Assess 0–1:** "It's not fast. It's a spring." · **Assess 2+:** "It needs dark to close the gap. Keep a light on it and the surge never lines up."
- **White Salts drop:** 12. **Insight:** +1/+0. **Habit punished:** standing in full dark near a wall. **Dismember threat:** Moderate.

## Monster 24 — Reliquary Imp

- **Archetype:** Burster (skirmisher) · **Level Range:** 5–25 · **HP:** 460 · **Move:** 3m twitching idle, 8m surge / ~1m recovery on the lunge · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A gilt devotional figure, small enough to fit a shelf — until it isn't on the shelf anymore.
- **Limbs:** custom. **Head: guarded** — the figure keeps its head tucked into its own chest cavity between lunges. Not targetable except in the round immediately after Gilt Lunge resolves, hit or parried. Once exposed: stagger 155, ×1.5 — **softer than standard, and the reason to bait the lunge at all.** **Arms: stagger 150, ×1.0** (thin cast gold, hollow). Sever → Gilt Lunge permanently disabled. **Legs: stagger 200, ×1.0.** Sever → it can no longer Play Statue or re-conceal.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Gilt Lunge | Heavy | "The gold figure's joints creak taut." | Target 1.3s, ±0.20s | 1 | 45 raw | Standard | Long recovery, joints locked |

- **Secondary Actions:**
  - **Play Statue** — *Trigger:* below 40% HP. *Cooldown:* 3 rounds. It goes rigid and shelf-shaped. Untargetable, takes no action, and ends the moment it is struck by an area attack or the player moves within 1m. If undisturbed for a full round it regains 80 HP and re-enters concealment.
  - **Gild** — *Trigger:* Gilt Lunge is parried. *Cooldown:* 3 rounds. No attack. It smears gold leaf across its own joints: incoming raw ×0.75 for 3 rounds, and its Head stagger threshold rises to 260 for the same duration.
- **Kitable:** Partial — Y between bursts, N mid-surge. **Assess 0–1:** "It's not fast. It's a spring." · **Assess 2+:** "Everything happens on the coil. Move the instant the joints lock, not after."
- **White Salts drop:** 12. **Insight:** +1/+0. **Habit punished:** standing still after its first miss. **Dismember threat:** Moderate.

## Monster 25 — Sedated Whisperer

- **Archetype:** Chanter (caster) · **Level Range:** 1–20 · **HP:** 320 · **Move:** 3m drifting glide, always hangs back, never closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A patient strapped to a gurney, no longer breathing in any way that matters, still murmuring sedation-talk that was never meant for anyone conscious.
- **Limbs:** standard defaults, no deviations — soft target, nothing to armour, dies before the headshot loop matters. **Note:** the gurney straps are scenery, not an implement, right up until Wake fires.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Sedation Murmur | Ranged/Aura | None — unparryable, always lands in range | N/A | N/A | 0 raw; 1 Insanity stack (DM may substitute Influence, per the archetype's dual pressure) | N/A | N/A |

- **Secondary Actions:**
  - **Increase the Dose** — *Trigger:* the player passed an Insanity or Influence save in the previous round. *Cooldown:* 2 rounds. Unparryable, no damage. The player's next such save this encounter is at **+3 DC**. Stacks with itself up to +6. Passing saves is not a way out of this.
  - **Wake** — *Trigger:* below 25% HP. *Cooldown:* once per encounter. Once. The straps tear. It stops murmuring entirely — the aura ends — gains 4m of Move, and for the rest of the encounter has a single Heavy: **Unsedated (target 1.15s, ±0.15s, Tier 2, 50 raw + 2 Insanity)**. Killing it slowly is how this happens.
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

- **Secondary Actions:**
  - **Patch Through** — *Trigger:* two or more other enemies are in the room. *Cooldown:* 3 rounds. No attack. It connects them. Until it dies, **any Influence applied to one enemy in the room is applied to all of them** — including Influence the player inflicts, which is the entire point and which Assess 2+ states outright.
  - **Crossed Line** — *Trigger:* it takes damage from a ranged attack. *Cooldown:* 2 rounds. Unparryable, 0 raw. The player's next attack this encounter resolves against a target of the DM's choosing within 3m of the intended one. Announced before the player commits, never after.
- **Kitable:** N/A — no melee attack to kite; correct play is closing distance and killing it fast.
- **Assess 0–1:** "It isn't attacking you, exactly." · **Assess 2+:** "No tell because there's nothing to parry. Kill it before the stacks matter."
- **White Salts drop:** 10. **Insight:** +1/+0. **Habit punished:** ignoring it because "it isn't attacking." **Dismember threat:** Low.

## Monster 27 — Plume-Choked Keeper

- **Archetype:** Spitter (controller) · **Level Range:** 1–20 · **HP:** 320 · **Move:** 3m retreating shuffle, keeps distance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** An aviary-keeper's throat gone to down and hollow bone. Every cough throws a storm of feather-barbs, fine enough to work under skin.
- **Limbs:** standard defaults, no deviations. Soft target — dies before the headshot loop matters.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Plume Cough | Ranged | "Its chest swells, feathers already leaking from the seams." | Target 1.6s, ±0.20s | 1 | 30 raw; 2 Corrosion stacks | Standard | Stands exposed, coughing through its own storm |

- **Secondary Actions:**
  - **Down Cloud** — *Trigger:* the player closes to within 3m. *Cooldown:* 3 rounds. No cough. A 4m sphere of down fills the space, breaking line of sight both ways for 2 rounds. No parry may be attempted through it by anyone, in either direction.
  - **Barb Bloom** — *Trigger:* the player has 3 or more Corrosion stacks. *Cooldown:* 3 rounds. Unparryable. Every Corrosion stack on the player deals its damage again immediately, and the Keeper heals for half that total.
- **Kitable:** N. **Assess 0–1:** "Closing the gap is safer than staying at range." · **Assess 2+:** "Rush it during the swell."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** backpedalling constantly. **Dismember threat:** Low.

## Monster 28 — Pulp-Throated Presser

- **Archetype:** Spitter (controller) · **Level Range:** 1–20 · **HP:** 340 · **Move:** 3m retreating shuffle, keeps distance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Throat packed solid with wet pulp gone dry and papery. The cough throws shredded fiber that catches in a wound and keeps working itself deeper.
- **Limbs:** standard defaults, no deviations. Soft target — dies before the headshot loop matters, though Set (Secondary Actions) will make a badly-timed commitment feel otherwise.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Pulp Cough | Ranged | "Its throat rattles, dry fiber already sifting loose." | Target 1.6s, ±0.20s | 1 | 30 raw; 2 Corrosion stacks | Standard | Stands exposed, coughing through the drift |

- **Secondary Actions:**
  - **Pack the Wound** — *Trigger:* the player has 1 or more Bleeding stacks. *Cooldown:* 2 rounds. Unparryable, 0 raw. **Converts 2 Bleeding stacks into 3 Corrosion stacks.** Strictly worse for the player, and a real decision about which track to manage first.
  - **Set** — *Trigger:* below 50% HP. *Cooldown:* 4 rounds. No attack. The pulp hardens across its whole body: incoming raw ×0.6 for 3 rounds, during which all of its own attacks are disabled. A window that costs it nothing to open and everything to hold.
- **Kitable:** N. **Assess 0–1:** "Closing the gap is safer than staying at range." · **Assess 2+:** "Rush it during the rattle."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** backpedalling constantly. **Dismember threat:** Low.

## Monster 29 — Seam-Breaker

- **Archetype:** Brute (heavy) · **Level Range:** 20–70 · **HP:** 2200 · **Move:** 4m slow, deliberate advance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Something that used to break coal for a living, and never really clocked out. Swings a pick the length of a man.
- **Limbs:** custom. **Head: stagger 300, ×1.5** (helmeted in fused coal and scale — reinforced well past standard). **Pick arm: stagger 240, ×1.1** (overbuilt by a lifetime of the same swing; tough, but damage transfers well when it lands). Sever → Seam Swing permanently disabled and **the pick becomes claimable on the floor.** **Off arm: stagger 150, ×0.8** — a trap target. Cheap to break, attached to nothing, achieves nothing. **Legs: stagger 220, ×1.0** (braced stance, permanently load-bearing). Sever → grounded to 1m, but its reach and swing arc are unchanged.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Seam Swing | Heavy | "It plants both feet, pick raised past its own shoulder." | Target 2.0s, ±0.20s | 2 | 90 raw | Standard | Long stationary recovery, pick buried in stone |

- **Secondary Actions:**
  - **Break the Seam** — *Trigger:* Seam Swing is parried. *Cooldown:* 3 rounds. It swings at the floor instead of recovering. A 3m fissure opens where the player is standing: Skill DC 13 to avoid, failure means 40 raw and being pinned in the fissure until a full Action is spent climbing out.
  - **Wedge** — *Trigger:* the pick arm is severed, or the pick is staggered. *Cooldown:* once per encounter. It drives the pick into the wall and leaves it there. **The pick becomes a claimable weapon on the floor.** The Seam-Breaker fights on bare-handed: 45 raw, target 1.30s ±0.20s — weaker, faster, and considerably harder to read.
- **Kitable:** Y in principle — it's enormous, and enormous is slow. **Assess 0–1:** "It's huge. It's also slow enough to just not be there when it lands." · **Assess 2+:** "Sever a leg and the approach stops being a threat at all."
- **White Salts drop:** 35. **Insight:** +1/+0. **Habit punished:** trading hits at melee range while under-levelled — genuine bisect threat. **Dismember threat:** Very High. **Retreat always reachable:** Y.

## Monster 30 — Frost-Iron Smith

- **Archetype:** Brute (heavy) · **Level Range:** 15–55 · **HP:** 1600 · **Move:** 4m slow, deliberate advance · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A smith frozen mid-strike when the forge finally went cold for good. The hammer still glows faintly with a heat that never quite left the iron.
- **Limbs:** custom. **Head:** protected by the **Forge Mask** — implement, **isolated HP pool**, stagger 100, no sever (it is knocked off, not destroyed). While masked, head stagger threshold is 300. Unmasked: standard 180, ×1.5. Two-phase head targeting. **Hammer arm: stagger 280, ×0.8** (overdeveloped and heat-hardened — tougher than standard and it gives up little). Sever → Cold Hammer permanently disabled. **Tongs arm: stagger 100, ×0.65** (worn, underworked, the weakest point on the body). Sever → the Smith reels (1 turn Discombobulation), but no attack was ever on this arm. **A trap target — easy to hit, achieves almost nothing.** **Legs: stagger 200, ×0.9** (weight-bearing under forge posture, weaker than standard). Sever → grounded, and its approach stops being a threat.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Cold Hammer | Heavy | "The hammer arm rises past its shoulder, trailing frost off dying heat." | Target 2.0s, ±0.20s | 2 | 90 raw; 1 Burning stack | Standard | Long stationary recovery, hammer stuck to the anvil |

- **Secondary Actions:**
  - **Quench** — *Trigger:* it has 2 or more Burning stacks, or it is below 50% HP. *Cooldown:* 4 rounds. It plunges the hammer into its own chest. All Burning cleared, 100 HP restored, and Cold Hammer's Burning application rises from 1 to 2 for the rest of the encounter.
  - **Draw the Heat** — *Trigger:* any creature within 6m has 3 or more Burning stacks. *Cooldown:* 3 rounds. Unparryable, no damage. It pulls every Burning stack in the room onto itself and converts each into 15 HP healed. Fire is the wrong tool in this fight and this is how the player finds out.
- **Kitable:** Y in principle. **Assess 0–1:** "It's huge. It's also slow enough to just not be there when it lands." · **Assess 2+:** "Sever a leg and the approach stops being a threat at all."
- **White Salts drop:** 35. **Insight:** +1/+0. **Habit punished:** trading hits at melee range while under-levelled. **Dismember threat:** Very High. **Retreat always reachable:** Y.

## Monster 31 — Wire-Boned Falconer

- **Archetype:** Drudge (elite) · **Level Range:** 5–20 · **HP:** 720 · **Move:** 3m relentless walk, never sprints · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A falconer whose arm rebuilt itself in wire and feather after the bird it once carried finished the job. Never stops advancing, never speeds up either.
- **Limbs:** custom. **Head: stagger 240, ×1.5** (hooded in stiffened leather — reinforced past standard). **Wire arm: stagger 150, ×1.2** (wire and hollow feather-bone; light, and it rings when struck). Sever → Wire-Boned Backhand permanently disabled **and Cast Off can never fire.** The tempo decision of the fight: take the arm early, or spend the encounter fighting two things. **Off arm:** standard (200, ×0.65). **Legs:** standard (300, ×0.75).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Wire-Boned Backhand | Heavy | "The wire arm swings wide with an audible creak." | Target 1.2s, ±0.25s | 1 | 55 raw | Standard | Long recovery re-settling its stance |

- **Secondary Actions:**
  - **Cast Off** — *Trigger:* the wire arm is staggered. *Cooldown:* 4 rounds. The wire-and-feather mass detaches and becomes a **separate creature: 120 HP, Move 9m flight, unparryable 20 raw per round.** The Falconer continues one-armed at 40 raw. Two problems where there was one.
  - **Recall** — *Trigger:* the detached bird is below 40 HP and the Falconer is above 50% HP. *Cooldown:* 3 rounds. No attack. The bird returns to the arm: both heal 60 HP and the arm's stagger clears. Kill the bird or kill the Falconer — leaving both alive resets the fight.
- **Kitable:** Y. **Assess 0–1:** "Slow, but it never stops coming." · **Assess 2+:** "Fully readable, fully punishable."
- **White Salts drop:** 15. **Insight:** +1/+0. **Habit punished:** greedy attacks after the tell begins. **Dismember threat:** High.

## Monster 32 — Anvil-Bound Apprentice

- **Archetype:** Drudge (elite) · **Level Range:** 10–20 · **HP:** 760 · **Move:** 2m deliberate advance, pauses after every attack · **Scale Band:** 1–20 (×1.0)
- **Flavour:** An apprentice still chained wrist-to-anvil, dragging the whole iron block behind it with every step, never once slowing to compensate.
- **Limbs:** custom. **Head:** standard (180). **Chain arm (anvil-chained): stagger 250** (the chain reinforces the arm — tougher than standard). Arm sever → Anvil Drag-Swing disabled, chain and anvil become a floor obstacle. **Free arm: stagger 130** (weak, unworked — easy to take off, but no attack on this arm; a trap target that achieves little). **Legs:** standard (300).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Anvil Drag-Swing | Target 1.3s, ±0.25s | 2 | 60 raw | Standard | Long recovery dragging the anvil back into line |

- **Secondary Actions:**
  - **Anchor** — *Trigger:* it was staggered, knocked down or parried in the previous round. *Cooldown:* 3 rounds. It sets the anvil and braces. Immune to stagger and knockdown for 2 rounds, Move drops to 0m, and its swing arc shortens to 2m. Parrying it stops being progress and becomes a waiting game.
  - **Slip the Chain** — *Trigger:* below 30% HP. *Cooldown:* once per encounter. Once. It tears its own wrist out of the cuff — the chain arm is lost permanently, exactly as though severed — and moves at 6m for the rest of the encounter with a bare 35-raw strike at 1.10s ±0.15s. No longer draggable, no longer slow.
- **Kitable:** Y. **Assess 0–1:** "Every hit hurts. Every swing is slow." · **Assess 2+:** "Its recovery is longer than its attack — survive one, answer with several."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** trading hits. **Dismember threat:** High.

## Monster 33 — Fuse-Throated Crier

- **Archetype:** Toller (mook) · **Level Range:** 1–20 · **HP:** 280 · **Move:** 2m slow walk, rarely closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Throat packed with a slow-burning fuse instead of a voice box. Every call is timed to a sputter that never quite reaches detonation.
- **Limbs:** standard defaults, plus non-standard: **Fuse-Horn** — limb, not an implement (embedded in the throat, part of the body). Multiplier ×2.0, stagger/sever threshold 30. Damage to the Fuse-Horn chips the Crier's main HP (raw × 2.0). Sever → Sputtered Call permanently disabled, throat destroyed.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Sputtered Call | Aura | "The fuse in its throat catches, sputtering toward a call." | Target 1.4s, ±0.30s total | 1 | 20 raw; 1 Burning stack | Standard | Long delay before the fuse catches again |

- **Secondary Actions:**
  - **Reach Detonation** — *Trigger:* Sputtered Call has been parried twice this encounter, or the Fuse-Horn is staggered. *Cooldown:* once per encounter. Once. The fuse finally gets where it was going: **60 raw + 3 Burning to everything within 4m**, the Crier included, and the Fuse-Horn is destroyed. It survives. It simply has nothing left to say.
  - **Pass the Light** — *Trigger:* another enemy is within 3m. *Cooldown:* 3 rounds. No call. It touches the fuse to an ally: that enemy takes 2 Burning and gains **+20 raw on its next attack**. It sets fires it does not need to be alive to see.
- **Kitable:** Y. **Assess 0–1:** "The call's worse than the creature." · **Assess 2+:** "Break the horn and it has nothing left at all."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** ignoring support enemies. **Dismember threat:** Low.

## Monster 34 — The Squall Box

- **Archetype:** Toller (mook) · **Level Range:** 1–20 · **HP:** 320 · **Move:** 2m slow walk, rarely closes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A cracked speaker cabinet strapped to its chest like a breastplate, still wired into whatever's left of its own throat.
- **Limbs:** standard defaults, plus non-standard: **Speaker Cabinet** — implement, not a limb (Ruleset §10): isolated HP pool, multiplier ×2.0, sever threshold 40. Damage to the cabinet does NOT chip the Squall Box's main HP. Breaking it disables Feedback Squall for the encounter.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Feedback Squall | Aura | "The cabinet crackles, building toward a squall." | Target 1.5s, ±0.30s total | 1 | 20 raw; 1 Discombobulation | Standard | Long delay before the next squall |

- **Secondary Actions:**
  - **Dead Air** — *Trigger:* the Speaker Cabinet implement is staggered. *Cooldown:* 3 rounds. No attack. The room goes silent. **For 2 rounds no tells are narrated for any enemy in the room** — every parry attempt in that window is made blind, on timing alone. Assess 2+ warns that damaging the cabinet does this.
  - **Overdrive** — *Trigger:* below 40% HP. *Cooldown:* once per encounter. Once. It routes everything through the cracked cabinet. Feedback Squall becomes an unparryable aura for the rest of the encounter: 15 raw + 1 Discombobulation every round to everything within 5m, while the Box takes 10 self-damage per round doing it.
- **Kitable:** Y. **Assess 0–1:** "The call's worse than the creature." · **Assess 2+:** "Break the cabinet and it has nothing left at all."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** ignoring support enemies. **Dismember threat:** Low.

## Monster 35 — Shuttle-Armed Weaver

- **Archetype:** Flailer (chaotic) · **Level Range:** 10–20 · **HP:** 760 · **Move:** 4m erratic, unpredictable direction changes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Four loom-shuttles grown fused to its limbs, each trailing a length of thread sharp enough to open skin. It doesn't move so much as it's operated.
- **Limbs:** custom. **Head: stagger 230, ×1.5** (thread-wound to the jaw). **Each shuttle arm, four of them: stagger 120, ×1.0** (the shuttles are fused on; the fusion is the weak part). Sever → Full Weave permanently loses one beat, to a floor of one. **Re-Thread restores beats but never restores a severed arm** — it can only replace what it still has sockets for. **Legs:** standard (300, ×0.75).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Thread Snap | Light | "A loose shuttle-thread snaps without warning." | None — unparryable chip | N/A | 20 raw | Standard | N/A |
| Full Weave | Heavy (chain) | "All four shuttles draw back in unison, then fire in sequence." | **3 sequential windows: 0.80s · 1.30s · 1.80s, each ±0.20s base** | 3 | 30 raw per unparried window (90 if all three land) | Standard | Chain continues from the missed beat |

**Full Weave — the ballistic chain** *(same archetype rule as the Bathhouse Flailer's Frenzied Whirl, reskinned)*: three windows resolved back to back, one stopwatch each, restarting from 0 at each beat.
- **All three parried →** Tier 1 Open, the weak point is Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9) — not automatic.
- **Miss any window →** take that beat's 30 raw and every remaining beat automatically. No partial credit, no opening.
- Parried beats deal no damage and don't open it on their own — only the full three do.

- **Secondary Actions:**
  - **Cross-Weave** — *Trigger:* another enemy is within 5m. *Cooldown:* 3 rounds. No attack. It stitches thread between itself and that ally: while both live, **all damage dealt to either is split evenly between them.** The thread is destroyed by an Arc attack (§10) declared against it, or by killing either end.
  - **Re-Thread** — *Trigger:* it has fewer than four shuttles remaining. *Cooldown:* 4 rounds. No attack. It draws a replacement shuttle out of its own torso: Full Weave's beat count rises by one, to a maximum of three.
- **Kitable:** N. **Assess 0–1:** "Stay calm. It isn't." · **Assess 2+:** "The weave isn't one attack, it's three. Read all of them or none."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** staying glued to its sides. **Dismember threat:** High.

## Monster 36 — Ream-Wrapped Binder

- **Archetype:** Flailer (chaotic) · **Level Range:** 10–25 · **HP:** 780 · **Move:** 4m erratic, unpredictable direction changes · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Wrapped shoulder to wrist in reams of uncut paper, each sheet honed razor-sharp at the edge by decades of the same motion repeated.
- **Limbs:** custom. **Head: stagger 250, ×1.5** (packed in reams to the crown). **Each arm: stagger 135, ×1.0** (paper, not muscle). Sever → Ream Cascade permanently loses one beat. **The Spine: stagger 160, ×1.3** — a bound block of uncut sheets stitched down its back where all the wrappings meet. **Only targetable from behind.** Spine sever → every wrapping falls away at once: Paper Cut and Ream Cascade both permanently disabled, and the Binder fights on bare at 20 raw unparryable. **Legs:** standard (300, ×0.75).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Paper Cut | Light | "A loose sheet slices without warning." | None — unparryable chip | N/A | 20 raw | Standard | N/A |
| Ream Cascade | Heavy (chain) | "Both arms draw the reams taut, then release in sequence." | **3 sequential windows: 0.80s · 1.30s · 1.80s, each ±0.20s base** | 3 | 30 raw per unparried window (90 if all three land) | Standard | Chain continues from the missed beat |

**Ream Cascade — the ballistic chain** *(same archetype rule, reskinned)*: three windows resolved back to back, one stopwatch each, restarting from 0 at each beat.
- **All three parried →** Tier 1 Open, the weak point is Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9) — not automatic.
- **Miss any window →** take that beat's 30 raw and every remaining beat automatically. No partial credit, no opening.
- Parried beats deal no damage and don't open it on their own — only the full three do.

- **Secondary Actions:**
  - **Bind** — *Trigger:* Ream Cascade is fully parried. *Cooldown:* 4 rounds. The Tier 1 Open is granted as normal — this does not take it away. But the player's movement budget is **0m** next round and no weapon swap is possible for that round. The opening is real and it is paid for.
  - **Dry Out** — *Trigger:* it has 1 or more Burning stacks at the start of the Enemy Phase. *Cooldown:* 2 rounds. It sheds the outer reams in a single burning sheet. All Burning cleared from it, and a 3m fire zone (2 Burning per round, 3 rounds) is left where it was standing.
- **Kitable:** N. **Assess 0–1:** "Stay calm. It isn't." · **Assess 2+:** "The cascade isn't one attack, it's three. Read all of them or none."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** staying glued to its sides. **Dismember threat:** High.

## Monster 37 — The Foundry Marshal *(boss, Cold Forge)*

- **Archetype:** Foundry (boss, heavy/reach-chain) · **HP:** 1400 (hand-set, exempt from scaling) · **Move:** 3m, never sprints, never retreats — but its swing radius reaches well past where its footsteps suggest.
- **Flavour:** Once oversaw the whole forge floor. Now its ribs are the furnace, and everything it swings is still hot from the inside.
- **Limbs:** standard defaults + **The Furnace Door** (weak point, chest) — multiplier ×1.75, sever 300. **Head: stagger 250** (furnace-built, thick). **Each arm:** standard (200). Arm sever → Marshal's Cross disabled (needs both arms for the crossing swing), but Foundry Reckoning (chest-based) still functions. Severing arms removes the simpler attack without ending the fight.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Marshal's Cross | Heavy | "It plants both feet, both arms crossing before a wide double swing." | Target 1.8s, ±0.20s | 1 | 70 raw; 1 Burning stack |
| Foundry Reckoning | Heavy (chain) | "The furnace door in its chest cracks open, venting three pulses of heat in sequence." | **3 sequential windows: 0.90s · 1.40s · 1.90s, each ±0.15s** | 3 | 40 raw per unparried window (120 if all three land), +1 Burning stack per landed window |

- **Secondary Actions:**
  - **Bank the Furnace** — *Trigger:* The Furnace Door takes any damage. *Cooldown:* 3 rounds. The door slams. No attack; The Furnace Door is untargetable next round, and the Marshal's next Marshal's Cross applies 3 Burning instead of 1.
  - **Stoke** — *Trigger:* Foundry Reckoning is fully parried. *Cooldown:* 4 rounds. The Tier 1 Open still stands. But it feeds the furnace with the round it would have spent recovering: **heals 120 HP, and every Burning stack currently on the player is doubled.** The opening costs something; it is not cancelled.
  - **Call the Floor** — *Trigger:* below 40% HP with fewer than two other enemies in the room. *Cooldown:* 5 rounds. No attack. It hammers the floor plate three times, and **two Anvil-Bound Apprentices arrive from the rail spur** at the start of the following round.
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

- **Secondary Actions:**
  - **Recast** — *Trigger:* The Crack takes any damage. *Cooldown:* 3 rounds. It pours fresh bronze into its own fault line: **The Crack's accumulated stagger progress resets to zero** and the Bellfounder heals 80 HP. The Crack cannot be closed — but it can be delayed forever by a player who never commits enough in a single hit.
  - **Overtone** — *Trigger:* the player has 4 or more Influence stacks. *Cooldown:* 3 rounds. Unparryable, no damage. Every Influence stack on the player is applied to **every other creature in the room as well**, companions included. Sharing the load is not relief.
- **Kitable:** N/A — never moves. Breaking line of sight is the counter, same as the Singer.
- **Assess 0–1:** "It's not hunting. It's still pouring." · **Assess 2+:** "The toll's just pressure. The pour is the real fight, and it comes in three."
- **White Salts drop:** 50. **Insight:** +1/+1.
- **Boss Gimmick:** Molten Pour follows the standard chain rule — **all three parried → Tier 1 Open on The Crack**, Lloyd's to attempt via the eased ±0.25s Tier 1 stopwatch (Ruleset §9), not automatic; **miss any window → take that beat's damage/Burning and the rest automatically.** Sever The Crack (base 350 at ×2.0 = 175 raw in one hit) to end the fight regardless of remaining HP. **Distinct twist:** every time all three Molten Pour windows land uncontested, the pour itself widens The Crack — its sever threshold **permanently drops by 50** for the rest of the fight (350 → 300 → 250 → …), an escalating vulnerability rather than a static number. Otherwise pure attrition — Founding Toll never stops, Influence climbs the whole fight, save DC rising with stack count. Sever never required (Ruleset §3).
- **Habit punished:** tanking the pour in the open instead of reading all three windows. **Dismember threat:** Moderate (no melee of its own, but Burning stacks compound if the chain lands clean). **Retreat always reachable:** Y.

## Monster 39 — Handfall

- **Archetype:** Swarm (elite) · **Level Range:** 5–20 · **HP:** 450 · **Move:** 4m, flows over any surface, never climbs so much as spreads · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A low tide of pale hands, wrist-deep and cut off clean, moving together with no body to belong to. No two are the same size. They test a surface before they cross it, the way a hand tests bathwater.
- **Limbs:** **no standard limb entries at all.** Single entry below. Precision Strike cannot be declared against Handfall — there is no anatomy to be greedy about, and any Precision Strike resolves as a plain Mass hit.

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Mass|×1.0|—|—|—|**Yes**|

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Undertow | Light | None — unparryable, no windup | N/A | N/A | 15 raw + 1 Influence to every creature within 2m | N/A | N/A |
| Closing Fist | Heavy | "A dozen hands stack into a single column and cock back." | Target 1.30s, ±0.20s | 1 | 45 raw + 1 Bleeding | Standard | The column collapses; it re-forms over ~2 player actions |

- **Secondary Actions:**
  - **Scatter** — *Trigger:* it takes an Arc attack (§10) or any AOE. *Cooldown:* 3 rounds. The hands disperse across the whole room. **Handfall cannot be damaged at all this round.** It deals no damage either, and reforms at the start of the next Enemy Phase anywhere the DM chooses within the room.
  - **Donate** — *Trigger:* another enemy in the room is below 50% HP. *Cooldown:* 4 rounds. No attack. The mass flows over and **transfers 60 of its own HP to that enemy**, up to that creature's own maximum. The swarm signature: damage the player deals does not necessarily stay dealt.
  - **Carry** — *Trigger:* it has dealt 40 or more cumulative raw this encounter. *Cooldown:* 4 rounds. No attack. The column lifts something loose off the floor — a dropped weapon, an item, a corpse — and carries it to the far side of the room. If nothing is loose, it lifts the player 2m and sets them down elsewhere.
- **Kitable:** Y. **Assess 0–1:** "There's nothing to aim at." · **Assess 2+:** "It has no anatomy. Sever, stagger and Precision Strikes are all off the table — this one dies to raw HP damage and nothing else. Area damage is worth more than accuracy here."
- **White Salts drop:** 16. **Insight:** +1/+0. **Habit punished:** Precision Strike dependency. **Dismember threat:** Low. **Retreat always reachable:** Y.

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

- **Secondary Actions:**
  - **Hold Breath** — *Trigger:* either bespoke entry takes damage. *Cooldown:* 3 rounds. No attack. It inflates and holds: incoming raw ×0.4 this round and next, and the room's air stops moving — **all Corrosion ticks on every creature are suspended** for the same duration.
  - **Full Exhale** — *Trigger:* below 35% HP. *Cooldown:* 5 rounds. It empties itself completely: 3 Corrosion to every creature in the room. It then **cannot act at all for 2 rounds** while it refills. The single largest free window in the entry, bought with the single largest hit.
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

- **Secondary Actions:**
  - **Surface** — *Trigger:* the Bath has taken 300 or more cumulative damage this encounter. *Cooldown:* once per encounter. Once. Something in the water finally comes up: a separate creature — **300 HP, Move 6m, unparryable 30 raw + 1 Influence per round** — climbs out and fights alongside it. The Bath loses Slosh permanently.
  - **Right Itself** — *Trigger:* it is overturned or prone, or a leg is severed. *Cooldown:* 3 rounds. No attack. It hauls back onto its remaining feet: heals 100 HP and clears one staggered limb, but the water level drops, permanently reducing Slosh by 10 raw each time this fires.
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

- **Secondary Actions:**
  - **Peristalsis** — *Trigger:* any creature has been inside the run for three consecutive rounds. *Cooldown:* 2 rounds. No Bile Sheet. Every creature inside is moved 4m **deeper**, and the walls close to 1m width for a round: no attacks of any kind may be declared inside the run, by anyone, while it holds.
  - **Regurgitate** — *Trigger:* it takes 200 or more damage in a single round. *Cooldown:* 4 rounds. It throws everything back. All creatures inside are ejected to the nearest entrance, and whatever it swallowed previously — a corpse, a dropped item, 20 White Salts — comes out with them.
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

- **Secondary Actions:**
  - **Bask** — *Trigger:* any creature or surface within 8m is Burning. *Cooldown:* 2 rounds. No dive. It settles onto the heat and feeds: heals 15 HP per Burning stack in range, clearing those stacks as it does. It is not immune to fire. It is worse than immune.
  - **Dust the Ceiling** — *Trigger:* it has been struck by a ranged attack. *Cooldown:* 3 rounds. No attack. It climbs out of reach and shakes: for 3 rounds any Burning applied to **anything** in the room applies 2 stacks instead of 1 — enemies included, which is occasionally useful and never safe.
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
| Strike-and-Sink | Heavy | "A single ripple, moving against the current." | Target 1.05s, ±0.15s | 2 | 60 raw + 1 Bleeding | Standard | It is *out* — head exposed for the following turn |
| Constrict | Heavy — only usable if the target is standing in water | "Coils break the surface on both sides of you at once." | Target 1.70s, ±0.20s | 1 | 40 raw per turn until broken; **Strength DC 15** as an Action to escape | Standard | Releases, head exposed |

- **Secondary Actions:**
  - **Sound** — *Trigger:* it has been struck twice this encounter while in water. *Cooldown:* 3 rounds. It submerges completely. Untargetable, takes no action, and surfaces at the start of the next Enemy Phase anywhere in connected water, with its next Strike-and-Sink resolving as an **ambush** (§10).
  - **Beach** — *Trigger:* it is on dry ground and below 50% HP. *Cooldown:* 4 rounds. No attack. It drags its full 2m toward the nearest water. **If it reaches water it heals 150 HP.** Cutting it off from the sump is the entire fight and Assess 2+ says so.
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

- **Secondary Actions:**
  - **Fold** — *Trigger:* the player spends a full round more than 1m from any wall. *Cooldown:* 2 rounds. No attack. The room's geometry shifts and one wall is now 2m closer than it was. Open floor is a finite resource in this room and it is being spent.
  - **Evert Early** — *Trigger:* Reveal is parried. *Cooldown:* 4 rounds. The Tier 1 Open is granted as normal. But the Vertex withdraws immediately afterwards and is **untargetable for the following 2 rounds.** You get your swing. You do not get the one you wanted.
- **Kitable:** N/A. **Assess 0–1:** "Get off the wall." · **Assess 2+:** "It can only reach you against a wall — the middle of the room is free. It surfaces every third turn and that's when it can be killed. Stand in the open and wait for it."
- **White Salts drop:** 26. **Insight:** +1/+0. **Habit punished:** back-to-the-wall kiting, the default instinct in a room full of enemies. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 46 — The Quiet

- **Archetype:** Chanter (elite) · **Level Range:** 5–20 · **HP:** 400 · **Move:** 3m drift, never hurries · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A soft, roughly person-sized absence. Not invisible — *unlistenable*. The ear refuses it the way the eye refuses a bright light, and the refusal spreads to everything standing near it.
- **Limbs:** standard humanoid defaults, no deviations. Soft, low HP, dies fast if it is actually prioritised — the headshot loop is not a problem on a creature that dies to two of anything. **The difficulty is deciding to hit it at all**, which is a targeting problem rather than an anatomy one.
- **Deafening Absence** *(passive, 6m radius, always on):*
  - Every tell inside the radius is delivered **visually only** — the DM gives no audio component in any tell description for any enemy in the bubble.
  - **Every parry and precision window inside the radius is narrowed by 0.10s** (applied to the ± tolerance, after Insight window bonus). This is a real mechanical debuff, not flavour.
  - Ends the instant the Quiet dies. It has no other trick.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Pressure | Light | None — unparryable | N/A | N/A | 20 raw + forces an Insanity save | N/A | N/A |

- **Secondary Actions:**
  - **Deafen** — *Trigger:* the player successfully parries anything in the room. *Cooldown:* 3 rounds. No attack. For 2 rounds every tell in the room is delivered **visually only**, with no audible component, and all parry tolerances narrow by 0.05s. Assess 2+ states this outright.
  - **Spread** — *Trigger:* it has taken no damage for two consecutive rounds. *Cooldown:* 3 rounds. Its radius grows by 3m, permanently for the encounter, and **one additional creature in the room becomes unlistenable** — that enemy's tells stop being narrated at all until The Quiet dies.
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
| Bite Down | Reactive | None — unparryable. Triggers on any creature that **ends its movement** on the Tooth. | N/A | N/A | 30 raw + 2 Bleeding | N/A | N/A |

- It never attacks anything not standing on it. It has no reach, no ranged option, and infinite patience.
- **Secondary Actions:**
  - **Grow** — *Trigger:* a full round passes in which nothing ends its movement on the Tooth. *Cooldown:* once per encounter. It extends 2m toward the nearest door, permanently, and may do this repeatedly with no cooldown. Waiting it out makes the room smaller every round.
  - **Grind** — *Trigger:* a creature is standing on it at the start of the Enemy Phase. *Cooldown:* 2 rounds. Unparryable. That creature takes 20 raw and **cannot leave the Tooth this round** — the enamel closes around the boot.
- **Kitable:** N/A. **Assess 0–1:** "Don't stop walking." · **Assess 2+:** "It only bites what stands still on it. Cross it in one movement and it never gets a turn — or cut lanes and make the crossing free for good."
- **White Salts drop:** 18. **Insight:** +1/+0. **Habit punished:** breaking a long movement into two turns. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 48 — The Afterimage

- **Archetype:** Effigy (elite) · **Level Range:** 10–20 · **HP:** 550 · **Move:** 5m — always arriving at where it already was · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A person-shape assembled out of the light a person leaves behind. It is doing something right now. You will find out what next turn.
- **Limbs:** custom, and none of it is solid. **Body: ×1.0, no stagger threshold, sever-immune** — it is the light a person left behind and it does not have joints. **The Lag: ×1.6, stagger 130, sever 200** — a second, dimmer outline standing exactly one turn behind the main shape. **It is only targetable during a round in which a Delayed Strike is pending**, because that is the only time the two shapes are separated far enough to tell apart. Lag sever → every pending Delayed Strike is cancelled outright and the Afterimage cannot declare another for 3 rounds.
- **Delay** *(defining mechanic):* every attack it makes is **declared and fully telegraphed on turn N, and resolves at the start of turn N+2.** It can have up to two Delayed Strikes in flight at once.
  - The parry stopwatch is rolled on the turn the attack **lands**, not the turn it is declared.
  - The player must **commit to parrying or not before taking their turn N+1 action** — you spend your turn knowing something is coming and having already chosen.
  - Killing the Afterimage does **not** cancel strikes already in flight. They still land.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Delayed Strike | Heavy (delayed 2 turns) | "It winds up, unhurried, and then stands there wound up." | Target 1.60s, ±0.20s, rolled on the landing turn | 2 | 70 raw | Standard | Nothing — it was never really there for the miss |

- **Secondary Actions:**
  - **Second Exposure** — *Trigger:* a Delayed Strike is parried on its landing turn. *Cooldown:* 3 rounds. No new wind-up. Instead the strike replays one round later at half damage, **unparryable.** Parrying it correctly does not stop it happening; it makes it cheaper.
  - **Persist** — *Trigger:* it takes 150 or more damage in a single round. *Cooldown:* 4 rounds. No attack. All damage dealt to it this round is refunded at the start of the next round — then locked in permanently one round after that if it is still alive. Burst damage requires follow-through here.
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
| Weigh | Aura | "The dial spins up and a ticket starts feeding through the slot." Every third turn. | None — unparryable | N/A | Target takes damage equal to **their current total status-track stacks × 10** (Bleeding + Insanity + Influence + Corrosion + Burning combined). Zero stacks = zero damage. | N/A | N/A |
| Slot Arm | Heavy | "The ticket slot swings open on its arm." | Target 1.45s, ±0.20s | 1 | 55 raw | Standard | Long mechanical reset |

- **Secondary Actions:**
  - **Print a Second Ticket** — *Trigger:* the player has 6 or more total status-track stacks. *Cooldown:* 3 rounds. No attack. It prints and offers a ticket. **The player may read it as a Full Action to learn one true fact about this room or this instance.** Reading it adds 2 Insanity. It is genuinely useful and it is genuinely not free.
  - **Tare** — *Trigger:* the player has zero status-track stacks at the start of the Enemy Phase. *Cooldown:* 3 rounds. Unparryable. It applies 1 stack each of Bleeding, Corrosion and Influence. It cannot weigh nothing and it will not be given nothing to weigh.
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

- **Secondary Actions:**
  - **Scatter** — *Trigger:* it takes an Arc attack (§10) or any AOE. *Cooldown:* 3 rounds. The sheet breaks apart across the walls. **Cannot be damaged at all this round**, deals no damage either, and reforms at the start of the next Enemy Phase up to 6m from where it broke.
  - **Donate** — *Trigger:* it has applied 5 or more cumulative Corrosion stacks this encounter. *Cooldown:* 4 rounds. No attack. The sheet flows onto another enemy in the room and **transfers 80 of its own HP** to it, up to that creature's maximum. What it takes off the player, it gives to something that can use it.
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
- **The Cup is physically inaccessible until three Petals are severed** — no Precision Strike against it resolves before then, regardless of opening.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Petal Sweep | Heavy | "One petal peels back off the ceiling and comes down flat across the floor." | Target 1.35s, ±0.20s | 1 | 60 raw |
| Pollen | Aura | "The cup breathes out." Every other turn. | Unparryable | N/A | Forces an Insanity save + 1 Influence stack |
| Fold | Heavy (chain) | "Every remaining petal draws inward at once, closing around you in sequence." | **3 sequential windows: 0.75s · 1.25s · 1.85s, each ±0.20s** | 3 | 35 raw per unparried window (105 if all three land) |

- **Fold — the ballistic chain.** All three parried → **Tier 1 Open on the Cup, even if petals remain sealed** — the only route to the weak point that doesn't require dismemberment first. Miss any window → take that beat and every remaining beat automatically, no partial credit.
- **Secondary Actions:**
  - **Furl** — *Trigger:* a Petal is severed. *Cooldown:* 2 rounds. No attack. The remaining petals draw in tight: incoming raw ×0.5 this round, The Cup untargetable, and its reach **increases** by 2m for that round as the petals stretch outward.
  - **Rebud** — *Trigger:* three or more Petals severed and it took no damage in the previous round. *Cooldown:* 5 rounds. No attack. One severed Petal regrows at half its original stagger threshold and its Petal Sweep line is restored. The fight has a clock running in both directions.
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

- **The ×0.5 Shell multiplier** — every hit against the Vessel while shelled deals half raw. Being at or below ×1.0 it triggers **no Precision Strike stopwatch** (Ruleset §10), so it is safe to hit and slow to kill, deliberately.
- **Two routes through the shell:** grind it to 0 HP, or **sever it in one hit (400 at ×0.5 = 800 raw — effectively impossible; it is there to be a wall, not a target).** Either way, when the shell fails:
- **Spilled phase:** the occupant tips out — a separate creature, **250 HP, Move 7m, standard humanoid limbs, no armour, actively panicking.** It does not fight; it runs.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Tip *(shelled)* | Heavy | "It lifts one side and pours." | Target 1.55s, ±0.20s | 1 | 45 raw + 1 Corrosion | Standard | Rights itself slowly |
| Flail *(spilled)* | Light | None — unparryable | N/A | N/A | 25 raw, and it immediately moves its full 7m toward the nearest exit | N/A | N/A |

- If the occupant reaches an exit it **escapes** — no drop, no Insight, nothing. The second phase is a chase, not a fight.
- **Secondary Actions:**
  - **Seal** — *Trigger:* the occupant is spilled and reaches within 2m of the shell. *Cooldown:* 4 rounds. The occupant climbs back in. **Shell HP restores to 40% of maximum and the fight returns to phase one.** Killing the occupant before it reaches cover is the entire purpose of the spill.
  - **Alms** — *Trigger:* the player's Purse is empty. *Cooldown:* once per encounter. Once. The shell tips and pours **25 White Salts** onto the floor between them. Picking them up is a Full Action inside its reach. It is not a trick. It is worse than a trick.
- **Kitable:** Y shelled, N spilled (it's faster than you). **Assess 0–1:** "Your hits aren't landing properly." · **Assess 2+:** "The copper is eating half of everything. There's no clever way through it — just work. And what's inside is going to bolt the moment it opens, so be ready to be somewhere else."
- **White Salts drop:** 26 (shell) + 10 (occupant, only if caught). **Insight:** +1/+0. **Habit punished:** assuming the fight ends when the health bar does. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 53 — The Pressure

- **Archetype:** Tide (hazard-creature) · **Level Range:** any · **HP:** **none — it cannot be killed** · **Move:** N/A — it is the room
- **Flavour:** Nothing to see. The room is simply at a depth it has no business being at, and every part of you knows it.
- **Limbs:** none. No body, no target, no attack roll. It is a condition with intent.
- **Effect:** at the end of every turn any creature spends in the affected space, that creature takes **10 raw and gains 1 Corrosion.** No save, no parry, no mitigation.
- **The out:** somewhere in the room is a valve, a stopcock, a cracked gauge — a physical thing that will shut it off. **Skill DC 16**, one attempt per turn as an Action. The DM places it in plain sight but not adjacent; crossing to it is the encounter.
- **Secondary Actions:**
  - **Descend** — *Trigger:* the player spends a full round taking no Action other than movement. *Cooldown:* 2 rounds. The depth increases. All Insanity saves in the room are at **+2 DC** for the rest of the encounter, cumulative up to +6. Standing still is not neutral here.
  - **Equalise** — *Trigger:* every creature in the room is below 60% HP. *Cooldown:* once per encounter. Once. The pressure releases entirely for 2 rounds — no saves, no effect, complete relief — and then returns at **double** its accumulated DC modifier.
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
- **Secondary Actions:**
  - **Spin Up** — *Trigger:* Sweep is parried twice in a row. *Cooldown:* 3 rounds. No single sweep. It turns fast enough that all four arms come round at once: unparryable, 30 raw, and the player's movement budget is halved next round.
  - **Seize** — *Trigger:* an arm is severed. *Cooldown:* once per encounter. It jams, permanently. Move stays 0m, **the d4 window roll stops, and its target time fixes at 1.60s ±0.20s** for the rest of the encounter. Severing an arm is how this fight becomes readable, and Assess 2+ says so plainly.
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

- **Secondary Actions:**
  - **Regard** — *Trigger:* the player breaks line of sight, enters cover, or douses a light. *Cooldown:* 2 rounds. No drop. Thirty lenses re-acquire: the player gains no benefit from concealment against anything in the room for 3 rounds, and the Watchwork's next Drop-Coil resolves as an **ambush** (§10).
  - **Shed Segment** — *Trigger:* three or more Segments have been severed. *Cooldown:* 4 rounds. It abandons its rear half: heals 100 HP, returns immediately to the ceiling, and the discarded segment remains on the floor as an inert 80 HP obstacle worth 4 White Salts. This fires **instead of** the split when the player would rather it didn't.
- **Kitable:** N — it goes over everything. **Assess 0–1:** "It's using the whole room and you're only using the floor." · **Assess 2+:** "Do **not** take segments off it. Three and it becomes two of them. This is the one you kill the boring way."
- **White Salts drop:** 26 (per body — a split creature pays out twice, which is the only consolation). **Insight:** +1/+0. **Habit punished:** reflexive limb-severing on anything with limbs. **Dismember threat:** Moderate. **Retreat always reachable:** N — it is faster than you and terrain doesn't slow it.

## Monster 56 — The Steeping

- **Archetype:** Shambler (elite) · **Level Range:** 5–20 · **HP:** 600 · **Move:** 5m, and it pours through gaps rather than going around them · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A person-shaped volume of scalding water, standing upright with nothing holding it in that shape. Not a ghost. Just water, holding the outline of the last thing that sat in it long enough to leave one.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Body|×1.0|—|—|—|**Yes** — all Precision Strikes, of any kind, resolve as Body|

- **Immunities:** Burning damage deals **0** against the Steeping. Corrosion deals **0**. It is water; there is nothing to burn and nothing to eat.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Scald | Light | None — unparryable | N/A | N/A | 30 raw + 1 Burning | N/A | N/A |
| Immerse | Heavy | "It leans toward you and loses its outline on the way." | Target 1.65s, ±0.25s | 1 | 65 raw + 2 Burning. **Additionally: the target's carried powder capsules are soaked** — the next Powder Charge attempt of any kind automatically fails as a dud. No Bleeding penalty on the dud (Ruleset §4 failure clause does not apply — nothing detonated). One capsule wasted. | Standard | Has to gather itself back upright |

- **Secondary Actions:**
  - **Pour** — *Trigger:* it is blocked by terrain, a chokepoint or a closed door. *Cooldown:* 2 rounds. No attack. It goes through the gap and reforms on the far side, ending adjacent to whatever it was trying to reach. There is no such thing as cover from this.
  - **Cool** — *Trigger:* below 40% HP. *Cooldown:* 4 rounds. No attack. It loses its outline and spreads flat across 4m of floor: **untargetable for one round**, and anything standing in that 4m takes 30 raw and 1 Burning at the end of it.
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
- **Secondary Actions:**
  - **Look Away** — *Trigger:* it takes damage from a Precision Strike or Precision Strike. *Cooldown:* 2 rounds. The cluster splits across seven positions at once. For 2 rounds it **cannot be Precision Strike at all** — plain attacks only, resolving against one seventh of the cluster per hit.
  - **Regard in Unison** — *Trigger:* the player has passed two Insanity saves in a row. *Cooldown:* 4 rounds. All seven turn together. Insanity save at **+4 DC**; on failure, 2 rounds of Fugue instead of one.
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

- **Secondary Actions:**
  - **Rime Over** — *Trigger:* the seam has burst and two or more rounds have passed. *Cooldown:* 4 rounds. No attack. Frost seals the split: Vent is disabled and the seam's stagger meter resets to zero. It can do this indefinitely — the burst must be exploited, not banked.
  - **Overpressure** — *Trigger:* below 30% HP with the seam burst. *Cooldown:* once per encounter. Once. It stops walking and begins to swell, taking no action at all. **At the end of the following round it detonates: 120 raw + 5 Burning to everything within 6m, itself included.** One full round of warning, stated plainly, and no way to stop it.
- **Kitable:** Y, and post-vent it becomes mandatory. **Assess 0–1:** "You're barely scratching it." · **Assess 2+:** "The plate is halving everything — the seam on its flank will open in one good hit and then it takes full damage. Understand that it starts venting the moment you do that, and it doesn't stop."
- **White Salts drop:** 40. **Insight:** +1/+0. **Habit punished:** rushing the obvious weak point without a plan for what comes after. **Dismember threat:** Very High. **Retreat always reachable:** Y.

## Monster 59 — The Yoked

- **Archetype:** Vessel (elite, paired) · **Level Range:** 8–20 · **HP:** 1200 **shared across both bodies** · **Move:** 4m each, independently · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Two bodies joined at the sternum by two metres of grey gut, drawn tight and never once allowed to go slack. Neither one leads. When one turns, the other has already turned.
- **Limbs:** standard humanoid defaults on each body. **One HP pool, two bodies** — damage to either drains the same 1200.
- **Sympathetic Recovery:** at the end of the enemy block, **whichever body was not damaged this round restores 40 HP to the shared pool.** Damage both in the same round and nothing is restored. A single attacker with a single Action cannot stop the bleed-back alone — this is the manual's first encounter explicitly designed around **having a second combatant**, and the first that a solo player should reasonably consider walking away from.
- Severing the gut connecting them is **not possible** — it is not a limb entry, it is not targetable, and Assess says so plainly rather than teasing it.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Paired Step | Heavy | "They step in together, from opposite sides, on the same beat." | Target 1.40s, ±0.20s — **one window, both bodies** | 1 | 40 raw **per body still standing** (80 if both) | Standard | Both recover together |

- **Secondary Actions:**
  - **Draw Taut** — *Trigger:* the two bodies are more than 2m apart at the start of the Enemy Phase. *Cooldown:* 2 rounds. No attack. The gut snaps tight and both bodies are hauled to the midpoint: anything standing on that line takes 35 raw and is knocked prone. Standing between them is the obvious play; this is why it is a bad one.
  - **Feed the Other** — *Trigger:* one body has taken damage in each of the last two rounds. *Cooldown:* 3 rounds. No attack. The undamaged body pushes **100 HP through the gut into the shared pool.** Splitting attention is not a preference here, it is the only way to make progress.
- **Kitable:** Y, but they close from two directions.
- **Assess 0–1:** "Hurting one doesn't seem to be enough." · **Assess 2+:** "One life between the two of them, and whichever one you leave alone is putting it back. You need to hit both in the same round or you're running to stand still. If you're alone here, leave."
- **White Salts drop:** 34. **Insight:** +1/+0. **Habit punished:** focusing a single target. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 60 — The Joist-Rider

- **Archetype:** Crawler (elite) · **Level Range:** 8–20 · **HP:** 620 · **Move:** 7m **beneath the floor**, through joists, voids and underfloor space · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Nothing in the room. Then a board lifts half an inch somewhere behind you and settles again. It has never been seen in full and its shape can only be inferred from the sound it makes travelling.
- **Limbs:** standard humanoid defaults — **but untargetable entirely while submerged.** It has no legal target of any kind until it surfaces.
- **Submerged (default state):** cannot be attacked, cannot be parried, takes no damage from any source including AOE and status ticks. It attacks *through* the floor.
- **Surfaced:** it breaks through to reposition or to land a Heavy, and is fully targetable for **that turn and the following turn** before it can submerge again.
- **The counter is terrain.** On stone, tile, poured floor or anything without a void beneath it, the Joist-Rider **cannot submerge at all** and fights as an ordinary elite. Any room with a hard floor neutralises it completely. Assess 2+ states this outright.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Underfoot | Light | None — unparryable, no tell, from below | N/A | N/A | 30 raw + 1 Bleeding | N/A | N/A |
| Breach | Heavy | "The boards under you buckle upward." | Target 1.15s, ±0.15s | 2 | 60 raw, and it is **surfaced** for this turn and the next | Standard | Left exposed on the surface an extra turn |

- **Secondary Actions:**
  - **Cut the Joists** — *Trigger:* it has been surfaced twice this encounter. *Cooldown:* 4 rounds. No attack. A 4m stretch of floor becomes unsound: any creature moving across it must pass **Skill DC 12** or fall through, taking 25 raw and needing a full Action to climb out.
  - **Follow Under** — *Trigger:* the player moves 6m or more in a single turn. *Cooldown:* 2 rounds. No attack. It tracks the movement exactly and ends directly beneath wherever the player stopped; its next Underfoot resolves as an **ambush** (§10). It does not need line of sight and it does not lose the trail.
- **Kitable:** N — it is under the floor you are standing on.
- **Assess 0–1:** "You can't fight what you can't reach." · **Assess 2+:** "It travels in the void under the boards. Get onto stone and it has nowhere to go — then it's just an ordinary thing with a bad temper. Otherwise your only windows are right after it comes up."
- **White Salts drop:** 24. **Insight:** +1/+0. **Habit punished:** fighting on the ground the enemy chose. **Dismember threat:** High. **Retreat always reachable:** Y.

## Monster 61 — The Sediment

- **Archetype:** Brute · **Level Range:** 8–20 · **HP:** 900 **at spawn, and climbing** · **Move:** 2m, and it never needs more · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A slow accumulation of everything that has settled in this room since it was last drained — mineral, cloth, hair, and other things. It is roughly upright. It gets less roughly upright as time passes.
- **Limbs:** no standard entries.

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Accretion|×1.0|—|—|—|**Yes**|

- **Accretion (the whole design):** at the end of **any round in which the Sediment took no damage**, it gains **+100 Max HP and +5 raw on Slump, permanently, uncapped.** Damage it at all — one chip hit, one status tick, anything — and it gains nothing that round. It never heals; it only ever grows.
- Ignoring it to clear the rest of the room is the natural instinct and it is the single worst available play. A Sediment left alone for six rounds is a 1500 HP creature hitting for 75.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Slump | Heavy | "The mass leans past its own balance point and comes down." | Target 1.95s, ±0.25s | 1 | 45 raw at spawn, +5 per Accretion tick | Standard | Very long — it has to reassemble itself |

- **Secondary Actions:**
  - **Draw Down** — *Trigger:* any creature in the room dies, or any limb is severed off anything. *Cooldown:* once per encounter. It absorbs the remains: **+150 HP and +1 Accretion tick immediately.** No cooldown. Killing things near the Sediment is how the Sediment gets bigger.
  - **Shed Load** — *Trigger:* below 40% of its current maximum HP. *Cooldown:* 3 rounds. No attack. It sloughs a third of its accumulated mass: loses 2 Accretion ticks and the damage that came with them, but **Move rises to 5m and Slump's target time drops to 1.40s** for the rest of the encounter.
- **Kitable:** Y, trivially — and kiting it is how you lose.
- **Assess 0–1:** "It's slow. Deal with it last." · **Assess 2+:** "Do not deal with it last. Every round you don't touch it, it gets bigger and hits harder, and none of that ever comes back off. Even a wasted chip hit is worth more than a clean turn spent elsewhere."
- **White Salts drop:** 28, **+4 per Accretion tick it managed to bank.** **Insight:** +1/+0. **Habit punished:** triaging by immediate threat. **Dismember threat:** High (late). **Retreat always reachable:** Y.

## Monster 62 — The Draught

- **Archetype:** Shambler (elite) · **Level Range:** 5–20 · **HP:** 700 · **Move:** 4m, drawn toward heat the way a flame leans toward air · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A long, thin, hollow thing shaped something like a chimney flue with a mouth at both ends. Where it stands, the air moves toward it, and anything burning nearby goes out.
- **Limbs:** custom, and it has no anatomy worth the name — it is a flue. **Upper mouth: stagger 135, ×1.3** (a thin flared rim; structurally the weakest thing about it). Sever → Reverse and Choke both permanently disabled. **Lower mouth: stagger 135, ×1.3.** Sever → Backdraught permanently disabled. **Severing both ends kills it outright regardless of remaining HP** — a flue with no openings is a pipe. **The Column: ×0.6, no stagger, sever-immune** — sheet iron, armour by the §10 rule. Safe to hit, slow to kill, and entirely pointless.
- **Feeds on fire (the whole design):** at the start of its turn, the Draught **removes all Burning stacks from every creature within 6m — itself included — and heals 25 HP per stack removed.** It takes **zero** damage from the Burning track under any circumstance.
- This makes a Burning-heavy loadout not merely useless but actively counterproductive: every stack applied anywhere in its radius is 25 HP handed to it. It also, incidentally, means the Draught is the most effective way in the game to clear Burning off yourself, if you can stomach the trade.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Backdraught | Ranged | "Both ends of it open at once and the air reverses." | Target 1.45s, ±0.20s | 1 | 40 raw + 2 Burning **to the target** (which it will then take back off them next turn, and heal from) | Standard | Collapses inward, stationary for a beat |

- **Secondary Actions:**
  - **Reverse** — *Trigger:* the player is more than 5m away. *Cooldown:* 2 rounds. No attack. Both ends open and every creature within 8m is pulled 3m toward it. Distance is not a defence against a thing that moves air.
  - **Choke** — *Trigger:* it has taken back 4 or more Burning stacks this encounter. *Cooldown:* 3 rounds. Unparryable, no damage. It closes both ends: **all Burning in the room is extinguished on every creature**, the player included, and the Draught heals 20 HP per stack removed.
- **Kitable:** Y. **Assess 0–1:** "Your fire isn't taking." · **Assess 2+:** "It eats the burn. Every stack in this room — yours, theirs, the floor's — goes into it and comes back out as health. Put the fire away entirely and it's an ordinary fight. Keep using it and you will not finish this one."
- **White Salts drop:** 26. **Insight:** +1/+0. **Habit punished:** running one damage type as a universal answer. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 63 — The Prompter

- **Archetype:** Chanter (elite, support) · **Level Range:** 10–20 · **HP:** 380 · **Move:** 4m, always keeping something between itself and the player · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A small hunched thing with a wide flat mouth and no eyes, tucked behind whatever else is in the room. It mouths along with the movements of everything around it, half a beat early, and it is not always right.
- **Limbs:** standard humanoid defaults. Very low HP — it dies to almost anything that reaches it, which is why it is built to never be reached. Soft target; the anatomy is not the puzzle.
- **False Prompt (the whole design):** while the Prompter lives, **once per round the DM delivers a deliberately incorrect tell for one other enemy in the room** — a wrong target time, a wrong tier, a wrong attack name, or a tell for an attack that isn't coming. The DM does not indicate which enemy, and does not flag the false one at the time.
  - It never lies about the Prompter's own attacks.
  - It cannot generate a false tell for an unparryable attack — it has to have a real window to corrupt.
  - **The lie dies with it, immediately.** All tells are true again from the moment it drops.
- This is distinct from the window-narrowing support enemy (Monster 46), which degrades timing honestly. The Prompter corrupts information rather than tolerance, and it is far more dangerous in a room with a Tier 2–3 attacker in it.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Cue | Light | None — unparryable | N/A | N/A | 15 raw + forces an Insanity save | N/A | N/A |

- **Secondary Actions:**
  - **Miscue** — *Trigger:* the player successfully parries anything in the room. *Cooldown:* 2 rounds. No attack. It raises the count: **two** false tells this round instead of one. Assess 2+ states plainly that the count has gone up. It never states which tell is the lie.
  - **Hide Behind** — *Trigger:* the player has line of sight to it and is within 6m. *Cooldown:* 2 rounds. No attack. It moves its full budget to put another enemy directly between itself and the player, and **cannot be targeted at all this round.** The counters are killing what it hides behind, or repositioning first.
- **Kitable:** Y, but it hides rather than flees, so reaching it costs position.
- **Assess 0–1:** "Something in this room is wrong about what it's telling you." · **Assess 2+:** "It's feeding you one bad read a round and you won't know which one. Three hundred and eighty HP, no defence, and everything goes honest the second it's down. Kill it before anything else in here."
- **White Salts drop:** 26. **Insight:** +1/+0. **Habit punished:** trusting every read at face value; leaving the small one for last. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 64 — The Shuttlecore

- **Archetype:** Vessel (elite) · **Level Range:** 10–20 · **HP:** 1100 · **Move:** 2m, ponderous · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A segmented iron drum the height of a person, mounted on a ring of small wheels. Six shuttered ports around its circumference. Behind one of them, at any given moment, something is very bright.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Port ×6 — **the one currently holding the Core**|×2.0|—|—|240|N|
|Port ×6 — **the five that don't**|**×0.5**|—|—|—|**Yes**|

- **The Core migrates.** At the **start of every enemy block** it moves to a different port — the DM rolls d6, rerolling the current position, and **states plainly where it now is** ("the bright one is on its left-rear face now"). No hidden information, no guessing: the challenge is positional, not informational. Getting to the right side of it costs movement, and it turns.
- **Severing the Core port kills it outright** regardless of HP. 240 at ×2.0 = **120 raw in one hit.** Every other surface is armour at ×0.5, no stagger, no sever, and no Precision watch (Ruleset §10).

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Port Vent | Ranged | "The bright shutter cracks open a finger's width." Fires from whichever port holds the Core. | Target 1.55s, ±0.20s | 1 | 50 raw + 1 Corrosion | Standard | Shutter jams open a beat — Core port stays put an extra round |

- **Secondary Actions:**
  - **Rotate** — *Trigger:* the currently-bright port takes damage. *Cooldown:* 1 rounds. No attack. The drum spins and the Core moves to a randomly determined different port. Accumulated damage on the old port is not lost — it is simply now on the wrong side of the drum.
  - **All Ports** — *Trigger:* three or more ports have been destroyed. *Cooldown:* 4 rounds. Every remaining shutter opens at once: unparryable, **25 raw per surviving port** to everything within 6m, and the Shuttlecore takes 50 self-damage doing it.
- **Kitable:** Y. **Assess 0–1:** "Only one part of that is worth hitting." · **Assess 2+:** "Five sixths of it is plate and the sixth moves every round. It'll tell you where — it can't help that, it glows. Everything is about whether you can be standing there when it does."
- **White Salts drop:** 30. **Insight:** +1/+0. **Habit punished:** attacking from wherever you happen to be standing. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 65 — The Reliquary Crawler

- **Archetype:** Crawler (mook) · **Level Range:** 5–20 · **HP:** 400 · **Move:** 6m, low and fast along skirting and pipework · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A flat, many-legged thing the size of a serving tray, with a glass-fronted cavity in its back. There is something inside the cavity. It is not part of the creature and never was.
- **Limbs:** custom. **Leg cluster, twelve of them: stagger 90 as a single group, ×0.6.** Severing legs is possible and achieves almost nothing — every four severed reduces Move by 2m and nothing else. There is no head entry and no torso entry: it is flat, fast and mostly cargo. **The glass cavity is neither a limb nor an implement.** It is cargo, and it takes whatever the creature takes — see the contents rules above.
- **It is carrying something, and the something is fragile.** Every Reliquary Crawler carries one item, weapon, or Salts cache in its dorsal cavity, visible through the glass. What happens to it depends entirely on how the Crawler dies:
  - **Killed by Light attacks only:** contents intact, recovered whole.
  - **Killed by any Heavy attack:** contents damaged — Salts halved, an item reduced to a single use, a weapon recovered but requiring hub repair before it can be equipped.
  - **Killed by any sever, or by AOE:** **contents destroyed outright.** Nothing recovered.
- The DM shows what is in the cavity, plainly, before the fight starts. The whole encounter is the player deciding whether the prize is worth fighting badly for.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Skitter-Bite | Light | None — unparryable | N/A | N/A | 20 raw | N/A | N/A |

- **Secondary Actions:**
  - **Bolt for the Skirting** — *Trigger:* it has taken damage from a Heavy attack or any sever. *Cooldown:* 3 rounds. No attack. It runs its full 6m for the nearest wall gap and is **gone at the end of the following round** unless killed or physically blocked. Hitting it wrong doesn't only damage the prize, it starts a clock.
  - **Present** — *Trigger:* the player has not attacked it for two consecutive rounds. *Cooldown:* 4 rounds. No attack. It stops, turns to face the player, and opens the glass: the contents are freely takeable as a Fast Action — **and the Crawler immediately turns hostile, dealing double Skitter-Bite damage for the rest of the encounter.** It offered a trade. It will not be robbed twice.
- **Kitable:** N — faster than you, though barely dangerous.
- **Assess 0–1:** "There's something in it." · **Assess 2+:** "Whatever's in that case comes out in the condition you leave the creature in. Hit it soft and slow, or hit it properly and accept you're only killing a bug."
- **White Salts drop:** 10 (plus contents). **Insight:** +1/+0. **Habit punished:** opening with your best attack out of reflex. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 66 — The Bolter

- **Archetype:** Burster (mook) · **Level Range:** 1–20 · **HP:** 300 · **Move:** 11m — the fastest thing in the manual · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A knot of grey limbs around a distended sac, running flat-out from the moment it is seen. The sac is full of White Salts and it is very obviously full of White Salts.
- **Limbs:** standard humanoid defaults. **The Sac** — implement, ×1.5, sever 150. Severing the sac drops the Salts on the spot and the Bolter keeps running, now worthless.
- **It is leaving.** The Bolter never attacks and never stops. It spends every turn moving its full 11m toward the nearest exit, and **after 4 rounds it is gone**, along with its drop, permanently — no chase, no second chance, no return later in the instance.
- A pure aggression check, and a deliberate counterweight to a manual that otherwise rewards patience almost everywhere. There is no safe way to take it: you commit immediately or you watch 45 Salts leave the room.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| — | — | It has no attack of any kind. | — | — | — | — | — |

- **Secondary Actions:**
  - **Drop Ballast** — *Trigger:* it takes any damage. *Cooldown:* 2 rounds. No attack. It sheds **8 White Salts** onto the floor behind it and gains +3m of movement this round. Chasing it gets cheaper and less rewarding at exactly the same rate.
  - **Panic Turn** — *Trigger:* its path to an exit is blocked. *Cooldown:* 2 rounds. No attack. It reverses completely and runs for the opposite side of the room, passing straight **through** any creature in the way: that creature takes 10 raw and loses 2m from next turn's budget.
- **Kitable:** N/A — you are not the one being avoided, you are the one being outrun.
- **Assess 0–1:** "That's running and it's carrying something." · **Assess 2+:** "Four rounds and it's gone for good. It can't hurt you and you almost certainly can't catch it — but the sac comes off in one good hit and it doesn't need to die for you to get paid."
- **White Salts drop:** 45. **Insight:** +1/+0. **Habit punished:** setting up carefully before committing. **Dismember threat:** None. **Retreat always reachable:** Y (it is retreating from you).

## Monster 67 — The Tally

- **Archetype:** Toller (elite) · **Level Range:** 8–20 · **HP:** 550 · **Move:** 3m, drifting at eye height · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A frame of counting-wires strung with black beads, hanging in the air without a hand near it. Beads move. There is a sound like a small door closing every time one does.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Frame|×1.0|800|—|—|N|
|The Wires *(implement)*|×2.0|—|—|200|N|

- **Destroying the Wires removes Reckoning entirely** — 100 raw in one hit — leaving a slow, harmless frame.
- **Reckoning (the whole design):** **every time any creature in the room uses an item** (Quick Item, Full Action item, consumable, anything from Ruleset §8), the Tally immediately takes a **free attack against that creature**, out of turn: **35 raw, unparryable, no tell.** Multiple item uses in one turn each trigger it separately.
- It does nothing else of consequence. It simply makes healing, clearing tracks, and refilling capsules cost blood — and it is at its worst in exactly the fights where you most need to spend an item.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Reckoning | Reactive | None — unparryable, triggers on any item use by any creature | N/A | N/A | 35 raw | N/A | N/A |
| Bead-Fall | Light | None — unparryable | N/A | N/A | 20 raw | N/A | N/A |

- **Secondary Actions:**
  - **Strike a Balance** — *Trigger:* no item has been used by any creature for two consecutive rounds. *Cooldown:* 3 rounds. Unparryable, no damage. **One random consumable is deleted from the player's inventory.** Not using items is not an escape from the Tally, only a slower way of paying it.
  - **Carry the Figure** — *Trigger:* it has dealt 100 or more cumulative raw this encounter. *Cooldown:* 4 rounds. No attack. The beads reset and the count transfers: **the next enemy killed in this room drops zero White Salts**, and the Tally heals for what the drop would have been.
- **Kitable:** Y. **Assess 0–1:** "It's counting what you spend." · **Assess 2+:** "Every tonic, every wrap, every capsule you load, it charges you thirty-five for. Break the wires or accept that this fight is going to be fought on what you walked in with."
- **White Salts drop:** 24. **Insight:** +1/+0. **Habit punished:** item-cycling as a default answer to pressure. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 68 — The Recoil

- **Archetype:** Drudge (elite) · **Level Range:** 12–20 · **HP:** 850 · **Move:** 3m, relentless, never varies · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A dense, low, four-armed thing built like a press. It swings, and when the swing is stopped it does not stumble — it takes note. The next one is heavier. It has been counting for a long time.
- **Limbs:** custom. **Head: stagger 280, ×1.5** (sunk between the shoulders; barely a head at all). **Each of four arms: stagger 150, ×1.0.** **Each arm severed reduces Press Down's accumulated parry bonus by 15 raw**, to a floor of its base 55, and removes one arm from the press. Severing arms is the only way to walk the escalation backwards, and therefore the only reason to keep parrying something that punishes parries. **Legs: stagger 240, ×0.9.** Sever → 1m, and it still presses.
- **Learns from being parried (the whole design):** **every successful parry against the Recoil permanently increases Press Down's damage by +15 raw for the remainder of the encounter, cumulatively and uncapped.** Parry it four times and it is hitting for 120.
  - Parry rewards are otherwise unchanged — a parry still buys the skipped turn and the eased follow-up (Ruleset §9). It is not a trap; it is a tax.
  - Dodging costs nothing and teaches it nothing.
- The manual's first enemy that makes the player's strongest tool the wrong long-term answer. Against the Recoil, parrying is correct for tempo and catastrophic as a habit, and the fight is entirely about knowing when to stop.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Press Down | Heavy | "All four arms come up, and it waits to see what you do about it." | Target 1.70s, ±0.20s | 1 | 55 raw at the start of the fight, **+15 per successful parry landed against it this encounter** | Standard | Long, honest recovery — the openings are real |

- **Secondary Actions:**
  - **Note It Down** — *Trigger:* the player takes any Action other than Hold for two consecutive rounds. *Cooldown:* 3 rounds. No attack. It lowers all four arms and waits — and gains **+10 raw anyway.** Refusing to parry is a slower version of the same problem, not a way out of it.
  - **Press Through** — *Trigger:* Press Down has reached 100 or more raw. *Cooldown:* once per encounter. Once. Press Down becomes **unparryable** for the rest of the encounter and stops gaining raw. The escalation has a ceiling; arriving at it is worse than the climb was.
- **Kitable:** Y. **Assess 0–1:** "It's watching how you answer it." · **Assess 2+:** "Every time you stop that swing, the next one costs more. It's a fair fight and a slow trap — take the openings you actually need and dodge the rest, or it will out-scale you before its health runs out."
- **White Salts drop:** 32. **Insight:** +1/+0. **Habit punished:** parrying on reflex because parrying is always right. **Dismember threat:** Very High (late). **Retreat always reachable:** Y.

## Monster 69 — The Spore-Kin

- **Archetype:** Swarm (elite, distributed) · **Level Range:** 10–20 · **HP:** 1000 **shared across five bodies** · **Move:** 5m each, independently · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Five pale, knee-high, roughly ovoid bodies moving in loose company. Each one is taut in a way that suggests pressure rather than muscle. None of them is the important one.
- **Limbs:** no standard entries on any body.

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Body ×5|×1.0|—|—|—|**Yes**|

- **One pool, five bodies.** Damage to any body drains the shared 1000. Bodies cannot be killed individually — they cannot be reduced, severed, staggered or removed.
- **Burst (the whole design):** when the shared pool reaches 0, the bodies do **not** simply die. **All five rupture simultaneously**, each dealing **50 raw + 3 Corrosion in a 3m radius** from wherever that body happens to be standing at that moment.
- The fight therefore ends with a coordinated detonation whose geometry the player has been passively arranging for the entire encounter without necessarily noticing. Killing it in a doorway with all five clustered around you is a 250-raw mistake. Herding them apart first is the actual skill.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Press | Light | None — unparryable, per body | N/A | N/A | 12 raw per body in contact | N/A | N/A |

- **Secondary Actions:**
  - **Consolidate** — *Trigger:* two or more bodies have been destroyed. *Cooldown:* 3 rounds. No attack. The survivors merge: body count halves (rounding up), **each remaining body's Press damage doubles**, and the shared pool is unaffected. Killing bodies without emptying the pool makes the fight worse.
  - **Burst** — *Trigger:* the shared pool drops below 200. *Cooldown:* once per encounter. Once. Every remaining body swells and detonates at the end of the **following** round: 40 raw + 3 Corrosion within 3m of each. One round of warning. Where they are standing when the pool empties is the whole fight.
- **Kitable:** Y — and kiting is how you survive the ending.
- **Assess 0–1:** "There's one thing here wearing five bodies." · **Assess 2+:** "They share a life and they all go off when it runs out. Where they're standing when that happens is entirely up to you, and you should start thinking about it well before the pool gets low."
- **White Salts drop:** 30. **Insight:** +1/+0. **Habit punished:** fighting in a doorway; not thinking about the kill until it happens. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 70 — The Sluice Mother *(boss, non-humanoid)*

- **Archetype:** Anchor (boss) · **HP:** **none — the body is never present** · **Move:** N/A
- **Flavour:** Somewhere below the room, wedged into the main drain, is something far too large to have got there. You will not see it. What you will see are six iron sluice-apertures set into the walls at varying heights, and what comes out of them.
- **The body is unreachable, untargetable, and unkillable.** There is no health bar. There is no phase where it emerges. **The fight is the six apertures**, and it ends when all six are sealed.

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Aperture ×6 *(implement)*|×1.5|—|—|**200** *(≈134 raw in one hit)*|N|

- **Sealing an aperture:** sever it (200 at ×1.5) **or** grind it down — each aperture has its own **250 HP**. Either works; sever is the fast route and grinding is always available (Ruleset §3).
- **Reflux:** at the end of every third round, **any aperture not yet sealed reopens 60 HP of damage already dealt to it** (never below 0, never past sealed). Apertures finished cleanly stay finished. Half-finished work rots.
- **Escalating reach:** the Mother distributes its effort. With six apertures open it makes **two** Limb attacks per round; with four open, **three**; with two open, **four.** It gets more dangerous as you win, and the last two apertures are the hardest part of the fight by a wide margin.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Limb | Heavy | "Something comes out of the third aperture, and it keeps coming out." | Target 1.30s, ±0.20s | 1 | 55 raw + 1 Corrosion |
| Backwash | Aura | "All six run at once." Every fourth round. | Unparryable | N/A | 25 raw + 1 Influence to everything in the room, **per aperture still open** — 150 raw and 6 Influence at the start, nothing at all by the end |
| The Draw | Heavy (chain) | "Three limbs withdraw together, and the water goes with them." | **3 sequential windows: 0.90s · 1.40s · 1.90s, each ±0.20s** | 3 | 40 raw per unparried window |

- **The Draw — ballistic chain.** All three parried → **the Mother overreaches: one aperture of the player's choice is immediately sealed outright**, no damage required. Miss any window → that beat and every remaining beat land automatically. This is the only opening in the fight that converts skill directly into progress, and on a six-aperture clock it is worth a great deal.
- **Secondary Actions:**
  - **Re-Open** — *Trigger:* three or more apertures have been sealed. *Cooldown:* 4 rounds. No attack. It forces one sealed aperture back open. The difficulty curve runs backwards **and it runs both ways** — sealing is progress that has to be defended, not banked.
  - **Reach Through** — *Trigger:* the player has been within 2m of any open aperture at the start of two consecutive Enemy Phases. *Cooldown:* 3 rounds. A limb comes out. **Heavy, target 1.20s ±0.15s, Tier 2, 70 raw**, and on a hit the player is dragged 3m and pinned for one round (Strength DC 15 as an Action to break free).
- **Kitable:** N/A. **Assess 0–1:** "Whatever that is, it isn't in this room and it isn't coming into this room." · **Assess 2+:** "There's no killing it. There's only closing the holes. Six of them — and it fights harder through every one that's left, so the front half of this is much easier than the back half. Finish what you start; half-shut ones creep back open."
- **White Salts drop:** 80. **Insight:** +1/+1.
- **Boss Gimmick:** **the first boss with no body, no HP bar and no kill.** It is resolved rather than defeated, its danger curve runs backwards (hardest at the end), and the Tier 3 chain pays out in objective progress rather than in a damage window. Retreat is always live and costs nothing but the run.
- **Habit punished:** treating a boss as a health bar with a face. **Dismember threat:** High. **Retreat always reachable:** Y.

## Monster 71 — The Understudy

- **Archetype:** Effigy (elite) · **Level Range:** 12–20 · **HP:** 800 · **Move:** 5m, and it moves the way you move · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A smooth, featureless, roughly person-height column of grey matter with no face and no front. It stands very still and watches how it is hit. It is not defending itself; it is taking notes.
- **Limbs:** custom, and **it has no anatomy until it has watched some.** At encounter start it is a single **Mass** entry: ×1.0, no stagger threshold, sever-immune. **Every time the player declares a Precision Strike at a specific limb — on the Understudy or on anything else in the room — the Understudy grows that limb**, permanently for the encounter, at the standard humanoid threshold and multiplier for it. A player who never calls a shot fights a featureless block with no weak points and no way to end it quickly. A player who plays their usual game builds it a head at ×1.5 and hands themselves a fast kill. **Each limb grown also raises Bare Copy by +8 raw, permanently.** Assess 2+ states this outright, which is the whole encounter: knowing the deal does not make it an easy call.
- **Adoption (the whole design):** the first time the Understudy is struck by a weapon with a **status-applying gimmick**, it permanently adopts that status for the rest of the encounter — every subsequent Bare Copy it lands applies **1 stack of that status**. It can hold **up to three** adopted statuses simultaneously, one per distinct source.
  - Hit it with a Burning weapon and it burns you. Hit it with three different gimmick weapons and it has all three.
  - It cannot adopt raw damage bonuses, accuracy effects, movement effects, or anything that isn't a status track — only tracks.
  - **A player who commits to a single plain weapon for the whole fight gives it nothing.**
- Directly punishes the loadout variety the rest of this manual encourages, which is the point: variety is correct almost everywhere, and this is the room where it costs.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Bare Copy | Heavy | "It reproduces your last swing, badly, and a half-beat slow." | Target — **matches the target time of the last attack the player made against it** (DM states it), ±0.20s | 1 | 50 raw + 1 stack of every status it has adopted | Standard | Standard |

- **Secondary Actions:**
  - **Take Notes** — *Trigger:* the player uses a weapon it has not yet seen this encounter. *Cooldown:* 2 rounds. No attack. It observes. From the following round Bare Copy may use that weapon's timing instead, and the Understudy gains **+10 raw permanently for each distinct weapon catalogued.**
  - **Perform** — *Trigger:* it has catalogued three or more distinct attacks. *Cooldown:* 4 rounds. It chains them: **three sequential windows using the target times of the last three distinct attacks the player made against it**, ±0.20s each, 30 raw per unparried window. Full parry grants the standard Tier 1 Open. The player's own repertoire, aimed back at them.
- **Kitable:** Y. **Assess 0–1:** "It's learning something off you." · **Assess 2+:** "Whatever you hit it with, it keeps. Three tricks maximum, and it only gets what you give it — so give it one boring weapon and nothing else, and this is a plain fight against a slow target."
- **White Salts drop:** 34. **Insight:** +1/+0. **Habit punished:** rotating through your best tools. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 72 — The Sealed

- **Archetype:** Vessel (elite) · **Level Range:** 10–20 · **HP:** 600 · **Move:** 3m · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A fused ovoid of grey plate about the size of a wardrobe, walking on two short columns. There is no seam anywhere on it. There is no seam right up until there is.
- **Limbs:**

|Limb|Multiplier|Stagger Threshold|Stagger Duration|Sever Threshold|Sever Immune?|
|-|-|-|-|-|-|
|Shell *(closed)*|×1.0|—|—|—|**Yes — and takes 0 damage from all sources**|
|Interior *(open)*|×1.5|180|1 turn|200|N|

- **It takes literally nothing while closed.** Not raw damage, not status ticks, not AOE, not Burning, not Corrosion. Zero, from everything, permanently, for as long as it is shut.
- **It opens only to attack**, and stays open **from the moment its tell begins until the end of the player's following turn.** That is the entire window and there is no other.
- Consequently, damage is only ever available to a player who is standing close enough to exploit the opening created by the thing that is trying to hit them. Retreating to safety is a guarantee of never winning.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Split | Heavy | "A seam appears where there wasn't one, and the whole front of it hinges apart." | Target 1.60s, ±0.20s | 1 | 70 raw | Standard | Stays open an extra full turn — the best window in the fight |

- **Secondary Actions:**
  - **Re-Seal** — *Trigger:* it has been open for two consecutive rounds. *Cooldown:* 3 rounds. No attack. The seam closes and vanishes. Accumulated damage on the interior is retained, but the interior is untargetable until it opens again.
  - **Hinge Wide** — *Trigger:* below 40% HP. *Cooldown:* once per encounter. It stops closing. The seam stays open permanently, the interior is always targetable, **and Split becomes an unparryable aura: 25 raw per round to anything within 2m**, every round, for the rest of the encounter.
- **Kitable:** Y, and kiting achieves precisely nothing.
- **Assess 0–1:** "You are not hurting that." · **Assess 2+:** "It's shut and nothing gets through a shut one. It has to open to swing at you, and it stays open a beat after — that's your only window, every single time. You cannot fight this one from a safe distance."
- **White Salts drop:** 28. **Insight:** +1/+0. **Habit punished:** playing safe; disengaging under pressure. **Dismember threat:** High. **Retreat always reachable:** Y.

## Monster 73 — The Cling

- **Archetype:** Burster (mook) · **Level Range:** 5–20 · **HP:** 180 · **Move:** 8m, then a 4m leap · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A flat wet disc the width of two hands, edged all round with small hooks. It moves in short bursts and it is not trying to fight anyone. It is trying to get onto someone.
- **Limbs:** none — a single sever-immune Body entry at ×1.0 while unattached.
- **Attachment (the whole design):** on a successful Latch, the Cling attaches to its target and **can no longer be attacked by that target at all** — it is on their back, in the one place they cannot reach. While attached:
  - It drains **10 HP per turn**, automatically, no save.
  - The host may spend a **full Action and pass a Skill DC 15** to tear it off. Failure wastes the action and deals 5 raw to the host.
  - **Any other creature can remove it as a Fast Action, automatically, no check.** A companion within reach ends the problem instantly.
- Individually trivial. Three of them at once, with no second party present, is a genuine spiral — and the second reason in this pass to think hard about walking in alone.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Latch | Heavy | "It gathers itself flat against the floor and then it isn't on the floor." | Target 0.95s, ±0.15s | 2 | Attaches (see above). No raw damage on the leap itself. | Standard | Lands badly, prone and free to hit for a turn |

- **Secondary Actions:**
  - **Drop Off** — *Trigger:* it has been attached for four consecutive rounds. *Cooldown:* 3 rounds. It releases voluntarily, takes its full 8m and re-enters concealment. It has had what it came for. The drain resumes the moment it lands again.
  - **Hook Deep** — *Trigger:* the host fails a removal attempt. *Cooldown:* 2 rounds. Drain rises from 10 to **18 HP per turn** and the removal DC rises to 18 for the rest of the attachment. Failing once makes failing again both likelier and more expensive.
- **Kitable:** N. **Assess 0–1:** "Don't let it land on you." · **Assess 2+:** "Once it's on you it's somewhere your arms don't go — you'll spend a whole turn and a good roll getting it off. Anyone else in the room can just pull it off you. Parry the leap and it never becomes a problem."
- **White Salts drop:** 8. **Insight:** +1/+0. **Habit punished:** ignoring small fast things. **Dismember threat:** None. **Retreat always reachable:** Y (unless attached).

## Monster 74 — The Wake

- **Archetype:** Lunger (elite) · **Level Range:** 10–20 · **HP:** 720 · **Move:** 0m — it never takes a step of its own · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A tall, thin, trailing shape that is always exactly behind you and has never been seen to travel. It does not follow. It is simply, each time you look, further along than it was.
- **Limbs:** custom. **Head: stagger 200, ×1.5.** **The Trailing Hem: stagger 120, ×1.3** — the length of it that is always further back than the rest of it is. **It is only targetable during a round in which Trail has fired**, because spending 5m+ is the only thing that ever makes the hem catch up with the body. Hem sever → Trail is permanently disabled and the Wake becomes an ordinary Lunger for the rest of the encounter. **The manual's only weak point that requires the player to deliberately do the wrong thing to expose.** **Arms:** standard (200, ×0.65). **Legs:** standard (300, ×0.75).
- **Draw (the whole design):** the Wake never moves on its own turn. Instead, **every time the player spends more than 4m of movement in a single turn, the Wake immediately moves that same distance toward them and takes a free Trail attack if it ends within reach** — out of turn, unparryable, no tell.
  - Spend 4m or less and it does not move at all, ever. It will stand in the same spot for the entire encounter.
  - It converts the movement budget (Ruleset §7) from a free resource into a priced one, and it makes hit-and-run — normally the safe, slow, low-reward option — the single most dangerous thing available.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Trail | Reactive | None — unparryable, triggers on the player spending 5m+ in a turn | N/A | N/A | 35 raw + 1 Insanity save | N/A | N/A |
| Overtake | Heavy | "It leans, and the lean covers more ground than a lean should." | Target 1.50s, ±0.20s | 1 | 65 raw | Standard | Standard |

- **Secondary Actions:**
  - **Close the Distance** — *Trigger:* the player has spent 4m or less for three consecutive rounds. *Cooldown:* 4 rounds. No attack. It takes one step of exactly 6m, and nothing the player did caused it. Standing still is a strategy, not a solution, and it has a shelf life.
  - **Trail Behind** — *Trigger:* Overtake is parried. *Cooldown:* 3 rounds. No recovery. It is simply not there, and is instead directly behind the player. Next round's Overtake resolves as an **ambush** (§10) unless the player spends an Action turning to face it.
- **Kitable:** **N — kiting is the one thing that cannot be done here.** This is the manual's first hard anti-kiting enemy.
- **Assess 0–1:** "Stop moving." · **Assess 2+:** "It only travels when you do, and only if you go further than a few paces. Fight it standing still and it's an ordinary thing on an honest tell. Try to keep away from it and it will be on you every single turn."
- **White Salts drop:** 28. **Insight:** +1/+0. **Habit punished:** kiting as a universal safety valve. **Dismember threat:** High. **Retreat always reachable:** Y — leaving the room outright still works; it does not pursue between rooms.

## Monster 75 — The Duplicant

- **Archetype:** Flailer (elite) · **Level Range:** 10–20 · **HP:** 800 · **Move:** 5m · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A loose, wet, upright thing with too many surfaces and no consistent outline. Every so often part of it separates and stands up on its own, and neither part seems to regard this as significant.
- **Limbs:** standard humanoid defaults, no deviations. Each copy has its own full set. **This is deliberate and should not be 'fixed' in a later pass** — the Duplicant is the manual's pure damage check and it is not supposed to have a weak point. Its variety comes from the Secondary Actions below, which run the clock in both directions.
- **Division (the whole design):** at the **end of every third round**, the Duplicant splits. It creates one copy with **half its current HP**, rounded down; the original keeps the other half. Both act independently thereafter, both have full attacks, and **both continue to divide on the same three-round clock.**
  - Killing a body removes it permanently — no reassembly.
  - The clock is global and does not reset on damage. Three rounds is three rounds.
- A soft enrage timer expressed as arithmetic. Kill it inside six rounds and it is an ordinary elite; take twelve and you are fighting four of them at once. There is no trick, no weak point and no gimmick to exploit — the only answer is being fast enough, which makes it the manual's cleanest pure damage check.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Slough | Heavy | "A whole sheet of it draws back and comes across." | Target 1.25s, ±0.20s | 1 | 45 raw + 1 Bleeding | Standard | Standard |

- **Secondary Actions:**
  - **Reabsorb** — *Trigger:* two or more copies are within 2m of each other and their combined HP is below 300. *Cooldown:* 3 rounds. No attack. The copies merge into a single body at their combined HP **+100**, and the three-round division clock resets. The only thing worse than a timer is a timer that runs backwards.
  - **Split Early** — *Trigger:* it takes 200 or more damage in a single round. *Cooldown:* once per encounter. It divides immediately rather than waiting for the clock, and the clock resets from that point. Burst damage does not beat the timer. It advances it.
- **Kitable:** Y — and every round spent kiting is a round on the clock.
- **Assess 0–1:** "There's going to be more of that." · **Assess 2+:** "It halves itself every three rounds and both halves keep doing it. No weak point, nothing clever — you are simply on a timer, and the timer does not care what you do."
- **White Salts drop:** 30 for the original, 10 per copy killed. **Insight:** +1/+0. **Habit punished:** slow, careful, attritional play. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 76 — The Offerer

- **Archetype:** Vessel (neutral) · **Level Range:** any · **HP:** 1400 · **Move:** 0m unless provoked, then 6m · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A tall, narrow, closed thing like a folded pair of hands the height of a door, standing where it will be noticed. When approached it opens along its length. Inside there is a shallow dish, and the dish is empty, and it is very clearly waiting.
- **Limbs:** standard humanoid defaults. Sever-viable, and considerably tougher than it looks. Deliberately unremarkable: the encounter is a decision, not an anatomy problem.
- **It does not attack. It will not attack. It is waiting to be paid.** The Offerer is a social encounter occupying a monster slot, and it is the manual's first entry that can be resolved entirely without combat.
- **The trade.** Place something in the dish as a Full Action and it gives something back. It accepts exactly one payment per encounter and then closes for good:

|Payment|Return|
|-|-|
|20 White Salts from Purse|A rolled item appropriate to the instance's loot tier|
|**2 or more stacks from a single status track** *(it takes them off you)*|**2 White Salts per stack removed**, and the track is genuinely cleared|
|1 Insight|A rolled weapon appropriate to the instance's loot tier|
|Nothing — walk away|Nothing. It closes when you leave the room and bears no grudge.|

- **If attacked, it changes.** It closes, and thereafter fights as a **Brute with 1400 HP, Move 6m, and a single Heavy: Fold (target 1.75s, ±0.20s, Tier 2, 95 raw)**. It drops **60 White Salts** — considerably more than trading with it would have yielded. That is deliberate: robbing it is genuinely more profitable and genuinely much harder, and it never offers again in that instance.
- **Secondary Actions:**
  - **Close** — *Trigger:* the player leaves the room, or a payment has been made. *Cooldown:* once per encounter. It shuts and does not reopen for the rest of this instance. No hostility, no pursuit, no grudge.
  - **Fold Faster** — *Trigger:* provoked, and parried twice this encounter. *Cooldown:* 3 rounds. Fold's target time drops from 1.75s to **1.30s** and its tolerance tightens to ±0.15s for the rest of the encounter. It was not fighting properly before.
- **Kitable:** Y once provoked. **Assess 0–1:** "It isn't hostile." · **Assess 2+:** "It's a transaction, and it will take almost anything off you — including the things you'd pay to be rid of. It'll also fight, if you'd rather have what's in it than what it's offering. It's a great deal harder than it looks and it pays better than it trades."
- **White Salts drop:** 0 if traded with, 60 if killed. **Insight:** +1/+0 on first sighting either way.
- **Habit punished:** none, deliberately — this entry rewards restraint and greed roughly equally and takes no view on which is correct. **Dismember threat:** Moderate (provoked). **Retreat always reachable:** Y.

## Monster 77 — The Hymnal

- **Archetype:** Swarm (elite) · **Level Range:** 5–20 · **HP:** 480 · **Move:** 6m, occupying a **4m × 4m column of air** rather than a point · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Every loose page from every hymnal in the building, in the air at once, turning slowly. Each page has a name written at the top in a different hand. None of the names are printed.
- **Limbs:** none. Single sever-immune **Mass** entry, ×1.0. Precision Strike cannot be declared, stagger never fires, Precision Strikes resolve as plain hits.
- **Attack shape (§10):** **Arc attacks deal full raw. Point attacks deal half, rounded up.** A knuckle through a page-storm accomplishes exactly what it sounds like it accomplishes.
- **Elemental (§10):** **Burning ×3.** **Bleeding immune** — there is nothing in it to open.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Recitation | Aura | None — unparryable, resolves at the end of the enemy block | N/A | N/A | 1 Influence to every creature inside the column | N/A | N/A |
| Papercut Squall | Light | None — unparryable | N/A | N/A | 12 raw + 1 Bleeding to every creature inside the column, **+6 raw for each consecutive round that creature has remained inside** | N/A | N/A |

- **Secondary Actions:**
  - **Scatter** — *Trigger:* it takes an Arc attack (§10) or any AOE. *Cooldown:* 3 rounds. The pages fly apart across the whole room. **The Hymnal cannot be damaged at all this round**, deals no damage either, and reforms at the start of the next Enemy Phase anywhere the DM chooses.
  - **Bind a Name** — *Trigger:* a creature has been inside the column for three consecutive rounds. *Cooldown:* 4 rounds. One page settles on that creature and adheres. It applies 1 Influence per round for the rest of the **instance** until removed with a Full Action. **If it lands on the player, the DM states the name written on it.** Whose name that is, is an Instance Quest and should be treated as one.
- **Kitable:** Y — it is slow and it is a place, not a pursuer. **Assess 0–1:** "There is nothing in there to hit and it is getting worse the longer you stand in it." · **Assess 2+:** "No anatomy and no stagger, but it is paper and it stands in the air. Something wide, or something burning, and it stops being a problem. Something quick and precise will take all day."
- **White Salts drop:** 20. **Insight:** +1 first sighting / +0 thereafter.
- **Boss Gimmick:** N/A. **Habit punished:** standing still inside a hazard because it only did 12 the first round. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 78 — The Rendering

- **Archetype:** Swarm (elite) · **Level Range:** 8–20 · **HP:** 520 · **Move:** 4m, occupying a **3m × 3m** volume at chest height · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Iron filings and slag dust, still hot, hanging together in a shape that keeps almost resolving into a person and then not bothering.
- **Limbs:** none. Single sever-immune **Mass** entry, ×1.0.
- **Attack shape (§10):** **Arc full raw, Point half, rounded up.**
- **Elemental (§10):** **Burning ×0 — fully immune. Corrosion ×2.** It is the heat; you cannot set it on fire.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Scour | Aura | None — unparryable | N/A | N/A | 8 raw + 1 Corrosion to every creature inside, **+4 raw per consecutive round that creature has remained inside** | N/A | N/A |
| Cling to Iron | Reactive | None — unparryable. Triggers whenever any creature strikes it with a metal weapon. | N/A | N/A | 1 Corrosion to the wielder, and that weapon's **next** attack loses 10 raw as the filings coat it | N/A | N/A |

- **Secondary Actions:**
  - **Disperse** — *Trigger:* it takes an Arc attack (§10) or any AOE. *Cooldown:* 3 rounds. It goes up into the roof space. **Cannot be damaged at all this round**, deals no damage, and reforms at the start of the next Enemy Phase within 6m.
  - **Donate** — *Trigger:* it has dealt 30 or more cumulative raw this encounter. *Cooldown:* 4 rounds. No attack. It flows onto another enemy in the room and **transfers 60 of its own HP** to it, up to that creature's maximum; that enemy's attacks also apply +2 Burning for 3 rounds. What it takes off the player goes somewhere useful.
- **Kitable:** Y. **Assess 0–1:** "It is warm and it is watching and there is nothing in it." · **Assess 2+:** "Fire does nothing at all. It eats metal — every time you punch it, your knuckles come out worse. Wide, non-metal, or leave."
- **White Salts drop:** 22. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** reaching for the same weapon regardless of what is in front of you. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 79 — The Lather

- **Archetype:** Swarm (mook) · **Level Range:** 1–15 · **HP:** 300 · **Move:** 3m, spreading rather than walking; occupies **5m × 5m** of floor at ankle-to-knee height · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A slow grey churn of soap scum and hair and other people's water, moving across the tiles with the deliberateness of something that has somewhere to be.
- **Limbs:** none. Single sever-immune **Mass** entry, ×1.0.
- **Attack shape (§10):** **Arc full raw, Point half, rounded up.**
- **Elemental (§10):** **Burning ×0 — fully immune. Corrosion ×2.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Slick | Aura | None — unparryable | N/A | N/A | No damage. Any creature inside it that spends 4m or more of movement must pass **Skill DC 12** or fall prone and forfeit the rest of its budget. | N/A | N/A |
| Saponify | Light | None — unparryable | N/A | N/A | 8 raw + 1 Corrosion to every creature inside, **+4 raw per consecutive round that creature has remained inside** | N/A | N/A |

- **Secondary Actions:**
  - **Rise** — *Trigger:* three or more creatures are standing inside it. *Cooldown:* 3 rounds. It climbs to chest height across its whole footprint: **line of sight is broken through it for 2 rounds** and no parry may be attempted through it, in either direction, by anyone.
  - **Drain Away** — *Trigger:* below 30% HP. *Cooldown:* once per encounter. No attack. It pours into the nearest grate and is gone. It drops nothing and it is not coming back. Not every fight is supposed to end in a kill.
- **Kitable:** Y — trivially. It is a floor, not a hunter. **Assess 0–1:** "You will go over in that." · **Assess 2+:** "It cannot be burned and it cannot be cut. Get out of it, or bring something wide and be quick about it — every round you stand there costs more than the last."
- **White Salts drop:** 10. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** spending the whole movement budget without checking what is underfoot. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 80 — The Ceiling Verger

- **Archetype:** Crawler (elite) · **Level Range:** 8–20 · **HP:** 640 · **Move:** 9m across walls and vaulting, 2m if grounded · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A verger's robe with six legs coming out of it, holding the vault with four and keeping two free. It has been up there long enough that the plaster has taken its shape.
- **Limbs:** custom, and it is all legs. **Six Legs, each: stagger 110, ×1.0, sever 160.** **Staggering any single leg drops it to the floor immediately** for the stagger's duration (2 turns). **Severing three ends wall and ceiling movement permanently** — 2m ground crawl for the rest of the encounter. **Head: guarded** — not targetable at all while it is overhead. Once grounded: stagger 180, ×1.5.
- **Reach:** its two striking legs reach **3m below the ceiling.** In a room with a low vault it can be met in melee; in the chancel or the bell tower it cannot be touched by anything held in a hand. **State ceiling height when the room is generated.**
- **Interception (§7):** while overhead and unspotted, the Verger does not act on the Enemy Phase. It answers the player *taking an Action*.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Overhead Intercept | **Interception** (§7) | None — fires on the player declaring any Action, including Hold | N/A — unparryable | N/A | 15 raw + 1 Discombobulation, **and the declared Action is lost.** The Verger does not act on the Enemy Phase this round. | N/A | N/A |
| Drop Sermon | Heavy *(grounded only)* | "It comes down off the vault and finds its feet." | Target 1.30s, ±0.20s | 1 | 50 raw + 1 Influence | Standard | Standard |

- **Stated counter (required by §7):** any ranged attack, thrown item, or AOE that reaches the ceiling **forces it down for one round, automatically, no check.** The Salvage Launcher does this by default. Knocking it down before committing to anything is the entire fight.
- **Secondary Actions:**
  - **Rethread the Vault** — *Trigger:* it is grounded. *Cooldown:* 2 rounds. No attack. It takes its full move straight back up and re-enters concealment. This is what it does with most grounded rounds; getting it down is easy, keeping it down is not.
  - **Spit Chrism** — *Trigger:* it is grounded and has already used Rethread the Vault this encounter. *Cooldown:* 3 rounds. Unparryable, ranged 8m, 0 raw: 2 Influence, and the target's parry tolerances narrow by 0.05s for 2 rounds.
- **Kitable:** N — it goes over everything and it is faster than you. **Assess 0–1:** "Something is above you and it is waiting for you to start something." · **Assess 2+:** "It answers the first thing you do, every round, and holding for a parry counts. Put something in the air first — anything at all — and it comes down. Break three legs and it stays down."
- **White Salts drop:** 26. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** committing to an Action before controlling the vertical. **Dismember threat:** Moderate. **Retreat always reachable:** N — it follows across the ceiling.

## Monster 81 — The Long Reach

- **Archetype:** Crawler (elite) · **Level Range:** 12–25 · **HP:** 700 · **Move:** 8m across walls and ceilings · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Eight legs, six of them ordinary. The other two are longer than the room is tall and they are the only two that have ever been used for anything.
- **Limbs:** custom. **Six Short Legs, each: stagger 120, ×1.0, sever 170.** **Two Long Legs, each: stagger 90, ×1.2, sever 130** — thin, over-extended, and the only limbs it strikes with. **Severing four legs of any kind ends ceiling movement permanently. Severing both Long Legs means it cannot attack from the ceiling at all** and must come down to do anything whatsoever. **Head: guarded** while overhead; once grounded, stagger 200, ×1.5.
- **Reach: unlimited downward.** Its Long Legs reach the floor from any ceiling height in the game. **It is never within melee reach of the player; the player is always within reach of it.** This is the variant that cannot be answered by a low ceiling.
- **Interception (§7):** it answers the player taking an Action rather than acting on the Enemy Phase.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Reach Down | **Interception** (§7) | None — fires on the player declaring any Action, including Hold | N/A — unparryable | N/A | 18 raw + 1 Discombobulation, **and the declared Action is lost.** It does not act on the Enemy Phase this round. | N/A | N/A |
| Pin | Heavy *(only against a creature within 2m of a wall)* | "One of the long ones comes down the wall behind you." | Target 1.20s, ±0.15s | 2 | 55 raw, and the target loses 4m from next turn's movement budget | Standard | Standard |

- **Stated counter (required by §7):** ranged attacks and thrown items reach it as normal — **and, uniquely, the Long Legs hang low enough that an Arc attack (§10) may be declared against them from the floor.** Point attacks cannot. A player with a wide weapon can cut this thing down without ever leaving the ground; a player with only fast, precise ones needs something that flies.
- **Secondary Actions:**
  - **Camouflage** — *Trigger:* it took damage in this round. *Cooldown:* 2 rounds. No attack. It takes the ceiling's colour: Ambush DC +6 for 3 rounds, and it cannot be targeted by ranged attacks at all without first passing an Ambush Perception check (§10).
  - **Winch** — *Trigger:* it has Intercepted twice this encounter. *Cooldown:* 4 rounds. No Interception this round. It lifts the player 3m off the floor and drops them: 25 raw, prone, and 3m of movement lost.
- **Kitable:** N. **Assess 0–1:** "It is above you and it does not need to come any closer." · **Assess 2+:** "Two of those legs are long and thin and they are the ones doing the work. They hang low enough to swing at, if you have something wide. Everything else about it is out of reach and always will be."
- **White Salts drop:** 30. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** owning only one shape of weapon. **Dismember threat:** Moderate. **Retreat always reachable:** N.

## Monster 82 — The Plaster Widow

- **Archetype:** Crawler (mook) · **Level Range:** 5–20 · **HP:** 420 · **Move:** 8m across walls and ceilings · **Scale Band:** 1–20 (×1.0)
- **Flavour:** The ceiling has a damp patch in it. The damp patch has six legs and it is exactly the colour of the ceiling, because it has been eating the ceiling.
- **Limbs:** custom. **Six Legs, each: stagger 100, ×1.0, sever 150.** Staggering any leg drops it for 2 turns; **severing three grounds it permanently** at a 2m crawl. **Head: guarded** while overhead; once grounded, stagger 170, ×1.5.
- **Camouflaged by default.** **Ambush DC 16**, not the standard band. A player who fails Ambush Perception (§10) does not know it is in the room at all until it Intercepts, and the DM should not describe it before then.
- **Reach:** 2m below the ceiling — genuinely meltable in a service corridor, untouchable in a gallery.
- **Interception (§7).**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| First Contact | **Interception** (§7) | None — fires on the player declaring any Action, including Hold | N/A — unparryable | N/A | 12 raw + 1 Discombobulation, **and the declared Action is lost.** It does not act on the Enemy Phase this round. | N/A | N/A |
| Spit Lime | Ranged *(grounded only)* | "It arches and its throat works." | Target 1.55s, ±0.20s | 1 | 20 raw + 2 Corrosion | Standard | Standard |

- **Stated counter (required by §7):** ranged, thrown or AOE reaching the ceiling brings it down for a round, no check. Passing the Ambush Perception check on entering the room means the Interception cannot fire at all until it re-conceals.
- **Secondary Actions:**
  - **Re-Plaster** — *Trigger:* it is grounded. *Cooldown:* 2 rounds. No attack. Full move back to the ceiling and it re-enters camouflage — **the player must pass Ambush Perception again to know where it is.**
  - **Drop the Ceiling** — *Trigger:* three or more legs staggered or severed. *Cooldown:* once per encounter. It tears a section of plaster down as it falls: 30 raw to everything within 3m, itself included, and the debris becomes difficult terrain (double movement cost) for the rest of the encounter.
- **Kitable:** N. **Assess 0–1:** "Look up." · **Assess 2+:** "It is the same colour as what it is standing on and it will not move until you do something. If you spotted it, it has lost its ambush — keep it in sight and it is an ordinary small thing."
- **White Salts drop:** 16. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** walking into a room without looking up. **Dismember threat:** Low. **Retreat always reachable:** N.

## Monster 83 — The Kettle-Spider

- **Archetype:** Crawler (elite) · **Level Range:** 10–20 · **HP:** 680 · **Move:** 8m across walls and ceilings · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Eight iron legs and, slung underneath on a short chain, a small sealed kettle that has never once stopped simmering. It walks the roof of the forge in the same circuit it has always walked.
- **Limbs:** custom. **Eight Legs, each: stagger 115, ×1.0, sever 165.** Staggering one drops it for 2 turns; **severing four grounds it permanently.** **The Kettle** — implement, **isolated HP pool** (damage to it does NOT chip the Spider's HP): ×1.5, stagger 70, sever 120. Kettle stagger → Scald Rain disabled 2 rounds. **Kettle sever → it ruptures where it hangs: 40 raw + 3 Burning to everything within 3m, the Spider included.** **Head: guarded** while overhead; grounded, stagger 200, ×1.5.
- **Reach:** 2m below the ceiling. **State ceiling height when the room is generated** — this is the variant that is a completely different fight in a crawlspace than in a hall.
- **Interception (§7), positional.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Scald Rain | Ranged *(from ceiling)* | "The kettle tips a few degrees and holds there." | Target 1.45s, ±0.20s | 1 | 30 raw + 2 Burning to a 2m radius directly beneath it | Standard | Standard |
| Leg Sweep | **Interception** (§7) | None — fires on the player declaring any Action **while standing directly beneath it** | N/A — unparryable | N/A | 15 raw, **and the declared Action is lost.** It does not act on the Enemy Phase this round. | N/A | N/A |

- **Stated counter (required by §7):** **the trigger is positional — do not stand underneath it.** Moving out from beneath is a complete answer, freely available every round, and Scald Rain exists to punish leaving it until the worst possible moment. Ranged and thrown attacks also bring it down for a round, as with any Crawler.
- **Secondary Actions:**
  - **Boil Over** — *Trigger:* it has 2 or more Burning stacks, or the Kettle is staggered. *Cooldown:* 3 rounds. It tips the kettle deliberately: a 3m pool of scalding wash on the floor beneath it, applying 2 Burning per round for 4 rounds.
  - **Hang Low** — *Trigger:* it has taken no damage for two consecutive rounds. *Cooldown:* 3 rounds. It descends to 1m above the floor. **Fully melee-able this round from anywhere in the room** — and Scald Rain's radius doubles to 4m while it is down there.
- **Kitable:** N. **Assess 0–1:** "Whatever is in that pot has not cooled in a hundred years." · **Assess 2+:** "It only intercepts what is standing under it, so don't. Break the kettle and it loses the rain — but it will not just spill, it will go off, and you should not be near it when it does."
- **White Salts drop:** 28. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** fighting from wherever you happen to be standing. **Dismember threat:** Moderate. **Retreat always reachable:** N.

## Monster 84 — The Assessor

- **Archetype:** Leech (elite) · **Level Range:** 5–20 · **HP:** 320 · **Move:** 5m, keeping 6m and a clear sightline · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A small hunched clerk in a good coat, holding a ledger open at a page with your handwriting on it. It has not looked up. It does not need to.
- **Limbs:** standard humanoid defaults — soft, low HP, dies to two of anything that reaches it. **The Ledger** — implement, **isolated HP pool**: ×1.5, stagger 60, sever 90. **Ledger sever → all drains stop permanently and the Assessor leaves the room immediately.**
- **It deals no physical damage of any kind.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Assessment | Aura *(range 10m, requires line of sight)* | None — unparryable. Begins the round after it establishes. | N/A | N/A | **Drains 6 White Salts from the player's Purse per round.** Zero damage. If the Purse is empty, it drains **1 Insight every third round** instead. | N/A | N/A |

- **Secondary Actions:**
  - **Revised Figure** — *Trigger:* the player took damage from any other source in the previous round. *Cooldown:* 2 rounds. The drain doubles to 12 Salts per round for 2 rounds. It is pricing risk, and it is pricing it correctly.
  - **File** — *Trigger:* it has drained 40 or more Salts. *Cooldown:* once per encounter. No drain. It closes the ledger and moves its full budget toward the nearest exit. **If it leaves the room the drained Salts are gone for the instance; killing it before it exits returns half of what it took.** The only Leech in the manual that can be made to give anything back.
- **Kitable:** Y, and pointless — the drain is line-of-sight, not melee range. **Breaking line of sight stops it outright**, which is usually cheaper than killing it and always more annoying.
- **Assess 0–1:** "It isn't coming for you." · **Assess 2+:** "It is taking your Purse, six a round, from across the room, and it will take more the worse your day is going. Break the book or break the sightline — hitting the clerk is the slow way round."
- **White Salts drop:** 18, plus whatever is recovered. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** triaging targets purely by damage output. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 85 — The Understanding

- **Archetype:** Leech (elite) · **Level Range:** 8–20 · **HP:** 280 · **Move:** 0m — it does not travel and it does not follow · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A patch of ordinary air, about the height of a person, that the eye keeps declining to settle on. It is not hidden. It is simply not interesting, and it is working very hard at that.
- **Limbs:** none. Single sever-immune **Presence** entry, ×1.0. No stagger, no Precision Strike, no Precision Strikes.
- **It deals no physical damage of any kind.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Comprehension | Aura *(5m radius)* | None — unparryable | N/A | N/A | **Drains 1 Insight from any creature inside the radius, every second round.** Zero damage. Insight taken this way is gone; it is not returned on the creature's death. | N/A | N/A |

- **Placement rule:** it is always placed on top of something the player wants. That is the entire encounter and the DM should not be subtle about it.
- **Secondary Actions:**
  - **Offer** — *Trigger:* it has drained 2 or more Insight this encounter. *Cooldown:* 4 rounds. No drain. Instead it **returns 1 Insight and states one true fact about this instance**, and the creature it returns it to takes **3 Insanity**. It is trading, and it is trading badly in the player's favour, which should be more worrying than it is.
  - **Widen** — *Trigger:* a creature has been inside the radius for three consecutive rounds. *Cooldown:* 3 rounds. The radius grows to 8m, permanently for the encounter.
- **Kitable:** N/A — it never moves. Walking out of the radius is a complete counter and costs nothing but the thing you came in for.
- **Assess 0–1:** "There is something there and you keep forgetting there is something there." · **Assess 2+:** "Whatever it is doing, it is doing it to the part of you that reads things. Every second round, and it does not give it back."
- **White Salts drop:** 0 — it has never held any. **Insight:** +1 first sighting, and it will take that straight back off you if you linger.
- **Boss Gimmick:** N/A. **Habit punished:** treating Insight as a number that only goes up. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 86 — The Borrower

- **Archetype:** Leech (mook) · **Level Range:** 1–20 · **HP:** 240 · **Move:** 7m, closing to 4m and then holding · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Waist-high, thin, and mostly hands. It has more hands than it has anywhere to put them, and it is holding several things that were recently yours.
- **Limbs:** custom. **Head:** standard (180, ×1.5). **Hands, two: stagger 80, ×1.2** — long, fine and used for precisely one thing. Sever one → Borrow takes half as much (rounding down, minimum nothing). **Sever both → Borrow permanently disabled.** **Legs:** standard (300, ×0.75).
- **It deals no physical damage of any kind.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Borrow | Aura *(4m)* | None — unparryable | N/A | N/A | **Removes one charge from a random carried item, or one Powder capsule, or one Salvage Launcher round, per round.** Zero damage. Everything it takes is held visibly in its hands. | N/A | N/A |

- **Secondary Actions:**
  - **Blink** — *Trigger:* it takes any damage. *Cooldown:* 1 round. No Borrow. It relocates up to 8m anywhere in the room it has line of sight to, ignoring terrain, walls excepted. Chasing it is exactly as productive as it sounds.
  - **Return** — *Trigger:* below 25% HP. *Cooldown:* once per encounter. It holds out everything it has taken. Accepting is a Fast Action within 2m and **it will not act that round**; taking the offer ends its hostility for the encounter and it leaves. Refusing means killing it, which drops everything anyway. **There is no mechanical difference between the two. There is a difference.**
- **Kitable:** N — it out-moves you and it does not want to be caught. **Assess 0–1:** "Check your pockets." · **Assess 2+:** "It is taking charges, one a round, and it will keep skipping out of reach every time you connect. Take the hands off it and it stops. Or wait — it gives everything back if you let it get frightened enough."
- **White Salts drop:** 12. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** assuming an enemy that can't hurt you can be ignored. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 87 — The Diminishing

- **Archetype:** Leech (elite) · **Level Range:** 10–25 · **HP:** 400 · **Move:** 4m · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Nothing. There is nothing there. There is a persistent sense of having been slightly better at things a minute ago.
- **Limbs:** **none while unrevealed — it has no legal target of any kind.** Once it has drained at least once and the DM has stated its position: standard humanoid defaults, with **Head: stagger 140, ×1.5** — soft, and it was never built to be found.
- **Invisible by default.** It cannot be targeted until it has drained once. **Assess reveals its presence but never its location.**
- **It deals no physical damage of any kind.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Diminish | Aura *(6m)* | None — unparryable | N/A | N/A | The player loses **2 points from one attribute of the DM's choosing, per round**, cumulative. Zero damage. **ESV, movement budget, save DCs and weapon damage all recalculate live.** Restored in full the moment the creature dies or the player leaves the room. | N/A | N/A |

- **Secondary Actions:**
  - **Choose Again** — *Trigger:* the drained attribute has fallen 6 or more points. *Cooldown:* 3 rounds. It switches to a different attribute and **keeps the first one drained.**
  - **Recede** — *Trigger:* it has been damaged twice this encounter. *Cooldown:* 3 rounds. No drain. It returns to invisibility and cannot be targeted again until it next drains — which it will, next round.
- **Kitable:** N/A — leaving the room is the complete counter and costs nothing but the room. **Assess 0–1:** "Something is wrong with you and it started when you walked in here." · **Assess 2+:** "It is taking points off you, two a round, and it will move to another score once it has ruined the first. It cannot be hit until it acts and it will hide again the moment it is hurt. The doorway is a full counter."
- **White Salts drop:** 24. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** fighting on through a debuff because the numbers on the sheet still look survivable. **Dismember threat:** None. **Retreat always reachable:** Y.

## Monster 88 — The Drain Mother

- **Archetype:** Snare (elite) · **Level Range:** 10–25 · **HP:** 2000 · **Move:** 0m — anchored through the main grate and grown into it · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Something took up residence in the outflow a long time ago and has been fed by the building ever since. It is mostly below the floor. What is above the floor is six arms and an opinion about where you should be standing.
- **Limbs:** custom. **Anchor Body: ×0.4, no stagger threshold, sever-immune** — armour by the §10 rule. Grinding 2000 HP through a ×0.4 multiplier is legal, will work, and will take all night. **This is not the intended kill.** **Six Tendrils, each: stagger 130, ×1.2, sever 190.** Each covers a stated arc and reaches **6m** from the anchor. **Tendril sever → that arc is permanently safe for the rest of the encounter and the Drain Mother loses one Lash per round.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Lash | Heavy — **one per surviving tendril, all resolving in the same Enemy Phase** | "Three of them come off the floor at once and there is no telling which." | Target 1.35s, ±0.20s each | 1 | 35 raw + 1 Bleeding per unparried Lash | Standard | Standard |

- **One parry per round (§7).** With six tendrils live, five Lashes land. With two live, one lands. The fight gets better only as fast as the player takes it apart.
- **Secondary Actions:**
  - **Haul** — *Trigger:* the player is within 3m of the anchor. *Cooldown:* 2 rounds. No Lashes. Every surviving tendril grabs at once: **Strength DC 15** or be dragged onto the grate and pinned for one round.
  - **Regrow** — *Trigger:* two or more tendrils severed and it took no damage in the previous round. *Cooldown:* 5 rounds. It spends **3 rounds** regrowing one tendril, taking no other action at all for the duration. Interrupting it with a single point of damage cancels it outright; letting it finish costs the arc back.
- **Kitable:** N/A — it never moves, and the room is the fight. Its reach shrinks as tendrils come off, so distance becomes a real strategy over the encounter rather than a binary.
- **Assess 0–1:** "It is not going to chase you. It does not have to." · **Assess 2+:** "The body is armoured and there is a great deal of it — you will not win that way. Six arms, each one owns a slice of the room, and every one you take off is a slice you can stand in. Do not go near the middle."
- **White Salts drop:** 45. **Insight:** +1/+0.
- **Boss Gimmick:** N/A — it is an elite, and it is built to be dismantled rather than defeated. **Habit punished:** treating a health bar as the objective. **Dismember threat:** High. **Retreat always reachable:** Y.

## Monster 89 — The Hanging Rood

- **Archetype:** Snare (elite) · **Level Range:** 8–20 · **HP:** 1500 · **Move:** 0m — grown into the rood screen across the width of the chancel · **Scale Band:** 1–20 (×1.0)
- **Flavour:** The screen has been repaired. Repeatedly, badly, and by something with a very clear idea of where people walk. Twelve wires run from it out into the pews at shin height, waist height, and throat height.
- **Limbs:** custom. **Screen Body: ×0.5, no stagger, sever-immune** — armour by the §10 rule; 1500 HP behind it. Not the intended kill. **Twelve Wires: no HP and no stagger threshold.** Each spans a stated 4m line across the room. **A wire is destroyed outright by a single Arc attack (§10) declared against it, or by any sever-capable hit. Point attacks cannot cut them at all.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Draw | Reactive | None — **unparryable, deliberately.** Triggers on any creature crossing a live wire. | N/A | N/A | 25 raw + 1 Bleeding, and the crossing creature forfeits the rest of its movement. **This applies to enemies as well, and the Rood does not care.** | N/A | N/A |
| Toll the Screen | Aura — every third round | "The wires all go tight at once and the note comes up out of the floor." | Unparryable | N/A | 1 Influence to everything in the room, **+1 per five wires still live** | N/A | N/A |

- **Secondary Actions:**
  - **Cinch** — *Trigger:* two or more creatures are standing between the same pair of wires. *Cooldown:* 3 rounds. The pair draws together: 40 raw to everything in that gap, held there for one round (**Strength DC 14** as an Action to break out).
  - **Restring** — *Trigger:* four or more wires cut. *Cooldown:* 4 rounds. No other action. Three wires are restored at the start of the following round.
- **Kitable:** N/A. The counter is cartography, not movement.
- **Assess 0–1:** "Do not walk in a straight line in here." · **Assess 2+:** "The screen itself is armoured and there is no point. The wires are the creature. Something wide cuts them; something quick will not. And they do not know whose side anyone is on — cut the right three and stand in the right place and the room will fight itself."
- **White Salts drop:** 40. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** moving before mapping. **Dismember threat:** Moderate. **Retreat always reachable:** Y — through a wire, at the usual price.

## Monster 90 — The Bellows Root

- **Archetype:** Snare (elite) · **Level Range:** 12–25 · **HP:** 1800 · **Move:** 1m per encounter — it drags its anchor a single metre and no more · **Scale Band:** 1–20 (×1.0)
- **Flavour:** The forge's bellows grew roots at some point and the roots grew opinions. Four leather arms come off a central knot that breathes on its own schedule, and each one has scorched a quadrant of the floor black.
- **Limbs:** custom. **Root Mass: ×0.5, no stagger, sever-immune** — armour by the §10 rule, 1800 HP behind it, not the intended kill. **Four Bellows Arms, each: stagger 150, ×1.1, sever 210.** Each owns a 90° quadrant out to **5m**. Sever → that quadrant is permanently safe and the Root loses one Blast per round. **The Throat: ×1.6, stagger 200, sever 280 — physically sealed until two Arms are severed**; no Precision Strike resolves against it before then. **Throat sever → it collapses regardless of remaining HP.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Blast | Heavy — **one per surviving Arm, simultaneous** | "The knot inflates and every arm that still works comes up." | Target 1.50s, ±0.20s each | 1 | 30 raw + 1 Burning per unparried Blast | Standard | Standard |
| Draw Air | Aura — every third round | "It breathes in and the room goes with it." | Unparryable | N/A | **All Burning stacks anywhere in the room consolidate onto the single creature nearest the Root.** No new stacks are created. | N/A | N/A |

- **Secondary Actions:**
  - **Bank** — *Trigger:* it has 3 or more Burning stacks. *Cooldown:* 3 rounds. It converts every Burning stack on itself into **+15 raw on all Blasts for the rest of the encounter**, cumulative. Setting fire to this is a mistake and Assess 2+ says so.
  - **Regrow** — *Trigger:* an Arm has been severed and the player is more than 5m from the anchor. *Cooldown:* 5 rounds. It spends **4 rounds** regrowing one Arm, taking no other action. Any damage cancels it.
- **Kitable:** N/A — it does not chase and it does not need to. **Assess 0–1:** "The floor is scorched in four wedges and you can see where they meet." · **Assess 2+:** "The body is armoured and pointless. Four arms, four quadrants; take two off and the middle opens up, and the middle ends it. Do not burn it — it eats that and hits harder."
- **White Salts drop:** 42. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** reaching for fire in a forge. **Dismember threat:** High. **Retreat always reachable:** Y.

## Monster 91 — The Sill

- **Archetype:** Snare (mook) · **Level Range:** 1–20 · **HP:** 900 · **Move:** 0m — it is a doorway · **Scale Band:** 1–20 (×1.0)
- **Flavour:** An ordinary doorframe with an ordinary door standing open in it. The jamb is slightly wet. It has been slightly wet for a very long time and the wet has started to have preferences about who passes.
- **Limbs:** custom. **Frame: ×0.3, no stagger, sever-immune** — it is masonry with opinions, and killing 900 HP through ×0.3 is not a plan. **Two Jamb Tendrils, each: stagger 110, ×1.2, sever 160.** **Severing both renders the Sill completely inert.** It never dies and it never needs to.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Threshold | Reactive | None — **unparryable, deliberately.** Triggers on any creature passing through the doorway, in either direction. | N/A | N/A | 30 raw + 2 Corrosion. **Applies to enemies as well.** | N/A | N/A |
| Clasp | Heavy *(only against a creature standing in the doorway at the start of the Enemy Phase)* | "The jamb flexes inward." | Target 1.25s, ±0.15s | 2 | 45 raw, and the target is held in the doorway until a full Action is spent breaking free | Standard | Standard |

- **Secondary Actions:**
  - **Narrow** — *Trigger:* a creature passed through in the previous round. *Cooldown:* 2 rounds. The gap closes: passing through next round costs the **entire** movement budget and triggers Threshold **twice**.
  - **Yawn** — *Trigger:* both Jamb Tendrils severed. *Cooldown:* once per encounter. It opens fully and stays that way — inert for the rest of the instance, and no longer obstructing anything at all.
- **Kitable:** N/A. It prices a route; it does not fight.
- **Assess 0–1:** "That door is not doing anything and you do not believe it." · **Assess 2+:** "Two soft things in the jamb, and taking both off ends it for good. The frame itself is a wall — do not waste your time. And it does not check whose side anyone is on, so consider leaving it working."
- **White Salts drop:** 20, **and only if both tendrils are severed** — killing it outright is not really available.
- **Boss Gimmick:** N/A. **Habit punished:** treating doorways as free. **Dismember threat:** Low. **Retreat always reachable:** Y, at the usual toll.

## Monster 92 — The Bathing Party

- **Archetype:** Pack (mook, group-only) · **Level Range:** 5–20 · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Four or five guests in the water and one attendant on the tiles with a whistle round its neck. They came together, they have stayed together, and they do everything at the same time because somebody is still telling them when.
- **Never appears alone.** Always 4–5 Bathers plus one Attendant of the Party.

**Members — The Bathers (×4–5).** HP 220 each · Move 6m · **Limbs:** standard humanoid defaults; soft, and they die to two of anything.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Grip | Light | None — unparryable | N/A | N/A | 15 raw |
| Duck | Heavy | "It takes a breath it does not need." | Target 1.20s, ±0.20s | 1 | 25 raw + 1 Influence |
| Circle | — | None | N/A | N/A | No damage. It moves its full budget to a flanking position. |

**Alpha — The Attendant of the Party.** HP 700 · Move 5m · **Limbs:** custom. **Head: stagger 240, ×1.5.** **The Whistle** — implement, **isolated HP pool**: ×1.5, stagger 50, sever 80. **Whistle sever → coherence breaks immediately, exactly as though the Attendant had died.** It is a far softer target than the Attendant and that is the entire point. **Arms/Legs:** standard.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Call the Order | Aura | "The whistle comes up." | Unparryable | N/A | No damage. **Every Bather takes the same declared action this round.** |

- **While the Attendant lives (or the Whistle is intact):** all Bathers use the same attack on the same round. Five Ducks in one Enemy Phase is 125 raw and 5 Influence against a single parry (§7).
- **Coherence broken:** each surviving Bather rolls independently each round — d3: 1 Grip, 2 Duck, 3 Circle. Nothing about their statlines has changed and the round is now perhaps a third as dangerous.
- **Secondary Actions — Attendant:**
  - **Surround** — *Trigger:* three or more Bathers are within 2m of the player. *Cooldown:* 3 rounds. No call. Every Bather in contact deals **+10 raw** next round if the player is still surrounded at the start of the next Enemy Phase.
  - **Sound the Retreat** — *Trigger:* two or more Bathers killed. *Cooldown:* 4 rounds. Surviving Bathers withdraw their full move and re-form around the Attendant; each heals 40 HP.
- **Secondary Actions — Bather (post-coherence only):**
  - **Flee** — *Trigger:* the Attendant is dead and this Bather is below 40% HP. *Cooldown:* once. It leaves the room entirely and relocates elsewhere in the instance. **The DM tracks where it went** and attaches it to whatever it finds there.
  - **Yield** — *Trigger:* the Attendant is dead and this Bather is the last one standing. *Cooldown:* once. It stops and holds up empty hands. It will not attack unless attacked, it can be questioned, and **it knows one true thing about this instance.**
- **Kitable:** N — five of them at 6m is not something you outwalk. **Assess 0–1:** "They are all doing the same thing at the same time." · **Assess 2+:** "One of them is calling it. Kill that one — or better, break the whistle, which is nothing at all to break — and they stop moving as one thing. They are individually pathetic. That is not the problem."
- **White Salts drop:** 8 per Bather, 35 for the Attendant. **Insight:** +1/+0 (Pack counts as one archetype sighting).
- **Boss Gimmick:** N/A. **Habit punished:** killing whatever is nearest. **Dismember threat:** Moderate in aggregate. **Retreat always reachable:** Y.

## Monster 93 — The Instar

- **Archetype:** Pack (mook–elite, group-only) · **Level Range:** 10–25 · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Five pale grubs the length of a forearm, and above them something with wings the colour of a stained window. The grubs do not look up at it. They do not need to look up at it.
- **Never appears alone.** Always 5 Grubs plus one Imago.

**Members — The Grubs (×5).** HP 160 each · Move 7m · **Limbs:** custom. **Body: stagger 80, ×1.0, sever 110** — one entry, no head, no arms, no legs.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Chew | Light | None — unparryable | N/A | N/A | 12 raw + 1 Bleeding |
| Rear | Heavy | "It stands up on the back half of itself." | Target 1.10s, ±0.15s | 2 | 22 raw |
| Burrow | — | None | N/A | N/A | No damage. **Untargetable this round**; resurfaces adjacent to the player at the start of the next. |

**Alpha — The Imago.** HP 620 · Move 10m flight · **Limbs:** custom. **Wings, two: stagger 100, ×1.3, sever 140.** Sever one → grounded, Move 3m. **Sever both → grounded permanently and Unison Cry is disabled.** **Body: stagger 200, ×1.0.**

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Unison Cry | Aura | "The wings stop, all at once, at the top of the beat." | Unparryable | N/A | No damage. **Every Grub takes the same declared action this round.** |
| Dust | Ranged | "It shakes something off the wings and it hangs in the air." | Target 1.50s, ±0.20s | 1 | 25 raw + forces an Insanity save |

- **While the Imago lives:** five Rears in a single Enemy Phase is 110 raw against one parry. Five Burrows means nothing in the room is targetable and all five resurface adjacent.
- **Coherence broken:** independent d3 rolls per Grub, and Burrowed Grubs stay under for 2 rounds instead of 1.
- **Secondary Actions — Imago:**
  - **Moult a Grub** — *Trigger:* fewer than three Grubs alive. *Cooldown:* 4 rounds. No cry. A new Grub emerges from its own abdomen at half HP. **Three times per encounter maximum.**
  - **Lift** — *Trigger:* it has taken damage twice in the same round. *Cooldown:* 3 rounds. It climbs beyond melee reach for 2 rounds; only ranged and Arc attacks (§10) reach it.
- **Secondary Actions — Grub (post-coherence only):**
  - **Play Dead** — *Trigger:* it takes a hit leaving it below 30% HP. *Cooldown:* once. It goes limp and is treated as a corpse in every respect. It rises at the start of any round in which the player's attention is elsewhere or a new enemy enters the room, with a full **ambush** opening (§10) — against the player, not for them.
  - **Pupate** — *Trigger:* it has survived three rounds after the Imago's death. *Cooldown:* once. It seals itself and is untargetable. **After 4 rounds it emerges as a second Imago at half HP and the pack re-coheres.** Killing the Alpha is not permanent unless the Grubs are cleaned up, and Assess 2+ says so.
- **Kitable:** N. **Assess 0–1:** "The big one is not fighting. The big one is conducting." · **Assess 2+:** "Kill the winged one and the rest stop working as a single animal — but do not walk away afterwards. One of them will get up, and one of them will become the next winged one if you let it sit."
- **White Salts drop:** 6 per Grub, 32 for the Imago. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** leaving a fight the moment it stops being dangerous. **Dismember threat:** Low individually, High in aggregate. **Retreat always reachable:** Y.

## Monster 94 — The Tallow Hounds

- **Archetype:** Pack (elite, group-only) · **Level Range:** 12–25 · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Three or four dogs rendered down and set again in roughly the original shape, and a man holding all their leads in one hand. He has not said anything. He does not have to; they are watching his hand.
- **Never appears alone.** Always 3–4 Hounds plus one Kennelman.

**Members — The Hounds (×3–4).** HP 260 each · Move 9m · **Limbs:** custom. **Head: stagger 150, ×1.5. Legs: stagger 100, ×1.0** — sever one → Move drops to 3m.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Snap | Light | None — unparryable | N/A | N/A | 18 raw + 1 Bleeding |
| Bear Down | Heavy | "It drops its shoulders and stops making any noise at all." | Target 1.05s, ±0.15s | 2 | 30 raw, and the target is knocked prone on a hit |
| Cut Off | — | None | N/A | N/A | No damage. It moves to block the player's nearest exit and holds there. |

**Alpha — The Kennelman.** HP 780 · Move 5m · **Limbs:** custom. **Head: stagger 260, ×1.5.** **Lead arm: stagger 130, ×1.2** — **sever → coherence breaks immediately, exactly as though he had died**, and he fights on alone. **Legs:** standard.

| Attack | Type | Tell | Window | Tier | Hit Effect |
|---|---|---|---|---|---|
| Set On | Aura | "His hand moves about an inch." | Unparryable | N/A | No damage. **Every Hound takes the same declared action this round.** |
| Crop | Heavy | "He winds the lead once round his fist." | Target 1.40s, ±0.20s | 1 | 45 raw + 1 Burning |

- **Secondary Actions — Kennelman:**
  - **Whip In** — *Trigger:* a Hound is below 40% HP. *Cooldown:* 3 rounds. That Hound withdraws to him and heals 80 HP. **No Set On this round**, so the pack acts independently for one round — a free window, bought by hurting one of them badly.
  - **Slip the Leads** — *Trigger:* below 35% HP. *Cooldown:* once per encounter. He lets go. All Hounds gain **+2m Move and +10 raw, permanently**, and **coherence can no longer be broken by killing him or taking his arm.** Assess 2+ warns that the lead is the thing to cut, and warns before this fires — not after.
- **Secondary Actions — Hound (post-coherence only):**
  - **Tame** — *Trigger:* the Kennelman is dead or disarmed, this Hound is below 25% HP, and the player has not attacked it this round. *Cooldown:* once. It stops, lies down, and **follows the player for the remainder of the instance as an Instance Companion** (generated per Ruleset §18: 260 HP, one Action per turn, Snap only). It expires with the layout, as all Instance Companions do.
  - **Cut Off** — *Trigger:* the player has moved 6m or more in a turn. *Cooldown:* 2 rounds. It takes the exit and stands in it.
- **Kitable:** N — 9m each, and they will take the door before you do. **Assess 0–1:** "The man is not the dangerous one and the man is the dangerous one." · **Assess 2+:** "They are watching his lead hand. Take the arm and they scatter — that is cheaper than killing him. But if you leave him alive too long he lets go on purpose, and after that nothing you do to him matters at all."
- **White Salts drop:** 10 per Hound, 38 for the Kennelman. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** grinding the biggest health bar first. **Dismember threat:** High. **Retreat always reachable:** N while the Hounds hold the exits.

## Monster 95 — The Bathhouse Warden

- **Archetype:** Stalker · **Level Range:** any — it is not levelled, it is survived · **HP:** 3000 (hand-set, exempt from scaling) · **Move:** 6m, relentless, never sprints, never stops, **crosses rooms** · **Scale Band:** exempt
- **Flavour:** Somebody's idea of a member of staff. Too tall for the corridors it walks and entirely untroubled by that. It has a brass plate bolted over its sternum with a number stamped on it, and the number is low.
- **Limbs:** custom. **Head: stagger 400, ×1.5.** **Arms, each: stagger 200, ×0.8** — stagger disables its grab on that side for 2 turns. **Knees, each: stagger 130, ×1.0** — **staggering a knee drops it for 3 rounds and it must spend a further round rising. Severing a knee (190) puts it down for 6 rounds and drops its Move to 4m permanently.** This is the intended interaction and the entire reason the archetype exists. **The Keyplate: ×0.9, stagger 900, sever 1200, and it takes ×0.5 incoming damage on top of that.** Sever it and the Warden stops, immediately and permanently. **Nothing in the current armoury comes within a factor of four of that number, and that is the point.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Take Hold | Heavy | "It reaches, and it does not hurry, because it does not have to." | Target 1.60s, ±0.20s | 1 | 60 raw, and the target is held for one round (**Strength DC 16** as an Action to break free) | Standard | Standard |
| Correction | Heavy *(only against a held target)* | "The other hand comes up." | Target 1.30s, ±0.15s | 2 | 110 raw | Standard | Standard |

- **Alert state.** Once it has seen the player it pursues for the remainder of the instance. It knows which room they are in. It does not lose interest. **Staggered limbs do not recover between rooms** — damage done to it persists across the whole run, which is the only mercy in the entry.
- **Environmental answers — the instance MUST contain at least one, decided when the layout is generated (Bible §0):** a floor grate or drop it can be walked onto (10 rounds to climb out); a boiler room or plant room it can be shut into; a flooded chamber that reduces it to 2m; or a Brute-tier creature that will engage it in preference to the player. **If a given roll genuinely has none, finding the anchor and leaving is the correct play and the DM must let that read cleanly.**
- **Secondary Actions:**
  - **Reset the Joint** — *Trigger:* a knee is staggered or severed. *Cooldown:* none. It stops where it is, kneels, and takes **2 full rounds doing nothing at all** while it puts the joint back. The stagger clears at the end of it; a sever does not come back. **Two free rounds, every single time, and they are the whole reason to break its legs.**
  - **Roar** — *Trigger:* the player has left a room without engaging it. *Cooldown:* 3 rounds. No attack. **Every enemy in the adjacent rooms joins its pursuit.** A player who has spent the run avoiding fights is now being followed by all of them at once, in a group, behind something that cannot be killed.
- **Kitable:** Y, at 6m against your 8m — and that two-metre margin is the entire relationship. **Assess 0–1:** "Do not." · **Assess 2+:** "The plate on its chest is the only thing that ends it and nothing you own will scratch it. The knees are what you have. Break one, take the two rounds it spends putting it back, and go."
- **White Salts drop:** 0 while it lives. **90** if it is ever actually stopped. **Insight:** +1 first sighting, +2 if stopped by any means.
- **Boss Gimmick:** N/A — it is not a boss, it is a condition of the instance. **Habit punished:** the assumption that everything in a room is there to be killed. **Dismember threat:** Very High. **Retreat always reachable:** Y, and it is the answer.

## Monster 96 — The Reliquarian

- **Archetype:** Stalker · **Level Range:** any · **HP:** 2400 (hand-set, exempt from scaling) · **Move:** 5m · **Scale Band:** exempt
- **Flavour:** A processional figure in vestments with a hinged brass casket where a head should be. The casket is sealed with wire and lead and it is very slightly too heavy for what it is walking on. It opens doors.
- **Limbs:** custom. **Head: guarded** — the casket is an implement, **isolated HP pool**, ×1.5, **stagger 300**, no sever (it is forced open, not destroyed). The head is not targetable at all until the casket is staggered. **Once open: The Relic — ×2.0, stagger 500, sever 700.** **Relic sever ends it permanently, and the relic can be claimed.** **Arms, each: stagger 250, ×0.8. Legs, each: stagger 160, ×1.0** — stagger → down for 2 rounds.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Censer Swing | Heavy | "The censer goes back on its chain and the chain is longer than it looked." | Target 1.70s, ±0.20s | 1 | 65 raw + 2 Influence | Standard | Standard |
| Litany | Aura — every third round | "You can hear it. You cannot tell from where." | Unparryable | N/A | 1 Influence to everything in the room. **It does not require line of sight and it works through walls within 15m.** | N/A | N/A |

- **It opens doors.** No barricade holds it and it takes exactly one round to get through anything the player has closed. The Litany means the player always knows roughly how close it is, which is worse than not knowing.
- **Environmental answers — at least one per instance:** deep water (it sinks and takes 8 rounds to walk out of anything over 2m); a collapsible stair or gallery (4 rounds to dig free); or leading it into a Snare's arcs and letting the room do the work.
- **Secondary Actions:**
  - **Open the Casket** — *Trigger:* the casket has been staggered. *Cooldown:* once per instance. It opens the casket itself, voluntarily, and does not close it again. The Relic is exposed permanently — **and every Influence effect it applies doubles for the rest of the instance.** Exposing the weak point is a genuine trade, not a reward.
  - **Consecrate** — *Trigger:* the player has been out of its line of sight for two consecutive rounds. *Cooldown:* 4 rounds. No attack. It blesses the room it is standing in: **that room's Influence saves are at +3 DC for the rest of the instance**, whether the Reliquarian is still in it or not. Hiding costs geography.
- **Kitable:** Y at 5m — the slowest Stalker in the manual and the hardest to lose. **Assess 0–1:** "It is coming and it is in no hurry and it knows where you are." · **Assess 2+:** "The head is in the box and the box will not break, only open. Force it and you can end this outright — and everything it does to your head gets twice as bad the moment you do."
- **White Salts drop:** 0 while it lives. **110** if stopped, plus the Relic. **Insight:** +1 first sighting, +2 if stopped.
- **Boss Gimmick:** N/A. **Habit punished:** believing a closed door is a solution. **Dismember threat:** High. **Retreat always reachable:** Y, and it will be there when you get back.

## Monster 97 — The Second Shift

- **Archetype:** Stalker · **Level Range:** any · **HP:** 2600 (hand-set, exempt from scaling) · **Move:** 6m · **Scale Band:** exempt
- **Flavour:** Something that clocked on and never clocked off, built up over the years out of whatever was to hand and whatever was still warm. There is a dull orange line where its sternum should be and it has never gone out.
- **Limbs:** custom. **Head: stagger 350, ×1.5.** **Arms, each: stagger 180, ×1.0. Legs, each: stagger 150, ×1.0** — stagger → down for 2 rounds. **The Slag Heart: ×1.2, stagger 800, sever 1000, and it takes ×0.4 incoming damage on top.** Sever ends it.
- **Regeneration — this is the whole entry.** **Any severed limb regrows in 4 rounds** provided the Second Shift takes no damage during them; it will stop and stand still to do it. Staggers clear in 2. **Nothing done to it is permanent except the Heart.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Cold Work | Heavy | "It changes its grip on nothing in particular." | Target 1.55s, ±0.20s | 1 | 70 raw + 1 Burning | Standard | Standard |
| Bearhug | Heavy *(only if the player is within 1m at the start of the Enemy Phase)* | "It stops walking and opens both arms." | Target 1.15s, ±0.15s | 2 | 90 raw + 3 Burning | Standard | Standard |

- **Environmental answers — at least one per instance:** the quench trough (full submersion stops regeneration entirely for 6 rounds); the rail spur (it can be pushed onto the spur and carried out of the instance for good); or the Frost-Iron Smith, who will engage it on sight and lose slowly, which is all anyone needs.
- **Secondary Actions:**
  - **Anneal** — *Trigger:* a limb has been severed. *Cooldown:* none. It stops where it stands and takes **no action at all for 4 rounds** while it regrows. **This is the window, it is generous, and it will use it as many times as it needs to.** Damaging it during the 4 rounds resets the regrowth but does not stop the standing-still.
  - **Bank the Heat** — *Trigger:* it has taken 400 or more cumulative damage. *Cooldown:* 5 rounds. The Slag Heart brightens: all its attacks apply **+2 Burning** for the rest of the instance, and its damage reduction on the Heart **drops from ×0.4 to ×0.6.** Wearing it down is not nothing. It is just not enough on its own.
- **Kitable:** Y at 6m. **Assess 0–1:** "It is putting itself back together while you watch." · **Assess 2+:** "Cut something off and it will stand there for four rounds fixing it, every time, without fail. That is not a weakness you can kill it with. It is four rounds of head start and you should spend them going somewhere."
- **White Salts drop:** 0 while it lives. **100** if stopped. **Insight:** +1 first sighting, +2 if stopped.
- **Boss Gimmick:** N/A. **Habit punished:** treating dismemberment as progress. **Dismember threat:** Very High. **Retreat always reachable:** Y.

## Monster 98 — The Rule of Silence

- **Archetype:** Rite (elite) · **Level Range:** 8–20 · **HP:** 700 · **Move:** 7m · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A tall grey figure with its hands folded, standing where it can see the whole room. It is not looking at anyone in particular. It is waiting to be given a reason.
- **Limbs:** standard humanoid defaults, and it makes no attempt whatsoever to protect them. It is not that kind of problem.
- **THE RULE — never stated outright to the player.** *It attacks only a creature that took an Action in the previous round.* A creature that spent a round moving only, or doing nothing at all, is invisible to it — completely, including while standing adjacent to it. **The rule never bends. If nobody acted, it does nothing at all that round.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Answer | Heavy | "It unfolds its hands and it is looking at exactly one of you." | Target 1.35s, ±0.20s | 1 | 65 raw + forces an Insanity save, **against one creature that took an Action last round.** If more than one did, the one that dealt the most damage. | Standard | Standard |

- **Secondary Actions:**
  - **Attend** — *Trigger:* no creature took an Action in the previous round. *Cooldown:* 1 round. No attack. It walks to stand directly in front of whichever creature it answered last and folds its hands again. **It is now within 1m, and the next Action anyone takes is answered from adjacent.** Patience is not free either.
  - **Amen** — *Trigger:* it has answered the same creature three times. *Cooldown:* once per encounter. Its next Answer against that creature is **unparryable and deals double.**
- **Kitable:** Y, and kiting is very nearly the intended solve. **Assess 0–1:** "It has not moved and everything else in here has." · **Assess 2+:** "It answers something. Not all of you — one of you, and it picks. Watch what it picks and you will have it inside two rounds."
- **The intended solves, none of which are free:** alternate acting and not acting, at half your normal speed against 700 HP. Or let the companion act, draw the Answer, and work in the gap — which means Maria taking 65 raw on a body with 55 HP unless she is kept out of reach. Or simply leave; it will not follow anyone who has not done anything.
- **White Salts drop:** 34. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** treating the action economy as free. **Dismember threat:** Moderate. **Retreat always reachable:** Y.

## Monster 99 — The Weights and Measures

- **Archetype:** Rite (elite) · **Level Range:** 5–20 · **HP:** 550 · **Move:** 3m · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A brass balance the height of a person, walking on the tripod it was mounted to. Both pans are empty. It has come over to have a look at everyone and it is clearly in the middle of deciding something.
- **Limbs:** custom. **Pans, two: stagger 120, ×1.2, sever 170.** **Severing a pan permanently disables one half of the rule** — it can no longer compare, and defaults to attacking whoever it hit last. **Beam: stagger 300, ×1.0.**
- **THE RULE — never stated outright.** *It attacks whichever creature in the room is currently carrying more, counted as total item and weapon count.* It re-evaluates every round, before acting. Ties go to whichever it struck most recently. **The rule never bends.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Redress | Heavy | "One pan drops. It is looking at whoever the pan dropped toward." | Target 1.45s, ±0.20s | 1 | 55 raw, **and it takes one carried item**, which is placed visibly in a pan | Standard | Standard |

- **Obeying the rule** means dropping things — a Fast Action, freely available. A player who dumps their pack fights a creature that has decided to attack their companion instead, which is a real cost and a real decision rather than a clean exploit.
- **Secondary Actions:**
  - **Level** — *Trigger:* two creatures are exactly equal in carried count. *Cooldown:* 2 rounds. No attack, nothing taken. It heals 60 HP and waits for someone to pick something up.
  - **Tip** — *Trigger:* it holds three or more taken items. *Cooldown:* once per encounter. The pans overbalance and everything in them spills onto the floor 3m away, freely recoverable. It immediately begins again.
- **Kitable:** Y — 3m and it is not trying to catch anyone. **Assess 0–1:** "It is looking at your hands." · **Assess 2+:** "It is weighing you against each other and it has a strong preference for the heavier. Whatever that means to it, it means it consistently."
- **White Salts drop:** 30. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** carrying everything, always, without ever thinking about it. **Dismember threat:** Low. **Retreat always reachable:** Y.

## Monster 100 — The Copyist

- **Archetype:** Rite (elite) · **Level Range:** 10–25 · **HP:** 640 · **Move:** 5m · **Scale Band:** 1–20 (×1.0)
- **Flavour:** A seated figure at a small desk that walks with it, pen already moving. It looks up only when there is something to look up at, and it has already written down what you did last.
- **Limbs:** standard humanoid defaults.
- **THE RULE — never stated outright.** *On its turn it performs the exact action the player performed on the immediately preceding Player Phase, aimed back at them.* Player attacked → it attacks, using that weapon's timing. Player Held → it Holds, and the player's next attack against it must beat a parry attempt. Player used an item → it uses the same category of item on itself, and it works. **Player Assessed → it Assesses, and the DM tells the player one true thing about the Copyist, out loud.** **The rule never bends. If the player did nothing, it does nothing.**

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| Copy | Variable — **no fixed statline** | "It finishes the line it was writing." | **Matches the target time of the player's own preceding action**, ±0.20s | 1 | **Damage equal to whatever the player's preceding action dealt, capped at 70 raw.** Status effects copy across as well. | Standard | Standard |

- **The exploit is Assess**, and it is meant to be findable. A player who works it out farms free, true information every round while the Copyist does nothing else — and spends the entire fight not killing it. That trade is the encounter.
- **Secondary Actions:**
  - **Fair Copy** — *Trigger:* the player has repeated the same Action three rounds running. *Cooldown:* 3 rounds. It performs that action **twice** this round instead of once.
  - **Marginalia** — *Trigger:* it has copied an Assess. *Cooldown:* 2 rounds. No attack. It writes something down. **If the Copyist is killed, its notes are recoverable and legible: one true fact about this instance per Assess it copied.** The exploit has a payout, and collecting the payout means eventually fighting it properly.
- **Kitable:** Y — it only ever does what you did. **Assess 0–1:** "It is writing." · **Assess 2+:** "Whatever you do, it does back. Including this."
- **White Salts drop:** 36. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** autopilot of any kind. **Dismember threat:** Moderate — it will bisect you with your own numbers if you let it. **Retreat always reachable:** Y.

## Monster 101 — The Lodger

- **Archetype:** Passenger (elite) · **Level Range:** 8–20 · **HP:** 180 (the Lodger itself; the host has its own) · **Move:** via its host · **Scale Band:** 1–20 (×1.0)
- **Flavour:** One of the things in the room is standing slightly better than it should be. Its head is level. Its hands are steady. Nothing else in here has steady hands.
- **Limbs:** **while riding, none — the host's limb table applies in full and the Lodger cannot be targeted at all, by anything.** **During transfer only: Body, ×1.4, stagger 90, sever 130** — sever-viable, for exactly one round.
- **Transfer.** When its host dies, the Lodger moves to the nearest available body within **8m**: any living enemy, any corpse including enemies killed earlier in the encounter, **and a companion.** A companion host is controlled by the DM until the Lodger is removed. **If nothing is within 8m, it is exposed on the floor for one round and then dies on its own.**
- **A ridden host gains:** +25% Max HP, +10 raw on all attacks, and +1m Move. It has no attacks of its own and never has.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| — | — | It uses whatever the host has, at the host's own numbers plus its rider bonus. | — | — | — | — | — |

- **Secondary Actions:**
  - **Ride Out** — *Trigger:* the host is below 25% HP and another body is within 8m. *Cooldown:* 3 rounds. It transfers voluntarily, before the host dies. **The old host drops dead on the spot and immediately becomes a valid future body.** Killing the host is not the same as killing the Lodger and it never was.
  - **Settle** — *Trigger:* no other body within 8m at the moment of transfer. *Cooldown:* once per encounter. It burrows into the floor rather than dying. It is gone for 3 rounds and returns riding **the next creature to enter the room** — which may well be one the player brought with them.
- **Kitable:** as the host. **Assess 0–1:** "One of them is different and you cannot say how." · **Assess 2+:** "Whatever is steering that thing is not that thing. Watch what is standing near it when it dies — and clear the floor first, because it will take a corpse."
- **White Salts drop:** 20 for the Lodger, plus the host's own drop. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** leaving bodies where they fall. **Dismember threat:** as the host. **Retreat always reachable:** Y.

## Monster 102 — The Second Occupant

- **Archetype:** Passenger (elite) · **Level Range:** 12–25 · **HP:** 240 · **Move:** via its host · **Scale Band:** 1–20 (×1.0)
- **Flavour:** Something the size of a folded coat, and it has been in this building longer than anything else in this building. It does not fight. It has never once fought. It arranges to be somewhere better.
- **Limbs:** **while riding, none.** **During transfer only: Body, ×1.6, stagger 110, sever 160** — one round.
- **Transfer range 12m**, and **it can ride the player.** **It prefers, in strict order:** the largest creature in the room, then the player, then any corpse.
- **While riding the player:** the player is **not** DM-controlled. Instead they take **15 HP per round**, all their parry and precision tolerances narrow by **0.05s**, and they cannot see the Second Occupant's HP. **Removal:** any other creature within reach removes it as a Full Action, automatically, no check. Alone, the player must pass **Resolve DC 16** as a full Action, once per round. This is the third entry in the manual built around having a second combatant present (Ruleset §18) and the most punishing of them.
- **A ridden enemy host gains:** +30% Max HP and +12 raw on all attacks.

| Attack | Type | Tell | Window | Tier | Hit Effect | Retaliation | Miss Punish |
|---|---|---|---|---|---|---|---|
| — | — | It has no attacks of its own and never has. | — | — | — | — | — |

- **Secondary Actions:**
  - **Vacate** — *Trigger:* the host takes 150 or more damage in a single round. *Cooldown:* 2 rounds. It leaves immediately and is **exposed for one round wherever it lands.** Burst damage is the tool; this is the only reliable way to make it targetable on purpose.
  - **Speak Through** — *Trigger:* it has ridden the same creature for three consecutive rounds. *Cooldown:* 3 rounds. No other effect. **The host says something true, out loud, in a voice the player recognises.** This is a lore delivery mechanism and it should be used as one, deliberately and sparingly.
- **Kitable:** as the host. **Assess 0–1:** "There is one more thing in this room than there are things in this room." · **Assess 2+:** "It moves when its ride is nearly finished, and for one moment on the way across it is a small soft thing in the open. Hit it hard enough in one go and it will jump early. Do not be the biggest thing standing near it."
- **White Salts drop:** 26, plus the host's own drop. **Insight:** +1/+0.
- **Boss Gimmick:** N/A. **Habit punished:** walking in alone. **Dismember threat:** as the host. **Retreat always reachable:** Y, unless it is riding you.

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

- **Secondary Actions** (Ruleset §7 — **at least one is mandatory on every new entry**, written in priority order. Each needs an objective trigger and a stated cooldown, and each must change the shape of the next round rather than just deal damage on a different line):
  - **[Name]** — *Trigger:* [objective, checkable condition]. *Cooldown:* [N rounds / once per encounter]. [Effect.]

- **Interception** (Ruleset §7 — omit entirely unless this entry acts during the Player Phase): *Trigger:* · *Effect:* · **Stated counter:** [mandatory — an interception with no stated answer is not shippable]
- **Attack shape / elemental** (Ruleset §10 — omit unless relevant): Arc/Point interaction · elemental multipliers or immunities
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
- **Passive — Powder Charge (melee variant):** load a capsule as a universal Fast Action (0m), same as the ranged variant. Unlike the Launcher, firing it is a **timed** detonation: target 1.00s, ±0.15s base, widened by Insight window bonus. **Confirmed effects (session 7):** success = ×1.5 damage modifier on that hit, plus 1 Discombobulation to the target. Failure = the wielder takes 2 Bleeding stacks and the turn ends immediately with no leftover movement to spend — harsher than a whiffed self-Rally, deliberately, since the capsule is armed either way.
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
- **Passive:** a long embroidery needle-blade. Self-initiated Precision Strikes (Ruleset §10 — an unparryable grasp, a stationary target) using this weapon have their tightened tolerance eased back one band, toward the limb's own baseline. Built specifically for ambush/precision play rather than raw output.
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
- **Passive:** an absurdly long, thin dueling blade. Every Precision Strike stopwatch (Ruleset §10, limb multiplier >1.0) is widened one full tolerance band while wielding this weapon — a true finesse pick, built entirely around Precision Strikes rather than raw weight.
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
- **Passive:** a fluted blade with a channel cut down its spine and a grip that has never been properly cleaned. **Both Light and Heavy deal +5 raw per Bleeding stack the wielder is currently carrying.** At 9 stacks that is +45 raw on every swing — roughly doubling its output — and at 10 stacks the wielder Ruptures (25% Max HP, Ruleset §5). The weapon does nothing to cause bleeding and nothing to stop it. It simply pays better the closer you are to going over.
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
  - **Every Heavy inflicts 1 Bleeding on the wielder, landed or missed.** The bar does not care whether it connected.
- **Sever viability:** best-in-class outside the Coronal. Heavy clears the Head's 120-raw line at **ESV 32** — fifteen ESV earlier than the Foundry Wedge, the previous benchmark. Arm (~308) and Leg (400) remain out of one-hit reach at any ESV, per the fixed-constant rule (Ruleset §10).

## Weapon 38 — The Hollow Coronal

*The first **Grade S** weapon in the game (Ruleset §4: S ×1.3). The ceiling, and priced like it.*

- **Type:** Heavy · **Stat/Grade:** Strength/S · **Hands:** Two
- **Acquisition:** found — boss-adjacent placement only, hand-placed, one per campaign until deliberately reintroduced. It should feel like a decision, not a drop.
- **Base:** 30. Light = 30+ESV×1.3 · Heavy = 60+ESV×1.95.
- **Worked rows:** ESV 8 → 41/76 · ESV 20 → 56/99 · ESV 47 → 92/152.
- **Passive:** a crown of fused iron on a shaft, or a shaft that ends in one — the join isn't visible. It is the heaviest thing anyone has carried down here and it is not neutral about being carried.
  - **While equipped, the wielder's Insanity and Influence save DC is +3, permanently and unconditionally.** This stacks with the Insight term and does not care about Resolve.
  - **It cannot be unequipped, stowed, or swapped away from inside an instance.** The choice is made at the hub, at the door, before anything is known about what is on the other side. It can be dropped — abandoned outright, per the gear-forfeit rules (Ruleset §12) — but not put away.
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
- **Passive:** a long thrusting lance with a heated collar behind the point, of the sort used to seal a wound shut rather than open one. **Every fully-landed Heavy applies 2 Burning to the target and clears 2 Bleeding from the wielder.** The heat runs both ways along the shaft.
- The Strength answer to a bleed problem — a build that runs hot, takes Bleeding freely, and burns it off by committing to Heavies rather than by spending item actions on Wrap.
- **Status Applied:** Burning (target), Bleeding removal (self).
- **Sever viability:** standard, per the general limb-model sever thresholds.

## Weapon 42 — The Grafted Limb

- **Type:** Quick · **Stat/Grade:** Skill/C · **Hands:** One — it **is** the hand
- **Acquisition:** found — deep instance loot, or offered. Attaching it is a decision, not a pickup.
- **Base:** 26. Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05.
- **Worked rows:** ESV 8 → 32/61 · ESV 47 → 59/102.
- **Passive:** a forearm and hand of dark worked metal that replaces the wielder's own from the elbow down. Once attached:
  - **It cannot be unequipped, swapped, or dropped except at the hub**, where removal follows the Mutation regret rules (Ruleset §10) — a real cost, not a menu option.
  - **It can never be disarmed** by any effect.
  - **All self-inflicted damage from the wielder's own weapon gimmicks is halved** — Powder Charge failure, the Debt-Iron's Bleeding, the Nursling's feeding, anything where the weapon costs you. It absorbs what it can.
  - **Severing that arm on the wielder destroys the weapon permanently.** It is a limb; limbs come off.
- **Insight Gate:** none, though below **Insight Tier 3** the wielder cannot read what it is actually doing to the arm (same threshold as full mutation stat-lines, Ruleset §10).
- **Sever viability:** standard, per the general limb-model sever thresholds.

## Weapon 43 — The Aggregate

- **Type:** Quick · **Stat/Grade:** Skill/C · **Hands:** One
- **Acquisition:** found — general Vault reward, no recipe tie.
- **Base:** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05.
- **Worked rows:** ESV 8 → 30/57 · ESV 47 → 57/98.
- **Passive:** a short blade of no consistent material, which is a polite way of saying it is made of pieces of other things. **After landing a killing blow, the Aggregate takes on one property of what it killed for the rest of the encounter:** the DM grants it one status application drawn from that creature's own kit — Burning, Corrosion, Influence, Bleeding or Discombobulation — applied on its Heavy attacks at 1 stack.
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
  - **It can never stagger a limb.** Its contribution to every stagger meter, on every hit, is **zero.** No stagger means no free Precision Strikes from crossing a threshold, and no limp limbs — ever.
- The most specialised weapon in the manual. It severs earlier than anything at its grade and it removes an entire subsystem from the wielder's toolkit to do it.
- **Sever viability:** Heavy clears the reduced Head line (96) at **ESV 33** — comparable to the Debt-Iron, at one grade lower and without the self-damage. Arm and Leg remain out of one-hit reach at any ESV even reduced, per the fixed-constant rule.

## Weapon 45 — The Last Recourse

- **Type:** Quick · **Stat/Grade:** Skill/C · **Hands:** One
- **Acquisition:** found — general Vault reward, no recipe tie.
- **Base:** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05.
- **Worked rows:** ESV 8 → 30/57 · ESV 20 → 38/69 · ESV 47 → 57/98.
- **Passive:** a short broad blade with a grip wrapped in something that was not originally leather. **It pays out on how badly the fight is going.** Every attack deals **+1 raw per full 5% of the wielder's Max HP currently missing**, to a maximum of +19 at 5% HP remaining.
  - At full health: nothing. At half: +10. At a quarter: +15.
  - It offers no defence, no healing and no warning, and it is at its best in the exact circumstances where one more hit taken ends the run.
- **Status Applied:** none.
- **Sever viability:** standard, per the general limb-model sever thresholds. At ESV 47 and 5% HP a Heavy reaches 117 raw — three short of the Head line, deliberately. It never quite gets you there on its own.

## Weapon 46 — The Bellows Maul

*The first weapon in the game governed by **Endurance**. Endurance has only ever set the movement budget (Ruleset §7); this is the first thing that makes it an offensive stat.*

- **Type:** Heavy · **Stat/Grade:** **Endurance/C** · **Hands:** Two
- **Acquisition:** found — Cold Forge / Bellfounder's Pit recipes, instance loot.
- **Base:** 28. Light = 28+ESV×0.7 · Heavy = 56+ESV×1.05. *(ESV drawn from Endurance, using the standard soft-cap table, Ruleset §4.)*
- **Worked rows:** ESV 8 → 34/65 · ESV 20 → 42/77 · ESV 47 → 61/106.
- **Passive:** a bellows-handle and its iron plate, torn off a forge wall and used as a two-hander. **Scaling and fuel come from the same stat**, which is the entire tension: a high-Endurance wielder has both the biggest movement budget and the hardest swings, and every Heavy taken is movement not spent.
  - **Additionally: a Heavy landed after spending at least 6m of movement in the same turn deals +20% raw.** The weapon wants a run-up and it makes you choose between the run-up and everything else the turn could have been.
- **Sever viability:** standard, per the general limb-model sever thresholds. Endurance is not a stat most builds push past 14 (the movement cap), so in practice this sits permanently mid-tier — a genuinely different power curve rather than a reskinned one.

## Weapon 47 — The Sight-Line

*The first weapon governed by **Insight** — a dial that is earned rather than bought, and that **falls every time it is spent** (Ruleset §11).*

- **Type:** Reach · **Stat/Grade:** **Insight/B** · **Hands:** Two
- **Acquisition:** found — behind an Insight-gated door only. It is never in an open room.
- **Base:** 24. Light = 24+ESV×0.9 · Heavy = 48+ESV×1.35. *(ESV drawn directly from the current Insight score, standard soft-cap table.)*
- **Worked rows:** ESV 8 → 32/59 · ESV 18 → 41/73 · ESV 20 → 42/75.
- **Passive:** a long, thin, forked shaft of something that is not quite metal, which is only fully visible to whoever is holding it. **Its damage tracks the wielder's Insight score in real time and updates the instant that score changes** — mid-encounter, mid-turn, immediately.
  - Earn a point of Insight from a first sighting and the weapon is stronger for the rest of the fight.
  - Spend Insight on a gate, a Memory Vendor trade, or the Tithe-Fork's own passive, and it weakens on the spot.
  - **At Insight 0 it is a Base 24 stick with no scaling at all**, and it will happily be that.
- **Insight Gate:** none to wield. The weapon *is* the gate.
- **Sever viability:** never clears the Head's 120-raw line at any realistic Insight score. This is not an output weapon — it is a weapon that makes the Insight bargain (§11) something you feel in your hands rather than only in your save DC.

## Weapon 48 — The Anathema

*The Resolve column has never gone past Grade C. This is its heavy.*

- **Type:** Heavy · **Stat/Grade:** Resolve/B · **Hands:** Two
- **Acquisition:** found — Reliquary / Choir Deep recipes, instance loot.
- **Base:** 28. Light = 28+ESV×0.9 · Heavy = 56+ESV×1.35.
- **Worked rows:** ESV 8 → 36/67 · ESV 20 → 46/83 · ESV 47 → 71/120.
- **Passive:** a heavy iron bar cast with a text down its length that has been chiselled out rather than worn away. **A fully-landed Heavy applies 2 Influence stacks to the target** (Enemy-side Influence Overload, Ruleset §5) — double the Hymnal Truncheon's rate, on a considerably bigger swing.
  - **Additionally, while equipped the wielder's own Influence save DC is −1** — the only weapon in the game that improves the wielder's saves. It is genuinely defensive as well as offensive, which is why it is priced at a grade the Resolve column has never had access to.
- A real endgame option for a Resolve build, and the first weapon a Persistent Companion could meaningfully be handed rather than merely carry.
- **Sever viability:** Heavy clears the Head's 120-raw line at **ESV 47** exactly — the same benchmark as the Foundry Wedge, reached through a stat that has never been able to sever before.

## Weapon 49 — The Vivisectionist's Rule

*The first **Grade A** weapon in the Skill column. Ruleset §4: A ×1.1.*

- **Type:** Quick · **Stat/Grade:** Skill/A · **Hands:** One
- **Acquisition:** found — deep instance loot only, hand-placed, never rolled.
- **Base:** 30. Light = 30+ESV×1.1 · Heavy = 60+ESV×1.65.
- **Worked rows:** ESV 8 → 39/74 · ESV 20 → 52/93 · ESV 47 → 82/138.
- **Passive:** a straight steel rule ground to an edge on all four sides, marked in a scale that does not correspond to any known measure. It is precise beyond reason and it does not tolerate imprecision in return.
  - **Every Precision Strike miss with this weapon ends the turn outright**, regardless of the band's normal miss punishment (Ruleset §10) — no torso consolation hit, no leftover movement, nothing. The greedy-target tax becomes all-or-nothing at every multiplier.
  - Ordinary torso swings are unaffected. The penalty applies only when a limb multiplier above ×1.0 is declared.
- The highest Skill output in the game, sold to a player confident enough in their timing to stake the whole turn on it every time they get greedy.
- **Sever viability:** Heavy clears the Head's 120-raw line at **ESV 36** — the earliest of any Skill weapon by a wide margin, and reachable at a Skill score most builds actually get to.

## Weapon 50 — The Sunk Hook

- **Type:** Reach (thrown) · **Stat/Grade:** Skill/C · **Hands:** Two
- **Acquisition:** found — flooded gallery / Bellfounder's Pit recipes, instance loot.
- **Base:** 26. Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05.
- **Worked rows:** ESV 8 → 32/61 · ESV 20 → 40/73 · ESV 47 → 59/102.
- **Passive:** a heavy grapple on a short length of chain, meant for dragging things out of water. It works in melee like any Reach weapon. It can also be **thrown**:
  - **Throw (Full Action, 2m):** range 10m, no timing check, guaranteed hit, deals full **Heavy** damage.
  - **The hook stays where it lands.** The wielder is unarmed — Fists (Ruleset §4) — until they physically go and retrieve it, which costs a **Fast Action while standing adjacent to it.**
  - The chain is not long enough to pull it back. That was the first thing everyone tried.
- A burst of Heavy damage at range, priced in the most inconvenient currency available: your own position, chosen by where the enemy happened to be standing.
- **Sever viability:** standard, per the general limb-model sever thresholds, thrown or held. The throw is a full Heavy and severs normally — which is the entire reason to accept the drawback.

## Weapon 51 — The Cascade

- **Type:** Quick · **Stat/Grade:** Skill/D · **Hands:** One
- **Acquisition:** found — general Vault reward.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75.
- **Worked rows:** ESV 8 → 26/50 · ESV 20 → 32/59 · ESV 47 → 46/80.
- **Passive:** a light fluted blade that runs hot along its spine the longer it is kept working. **Momentum:** each consecutive turn in which the wielder lands at least one attack adds **+8 raw to all attacks**, cumulative and uncapped.
  - **The whole stack is lost the moment the wielder takes damage from any source** — including chip, status ticks, Burning, Corrosion and Rupture. Not reduced. Lost.
  - A turn spent moving, using an item, parrying without following up, or missing also breaks it, at zero.
- Low base numbers with a very high ceiling that only exists for a player who is winning cleanly and does not stop. Five untouched turns is +40 raw; one Burning tick is zero.
- **Sever viability:** standard normally. At six turns of momentum a Heavy at ESV 47 reaches 128 raw and clears the Head line — which requires six consecutive clean turns, which is the point.

## Weapon 52 — The Grudge

- **Type:** Heavy · **Stat/Grade:** Strength/C · **Hands:** Two
- **Acquisition:** found — general Vault reward.
- **Base:** 26. Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05.
- **Worked rows:** ESV 8 → 32/61 · ESV 20 → 40/73 · ESV 47 → 59/102.
- **Passive:** a notched iron bar that has clearly been swung at a great many things and connected with rather fewer. **The exact inverse of the Cascade:** every **missed** attack this encounter adds **+10 raw** to the weapon's damage, cumulative and uncapped. The entire stack clears the moment an attack lands.
  - Precision Strike misses count. Whiffed Powder Charges count. Any declared attack that fails to connect counts.
  - It is the only weapon in the game that gets better while you are playing badly, and it stops the instant you stop.
- Pairs unusually well with a high-multiplier greedy build that misses often by design, and does nothing at all for a careful one.
- **Sever viability:** standard normally. Four consecutive misses at ESV 47 put the next Heavy at 99 raw; seven put it past the Head line. Getting there requires seven misses in a row, and surviving seven misses in a row is its own problem.

## Weapon 53 — The Blunt Reckoner

- **Type:** Heavy · **Stat/Grade:** Strength/C · **Hands:** Two
- **Acquisition:** found — Cold Forge / Paper Mill recipes, instance loot.
- **Base:** 28. Light = 28+ESV×0.7 · Heavy = 56+ESV×1.05.
- **Worked rows:** ESV 8 → 34/65 · ESV 20 → 42/77 · ESV 47 → 61/106.
- **Passive:** a squared-off iron beam with no edge, no point and no finesse whatsoever. **Precision Strikes with this weapon skip the Precision Strike stopwatch entirely** (Ruleset §10) — declare any limb, at any multiplier, and it simply lands. No timing check, no tolerance band, no miss punishment, ever.
  - **The cost: all damage is reduced by 40%**, applied to raw before limb multipliers and before any other modifier.
  - **Worked:** at ESV 47, Heavy 106 → **64 raw**; against a head at ×1.5 that is 96 effective damage with zero risk, versus 159 with the watch and a ±0.13s window to hit.
- The accessibility option, and a genuinely different way to engage the limb system: it converts the entire greedy-target subsystem from a timing test into a flat, permanent damage tax. Nothing else in the manual lets a player use limbs without ever touching a stopwatch.
- **Sever viability:** poor — reduced raw never clears the Head's 120-raw line at any ESV. This weapon staggers reliably and severs never, which is the honest shape of the trade.

## Weapon 54 — The Alembic Blade

- **Type:** Quick · **Stat/Grade:** Skill/D · **Hands:** One
- **Acquisition:** found — Gaslight Ward / Reliquary recipes, instance loot.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75.
- **Worked rows:** ESV 8 → 26/50 · ESV 20 → 32/59 · ESV 47 → 46/80.
- **Passive:** a narrow blade with a sealed glass reservoir set into the flat, half-full of something that moves more slowly than liquid should. **Transmute (Fast Action, 0m):** convert **2 stacks of Bleeding from the wielder into 1 stack of Corrosion on a target within reach.** Usable once per turn.
  - The first weapon in the game that moves a status track from one creature to another rather than applying a new one.
  - It is a bleed-management tool that happens to be offensive, and it is at its best in exactly the builds that generate self-inflicted Bleeding on purpose — the Powder Charge, the Debt-Iron, the Hemorrhage.
- **Sever viability:** standard, per the general limb-model sever thresholds.

## Weapon 55 — The Toll-Blade

- **Type:** Quick · **Stat/Grade:** Skill/B · **Hands:** One
- **Acquisition:** found — hub sub-basement, tied to the toll/token economy alongside the Toll-Press. Character-agnostic.
- **Base:** 26. Light = 26+ESV×0.9 · Heavy = 52+ESV×1.35.
- **Worked rows:** ESV 8 → 34/63 · ESV 20 → 44/79 · ESV 47 → 69/116.
- **Passive:** a slot-mouthed blade with a coin channel running the length of the fuller. **Every Heavy attack costs 2 White Salts from the Purse, paid at the moment of the swing.**
  - **An empty Purse means no Heavy** — the blade will not complete the motion. Light attacks are always free.
  - Salts spent this way are gone whether the attack lands, misses, or is interrupted.
  - **It costs nothing at the hub** and everything in a long run, which means it is at its weakest precisely when the Purse is thin and the run has gone badly.
- The first weapon in the game that draws on the Salts economy (Ruleset §4/§18) as an ammunition type. A Skill/B one-hander is genuinely strong; you are simply paying for it in the same currency as your levels.
- **Sever viability:** standard, per the general limb-model sever thresholds. Never clears the Head line, so the Salts buy consistency rather than a sever route.

## Weapon 56 — The Winnowing Fan

- **Type:** Reach · **Stat/Grade:** Strength/C · **Hands:** Two
- **Acquisition:** found — general Vault reward, no recipe tie.
- **Base:** 26. Light = 26+ESV×0.7 · Heavy = 52+ESV×1.05.
- **Worked rows:** ESV 8 → 32/61 · ESV 20 → 40/73 · ESV 47 → 59/102.
- **Passive:** a broad winnowing blade on a long haft, made for separating chaff from grain by moving a very great deal of very small things at once. **All damage is doubled against any target whose limb table consists of a sever-immune Mass, Accretion or Body entry** — that is, against the Swarm archetype and anything else with no anatomy to speak of (Ruleset §16).
  - Against everything else it is a plain, slightly under-powered Strength/C Reach weapon with no gimmick at all.
- The manual's first deliberately **archetype-specific counter weapon.** Swarms exist specifically to be immune to precision play and to be killed only by raw HP damage; this is the tool that makes that a fair fight rather than a long one. It is dead weight in most rooms, which is the price of it being decisive in some.
- **Sever viability:** standard against anything that can be severed — which, notably, is never the thing it is good against.

## Weapon 57 — The Riposte Bar

- **Type:** Quick · **Stat/Grade:** Skill/C · **Hands:** One
- **Acquisition:** found — Hall of Broken Mirrors / Cold Forge recipes, instance loot.
- **Base:** 24. Light = 24+ESV×0.7 · Heavy = 48+ESV×1.05.
- **Worked rows:** ESV 8 → 30/57 · ESV 20 → 38/69 · ESV 47 → 57/98.
- **Passive:** a short weighted bar with a swept guard, balanced for stopping a blow rather than landing one. **On a successful parry, a second stopwatch fires immediately — target 0.70s, ±0.15s, widened by the Insight window bonus as normal.**
  - **Hit:** a free Light attack against the parried enemy, resolving instantly and outside the action economy. Contributes to stagger meters normally. This is *in addition to* everything the parry already bought (Ruleset §9) — the skipped turn and the eased follow-up remain.
  - **Miss:** the parry still succeeds and still buys everything it normally buys, but **the eased Tier follow-up attempt is forfeited** for that opening.
- The first weapon to put a second timing check inside a parry. It asks whether the player is confident enough to gamble the opening they just earned on a very tight window, immediately, with no time to reset.
- **Sever viability:** standard, per the general limb-model sever thresholds. The free Light is a full Light and severs normally if it somehow reaches a threshold.

## Weapon 58 — The Second Hand

*The first weapon in the manual **written for the companion side of the party** rather than the player (Ruleset §18, Companions).*

- **Type:** Quick · **Stat/Grade:** Resolve/D · **Hands:** One
- **Acquisition:** found — instance loot, any recipe. Always found as a matched pair with nothing to match it to.
- **Base:** 22. Light = 22+ESV×0.5 · Heavy = 44+ESV×0.75.
- **Worked rows:** ESV 8 → 26/50 · ESV 20 → 32/59 · ESV 47 → 46/80.
- **Passive:** a plain, light, well-balanced blade with a second grip set behind the first, as though it expects to be held by someone standing just over your shoulder. **It may be handed to a Persistent Companion** (Ruleset §18), which no other weapon in the game may be.
  - **While a companion wields it:** they gain a melee attack option using their own governing stat and their own ESV, resolved on their own turn within their existing one-Action economy. It grants no Precision Strikes, no visceral capability, and no second action — it simply means a support companion is no longer defenceless when something reaches them.
  - **While the player wields it:** it is an unremarkable Resolve/D one-hander with no bonus whatsoever.
- Companion stat blocks are generated as canon on first accompanied run (Ruleset §18); handing this over is a permanent addition to that block until it is taken back at the hub.
- **Sever viability:** none in companion hands — companions never sever, per the standing companion constraint. Standard in player hands, for whatever that is worth.

## Weapon 59 — The Sundering Wedge

- **Type:** Heavy · **Stat/Grade:** Strength/B · **Hands:** Two
- **Acquisition:** found — Cold Forge recipe, instance loot. Sits alongside the Foundry Wedge as its ugly cousin.
- **Base:** 28. Light = 28+ESV×0.9 · Heavy = 56+ESV×1.35.
- **Worked rows:** ESV 8 → 36/67 · ESV 20 → 46/83 · ESV 47 → 71/120.
- **Passive:** a splitting wedge with a shaft driven through it at an angle no one would choose. **Any limb that crosses its stagger threshold while this weapon is equipped may instead be severed outright**, at the wielder's choice, declared as the threshold is crossed.
  - **The cost:** the wielder immediately takes **self-damage equal to that limb's stagger threshold ÷ 20**, unmitigable, ignoring all reduction.
  - **Worked:** Head (180) → **9 self.** Arm (200) → **10 self.** Leg (300) → **15 self.** Torso (800) → **40 self** — and a torso sever kills outright, which is why the price is what it is.
- This converts the stagger subsystem into a sever engine and makes the fixed-constant one-hit thresholds (Ruleset §10) largely irrelevant to a patient Strength build — arms and legs, which are explicitly stated to stay out of one-hit reach at any score, become reachable over several hits for a price in HP. That is a significant structural change and it is deliberately expensive.
- **Sever viability:** Heavy clears the Head's 120-raw line at **ESV 47** conventionally. The passive is the real sever route and it works at any ESV.

## Weapon 60 — The Deadfall

- **Type:** Heavy · **Stat/Grade:** Strength/A · **Hands:** Two
- **Acquisition:** found — deep instance loot, hand-placed, never rolled.
- **Base:** 32. Light = 32+ESV×1.1 · Heavy = 64+ESV×1.65.
- **Worked rows:** ESV 8 → 41/78 · ESV 20 → 54/97 · ESV 47 → 84/142.
- **Passive:** a counterweighted iron head on a ratcheted arm, which does not swing so much as it is released. **After any Heavy attack, the Deadfall is spent** — it cannot attack again, in any form, until it is reset with a **full Action (3m)**.
  - Light attacks do not spend it and do not reset it.
  - The practical cadence is therefore Heavy, reset, Heavy, reset — **one real attack every two turns**, with those turns fully exposed and nothing else happening in them.
- The single hardest-hitting cadence-limited weapon in the game. Against a boss that gives one opening every two rounds anyway, it costs almost nothing; against anything fast, it is close to unusable.
- **Sever viability:** Heavy clears the Head's 120-raw line at **ESV 34.** Combined with a parry opening and a limb multiplier, this is among the most reliable one-hit sever routes available — once every two turns, forever.

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

- **Role:** hub-accessible Insight trader. Trades Insight for voluntary mutations, mutation removal, and Scar removal. **Location:** hub — a fixed alcove, not signposted, not advertised. Visible only to those at Insight 10+. **No threshold gate — if Insight drops below 10, she vanishes immediately**, mid-conversation if necessary. Reappears when Insight climbs back. **Fightable:** N.
- **Fixed appearance:** ghostly, ephemeral — translucent, edges indistinct, more suggestion than person. Never fully solid. Voice arrives slightly before or after her mouth moves. Details shift if you look away and back — hair length, hand count, whether she's standing or seated. The one constant: she's always facing you.
- **On arrival:** doesn't introduce herself. Knows the player's Insight score without being told. Opens with what she can offer, not who she is. **Never** accepts Salts, items, or favours as payment. **Never** allows a clean Insight dump — every trade has a physical cost attached.
- **Never does:** raise her voice, touch anything physical, appear to anyone below Insight 10, leave the alcove. **Never says directly:** her own name (the player names her, or doesn't), what she does with the Insight she collects, or why she's in the Hydro.
- **Dialogue seeds:** measured, transactional, unbothered by refusal. "You've seen enough to find me. That's the price of admission." / "I don't sell power. I rearrange what's already yours." / "Come back when you have something to trade — or something you want taken away." / Treats a refusal as fact, not a slight.
- **Mechanical function:**
  - **Voluntary mutation (buy):** 5 Insight → player chooses a limb, DM generates a mutation (upside + downside, same Mutation shape as ruleset §10). The limb doesn't need to be lost first — the Vendor changes it in place. Mutation is permanent until removed. Full stat-line legible immediately (Insight threshold already met by access requirement). Always available — no prerequisite.
  - **Mutation removal:** 5 Insight → removes one existing mutation, limb reverts to human. **Requires** having at least one existing mutation or Scar — the Vendor won't accept Insight with nothing on the table.
  - **Scar removal:** only route. Scar 1 = 6 Insight, Scar 2 = 10, Scar 3+ = escalating. **Requires** having the Scar (same constraint — no phantom trades).
  - **Hard constraint:** the player must either purchase a mutation OR have an existing mutation/Scar to remove. No clean Insight dumps. The cheapest "clean" Insight reduction (buy mutation + immediately remove it) costs 10 Insight for zero lasting change. Accepting the mutation costs 5 and you keep the upside+downside. This is by design — rewards commitment over cycling.
  - **No debt system.** Hub-accessible means all trades are immediate, no cross-run payment plans.
  - **Single-conversation resolution.** All trades within one visit resolve before the Insight threshold check kicks in. The player can make multiple trades in a sitting even if intermediate Insight drops would take them below 10. Once the conversation ends and the player walks away, the threshold applies — if Insight is below 10, she's gone until it climbs back.
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
  - **Judgment Spark** — single-target, RES/E, Light Action (1m), ranged: 27 dmg. Deliberately her weakest number; can never be used for Precision Strikes or limb targeting.
  - **Imbue Weapon** — Full Action (2m), range 5m (session 9 ruling): +12 flat damage to Lloyd's next attack, light or heavy, whichever he swings first. One charge at a time, doesn't stack with itself, does stack with the Charm (different source — hers scales off RES, the Charm is a flat item bonus).
  - **Steadying Grace** — Full Action (2m), range 5m (session 9 ruling): usable only the turn immediately after Lloyd takes a hit and doesn't land a qualifying attack that turn (his Rally window closing). Recovers 50% of whatever grey Rally HP is currently pending into real HP; the other half is lost, same as a whiffed self-Rally. Bound entirely to the existing Rally system — no new resource.
  - **Steady Faith** *(passive)* — within 5m of Lloyd, he gets −1 to his own Insanity/Influence save DC.
  - **Boot Knife** — Skill/E, Base 12, backup melee only, not sever-viable. Can Hold/parry like Lloyd if something closes on her, but it's not her preference — she backs off and casts before she trades hits.
- **Status:** Active.
- **Lore (DM-only — Lloyd does not know this):** member of the Church of St Narrikon's Redemption of Mankind. The Church is genuinely sinister — Lloyd's heard rumours, and they're true — but **Maria doesn't know this.** She is naive, devout, and believes the Church is righteous. She left of her own accord after becoming romantically involved with someone, believing herself impure and unworthy of her vows. She has not been expelled — she fled in shame. She believes the Church will never forgive her and that she can never return. She is at the Hydro to redeem herself to St Narrikon by helping others — genuine penance, not a cover story. Her motivation is sincere: she wants to do good because she believes she failed at being good. She does not want the Deep Salts. What she wants is absolution she doesn't believe she'll receive. **Key dramatic tension:** everything Lloyd has heard about the Church is probably true, but Maria is not complicit — she's a true believer who doesn't see what she was part of. This should surface slowly, not in a single revelation. The linen strip on her wrist is connected to the person she was involved with — not yet revealed. **The "sinister background" is the Church's, not hers.**

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
- **Effect:** clears 2 Bleeding stacks.
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
- **Effect:** fully clears Bleeding to 0, regardless of current stack count.
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
- **Acquisition:** found — general instance loot. Bought at 10 Salts. **Design note:** the first dedicated Influence-clear Quick Item — closes the last gap in track-clear parity (Bleeding/Wrap, Insanity/Camphor, Corrosion/Scour, now Influence/this).
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
- **Effect:** clears 1 stack from any single status track of the wielder's choice (Bleeding, Insanity, Influence, Corrosion, or Burning).
- **Duration:** instant. **Consumable:** Y, Uses: 1, **not Hub Kit** — doesn't refill on hub return, must be found or bought fresh each time.
- **Carry Limit:** 3.
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot, uncommon. Bought at 20 Salts. **Design note:** the flexible wildcard — priced and gated (no Hub Kit refill) to sit above the single-track clears without replacing them outright.

## Item 19 — Thread-Count Bandage

- **Type:** Quick · **Action Cost:** Fast Action
- **Effect:** clears 1 Bleeding stack **and** ends the wielder's current Off-Balance status, if active, in the same use.
- **Duration:** instant. **Consumable:** Y. **Carry Limit:** 2 (a combo item, deliberately rarer than plain Wrap).
- **Insight Gate:** none. **Limb Requirement:** a working hand.
- **Acquisition:** found — general instance loot, uncommon. Bought at 15 Salts.

## Item 20 — Bone-Set Splint

- **Type:** Action Item · **Action Cost:** full Action, costs the entire remaining movement budget for the turn (same tax as Cautery Iron)
- **Effect:** fully clears Bleeding to 0, regardless of current stack count.
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
- **Effect:** pulls the user 5m toward a fixed surface (wall, pillar, railing) — never toward an enemy or a hazard. Pure repositioning, no damage, no Precision Strike.
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
- **Effect:** once per hub cycle, the first Bleeding stack taken during a run is negated entirely (as if it never happened) — same cadence convention as the Vigor 40 perk *Second Wind*.
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
- **Effect:** self-initiated Precision Strikes (Ruleset §10) have their tightened tolerance eased back half a band instead of the full band.
- **Consumable:** N.
- **Insight Gate:** none. **Limb Requirement:** a working hand, worn on it.
- **Acquisition:** found — general instance loot, uncommon.

## Item 35 — Salt-Stained Ribbon

- **Type:** Passive/Equip · **Action Cost:** none, worn
- **Effect:** once per hub cycle, the next Bleeding application against the wielder is reduced by 25%, rounded down. Stacks additively with the Vigor 20 perk *Thick Blood* if both are active — **combined reduction from any source caps at 50% total**, stated explicitly to prevent runaway stacking.
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

*Bleeding is fully defined in Ruleset §5 — not restated here. This section holds only effects the ruleset doesn't cover.*

## Status Effect Template (blank)

**Type (Tick/Track/Condition):** · **Affects:** · **Resisted on application:**
**If Tick:** applied value · effect per stack · drains 1/turn · cap · clear condition
**If Track:** stacks per application · effect per stack/turn · cap · overflow effect · clear condition
**If Condition:** trigger · effect while held · clear condition
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
