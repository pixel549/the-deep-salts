# Monster Manual — Limb/Implement Sanity Pass

## Context

The Deep Salts is a Soulsborne-inspired TTRPG. The monster manual lives in the design bible (`deep-salts-design-bible-v4.6.md` or whatever the current version is). Each monster entry has a `**Limbs:**` line describing its targetable body parts.

The game has a problem: every fight devolves into "parry → visceral → headshot → sever → instant kill" because the head is always the optimal target (highest multiplier ×1.5, lowest effective sever threshold, instant kill on sever). This pass fixes that by giving monsters interesting limb tables that create tactical variety.

## Key Rules

### Limbs vs Implements

**Limbs** are parts of the enemy's body. Damage to a limb chips the enemy's main HP pool (raw × limb multiplier). Limbs have stagger thresholds (cumulative damage → temporary daze) and sever thresholds (single-hit damage → permanent removal).

**Implements** are objects the enemy carries or has strapped to them. Implements have their own **isolated HP pool** — damage to an implement does NOT chip the enemy's main HP. Implements also have stagger/sever thresholds with specific effects (stagger = partial disable, sever = destroyed).

**The test:** if ripping it off would leave a wound, it's a limb. If it'd leave the enemy holding nothing, it's an implement. A horn grown into a throat = limb. A bell on a chain = implement. A megaphone fused to a jaw = implement (it's fused TO the jaw, not part of the jaw itself).

### Standard Humanoid Defaults

The baseline table (from the ruleset §10):

| Limb | Multiplier | Stagger Threshold |
|---|---|---|
| Head | ×1.5 | 180 |
| Torso | ×1.0 | 800 |
| Arm | ×0.65 | 200 |
| Leg | ×0.75 | 300 |

Sever = reaching the stagger threshold in a single hit (raw × multiplier ≥ threshold).

### The Problem with Standard Defaults

At the player's current power level (~70 raw per Imbued visceral), the head is always the easiest sever: 70 × 1.5 = 105 per hit, threshold 180, and with accuracy bonuses (×1.3 to ×3.0) a single hit can sever.

Arms at ×0.65 need 308 raw to sever (200 ÷ 0.65). Legs at ×0.75 need 400 raw. These are effectively unseverable. So the player always targets the head.

### The Fix: Three Tools

**1. Reinforced heads.** Elites and repeat-encounter enemies should have head stagger thresholds above 180 (e.g. 240, 250, 350). This makes the head harder to sever than standard.

**2. Custom multipliers on weak points.** Give the intended weak-point limb a HIGHER multiplier than the standard table (×1.0 or ×1.2 instead of ×0.65 for arms). This makes the weak point genuinely easier to sever than the reinforced head. The weak point should have a lower stagger threshold too.

**3. Head guarding.** Some enemies protect their head by posture or armor. The head isn't targetable until another limb is staggered first. This forces multi-step combat.

### Sever Effects

Every custom limb should have a specific sever consequence that matters tactically:
- Arm sever → disables the attack that arm performs
- Leg sever → grounds the enemy (reduced to crawl speed)
- Weak point sever → disables a specific ability or ends the fight
- Implement sever → destroys the object, removes its function

## What to Do

Go through every monster entry in the design bible. For each one:

1. **If it already has a custom limb table** — check that multipliers are present on every entry, that the intended weak point is genuinely easier to target than the head, and that sever effects are specified. Fix if not.

2. **If it says "standard defaults, no deviations"** — decide:
   - **Is this a soft/low-HP mook where the headshot loop isn't a problem?** (e.g. The Annotator, The Quiet, The Prompter — they die fast regardless.) Leave as standard defaults. Add a note like "soft target, dies before the loop matters."
   - **Is this an elite, repeat-encounter, or named enemy?** Give it a custom limb table. Read its flavour text and attack descriptions to figure out what makes sense — a creature wrapped in something should have a reinforced head, a creature with a visible weak joint should have a targetable limb, etc.
   - **Is it non-humanoid with its own table format?** Leave it alone unless the table is incomplete.

3. **For implement entries** — make sure the wording says "isolated HP pool" and "damage does NOT chip the enemy's main HP." Remove any "Deals full HP damage on hit like any other strike" language — that's the old (incorrect) ruling.

4. **For entries with embedded body parts described as implements** — if the object is part of the body (grown into the throat, fused to bone, etc.), change it to a limb. If it's carried, strapped on, or held, keep it as an implement.

## Format

Custom limb entries should follow this format:

```
- **Limbs:** custom. **Head: stagger [threshold], ×1.5** ([description — reinforced/guarded/standard]). **[Weak point]: stagger [threshold], ×[multiplier]** ([description]). [Weak point] sever → [specific tactical effect]. **Arms:** [details]. **Legs:** [details].
```

Or for guarded heads:

```
- **Limbs:** custom. **Head: guarded** — [description of why it's guarded]. Not targetable until [condition]. Once exposed: [threshold and multiplier]. **[Other limbs with details].**
```

## Monsters Already Fixed (do not change these)

- Monster 1 (Waterlogged Guest) — head guarded, weak arms ×1.0
- Monster 2 (Chapel Penitent) — weak legs (150), standard head
- Monster 3 (Drowned Bellkeeper) — bell is implement, isolated pool
- Monster 4 (Salt-Eaten Custodian) — reinforced head (250), scraper arm ×1.2
- Monster 5 (Brine Spitter) — jaw implement, standard head
- Monster 6 (Bathhouse Flailer) — reinforced head (240), weak arms ×1.0
- Monster 7 (Marble Attendant) — very reinforced head (350), arms/legs ×1.0
- Monster 8 (Singer) — Open Throat weak point, already good
- Monster 9 (Cinderbound Attendant) — head guarded by apron, weak arms ×1.0
- Monster 33 (Fuse-Throated Crier) — Fuse-Horn is a LIMB (embedded)
- Monster 16 (Brass-Throated Barker) — Megaphone is implement, isolated pool
- Monster 34 (Squall Box) — Speaker Cabinet is implement, isolated pool

## Design Principles

- The player should have a reason to think about which limb to target, not autopilot to the head every time.
- Not every monster needs to be complex — basic mooks can stay simple. The variety comes from elites and enemies the player fights repeatedly.
- Weak points should make narrative sense. Read the flavour text. A creature described as having a corroded joint, a cracked shell, exposed wiring, or a fragile appendage — those are your weak points.
- Don't make heads unseverable — just make them harder than the alternative. The player should still be able to headshot if they commit resources (Powder Charges, perfect accuracy), but the weak point should be the efficient play.
- Sever effects should change how the fight plays, not just do damage. Disabling attacks, grounding enemies, removing armor — these are tactical rewards.

## After Editing

Commit with a descriptive message. Don't version-bump the file — Jake will do that manually if warranted.
