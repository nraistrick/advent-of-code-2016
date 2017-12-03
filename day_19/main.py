"""
For a large group of elves misunderstanding a 'White Elephant' party game,
calculate the elf left with all the remaining presents.
"""


def calculate_elf_with_all_presents(number_of_elves):
    """
    :type number_of_elves: int
    :rtype: int

    >>> calculate_elf_with_all_presents(2)
    1
    >>> calculate_elf_with_all_presents(3)
    3
    >>> calculate_elf_with_all_presents(4)
    1
    >>> calculate_elf_with_all_presents(5)
    2
    >>> calculate_elf_with_all_presents(6)
    3
    >>> calculate_elf_with_all_presents(7)
    5
    >>> calculate_elf_with_all_presents(8)
    7
    >>> calculate_elf_with_all_presents(9)
    9
    >>> calculate_elf_with_all_presents(10)
    1
    >>> calculate_elf_with_all_presents(11)
    2
    >>> calculate_elf_with_all_presents(12)
    3
    >>> calculate_elf_with_all_presents(13)
    4
    >>> calculate_elf_with_all_presents(14)
    5
    >>> calculate_elf_with_all_presents(15)
    6
    >>> calculate_elf_with_all_presents(16)
    7
    >>> calculate_elf_with_all_presents(17)
    8
    >>> calculate_elf_with_all_presents(18)
    9
    >>> calculate_elf_with_all_presents(19)
    11
    >>> calculate_elf_with_all_presents(20)
    13
    >>> calculate_elf_with_all_presents(21)
    15
    >>> calculate_elf_with_all_presents(22)
    17
    >>> calculate_elf_with_all_presents(23)
    19
    >>> calculate_elf_with_all_presents(24)
    21
    >>> calculate_elf_with_all_presents(25)
    23
    >>> calculate_elf_with_all_presents(26)
    25
    >>> calculate_elf_with_all_presents(27)
    27
    >>> calculate_elf_with_all_presents(28)
    1
    >>> calculate_elf_with_all_presents(29)
    2
    >>> calculate_elf_with_all_presents(30)
    3
    >>> calculate_elf_with_all_presents(31)
    4
    >>> calculate_elf_with_all_presents(32)
    5
    >>> calculate_elf_with_all_presents(33)
    6
    >>> calculate_elf_with_all_presents(34)
    7
    >>> calculate_elf_with_all_presents(35)
    8
    >>> calculate_elf_with_all_presents(36)
    9
    >>> calculate_elf_with_all_presents(37)
    10
    >>> calculate_elf_with_all_presents(38)
    11
    >>> calculate_elf_with_all_presents(39)
    12
    >>> calculate_elf_with_all_presents(40)
    13
    >>> calculate_elf_with_all_presents(41)
    14
    >>> calculate_elf_with_all_presents(42)
    15
    >>> calculate_elf_with_all_presents(43)
    16
    >>> calculate_elf_with_all_presents(44)
    17
    >>> calculate_elf_with_all_presents(45)
    18
    >>> calculate_elf_with_all_presents(46)
    19
    >>> calculate_elf_with_all_presents(47)
    20
    >>> calculate_elf_with_all_presents(48)
    21
    >>> calculate_elf_with_all_presents(49)
    22
    >>> calculate_elf_with_all_presents(50)
    23
    >>> calculate_elf_with_all_presents(51)
    24
    >>> calculate_elf_with_all_presents(52)
    25
    >>> calculate_elf_with_all_presents(53)
    26
    >>> calculate_elf_with_all_presents(54)
    27
    >>> calculate_elf_with_all_presents(55)
    29
    >>> calculate_elf_with_all_presents(56)
    31
    >>> calculate_elf_with_all_presents(57)
    33
    """
    elves = range(1, number_of_elves + 1)

    current = 0  # The index of the current elf
    removed = 0  # The number of elves removed during a single loop
    skipped = 0  # The number of eliminated elves we jump over in a single loop

    while len(elves) > 1:

        # A tracker to help us point correctly to the opposite elf
        index_adjustment = removed - skipped

        # The elf to remove is the opposite one in the circle
        opposite_elf_index = (current + index_adjustment + (number_of_elves / 2)) % len(elves)

        # Eliminate the opposite elf from the game
        elves[opposite_elf_index] = None
        number_of_elves -= 1
        removed += 1

        # Let the next elf have a turn
        current += 1

        # Skip over any eliminated elves
        while current < len(elves) and not elves[current]:
            current += 1
            skipped += 1

        # When we get back to the start of the circle,
        # clean up all eliminated elves and reset
        if current >= len(elves):
            current, removed, skipped = 0, 0, 0
            elves = [e for e in elves if e]

    return elves[0]


def main():
    elf = calculate_elf_with_all_presents(3018458)
    print "The elf with all the presents is %d" % elf


if __name__ == '__main__':
    main()
