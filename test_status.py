from monitor import check_status
import unittest

class TestCheckStatus(unittest.TestCase):
    def test_zero_usage(self):
        self.assertEqual(check_status(0), "Normal")

    def test_normal_boundary(self):
        self.assertEqual(check_status(49), "Normal")

    def test_moderate_start(self):
        self.assertEqual(check_status(50), "Moderate")

    def test_moderate_boundary(self):
        self.assertEqual(check_status(79), "Moderate")

    def test_high_start(self):
        self.assertEqual(check_status(80), "High")
        
    def test_max_usage(self):
        self.assertEqual(check_status(100), "High")




