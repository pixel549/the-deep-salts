"""
The Deep Salts — live combat state tracker.

A JSON file is the single source of truth for what's happening *inside* a
fight — HP, status stacks, limb damage, round number. Between fights,
deep-salts-character-sheet.md stays the source of truth as it always has;
this only exists because that document is rewritten by hand after a fight,
not live during one, and "approximately 260/500" is exactly the failure
mode this whole toolset exists to kill.

Wraps resolver.py for anything that's actually arithmetic (limb hits,
status ticks) rather than reimplementing it here.
"""

import copy
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "resolver"))
import resolver  # noqa: E402

# Status caps per ruleset §5. Anything not listed here is uncapped (Bleeding,
# Burning, Frenzy, Influence).
STATUS_CAPS = {
    "discombobulation": 3,
    "stone_skin": 3,
    "insanity": 10,
    "corrosion": 10,
    "crust": 4,
    "fervour": 10,
}

DEFAULT_STATUS = {
    "bleeding": 0,
    "burning": 0,
    "discombobulation": 0,
    "stone_skin": 0,
    "frenzy": 0,
    "insanity": 0,
    "influence": 0,
    "corrosion": 0,
    "crust": 0,
    "fervour": 0,
    "fugue": False,
}


def load(path):
    with open(path) as f:
        return json.load(f)


def save(state, path):
    with open(path, "w") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
        f.write("\n")


def new_encounter(name="", round_number=1):
    return {"encounter": name, "round": round_number, "combatants": {}}


def new_combatant(combatant_id, name, max_hp, hp=None, limbs=None, side="enemy"):
    """side is 'player', 'companion', or 'enemy' — narrative bookkeeping only,
    nothing here treats them differently mechanically."""
    return {
        "id": combatant_id,
        "name": name,
        "side": side,
        "max_hp": max_hp,
        "hp": max_hp if hp is None else hp,
        "alive": True,
        "status": copy.deepcopy(DEFAULT_STATUS),
        "limbs": limbs or {},
    }


def add_combatant(state, combatant):
    state["combatants"][combatant["id"]] = combatant
    return state


def _get(state, combatant_id):
    if combatant_id not in state["combatants"]:
        raise KeyError(f"no combatant {combatant_id!r} in this encounter")
    return state["combatants"][combatant_id]


def apply_status_stack(state, combatant_id, status_name, delta):
    """Add (or remove, with a negative delta) stacks of a status. Clamps at
    0 and at the ruleset cap, where one exists."""
    combatant = _get(state, combatant_id)
    if status_name not in combatant["status"]:
        raise KeyError(f"unknown status: {status_name!r}")
    current = combatant["status"][status_name]
    new_value = current + delta
    new_value = max(new_value, 0)
    cap = STATUS_CAPS.get(status_name)
    if cap is not None:
        new_value = min(new_value, cap)
    combatant["status"][status_name] = new_value
    return new_value


def apply_flat_damage(state, target_id, damage):
    """Damage with no limb targeting — a default torso-equivalent hit."""
    target = _get(state, target_id)
    target["hp"] = max(target["hp"] - damage, 0)
    if target["hp"] <= 0:
        target["alive"] = False
    return {"damage": damage, "hp": target["hp"], "alive": target["alive"]}


def apply_limb_attack(state, target_id, limb_name, raw_damage):
    """Attack a specific limb. Requires the limb to already exist on the
    target with its own multiplier/threshold (set via add_combatant's
    limbs dict or a direct write) — this function never guesses a
    monster's thresholds, per resolver.py's own rule about that."""
    target = _get(state, target_id)
    if limb_name not in target["limbs"]:
        raise KeyError(f"{target_id!r} has no limb {limb_name!r} on record")
    limb = target["limbs"][limb_name]
    result = resolver.limb_hit(
        raw_damage, limb["multiplier"], limb["threshold"], accumulated=limb.get("accumulated", 0)
    )
    limb["accumulated"] = result["accumulated"]
    limb["staggered"] = result["staggered"]
    if result["severed"]:
        limb["severed"] = True

    target["hp"] = max(target["hp"] - result["effective_damage"], 0)
    killed_by_sever = result["severed"] and limb_name in ("head", "torso")
    if target["hp"] <= 0 or killed_by_sever:
        target["alive"] = False

    return {
        "effective_damage": result["effective_damage"],
        "staggered": result["staggered"],
        "severed": result["severed"],
        "hp": target["hp"],
        "alive": target["alive"],
    }


def tick_start_of_turn(state, combatant_id):
    """Apply the start-of-turn ticks that drain or hold on their own:
    Bleeding and Corrosion. Returns a log of what fired, so the DM can
    narrate it without doing the maths by hand. Corrosion is passed
    managed_this_turn=False here deliberately — call
    manage_track(state, combatant_id, 'corrosion') separately on a turn
    where an action was spent clearing it."""
    combatant = _get(state, combatant_id)
    log = []

    bleeding = combatant["status"]["bleeding"]
    if bleeding > 0:
        result = resolver.bleeding_tick(bleeding)
        combatant["hp"] = max(combatant["hp"] - result["damage"], 0)
        combatant["status"]["bleeding"] = result["remaining"]
        log.append({"status": "bleeding", "damage": result["damage"], "remaining": result["remaining"]})

    burning = combatant["status"]["burning"]
    if burning > 0:
        combatant["hp"] = max(combatant["hp"] - 5, 0)
        combatant["status"]["burning"] = max(burning - 1, 0)
        log.append({"status": "burning", "damage": 5, "remaining": combatant["status"]["burning"]})

    corrosion = combatant["status"]["corrosion"]
    if corrosion > 0:
        result = resolver.corrosion_tick(corrosion, managed_this_turn=False)
        combatant["hp"] = max(combatant["hp"] - result["damage"], 0)
        log.append({"status": "corrosion", "damage": result["damage"], "remaining": result["remaining"]})

    if combatant["hp"] <= 0:
        combatant["alive"] = False

    return log


def manage_track(state, combatant_id, status_name):
    """Spend the action a held-type track needs to actually decrement
    (Corrosion only decays if a turn was spent managing it; Crust only if
    the whole turn took no Action at all — call this to represent that
    turn having happened)."""
    combatant = _get(state, combatant_id)
    if status_name == "corrosion":
        result = resolver.corrosion_tick(combatant["status"]["corrosion"], managed_this_turn=True)
        combatant["status"]["corrosion"] = result["remaining"]
    elif status_name == "crust":
        combatant["status"]["crust"] = max(combatant["status"]["crust"] - 1, 0)
    else:
        raise ValueError(f"{status_name!r} isn't a manage-to-decay track")
    return combatant["status"][status_name]


def advance_round(state):
    state["round"] += 1
    return state["round"]
