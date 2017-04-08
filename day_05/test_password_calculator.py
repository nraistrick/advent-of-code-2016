import unittest
from day_05.day_5 import calculate_password


class TestPasswordCalculator(unittest.TestCase):
    door_input = "abc"
    valid_password = "18f47a30"

    def test_password_is_correct(self):
        password = calculate_password(TestPasswordCalculator.door_input)
        self.assertEqual(TestPasswordCalculator.valid_password, password)


if __name__ == '__main__':
    unittest.main()
