from copy import deepcopy
from unittest import TestCase

from day_11.building.building import Building
from day_11.floor.floor import Floor
from day_11.test.building import \
    DUMMY_FLOOR_ITEM_1, \
    DUMMY_FLOOR_ITEM_2, \
    DUMMY_FLOOR_ITEM_3

EMPTY_FLOOR = Floor()
SINGLE_EMPTY_FLOOR = [EMPTY_FLOOR]
MULTIPLE_EMPTY_FLOORS = [EMPTY_FLOOR, EMPTY_FLOOR, EMPTY_FLOOR]


class TestBuilding(TestCase):
    def test_cannot_add_duplicate_items(self):
        with self.assertRaises(ValueError):
            Building([Floor({DUMMY_FLOOR_ITEM_1}), Floor({DUMMY_FLOOR_ITEM_1})])

    def test_all_items(self):
        building = Building(MULTIPLE_EMPTY_FLOORS)
        self.assertEqual(len(building.all_items), 0)

        building = Building([Floor({DUMMY_FLOOR_ITEM_1})])
        self.assertEqual(building.all_items, [DUMMY_FLOOR_ITEM_1])

        building = Building([Floor({DUMMY_FLOOR_ITEM_1}), Floor({DUMMY_FLOOR_ITEM_2})])
        self.assertEqual(building.all_items, [DUMMY_FLOOR_ITEM_1, DUMMY_FLOOR_ITEM_2])

    def test_all_floors_below_empty(self):
        building = Building([Floor({DUMMY_FLOOR_ITEM_1}), Floor({DUMMY_FLOOR_ITEM_2}), EMPTY_FLOOR])
        self.validate_floors_below_empty(building, 1)

        building = Building([EMPTY_FLOOR, Floor({DUMMY_FLOOR_ITEM_1}), EMPTY_FLOOR])
        self.validate_floors_below_empty(building, 2)

        building = Building([EMPTY_FLOOR, EMPTY_FLOOR, Floor({DUMMY_FLOOR_ITEM_3})])
        self.validate_floors_below_empty(building, 3)

    def validate_floors_below_empty(self, building, lowest_populated_floor):
        for floor_id in building.floor_numbers:
            building._elevator_floor_id = floor_id
            items_below = True if floor_id > lowest_populated_floor else False
            self.assertEqual(building.items_on_floors_below, items_below)

    def test_grab_and_drop_items(self):
        all_floor_items = {DUMMY_FLOOR_ITEM_1, DUMMY_FLOOR_ITEM_2, DUMMY_FLOOR_ITEM_3}
        items_to_pickup = {DUMMY_FLOOR_ITEM_1, DUMMY_FLOOR_ITEM_2}
        remaining_items = {DUMMY_FLOOR_ITEM_3}

        floor = Floor(all_floor_items)
        building = Building([floor])

        # Check we can't pick up more than the maximum number of items
        with self.assertRaises(ValueError) as context:
            building.grab_items(all_floor_items)
        self.assertTrue("Cannot pick up" in context.exception.message)

        # Check we can't pick up additional items before dropping our current ones
        building.grab_items(items_to_pickup)
        self.assertEqual(building.elevator_items, items_to_pickup)
        self.assertEqual(building.current_floor_items, remaining_items)
        with self.assertRaises(ValueError) as context:
            building.grab_items(remaining_items)
        self.assertTrue("Must drop items before" in context.exception.message)

        # Check items are placed back on the current floor correctly
        building.drop_items()
        self.assertEqual(building.current_floor_items, all_floor_items)

    def test_move_items_in_lift(self):
        floor_1_contents = {DUMMY_FLOOR_ITEM_1, DUMMY_FLOOR_ITEM_2}
        floor_2_contents = set()
        building = Building([Floor(floor_1_contents), Floor(floor_2_contents)])

        with self.assertRaises(ValueError) as context:
            building.go_up_in_elevator()
        self.assertTrue("Must be holding at least one item" in context.exception.message)

        building.grab_items(set(floor_1_contents))
        building.go_up_in_elevator()
        self.assertEqual(building._elevator_floor_id, 2)
        self.assertEqual(len(building.elevator_items), 0)
        self.assertEqual(floor_2_contents, {DUMMY_FLOOR_ITEM_1, DUMMY_FLOOR_ITEM_2})

        with self.assertRaises(ValueError) as context:
            building.go_down_in_elevator()
        self.assertTrue("Must be holding at least one item" in context.exception.message)

        building.grab_items({DUMMY_FLOOR_ITEM_1})
        building.go_down_in_elevator()
        self.assertEqual(building._elevator_floor_id, 1)
        self.assertEqual(len(building.elevator_items), 0)
        self.assertTrue(DUMMY_FLOOR_ITEM_1 in floor_1_contents and
                        DUMMY_FLOOR_ITEM_2 in floor_2_contents)

    def test_building_equality(self):
        floor_1_contents = {DUMMY_FLOOR_ITEM_1, DUMMY_FLOOR_ITEM_2}
        building = Building([Floor(floor_1_contents), Floor()])
        existing_buildings = [building]
        another_building = deepcopy(building)
        self.assertNotEqual(id(building), id(another_building))
        self.assertTrue(another_building in existing_buildings)

        another_building.grab_items(floor_1_contents)
        another_building.go_up_in_elevator()
        self.assertNotEqual(building.elevator_floor_id, another_building.elevator_floor_id)
        self.assertFalse(another_building in existing_buildings)

        building = Building([EMPTY_FLOOR, EMPTY_FLOOR])
        another_building = Building([EMPTY_FLOOR, EMPTY_FLOOR])
        another_building._elevator_floor_id = 2
        self.assertNotEqual(building.elevator_floor_id, another_building.elevator_floor_id)
        self.assertFalse(building == another_building)

    def test_deepcopy(self):
        building = Building([EMPTY_FLOOR])
        copied_building = deepcopy(building)
        self.assertNotEqual(id(building), id(copied_building))

        building.floors[0].add_items({DUMMY_FLOOR_ITEM_1})
        self.assertNotEqual(building.floors[0], copied_building.floors[0])
