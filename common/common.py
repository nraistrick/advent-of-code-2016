"""
Shared functionality for advent of code
"""
import hashlib
from itertools import izip_longest


def get_file_lines(file_path):
    """
    :type file_path: str
    :return:
    """
    with open(file_path, "r") as instructions:
        for line in instructions:
            yield line.strip('\n')


def grouper(iterable, chunk_size, fill_value=None):
    """
    Chunks an iterable into a series of tuples

    :type iterable: collections.Iterable
    :type chunk_size: int
    :param fill_value: The default object to insert to pad an empty group
    :rtype: list[tuple]
    """
    args = [iter(iterable)] * chunk_size
    return izip_longest(*args, fillvalue=fill_value)


def count_characters(input_text):
    """
    Creates sum totals of all characters from an input

    :type input_text: collections.Iterable
    :rtype: dict
    """
    counts = {}
    for character in input_text:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1

    return counts


def rotate_character(character, rotations):
    """
    Rotate a alphabetic character forward a number of times. Each rotation
    moves the character to the next one in the alphabet
    e.g. a -> b, b -> c, z -> a

    :param str character: A single letter from a-z
    :param int rotations: The number of times to rotate the character by
    :rtype: str
    """
    # Ensure we're working in lower case for consistent ASCII values
    character = character.lower()

    current_character_value = ord(character)
    for _ in range(rotations):
        current_character_value += 1
        if current_character_value > ord('z'):
            current_character_value = ord('a')

    return chr(current_character_value)


def get_md5_hash(text):
    """
    Gets the MD5 hash value for an input string

    :param str text: The input string
    :return: The MD5 hash
    :rtype: str
    """
    return hashlib.md5(text).hexdigest()


def get_sliding_window_snapshots(string, window_size=4, slide_step_size=1):
    """
    Generates a series of substring values based off a sliding-window mechanism
    operating on a larger string

    :param str string: The string to slide over
    :param int window_size: The size of the window to snapshot
    :param int slide_step_size: The number of steps to take between window snapshots
    :return:
    """
    for i in xrange(0, len(string) - window_size + 1, slide_step_size):
        yield string[i: i + window_size]


def is_palindrome(text):
    """
    :type text: str
    :rtype: bool
    """
    return text == text[::-1]
