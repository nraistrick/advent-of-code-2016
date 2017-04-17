import os
import unittest
from day_10 import \
    get_container_object_ids, \
    get_initialised_containers, \
    initialise_containers, \
    find_bot_to_compare_chips, \
    get_microchip_product

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
TEST_FILE = os.path.join(CURRENT_DIRECTORY, "input/test_input.txt")


class TestMicrochipPassing(unittest.TestCase):
    @staticmethod
    def get_test_instructions():
        return open(TEST_FILE).read().split('\n')

    def test_invalid_container_type(self):
        with self.assertRaises(ValueError):
            get_container_object_ids([], "blah")

    def test_invalid_instruction(self):
        instructions = ["blah blah blah"]
        with self.assertRaises(ValueError):
            initialise_containers(instructions, {}, {})

    def test_find_bot_comparing_microchips(self):
        instructions = self.get_test_instructions()
        bots, _ = get_initialised_containers(instructions)
        self.assertEqual(find_bot_to_compare_chips(bots, 2, 5), 2)

    def test_find_microchip_product(self):
        instructions = self.get_test_instructions()
        bots, outputs = get_initialised_containers(instructions)
        self.assertEqual(get_microchip_product(bots, outputs), 30)


if __name__ == '__main__':
    unittest.main()
