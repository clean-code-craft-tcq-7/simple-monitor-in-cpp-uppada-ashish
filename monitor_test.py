import unittest
from monitor import are_vitals_normal

class VitalSignsTest(unittest.TestCase):
    def test_temp_above_limit(self):
        self.assertFalse(are_vitals_normal(103, 80, 95))  # Too high temp

    def test_temp_below_limit(self):
        self.assertFalse(are_vitals_normal(94, 80, 95))   # Too low temp

    def test_pulse_below_range(self):
        self.assertFalse(are_vitals_normal(98, 55, 95))   # Low pulse rate

    def test_pulse_above_range(self):
        self.assertFalse(are_vitals_normal(98, 105, 95))  # High pulse rate

    def test_oxygen_below_threshold(self):
        self.assertFalse(are_vitals_normal(98, 80, 89))   # Low SpO2

    def test_vitals_within_normal_range(self):
        self.assertTrue(are_vitals_normal(98.6, 75, 96))  # All normal

    def test_stop_at_first_failure(self):
        self.assertFalse(are_vitals_normal(103, 120, 85))  # Fails on temperature

if __name__ == '__main__':
    unittest.main()
