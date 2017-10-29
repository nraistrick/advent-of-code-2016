"""
Beginning at 0, find the route with the fewest number of steps for a cleaning
robot to visit all available numbers on a map.

e.g. Where '#' is a wall

 ---------------> x
|
|   ###########
|   #0.1.....2#
|   #.#######.#
|   #4.......3#
|   ###########
v
y

"""
from collections import namedtuple
from itertools import permutations
from common.common import get_file_lines

OPEN = "."
WALL = "#"

Move = namedtuple('Move', 'x y steps')


def get_start_location(robot_map):
    """
    :type robot_map: list[list[str]]
    :rtype: int, int
    """
    for x, column in enumerate(robot_map):
        for y, location in enumerate(column):
            if location == '0':
                return x, y


def get_all_location_numbers(robot_map):
    """
    :type robot_map: list[list[str]]
    :rtype: list[str]

    >>> robot_map = create_indexed_map(['1.3',
    ...                                 '#0.',
    ...                                 '.2.'])
    >>> get_all_location_numbers(robot_map)
    ['0', '1', '2', '3']
    """
    numbers = []
    for x, column in enumerate(robot_map):
        for y, location in enumerate(column):
            if location.isdigit():
                numbers.append(location)

    return sorted(numbers)


def create_indexed_map(lines):
    """
    Creates a map with locations that can be accessed with indexes i.e. map[x][y]

    :type lines: list[str]
    :rtype: list[list[str]]

    >>> robot_map = create_indexed_map(['1.',
    ...                                 '#0'])
    >>> robot_map[0][0] == '1'
    True
    >>> robot_map[1][0] == OPEN
    True
    >>> robot_map[0][1] == WALL
    True
    >>> robot_map[1][1] == '0'
    True
    """
    robot_map = [[] for _ in lines[0]]
    for line in lines:
        for x, character in enumerate(line):
            robot_map[x].append(character)

    return robot_map


def available_moves(x, y, robot_map):
    """
    :type x: int
    :type y: int
    :type robot_map: list[list[str]]
    :rtype: list[(int, int)]

    >>> robot_map = create_indexed_map(['1..',
    ...                                 '#0.',
    ...                                 '...'])
    >>> available_moves(0, 0, robot_map)
    [(1, 0)]
    >>> available_moves(1, 0, robot_map)
    [(1, 1), (0, 0), (2, 0)]
    >>> available_moves(1, 1, robot_map)
    [(1, 0), (1, 2), (2, 1)]
    >>> available_moves(2, 2, robot_map)
    [(2, 1), (1, 2)]
    """
    moves = []

    if y > 0 and robot_map[x][y - 1] != WALL:
        moves.append((x, y - 1))  # Down

    if y < len(robot_map[0]) - 1 and robot_map[x][y + 1] != WALL:
        moves.append((x, y + 1))  # Up

    if x > 0 and robot_map[x - 1][y] != WALL:
        moves.append((x - 1, y))  # Left

    if x < len(robot_map) - 1 and robot_map[x + 1][y] != WALL:
        moves.append((x + 1, y))  # Right

    return moves


def find_shortest_path_to_number(coordinates, robot_map, number=None):
    """
    Finds the shortest path to the next number in a map using a
    breadth-first search

    :type coordinates: (int, int)
    :type robot_map: list[list[str]]
    :type number: str
    :rtype: Move

    >>> robot_map = create_indexed_map(['...',
    ...                                 '##.',
    ...                                 '1..'])
    >>> find_shortest_path_to_number((0, 0), robot_map)
    Move(x=0, y=2, steps=6)
    """
    visited = []
    locations = [Move(coordinates[0], coordinates[1], 0)]
    while locations:
        move = locations.pop(0)
        x, y, steps = move.x, move.y, move.steps

        if steps != 0:
            if robot_map[x][y].isdigit() and not number:
                return move

            elif robot_map[x][y] == number:
                return move

        if (x, y) in visited:
            continue

        visited.append((x, y))

        steps += 1
        for x, y in available_moves(x, y, robot_map):
            if (x, y) not in visited:
                locations.append(Move(x, y, steps))


def moves_to_visit_each_number(robot_map):
    """
     :type robot_map: list[list[str]]
     :rtype: int
     """
    x, y = get_start_location(robot_map)
    move = find_shortest_path_to_number((x, y), robot_map)

    steps = 0
    while move:
        steps += move.steps
        x, y = move.x, move.y

        # Set the number to an empty space so we don't revisit it again
        robot_map[x][y] = OPEN

        move = find_shortest_path_to_number((x, y), robot_map)

    return steps


def get_shortest_round_trip(robot_map):
    """
    :type robot_map: list[list[str]]
    :rtype: int
    """
    available_numbers = get_all_location_numbers(robot_map)
    move_cache = {number: {} for number in available_numbers}
    available_numbers.remove('0')

    start = get_start_location(robot_map)

    fewest_steps = None
    for locations in permutations(available_numbers):

        # Add return location
        locations += '0',

        x, y = start
        steps = 0

        for i, number in enumerate(locations):

            # Calculate the distance between two numbers if not already cached
            last_number = locations[i - 1]
            if number not in move_cache[last_number]:
                move = find_shortest_path_to_number((x, y), robot_map, number)
                move_cache[last_number][number] = move

            move = move_cache[last_number][number]
            steps += move.steps

            if fewest_steps and steps > fewest_steps:
                break

            if i == len(locations) - 1:
                fewest_steps = steps

            x, y = move.x, move.y

    return fewest_steps


def main():
    lines = [line for line in get_file_lines("input/input.txt")]
    robot_map = create_indexed_map(lines)
    move_count = get_shortest_round_trip(robot_map)

    print "Move count is: %d" % move_count


if __name__ == '__main__':
    main()
