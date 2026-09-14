import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import resolver


class TestESVAndWeaponDamage(unittest.TestCase):
    def test_esv_brackets(self):
        self.assertEqual(resolver.esv(8), 8.0)
        self.assertEqual(resolver.esv(20), 20.0)
        self.assertEqual(resolver.esv(40), 37.0)
        self.assertAlmostEqual(resolver.esv(99), 65.7)

    def test_cautery_saw_worked_examples(self):
        # Ruleset §4 worked example: Cautery Saw heavy, base 30, Strength/B.
        self.assertEqual(resolver.weapon_damage(30, 8, "B", "heavy"), 71)
        self.assertEqual(resolver.weapon_damage(30, 40, "B", "heavy"), 110)
        self.assertEqual(resolver.weapon_damage(30, 99, "B", "heavy"), 149)

    def test_light_formula(self):
        # Base + ESV*grade, round up.
        self.assertEqual(resolver.weapon_damage(22, 20, "D", "light"), 32)

    def test_charged_heavy_is_stronger_than_heavy(self):
        heavy = resolver.weapon_damage(30, 40, "B", "heavy")
        charged = resolver.weapon_damage(30, 40, "B", "charged_heavy")
        self.assertGreater(charged, heavy)

    def test_double_swing_rounds_up(self):
        self.assertEqual(resolver.double_swing_second_hit(33), 17)


class TestLimbHits(unittest.TestCase):
    def test_ruleset_leg_sever_worked_example(self):
        # §10: leg x0.75, 325 threshold, 450 raw in one hit -> 338, severs.
        result = resolver.limb_hit(450, 0.75, 325)
        self.assertEqual(result["effective_damage"], 338)
        self.assertTrue(result["severed"])
        self.assertFalse(result["staggered"])

    def test_stagger_without_sever(self):
        # Two hits that only cross the threshold cumulatively, not in one hit.
        first = resolver.limb_hit(160, 0.65, 200)
        self.assertFalse(first["severed"])
        self.assertFalse(first["staggered"])
        second = resolver.limb_hit(160, 0.65, 200, accumulated=first["accumulated"])
        self.assertFalse(second["severed"])
        self.assertTrue(second["staggered"])

    def test_torso_hit_full_multiplier(self):
        result = resolver.limb_hit(450, 1.0, 800)
        self.assertEqual(result["effective_damage"], 450)


class TestAccuracyTiers(unittest.TestCase):
    def test_dead_centre_is_critical(self):
        self.assertEqual(resolver.accuracy_tier_multiplier(0.10, 0.0), 3.0)

    def test_single_band_window_never_bonuses(self):
        # Tightest required tolerance (2.01+ multiplier) has nowhere to go deeper.
        self.assertEqual(resolver.accuracy_tier_multiplier(0.02, 0.01), 1.0)
        self.assertEqual(resolver.accuracy_tier_multiplier(0.02, 0.0), 3.0)

    def test_deep_hit_gets_bonus(self):
        # Required 0.10s window, landed within 0.02s -> counts bands
        # [0.10, 0.07, 0.04, 0.02] = 4 deep -> x1.1.
        self.assertEqual(resolver.accuracy_tier_multiplier(0.10, 0.02), 1.1)

    def test_shallow_hit_no_bonus(self):
        self.assertEqual(resolver.accuracy_tier_multiplier(0.25, 0.24), 1.0)

    def test_beyond_tolerance_raises(self):
        with self.assertRaises(ValueError):
            resolver.accuracy_tier_multiplier(0.10, 0.15)

    def test_tolerance_band_lookup_matches_ruleset_table(self):
        self.assertEqual(resolver.tolerance_band_for_multiplier(0.3), 0.25)
        self.assertEqual(resolver.tolerance_band_for_multiplier(1.0), None)
        self.assertEqual(resolver.tolerance_band_for_multiplier(1.4), 0.10)
        self.assertEqual(resolver.tolerance_band_for_multiplier(2.5), 0.02)


class TestInsight(unittest.TestCase):
    def test_tier_breakpoints(self):
        self.assertEqual(resolver.insight_tier(0), 0)
        self.assertEqual(resolver.insight_tier(1), 0)
        self.assertEqual(resolver.insight_tier(2), 1)
        self.assertEqual(resolver.insight_tier(5), 2)
        self.assertEqual(resolver.insight_tier(11), 5)

    def test_window_bonus_flat_not_additive(self):
        self.assertEqual(resolver.insight_window_bonus(11), 0.10)
        self.assertEqual(resolver.insight_window_bonus(7), 0.04)  # Tier 3 inherits Tier 2's value


class TestSaveRoll(unittest.TestCase):
    def test_ruleset_worked_examples(self):
        # Resolve 8, Insight 1, 2nd Influence stack -> 10+2-0+0 = 12
        self.assertEqual(resolver.save_dc(track=2, resolve=8, insight=1), 12)
        # Resolve 30, Insight 6, Influence 6 -> 10+6-3+3 = 16
        self.assertEqual(resolver.save_dc(track=6, resolve=30, insight=6), 16)


class TestStatusMaths(unittest.TestCase):
    def test_bleeding_totals(self):
        self.assertEqual(resolver.bleeding_total(3), 6)
        self.assertEqual(resolver.bleeding_total(5), 15)
        self.assertEqual(resolver.bleeding_total(10), 55)
        self.assertEqual(resolver.bleeding_total(15), 120)
        self.assertEqual(resolver.bleeding_total(25), 325)

    def test_bleeding_tick_drains_itself(self):
        result = resolver.bleeding_tick(5)
        self.assertEqual(result["damage"], 5)
        self.assertEqual(result["remaining"], 4)

    def test_corrosion_holds_unless_managed(self):
        unmanaged = resolver.corrosion_tick(6)
        self.assertEqual(unmanaged["damage"], 6)
        self.assertEqual(unmanaged["remaining"], 6)
        managed = resolver.corrosion_tick(6, managed_this_turn=True)
        self.assertEqual(managed["remaining"], 5)

    def test_stone_skin_caps_at_three_stacks(self):
        self.assertAlmostEqual(resolver.stone_skin_reduction(3), 0.30)
        self.assertAlmostEqual(resolver.stone_skin_reduction(5), 0.30)

    def test_crust_caps_at_four(self):
        self.assertEqual(resolver.crust_movement_penalty(4), -4)
        self.assertEqual(resolver.crust_movement_penalty(9), -4)

    def test_fervour_bonus_scales_per_stack(self):
        bonus = resolver.fervour_bonus(4)
        self.assertEqual(bonus["bonus_damage"], 12)
        self.assertEqual(bonus["bonus_movement"], 2.0)
        self.assertEqual(resolver.fervour_whiff_cost(4), 12)


if __name__ == "__main__":
    unittest.main()
