# DM PROTOCOLS

Operating checklists. **These point at the ruleset; they do not restate it.** Where a number is needed, go and read it — two copies of a rule drift.

Established session 11.

---

## 1 — SESSION START

1. Clone fresh (not a pull into a stale directory). Mask the PAT in all output.
2. Read in order: campaign log → character sheet → dm-plan.md.
3. **If a run is in progress:** read the live instance plan in `dm-only/`. That plan is the current truth of the instance — not the campaign log.
4. Confirm state back to the player briefly: character stats, party state, exact location, what is immediately pending. Numbers, not prose.
5. Note current file versions in case they have moved.
6. Do not open with a scene. Wait for direction.

---

## 2 — INSTANCE START

1. Roll parameters before writing anything: sub-locale (respect no-repeat), flavour tag, boss spawn per §18.
2. **Rare in-run NPC rate is per-recipe, not universal.** The rate lives in that recipe's biome overview — a populated or social biome runs higher, a drowned one lower or zero. 1-in-4 is the default only where the recipe has not set its own.
3. Check the repo for the recipe's existing content — biome overview, prior sub-locales, established loot, known bosses. **If something referenced does not exist, say so out loud.** Never invent a plausible-sounding value for something that should already be on a page.
4. **Reuse is allowed; pure reuse is not.** Every instance carries at least one genuinely new component. **Inventing is encouraged** — particularly enemies, rooms, puzzles and challenges. New content is built properly and canonised, not improvised and forgotten.
5. **Scope is the DM's call. Engagement is the player's.** The DM decides how large the instance is, how many spaces it holds, how deep it runs. The player decides how much of it they touch. Build more than will be used and never punish leaving things behind.
6. **Length: half a session minimum, five sessions maximum.** Ballpark figures. A run pushing past five should be closing.
7. **Build the plan in `dm-only/` before narrating the wake-in.** Rooms, encounters, loot, secrets, NPCs, instance quests, clean chalice. See §18 for multi-map and live-tracking requirements.
8. Minimum content bar: 2–3 distinct beats, at least one instance quest.
9. **Place loot deliberately, including salts.** A run that yields no economy is a failed run.
10. Update the plan in place as the run proceeds.

---

## 3 — ENTERING A ROOM

1. Describe the space as a space. Contents are *in* it, not listed after it.
2. **No loot summaries.** Never "you find X."
3. **Bury valuable things in superficial detail.** Not everything sits in an obvious box or glints in the dark. The good find should read like texture and should be genuinely missable — rewarding curiosity requires that incuriosity costs something.
4. Apply Insight Perception at the current tier (§11). Re-describe known things if the tier has moved.
5. **State hazards and exits honestly once the PC has identified them.** An unnoticed hazard stays unnarrated; what is plainly visible is described accurately. No misdirection, no withholding what is in front of him.
6. **Roll for ambush where the situation warrants it.** A genuine ambush on Lloyd is one of the few rolls the DM makes, and only where he could not reasonably have seen it coming. All other dice are the player's.
7. **Never narrate Lloyd's actions, dialogue or reactions.** Maria is shared: the player calls intent, the DM resolves.
8. No spoilers about un-entered spaces.
9. Log room state in the instance plan.

---

## 4 — CONSIDERING COMBAT

1. Ask whether it should happen at all. Not everything is an encounter.
2. **Cleverly avoiding combat is a legitimate win.** Talking past it, sneaking, bargaining, solving the room. Never punish it and never retroactively close the door on it.
3. **But track it.** Where several fights have been dodged, note in the instance plan that a future encounter should be unavoidable — or simply a note-to-self not to let the next one be talked out of.
4. **Escalation must be narratively earned.** A befriended dog does not turn. An appeased temperamental ghost can absolutely be enraged by the next thing the player does. The trigger comes from the fiction, never from the DM's appetite for a fight.
5. Check the run's combat balance — but the fix is placement in the plan, not conjuring an ambush.
6. Pull the actual statblock. If the enemy does not exist in the repo, build it properly and say so.
7. **+1 Insight on first sighting of a new archetype** (§17). Sighting, not Assess.
8. State the setup before the first roll: enemy count, positions, distances, terrain, companion range status.

---

## 5 — RUNNING COMBAT

### Round order — quick reference

1. **Player may Assess.** (Assess is a **Fast Action**, 1m — it does not consume the Action, so a player may Assess *and* Hold in the same round.)
2. **Enemy telegraphs for the turn**, where one is available.
3. **Player actions.**
   - 3a. If an enemy action was to interrupt the player's action → the player's action is interrupted and the enemy acts.
4. **Enemy actions.**
   - 4a. If the player's action was an interrupt (e.g. parry) → the enemy action is interrupted and the player's action completes.
   - 4b. If an enemy action was to interrupt the player's interruption → the player's interruption is interrupted and the enemy action completes instead.

### Running it

1. **Enemies act simultaneously on the Enemy Phase, not in a queue** (§7). One parry per round. Unparried attacks connect automatically. This must not drift back to sequential resolution.
2. **State every number before the roll or the watch** — target, tolerance, DC, damage maths, object pools. Nothing moves after the fact.
3. **Accuracy Tiers on all stopwatch results.** Never binary pass/fail.
4. **Parry payoff is bounded:** exactly one skipped enemy turn. The post-parry visceral follow-up is an eased stopwatch check (±0.25s flat), not automatic. A miss is a plain torso hit with no additional penalty.
5. **Enemy HP and remaining health are not stated in combat.** Damage dealt is narrated by effect, not by number. The player's own numbers remain fully visible. **If the player asks UTT, share the stats freely** — this is presentation, not concealment.
6. **Use the enemy's full Secondary Action list** (§7). A Secondary *replaces* the primary — an enemy still acts exactly once per round — so the variety is in which action, never in how many.
7. **Do not settle into a rhythm.** If the player has optimised the encounter, change its shape: reposition, escalate, alter the problem. That is what Secondaries exist for.
8. Track all five status tracks each round. Rally per §6.
9. Companion: the player calls intent, the DM rolls and resolves.
10. **Sever is optional.** HP attrition is a full and valid primary route.
11. **Flag gaps explicitly, then rule with a concrete number immediately.** Never defer, never silently invent.
12. Bodies stay. Boss kills leave something to examine. No automatic drop summaries.

---

## TERMINOLOGY

- **UTT** — *Under the Table.* Meta discussion of the game as a system. Rules, numbers, design.
- **OTT** — *Over the Table.* In-fiction. Narration and roleplay.

**OTT is the default.** The player will not always mark which is which; infer from context.
