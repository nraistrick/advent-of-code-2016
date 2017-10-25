"""
Based off a given file input and a list of instructions, generate a scrambled
password.
"""

from common.common import get_file_lines


def reverse(text, from_index, to_index):
    """
    :type text: str
    :type from_index: int
    :type to_index: int
    :rtype: str

    >>> reverse("ab", 0, 1)
    'ba'
    >>> reverse("abc", 0, 1)
    'bac'
    >>> reverse("abcde", 0, 4)
    'edcba'
    >>> reverse("abcde", 1, 3)
    'adcbe'
    >>> reverse("abcde", 0, 5)
    'edcba'
    >>> reverse("abcdefgh", 5, 7)
    'abcdehgf'
    """
    split = list(text)
    reversed_list = split[from_index:to_index + 1][::-1]
    split[from_index:to_index + 1] = reversed_list
    return ''.join(split)


def move(text, from_index, to_index):
    """
    :type text: str
    :type from_index: int
    :type to_index: int
    :rtype: str

    >>> move("ab", 0, 1)
    'ba'
    >>> move("ba", 1, 0)
    'ab'
    >>> move("abc", 0, 1)
    'bac'
    >>> move("abc", 1, 2)
    'acb'
    >>> move("bcdea", 1, 4)
    'bdeac'
    >>> move("abcdefgh", 2, 7)
    'abdefghc'
    >>> move("abcdefgh", 7, 2)
    'abhcdefg'
    """
    split = list(text)
    letter_to_move = split[from_index]
    del split[from_index]
    split.insert(to_index, letter_to_move)
    return ''.join(split)


def rotate_left(text, count):
    """
    :type text: str
    :type count: int
    :rtype: str

    >>> rotate_left("ab", 1)
    'ba'
    >>> rotate_left("ab", 2)
    'ab'
    >>> rotate_left("abcd", 1)
    'bcda'
    >>> rotate_left("abcd", 3)
    'dabc'
    >>> rotate_left("abcd", 9)
    'bcda'
    >>> rotate_left("abcdefgh", 4)
    'efghabcd'
    """
    if count != 0:
        text = rotate_left(text[1:] + text[:1], count - 1)

    return text


def rotate_right(text, count):
    """
    :type text: str
    :type count: int
    :rtype: str

    >>> rotate_right("ab", 1)
    'ba'
    >>> rotate_right("ab", 2)
    'ab'
    >>> rotate_right("abcd", 1)
    'dabc'
    >>> rotate_right("abcd", 3)
    'bcda'
    >>> rotate_right("abcd", 9)
    'dabc'
    >>> rotate_right("abcdefgh", 4)
    'efghabcd'
    """
    if count != 0:
        text = rotate_right(text[-1:] + text[:-1], count - 1)

    return text


def rotate_based_on_letter(text, letter):
    """
    Get the index of the provided letter, add one to it, and add an additional
    one if the index is at least four. Then perform that number of right
    rotations on the text.

    :type text: str
    :type letter: str
    :rtype: str

    >>> rotate_based_on_letter("abdec", "b")
    'ecabd'
    >>> rotate_based_on_letter("ecabd", "d")
    'decab'
    >>> rotate_based_on_letter("abcdefgh", "d")
    'efghabcd'
    >>> rotate_based_on_letter("abcdefgh", "f")
    'bcdefgha'
    """
    rotations = text.index(letter)
    if rotations >= 4:
        rotations += 1
    rotations += 1
    return rotate_right(text, rotations)


def swap_indexes(text, index_one, index_two):
    """
    :type text: str
    :type index_one: int
    :param index_two: int
    :rtype str

    >>> swap_indexes("ab", 0, 1)
    'ba'
    >>> swap_indexes("ab", 1, 0)
    'ba'
    >>> swap_indexes("abcde", 0, 4)
    'ebcda'
    """
    split = list(text)
    split[index_one], split[index_two] = split[index_two], split[index_one]
    return ''.join(split)


def swap_letters(text, first_letter, second_letter):
    """
    :type text: str
    :type first_letter: str
    :param second_letter: str
    :rtype str

    >>> swap_letters("ab", "a", "b")
    'ba'
    >>> swap_letters("ba", "b", "a")
    'ab'
    >>> swap_letters("abc", "a", "c")
    'cba'
    >>> swap_letters("abcde", "d", "b")
    'adcbe'
    """
    split = list(text)
    return swap_indexes(text, split.index(first_letter), split.index(second_letter))


def generate_scrambled_password(text, instructions):
    """
    :type text: str
    :type instructions: list[str]
    :rtype: str

    >>> generate_scrambled_password("abcde", ["swap position 4 with position 0"])
    'ebcda'
    >>> generate_scrambled_password("ebcda", ["swap letter d with letter b"])
    'edcba'
    >>> generate_scrambled_password("edcba", ["reverse positions 0 through 4"])
    'abcde'
    >>> generate_scrambled_password("abcde", ["rotate left 1 step"])
    'bcdea'
    >>> generate_scrambled_password("bcdea", ["move position 1 to position 4"])
    'bdeac'
    >>> generate_scrambled_password("ecabd", ["rotate based on position of letter d"])
    'decab'
    >>> generate_scrambled_password("abcde", ["rotate right 2 step"])
    'deabc'
    >>> generate_scrambled_password("abcde", ["invalid"]) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ValueError: Got unexpected command: 'invalid'
    """
    for i in instructions:
        split_command = i.split(" ")
        command = split_command[0]

        if command == "swap":
            if split_command[1] == "position":
                text = swap_indexes(text, int(split_command[2]), int(split_command[5]))
            elif split_command[1] == "letter":
                text = swap_letters(text, split_command[2], split_command[5])

        elif command == "reverse":
            text = reverse(text, int(split_command[2]), int(split_command[4]))

        elif command == "rotate":
            if split_command[1] == "based":
                text = rotate_based_on_letter(text, split_command[6])
            elif split_command[1] == "left":
                text = rotate_left(text, int(split_command[2]))
            elif split_command[1] == "right":
                text = rotate_right(text, int(split_command[2]))

        elif command == "move":
            text = move(text, int(split_command[2]), int(split_command[5]))

        else:
            raise ValueError("Got unexpected command: '%s'" % command)

    return text


def main():
    test_instructions = [line for line in get_file_lines("input/testinput.txt")]
    scrambled_password = generate_scrambled_password("abcde", test_instructions)
    print "The test scrambled password is: %s" % scrambled_password

    instructions = [line for line in get_file_lines("input/input.txt")]
    scrambled_password = generate_scrambled_password("abcdefgh", instructions)
    print "The scrambled password is: %s" % scrambled_password


if __name__ == '__main__':
    main()
