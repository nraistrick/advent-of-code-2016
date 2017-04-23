from copy import copy
from unittest import TestCase

from day_11.floor.item import FloorItem
from day_11.floor.item_type import FloorItemType
from day_11.test.floor import \
    ELEMENT_1, \
    ELEMENT_1_GENERATOR_STRING, \
    ELEMENT_1_MICROCHIP_STRING, \
    INVALID_FLOOR_ITEM_TYPE


class TestFloorItem(TestCase):
    @staticmethod
    def test_create_floor_items():
        FloorItem(ELEMENT_1, FloorItemType.GENERATOR)
        FloorItem(ELEMENT_1, FloorItemType.MICROCHIP)

    def test_create_invalid_floor_items(self):
        with self.assertRaises(ValueError) as context:
            FloorItem("", FloorItemType.GENERATOR)
        self.assertTrue("element name must be specified" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            FloorItem(ELEMENT_1, INVALID_FLOOR_ITEM_TYPE)
        self.assertTrue("must be one of the valid floor item types" in str(context.exception))

    def test_floor_item_representation(self):
        generator = FloorItem(ELEMENT_1, FloorItemType.GENERATOR)
        self.assertEqual(ELEMENT_1_GENERATOR_STRING, repr(generator))

        microchip = FloorItem(ELEMENT_1, FloorItemType.MICROCHIP)
        self.assertEqual(ELEMENT_1_MICROCHIP_STRING, repr(microchip))

    def test_floor_item_equalities(self):
        generator = FloorItem(ELEMENT_1, FloorItemType.GENERATOR)
        microchip = FloorItem(ELEMENT_1, FloorItemType.MICROCHIP)
        microchip_copy = copy(microchip)

        # Check items are compared by properties and not memory locations
        self.assertNotEqual(id(microchip), id(microchip_copy))
        self.assertTrue(microchip == microchip_copy)
        self.assertFalse(microchip != microchip_copy)

        # Check objects with different properties
        self.assertTrue(generator != microchip)
        self.assertFalse(generator == microchip)
