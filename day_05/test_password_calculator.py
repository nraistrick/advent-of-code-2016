import unittest
from day_05.day_5 import calculate_password, calculate_advanced_password


class TestPasswordCalculator(unittest.TestCase):
    door_input = "abc"
    valid_password = "18f47a30"
    valid_advanced_password = "05ace8e3"

    def test_password_correct(self):
        password = calculate_password(TestPasswordCalculator.door_input)
        self.assertEqual(TestPasswordCalculator.valid_password, password)

    def test_advanced_password_correct(self):
        password = calculate_advanced_password(TestPasswordCalculator.door_input)
        self.assertEqual(TestPasswordCalculator.valid_advanced_password, password)


if __name__ == '__main__':
    unittest.main()
