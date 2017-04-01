import os
import unittest
from unittest import TestCase
from day_02.day_2 import follow_instructions, follow_complex_instructions

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
TEST_FILE = os.path.join(CURRENT_DIRECTORY, "input/keypad_test_instructions.txt")


class TestKeypadCodeFinder(TestCase):
    """
    Pass valid data to the program to check it calculates the right answers
    """
    def test_keypad(self):
        pin = follow_instructions(TEST_FILE)
        self.assertEqual("1985", pin)

    def test_complex_keypad(self):
        pin = follow_complex_instructions(TEST_FILE)
        self.assertEqual("5DB3", pin)


if __name__ == '__main__':
    unittest.main()
