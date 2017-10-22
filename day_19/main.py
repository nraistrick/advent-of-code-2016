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
    """
    elves = range(1, number_of_elves + 1)

    current = 0

    while len(elves) > 1:

        # The elf to remove is the opposite one in the circle
        opposite_elf_index = (current + (len(elves) / 2)) % len(elves)
        if opposite_elf_index < current:
            current -= 1

        # Eliminate the opposite elf from the game
        del elves[opposite_elf_index]

        # Let the next elf have a turn
        current += 1
        current %= len(elves)

    return elves[0]


def main():
    elf = calculate_elf_with_all_presents(3018458)
    print "The elf with all the presents is %d" % elf


if __name__ == '__main__':
    main()
