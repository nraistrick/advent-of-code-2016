import unittest
from day_05.day_5 import password_hash_values, \
    calculate_password, \
    calculate_advanced_password


class TestPasswordCalculator(unittest.TestCase):
    door_input = "abc"
    valid_password = "18f47a30"
    valid_advanced_password = "05ace8e3"

    def test_password_hash_values(self):
        hash_values = password_hash_values("wtnhxymk")
        first_hash_values = [next(hash_values) for _ in range(3)]
        self.assertEqual(first_hash_values,
                         ['0000027b9705c7e6fa3d4816c490bbfd',
                          '00000468c8625d85571d250737c47b5a',
                          '0000013e3293b49e4c78a5b43b21023b'])

    def test_password_correct(self):
        password = calculate_password(TestPasswordCalculator.door_input)
        self.assertEqual(TestPasswordCalculator.valid_password, password)

    def test_advanced_password_correct(self):
        password = calculate_advanced_password(TestPasswordCalculator.door_input)
        self.assertEqual(TestPasswordCalculator.valid_advanced_password, password)


if __name__ == '__main__':
    unittest.main()
