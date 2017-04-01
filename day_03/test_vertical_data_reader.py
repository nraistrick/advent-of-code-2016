import os
import unittest
from day_03.day_3 import get_vertical_triangle_data

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
TEST_FILE = os.path.join(CURRENT_DIRECTORY, "input/test_vertical_data.txt")


class TestVerticalDataReader(unittest.TestCase):
    valid_output = [(101, 102, 103), (201, 202, 203), (301, 302, 303),
                    (401, 402, 403), (501, 502, 503), (601, 602, 603)]

    def test_parse_vertical_input(self):
        triangle_data = get_vertical_triangle_data(TEST_FILE)
        self.assertEqual(triangle_data, self.valid_output)


if __name__ == '__main__':
    unittest.main()
