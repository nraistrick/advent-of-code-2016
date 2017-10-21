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
    3
    >>> calculate_elf_with_all_presents(6)
    5
    >>> calculate_elf_with_all_presents(7)
    7
    >>> calculate_elf_with_all_presents(8)
    1
    """
    elves = range(1, number_of_elves + 1)

    current = 0

    # We only want the one remaining elf
    while len(elves) > 1:

        remaining_elves = []

        # Eliminate every other elf from the game
        while current < len(elves):
            remaining_elves.append(elves[current])
            current += 2

        # Point to correct starting elf for the next round and repeat
        current %= len(elves)
        elves = remaining_elves

    return elves[0]


def main():
    elf = calculate_elf_with_all_presents(3018458)
    print "The elf with all the presents is %d" % elf


if __name__ == '__main__':
    main()
