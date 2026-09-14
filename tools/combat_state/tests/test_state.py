import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import state as combat_state


def make_encounter():
    enc = combat_state.new_encounter("test fight")
    lloyd = combat_state.new_combatant("lloyd", "Lloyd", max_hp=120, side="player")
    enemy = combat_state.new_combatant(
        "enemy1",
        "Test Mook",
        max_hp=400,
        side="enemy",
        limbs={
            "head": {"multiplier": 1.5, "threshold": 180},
            "torso": {"multiplier": 1.0, "threshold": 800},
            "arm": {"multiplier": 0.65, "threshold": 200},
        },
    )
    combat_state.add_combatant(enc, lloyd)
    combat_state.add_combatant(enc, enemy)
    return enc


class TestCombatantLifecycle(unittest.TestCase):
    def test_flat_damage_kills_at_zero(self):
        enc = make_encounter()
        combat_state.apply_flat_damage(enc, "lloyd", 200)
        self.assertEqual(enc["combatants"]["lloyd"]["hp"], 0)
        self.assertFalse(enc["combatants"]["lloyd"]["alive"])

    def test_flat_damage_does_not_go_negative(self):
        enc = make_encounter()
        combat_state.apply_flat_damage(enc, "lloyd", 200)
        self.assertEqual(enc["combatants"]["lloyd"]["hp"], 0)


class TestLimbAttacks(unittest.TestCase):
    def test_unknown_limb_raises(self):
        enc = make_encounter()
        with self.assertRaises(KeyError):
            combat_state.apply_limb_attack(enc, "enemy1", "wing", 100)

    def test_arm_sever_does_not_kill(self):
        enc = make_encounter()
        # 200 threshold / 0.65 mult -> raw >= 308 severs in one hit.
        result = combat_state.apply_limb_attack(enc, "enemy1", "arm", 320)
        self.assertTrue(result["severed"])
        self.assertTrue(enc["combatants"]["enemy1"]["alive"])
        self.assertTrue(enc["combatants"]["enemy1"]["limbs"]["arm"]["severed"])

    def test_head_sever_kills_regardless_of_remaining_hp(self):
        enc = make_encounter()
        # 180 threshold / 1.5 mult -> raw >= 120 severs. Enemy has 400 HP,
        # effective damage here is nowhere near enough to zero it by HP alone.
        result = combat_state.apply_limb_attack(enc, "enemy1", "head", 130)
        self.assertTrue(result["severed"])
        self.assertFalse(result["alive"])
        self.assertGreater(result["hp"], 0)  # died by sever, not by HP

    def test_cumulative_stagger_across_two_hits(self):
        enc = make_encounter()
        combat_state.apply_limb_attack(enc, "enemy1", "arm", 160)  # 104 effective
        result = combat_state.apply_limb_attack(enc, "enemy1", "arm", 160)  # 104 + 104 = 208 >= 200
        self.assertTrue(result["staggered"])
        self.assertFalse(result["severed"])


class TestStatusStacks(unittest.TestCase):
    def test_stacks_clamp_at_cap(self):
        enc = make_encounter()
        combat_state.apply_status_stack(enc, "lloyd", "discombobulation", 5)
        self.assertEqual(enc["combatants"]["lloyd"]["status"]["discombobulation"], 3)

    def test_stacks_never_go_negative(self):
        enc = make_encounter()
        combat_state.apply_status_stack(enc, "lloyd", "bleeding", -5)
        self.assertEqual(enc["combatants"]["lloyd"]["status"]["bleeding"], 0)

    def test_uncapped_status_has_no_ceiling(self):
        enc = make_encounter()
        combat_state.apply_status_stack(enc, "lloyd", "bleeding", 25)
        self.assertEqual(enc["combatants"]["lloyd"]["status"]["bleeding"], 25)

    def test_unknown_status_raises(self):
        enc = make_encounter()
        with self.assertRaises(KeyError):
            combat_state.apply_status_stack(enc, "lloyd", "nonsense", 1)


class TestTicks(unittest.TestCase):
    def test_bleeding_drains_and_damages(self):
        enc = make_encounter()
        combat_state.apply_status_stack(enc, "lloyd", "bleeding", 5)
        log = combat_state.tick_start_of_turn(enc, "lloyd")
        self.assertEqual(enc["combatants"]["lloyd"]["hp"], 115)
        self.assertEqual(enc["combatants"]["lloyd"]["status"]["bleeding"], 4)
        self.assertEqual(log[0]["status"], "bleeding")

    def test_corrosion_holds_without_manage(self):
        enc = make_encounter()
        combat_state.apply_status_stack(enc, "lloyd", "corrosion", 6)
        combat_state.tick_start_of_turn(enc, "lloyd")
        self.assertEqual(enc["combatants"]["lloyd"]["status"]["corrosion"], 6)
        self.assertEqual(enc["combatants"]["lloyd"]["hp"], 114)

    def test_manage_track_decays_corrosion(self):
        enc = make_encounter()
        combat_state.apply_status_stack(enc, "lloyd", "corrosion", 6)
        combat_state.manage_track(enc, "lloyd", "corrosion")
        self.assertEqual(enc["combatants"]["lloyd"]["status"]["corrosion"], 5)

    def test_death_by_ticks(self):
        enc = make_encounter()
        combat_state.apply_flat_damage(enc, "lloyd", 118)
        combat_state.apply_status_stack(enc, "lloyd", "bleeding", 5)
        combat_state.tick_start_of_turn(enc, "lloyd")
        self.assertFalse(enc["combatants"]["lloyd"]["alive"])


class TestPersistence(unittest.TestCase):
    def test_save_and_load_roundtrip(self):
        enc = make_encounter()
        combat_state.apply_flat_damage(enc, "lloyd", 30)
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = f.name
        try:
            combat_state.save(enc, path)
            reloaded = combat_state.load(path)
            self.assertEqual(reloaded["combatants"]["lloyd"]["hp"], 90)
        finally:
            os.remove(path)


class TestRounds(unittest.TestCase):
    def test_advance_round(self):
        enc = make_encounter()
        self.assertEqual(enc["round"], 1)
        combat_state.advance_round(enc)
        self.assertEqual(enc["round"], 2)


if __name__ == "__main__":
    unittest.main()
