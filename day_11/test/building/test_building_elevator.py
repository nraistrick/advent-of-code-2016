from unittest import TestCase

from day_11.building.building import Building, ElevatorMovementType
from day_11.floor.floor import Floor
from day_11.test.building import DUMMY_FLOOR_ITEM_1


class TestBuildingElevator(TestCase):

    EMPTY_FLOOR = Floor()

    SINGLE_EMPTY_FLOOR = [EMPTY_FLOOR]
    MULTIPLE_EMPTY_FLOORS = [EMPTY_FLOOR, EMPTY_FLOOR, EMPTY_FLOOR]

    def test_floors_set_correctly(self):
        building = Building(self.MULTIPLE_EMPTY_FLOORS)
        self.assertEqual(building.floor_numbers, [1, 2, 3])

    def test_defaults_to_ground_floor(self):
        building = Building(self.MULTIPLE_EMPTY_FLOORS)
        self.assertEqual(building.elevator_floor_id, 1)

    def test_stops_at_top_floor(self):
        building = Building(self.SINGLE_EMPTY_FLOOR)
        building._elevator_items = [DUMMY_FLOOR_ITEM_1]
        with self.assertRaises(ValueError) as context:
            building.go_up_in_elevator()
        self.assertTrue("elevator cannot go higher" in str(context.exception))

    def test_stops_at_bottom_floor(self):
        building = Building(self.SINGLE_EMPTY_FLOOR)
        building._elevator_items = [DUMMY_FLOOR_ITEM_1]
        with self.assertRaises(ValueError) as context:
            building.go_down_in_elevator()
        self.assertTrue("elevator cannot go lower" in str(context.exception))

    def test_available_directions(self):
        building = Building(self.MULTIPLE_EMPTY_FLOORS)
        building._elevator_floor_id = building.bottom_floor_id
        self.assertEqual(building.available_elevator_directions,
                         [ElevatorMovementType.UP])

        building._elevator_floor_id = 2
        self.assertEqual(building.available_elevator_directions,
                         [ElevatorMovementType.UP, ElevatorMovementType.DOWN])

        building._elevator_floor_id = building.top_floor_id
        self.assertEqual(building.available_elevator_directions,
                         [ElevatorMovementType.DOWN])
