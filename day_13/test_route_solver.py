from unittest import TestCase

from day_13.main import \
    create_coordinate_map, \
    add_number, \
    get_binary_counts, \
    create_wall_map, \
    find_shortest_route


class TestRouteSolver(TestCase):
    def test_wall_map_created_correctly(self):
        designers_favourite_number = 10
        correct_map = \
            [['.', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
             ['.', '.', '#', '.', '.', '#', '.', '.', '.', '#'],
             ['#', '.', '.', '.', '.', '#', '#', '.', '.', '.'],
             ['#', '#', '#', '.', '#', '.', '#', '#', '#', '.'],
             ['.', '#', '#', '.', '.', '#', '.', '.', '#', '.'],
             ['.', '.', '#', '#', '.', '.', '.', '.', '#', '.'],
             ['#', '.', '.', '.', '#', '#', '.', '#', '#', '#'],
             ['.', '#', '#', '.', '.', '#', '.', '#', '#', '.'],
             ['#', '.', '#', '#', '#', '.', '.', '.', '.', '#'],
             ['#', '#', '#', '.', '#', '#', '#', '#', '.', '#']]

        coordinate_map = create_coordinate_map(10, 10)
        favourite_number_added_map = add_number(coordinate_map,
                                                designers_favourite_number)
        binary_count_map = get_binary_counts(favourite_number_added_map)
        wall_map = create_wall_map(binary_count_map)
        self.assertEqual(correct_map, wall_map)

    def test_shortest_route(self):
        designers_favourite_number = 10
        target_coordinates = (7, 4)
        map_size = (10, 10)

        coordinate_map = create_coordinate_map(*map_size)
        favourite_number_added_map = add_number(coordinate_map, designers_favourite_number)
        binary_count_map = get_binary_counts(favourite_number_added_map)
        wall_map = create_wall_map(binary_count_map)

        steps_taken = find_shortest_route(wall_map, target_coordinates)
        self.assertEqual(steps_taken, 11)
