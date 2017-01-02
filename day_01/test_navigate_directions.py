from unittest import TestCase
from day_01.day_1 import calculate_block_distance, \
    get_final_coordinates, \
    get_actual_bunny_hq_coordinates

JOURNEY_1 = "R2, L3"
END_LOCATION_1 = (2, 3)
FINAL_DISTANCE_1 = 5

JOURNEY_2 = "R2, R2, R2"
END_LOCATION_2 = (0, -2)
FINAL_DISTANCE_2 = 2

JOURNEY_3 = "R5, L5, R5, R3"
END_LOCATION_3 = (10, 2)
FINAL_DISTANCE_3 = 12

JOURNEY_4 = "L100, L100, L50, L200"
END_LOCATION_4 = (-50, 100)
ACTUAL_END_LOCATION_4 = (-50, 0)
FINAL_DISTANCE_4 = 150

JOURNEY_5 = "R5, R5, R3, R10"
END_LOCATION_5 = (2, 5)
ACTUAL_END_LOCATION_5 = (2, 0)
FINAL_DISTANCE_5 = 7


class TestNavigateDirections(TestCase):
    def test_calculate_block_distance(self):
        distance = calculate_block_distance(END_LOCATION_1)
        self.assertEqual(distance, FINAL_DISTANCE_1)

        distance = calculate_block_distance(END_LOCATION_2)
        self.assertEqual(distance, FINAL_DISTANCE_2)

        distance = calculate_block_distance(END_LOCATION_3)
        self.assertEqual(distance, FINAL_DISTANCE_3)

        distance = calculate_block_distance(END_LOCATION_4)
        self.assertEqual(distance, FINAL_DISTANCE_4)

        distance = calculate_block_distance(END_LOCATION_5)
        self.assertEqual(distance, FINAL_DISTANCE_5)

    def test_calculate_final_location(self):
        final_coordinates = get_final_coordinates(JOURNEY_1)
        self.assertEqual(final_coordinates, END_LOCATION_1)

        final_coordinates = get_final_coordinates(JOURNEY_2)
        self.assertEqual(final_coordinates, END_LOCATION_2)

        final_coordinates = get_final_coordinates(JOURNEY_3)
        self.assertEqual(final_coordinates, END_LOCATION_3)

        final_coordinates = get_final_coordinates(JOURNEY_4)
        self.assertEqual(final_coordinates, END_LOCATION_4)

        final_coordinates = get_final_coordinates(JOURNEY_5)
        self.assertEqual(final_coordinates, END_LOCATION_5)

    def test_calculate_actual_location(self):
        actual_coordinates = get_actual_bunny_hq_coordinates(JOURNEY_4)
        self.assertEqual(actual_coordinates, ACTUAL_END_LOCATION_4)

        actual_coordinates = get_actual_bunny_hq_coordinates(JOURNEY_5)
        self.assertEqual(actual_coordinates, ACTUAL_END_LOCATION_5)
