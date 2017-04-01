"""
Calculates the number of valid triangles from a list of data containing
three side lengths
"""

from common.common import get_file_lines, grouper


def parse_triangle_data(file_path):
    """
    :type file_path: str
    :return: A collection of triangle side lengths
    :rtype: list[(int, int, int)]
    """
    triangles = []
    for line in get_file_lines(file_path):
        side_1, side_2, side_3 = filter(None, line.split(' '))
        triangle_data = int(side_1), int(side_2), int(side_3)
        triangles.append(triangle_data)

    return triangles


def get_vertical_triangle_data(file_path):
    """
    Read in triangle data from a file

    :param str file_path: Path to the file
    :return: A list of triangle data
    :rtype: list(tuple)
    """
    triangles = []

    triangle_column_0 = []
    triangle_column_1 = []
    triangle_column_2 = []

    with open(file_path, "r") as triangle_data:
        for triangle_line in triangle_data:
            line_data = filter(None, triangle_line.strip('\n').split(' '))
            triangle_column_0.append(int(line_data[0]))
            triangle_column_1.append(int(line_data[1]))
            triangle_column_2.append(int(line_data[2]))

        serial_triangle_values = triangle_column_0 + triangle_column_1 + triangle_column_2
        for group_data in grouper(serial_triangle_values, 3):
            triangles.append(group_data)

    return triangles


def count_valid_triangles(triangle_data):
    """
    :type triangle_data: list[(int, int, int)]
    :rtype: int
    """
    valid_triangle_counter = 0
    for triangle in triangle_data:
        if is_valid_triangle(triangle[0], triangle[1], triangle[2]):
            valid_triangle_counter += 1

    return valid_triangle_counter


def is_valid_triangle(first_side_length, second_side_length, third_side_length):
    """
    :type first_side_length: int
    :type second_side_length: int
    :type third_side_length: int
    :rtype: bool
    """
    # Confirm we have valid ints for the lengths of the triangle sides
    first_side_length = int(first_side_length)
    second_side_length = int(second_side_length)
    third_side_length = int(third_side_length)

    if first_side_length + second_side_length <= third_side_length:
        return False

    if first_side_length + third_side_length <= second_side_length:
        return False

    if second_side_length + third_side_length <= first_side_length:
        return False

    return True


def main():
    input_file_path = "input/triangle_data.txt"

    triangle_data = parse_triangle_data(input_file_path)
    print "Number of horizontal triangles %s" % count_valid_triangles(triangle_data)

    triangle_data = get_vertical_triangle_data(input_file_path)
    print "Number of vertical triangles %s" % count_valid_triangles(triangle_data)


if __name__ == '__main__':
    main()
