"""
Based off the first row of tiles in a room, figures out the number of safe and
unsafe tiles in a room. For example, a room with 38 safe tiles:

.^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^

Where ^ is a trap and . is a safe tile
"""

TRAP = "^"
SAFE = "."


def get_tile(left, centre, right):
    """
    Calculates a new tile based off its parents

    :type left: str
    :type centre: str
    :type right: str
    :rtype: str

    >>> get_tile(SAFE, SAFE, SAFE)
    '.'
    >>> get_tile(TRAP, SAFE, SAFE)
    '^'
    >>> get_tile(SAFE, TRAP, SAFE)
    '.'
    >>> get_tile(TRAP, TRAP, SAFE)
    '^'
    >>> get_tile(SAFE, SAFE, TRAP)
    '^'
    >>> get_tile(TRAP, SAFE, TRAP)
    '.'
    >>> get_tile(SAFE, TRAP, TRAP)
    '^'
    >>> get_tile(TRAP, TRAP, TRAP)
    '.'
    """
    combination = left, centre, right
    if (combination == (TRAP, TRAP, SAFE)) or \
            (combination == (SAFE, TRAP, TRAP)) or \
            (combination == (TRAP, SAFE, SAFE)) or \
            (combination == (SAFE, SAFE, TRAP)):
        return TRAP

    return SAFE


def get_next_row(row):
    """
    :type row: str
    :rtype: str

    >>> get_next_row("..^^.")
    '.^^^^'
    >>> get_next_row(".^^^^")
    '^^..^'
    >>> get_next_row(".^^.^.^^^^")
    '^^^...^..^'
    """
    next_row = ""
    number_of_tiles = len(row)

    for i in range(number_of_tiles):
        left = row[i - 1] if i > 0 else SAFE
        right = row[i + 1] if i < number_of_tiles - 1 else SAFE
        centre = row[i]
        next_row += get_tile(left, centre, right)

    return next_row


def count_number_of_safe_tiles(row):
    """
    :type row: str
    :rtype: int
    >>> count_number_of_safe_tiles(".^^^^")
    1
    >>> count_number_of_safe_tiles("..^^.")
    3
    >>> count_number_of_safe_tiles(".....")
    5
    """
    return row.count(SAFE)


def calculate_number_of_safe_tiles(first_row, number_of_rows):
    """
    :type first_row: str
    :type number_of_rows: int
    :rtype: int

    >>> calculate_number_of_safe_tiles(".^^.^.^^^^", 10)
    38
    """
    trap_count = 0

    row = first_row
    for _ in range(number_of_rows):
        trap_count += count_number_of_safe_tiles(row)
        row = get_next_row(row)

    return trap_count


def main():
    first_row = "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^" + \
                "^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"
    safe_tiles = calculate_number_of_safe_tiles(first_row, 400000)
    print "Number of safe tiles: %d" % safe_tiles


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
