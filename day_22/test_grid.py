import os
import unittest
from common.common import get_file_lines
from day_22.grid import Grid
from day_22.node import Node

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
TEST_FILE = os.path.join(CURRENT_DIRECTORY, "input/testinput.txt")


class TestGrid(unittest.TestCase):
    def test_get_move_count(self):
        input_text = [line for line in get_file_lines(TEST_FILE)]
        nodes = [Node.from_string(line) for line in input_text[2:]]
        grid = Grid(nodes)
        move_count = grid.solve()
        self.assertEqual(move_count, 7)


if __name__ == '__main__':
    unittest.main()
