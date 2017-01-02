"""
Using a long series of instructions, calculates the final distance
from a bunny HQ from an origin (0, 0) starting point.
"""
from day_01.coordinate_map import CoordinateMap

INPUT = "R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, " \
        "L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, " \
        "R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, " \
        "L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, " \
        "R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, " \
        "L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, " \
        "L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, " \
        "R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, " \
        "R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, " \
        "L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, " \
        "R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, " \
        "R1, R5, R3"


def get_actual_bunny_hq_coordinates(directions):
    """
    Follows the specified directions until we visit the same coordinates twice.
    This is where the actual bunny HQ is.

    :param str directions: A long stream of instructions
    :return: Final (x, y) coordinates
    :rtype: tuple[int, int]
    """
    visited_locations = set()

    coordinate_map = CoordinateMap()
    for coordinates in get_next_coordinates(coordinate_map, directions):
        if coordinates in visited_locations:
            return coordinates
        visited_locations.add(coordinates)


def get_final_coordinates(directions):
    """
    Calculate final location coordinates for bunny HQ

    :param str directions: A long stream of instructions
    :return: Final (x, y) coordinates
    :rtype: tuple[int, int]
    """
    coordinate_map = CoordinateMap()
    coordinates = None
    for coordinates in get_next_coordinates(coordinate_map, directions):
        pass

    return coordinates


def get_next_coordinates(coordinate_map, directions):
    """
    :type coordinate_map: CoordinateMap
    :type directions: str
    :rtype: tuple
    """
    change_direction = {"L": coordinate_map.turn_left,
                        "R": coordinate_map.turn_right}

    for direction, steps in get_next_movement(directions):
        change_direction[direction]()
        for _ in xrange(steps):
            coordinate_map.step_forward()
            yield tuple(coordinate_map.coordinates)


def get_next_movement(directions):
    """
    Generates a list of instructions from an input.
    Each instruction consists of two parts:
    * Whether to turn left or right
    * The number of steps to move

    :param str directions: The directions to follow
    :rtype: tuple(str, int)
    """
    for d in directions.split(", "):
        left_or_right = d[0]
        distance_to_move = int(d[1:])
        yield (left_or_right, distance_to_move)


def calculate_block_distance(coordinates):
    """
    Calculates the distance from origin (0, 0) to the provided coordinates

    :type coordinates: tuple[int, int]
    :rtype: int
    """
    return abs(coordinates[0]) + abs(coordinates[1])


def main():
    final_coordinates = get_final_coordinates(INPUT)
    print "Final Coordinates: %s" % str(final_coordinates)

    distance_from_bunny_hq = calculate_block_distance(final_coordinates)
    print "Block distance from origin: %s" % str(distance_from_bunny_hq)

    actual_hq_coordinates = get_actual_bunny_hq_coordinates(INPUT)
    print "Actual HQ Coordinates: %s" % str(final_coordinates)

    distance_from_bunny_hq = calculate_block_distance(actual_hq_coordinates)
    print "Block distance from origin: %s" % str(distance_from_bunny_hq)


if __name__ == '__main__':
    main()
