"""
Using a given set of instructions, figure out what the PIN is for a
bathroom door keypad
"""

from common.common import get_file_lines
from day_02.keypad import Keypad


def get_list_of_steps(file_name):
    """
    Reads the steps to follow to get the PIN into a list

    :param file_name:
    :return: A list of steps for each digit
    :rtype: list
    """
    steps_for_each_digit = []
    for line in get_file_lines(file_name):
        steps_for_each_digit.append(line)

    return steps_for_each_digit


def create_pin(keypad, steps_for_each_digit):
    """
    Generates the PIN for a keypad based off a list of steps

    :param Keypad keypad: An instance of a keypad object
    :param list(str) steps_for_each_digit: A list of steps to follow
    :return: The generated PIN number
    :rtype: str
    """
    pin = []
    for one_digit_steps in steps_for_each_digit:
        for step in one_digit_steps:
            keypad.move(step)
        pin.append(keypad.key)

    return "".join(pin)


def follow_instructions(file_name):
    """
    Using the instructions, find the PIN code for the toilet on the basic keypad

    :param str file_name: The file name to get the instructions from
    :return: The resulting PIN
    :rtype: str
    """
    keypad = Keypad(1, 1, Keypad.LAYOUT)
    steps_for_each_digit = get_list_of_steps(file_name)
    pin = create_pin(keypad, steps_for_each_digit)

    return pin


def follow_complex_instructions(file_name):
    """
    Using the instructions, find the PIN code for the toilet on the complex keypad

    :param str file_name: The file name to get the instructions from
    :return: The resulting PIN
    :rtype: str
    """
    keypad = Keypad(2, 0, Keypad.COMPLEX_LAYOUT)
    steps_for_each_digit = get_list_of_steps(file_name)
    pin = create_pin(keypad, steps_for_each_digit)

    return pin


def main():
    pin = follow_instructions("input/actual_instructions.txt")
    print "Toilet door PIN: %s" % pin

    pin = follow_complex_instructions("input/actual_instructions.txt")
    print "Complex toilet door PIN: %s" % pin


if __name__ == '__main__':
    main()
