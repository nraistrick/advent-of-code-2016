"""
Calculates the walls and open spaces on a map to find the shortest
allowable route between two locations.

e.g.
                x
  (x,y) --------------->
    | S o o # . . . . .
    | . . o # # . . E .
    | . . o o # . . o .
    | . . . o # . . o .
    | . . . o o o o o .
    | . . . . . . . . .
  y v

"""
from common.common import is_even

FREE_SPACE_MARKER = "."
WALL_MARKER = "#"
LOCATION_VISITED_MARKER = "o"


def create_coordinate_map(columns, rows):
    """
    :type columns: int
    :type rows: int
    :rtype: list[list[int]]
    """
    return [[calculate_coordinate_value(x, y) for x in range(columns)] for y in range(rows)]


def calculate_coordinate_value(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return x*x + 3*x + 2*x*y + y + y*y


def add_number(coordinate_map, number):
    """
    :type coordinate_map: list[list[int]]
    :type number: int
    :rtype: list[list[int]]
    """
    return [[x + number for x in y] for y in coordinate_map]


def get_binary_counts(coordinate_map):
    """
    Counts the number of 1s in the binary representation of each number

    :type coordinate_map: list[list[int]]
    :rtype coordinate_map: list[list[int]]
    :rtype: list[list[int]]
    """
    return [[bin(x).count("1") for x in y] for y in coordinate_map]


def create_wall_map(coordinate_map):
    """
    :type coordinate_map: list[list[int]]
    :rtype: list[list[str]]
    """
    return [[FREE_SPACE_MARKER if is_even(x) else WALL_MARKER for x in y]
            for y in coordinate_map]


def print_map(coordinate_map, spacing=2):
    """
    :type coordinate_map: list[list]
    :type spacing: int
    """
    print('\n'.join([''.join([('{:%d}' % spacing).format(x) for x in y])
                     for y in coordinate_map]))
    print


def visit_maze_location(coordinate_map, start=(1, 1)):
    """
    Generates all available locations in a maze using a breadth-first search

    :type coordinate_map: list[list[str]]
    :type start: (int, int)
    :return: (x, y) coordinates and the number of moves to get to that location
    :rtype: ((int, int), int)
    """
    x, y = start
    max_bottom_edge_coordinate = len(coordinate_map) - 1
    max_right_edge_coordinate = len(coordinate_map[y]) - 1

    locations = [(x, y, 0)]
    while locations:
        x, y, move_count = locations.pop(0)

        # Check we're within maze boundaries
        if x < 0 or x > max_right_edge_coordinate or \
           y < 0 or y > max_bottom_edge_coordinate:
            continue

        # Check this location is an unvisited empty-space
        if coordinate_map[y][x] != FREE_SPACE_MARKER:
            continue

        coordinate_map[y][x] = LOCATION_VISITED_MARKER

        # Add future locations to try visit
        locations += [(x + 1, y, move_count + 1),  # Right
                      (x, y + 1, move_count + 1),  # Down
                      (x - 1, y, move_count + 1),  # Left
                      (x, y - 1, move_count + 1)]  # Up

        yield (x, y), move_count


def find_shortest_route(coordinate_map, end):
    """
    Finds the shortest route through a maze using a breadth-first search

    :type coordinate_map: list[list[str]]
    :param (int, int) end: (x, y)
    """
    for coordinates, move_count in visit_maze_location(coordinate_map):
        if coordinates == end:
            return move_count


def main():
    designers_favourite_number = 1352
    end_coordinates = (31, 39)

    coordinate_map = create_coordinate_map(50, 50)
    favourite_number_added_map = add_number(coordinate_map, designers_favourite_number)
    binary_count_map = get_binary_counts(favourite_number_added_map)
    wall_map = create_wall_map(binary_count_map)

    move_count = find_shortest_route(wall_map, end_coordinates)

    print_map(wall_map)
    print "Solution found in %d steps" % move_count


if __name__ == '__main__':
    main()
