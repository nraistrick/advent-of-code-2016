import os
import unittest
from day_06.day_6 import get_columns, get_most_common_character, recover_original_text

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
TEST_FILE = os.path.join(CURRENT_DIRECTORY, "input/example_scrambled_input.txt")


class TestRecoverMessage(unittest.TestCase):
    valid_first_column = "ederatsrnnstvvde"
    valid_first_column_character = "e"
    valid_message = "easter"
    actual_valid_message = "advent"

    def test_get_valid_column(self):
        column_data = get_columns(TEST_FILE)
        self.assertEqual(self.valid_first_column, column_data[0])

    def test_get_most_common(self):
        common = get_most_common_character(list(self.valid_first_column))
        self.assertEqual(self.valid_first_column_character, common)

    def test_recover_message(self):
        message = recover_original_text(TEST_FILE)
        self.assertEqual(self.valid_message, message)

    def test_recover_actual_message(self):
        message = recover_original_text(TEST_FILE, False)
        self.assertEqual(self.actual_valid_message, message)


if __name__ == '__main__':
    unittest.main()
