import os
import unittest
from common.common import get_file_lines
from day_24.main import create_indexed_map, \
    moves_to_visit_each_number, \
    get_shortest_round_trip

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
TEST_FILE = os.path.join(CURRENT_DIRECTORY, "input/testinput.txt")


class TestRobot(unittest.TestCase):
    def test_solve_maze(self):
        lines = [line for line in get_file_lines(TEST_FILE)]
        robot_map = create_indexed_map(lines)
        move_count = moves_to_visit_each_number(robot_map)
        self.assertEqual(move_count, 14)

    def test_shortest_round_trip(self):
        lines = [line for line in get_file_lines(TEST_FILE)]
        robot_map = create_indexed_map(lines)
        move_count = get_shortest_round_trip(robot_map)
        self.assertEqual(move_count, 20)


if __name__ == '__main__':
    unittest.main()
