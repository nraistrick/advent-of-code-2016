from copy import deepcopy
from unittest import TestCase

from day_11.floor.floor import Floor
from day_11.floor.item import FloorItem
from day_11.floor.item_type import FloorItemType
from day_11.floor.microchip_destroyed import MicrochipDestroyed
from day_11.test.floor import ELEMENT_1, ELEMENT_2

ELEMENT_1_GENERATOR = FloorItem(ELEMENT_1, FloorItemType.GENERATOR)
ELEMENT_1_MICROCHIP = FloorItem(ELEMENT_1, FloorItemType.MICROCHIP)
ELEMENT_2_GENERATOR = FloorItem(ELEMENT_2, FloorItemType.GENERATOR)
ELEMENT_2_MICROCHIP = FloorItem(ELEMENT_2, FloorItemType.MICROCHIP)


class TestFloor(TestCase):
    @staticmethod
    def test_can_create_safe_floor():
        """
        Checks we can create a floor with a valid set of items without raising
        an exception.
        """
        contents = {ELEMENT_1_GENERATOR, ELEMENT_1_MICROCHIP}
        Floor(contents)

    def test_cannot_create_unsafe_floor(self):
        """
        Checks the floor will raise an exception that a microchip has been
        destroyed with an invalid floor item configuration.
        """
        contents = {ELEMENT_1_GENERATOR, ELEMENT_2_MICROCHIP}
        with self.assertRaises(MicrochipDestroyed) as context:
            Floor(contents)
        self.assertTrue("Microchip(s) destroyed" in context.exception.message)

    def test_remove_at_least_one_item(self):
        floor = Floor()
        with self.assertRaises(ValueError):
            floor.remove_items(set())

    def test_make_floor_unsafe(self):
        floor = Floor({ELEMENT_1_GENERATOR})
        with self.assertRaises(MicrochipDestroyed) as context:
            floor.add_items({ELEMENT_2_MICROCHIP})
        self.assertTrue("Microchip(s) destroyed" in context.exception.message)

        floor = Floor({ELEMENT_1_GENERATOR, ELEMENT_1_MICROCHIP, ELEMENT_2_GENERATOR})
        with self.assertRaises(MicrochipDestroyed) as context:
            floor.remove_items({ELEMENT_1_GENERATOR})
        self.assertTrue("Microchip(s) destroyed" in context.exception.message)

    def test_floor_equalities(self):
        floor_1 = Floor({ELEMENT_1_GENERATOR, ELEMENT_1_MICROCHIP})
        floor_2 = Floor({ELEMENT_1_GENERATOR, ELEMENT_1_MICROCHIP})
        self.assertNotEqual(id(floor_1), id(floor_2))
        self.assertTrue(floor_1 == floor_2)
        self.assertFalse(floor_1 != floor_2)

        copied_floor_1 = deepcopy(floor_1)
        self.assertNotEqual(id(floor_1), id(floor_2))
        self.assertTrue(floor_1 == copied_floor_1)
        self.assertFalse(floor_1 != copied_floor_1)

        floor_1 = Floor()
        floor_2 = Floor({ELEMENT_1_GENERATOR, ELEMENT_1_MICROCHIP})
        self.assertFalse(floor_1 == floor_2)
        self.assertTrue(floor_1 != floor_2)

        floor_1 = Floor({ELEMENT_1_GENERATOR, ELEMENT_1_MICROCHIP})
        floor_2 = Floor({ELEMENT_2_GENERATOR, ELEMENT_2_MICROCHIP})
        self.assertFalse(floor_1 == floor_2)
        self.assertTrue(floor_1 != floor_2)

    def test_sort_floor_items(self):
        unsorted_items = [ELEMENT_1_MICROCHIP, ELEMENT_2_MICROCHIP,
                          ELEMENT_2_GENERATOR, ELEMENT_1_GENERATOR]
        sorted_items = [ELEMENT_1_GENERATOR, ELEMENT_1_MICROCHIP,
                        ELEMENT_2_GENERATOR, ELEMENT_2_MICROCHIP]
        self.assertEqual(Floor.sort_items(unsorted_items), sorted_items)
