"""
Decompresses a character sequence that has been compressed with
some experimental format
"""

import re
from common.common import consume, get_file_lines

COMPRESSION_MARKER = '('
NUMBER_OF_CHARACTERS = "number_of_characters"
REPETITIONS = "repetitions"
DECOMPRESSION_PATTERN = "[(](?P<%s>[0-9]+)x(?P<%s>[0-9]+)[)]" \
                        % (NUMBER_OF_CHARACTERS, REPETITIONS)


def decompress(text):
    """
    Decompresses a string based on v1 of a decompression algorithm

    :type text: str
    :return: The decompressed string
    :rtype str
    """
    index_adjustment = 0

    decompression_matches = iter(re.finditer(DECOMPRESSION_PATTERN, text))
    for match in decompression_matches:
        # We need to adjust index for previously decompressed characters
        index = match.end() + index_adjustment

        # Get next decompression match
        match_length = len(match.group(0))
        number_of_characters = int(match.group(NUMBER_OF_CHARACTERS))
        repetitions = int(match.group(REPETITIONS))

        # Decompress the data
        characters_to_repeat = text[index:index + number_of_characters]
        decompressed_characters = characters_to_repeat * (repetitions - 1)

        # Skip matches within the data field of the current decompression marker
        matches_to_ignore = text[index:index + number_of_characters].count(COMPRESSION_MARKER)
        consume(decompression_matches, matches_to_ignore)

        # Insert decompressed data
        text = text[:index - match_length] + decompressed_characters + text[index:]
        index_adjustment += len(decompressed_characters) - match_length

    return text


def decompress_v2_length(string):
    """
    Get the total length of a string decompressed with the algorithm V2

    :param str string: A compressed string
    :return: The total length
    :rtype: int
    """
    return len(string) + decompress_v2_length_increase(string)


def decompress_v2_length_increase(text):
    """
    Recursively calculates the difference in length between the original and
    decompressed string using V2 of the decompression algorithm. The difference
    with V2 of the algorithm is that we now recursively decompress data.

    We don't store the output string as it would require multiple GBs of memory.

    :param str text: The compressed data
    :return: The difference in size between the original and decompressed string
    :rtype: int
    """
    size_change = 0

    decompression_matches = iter(re.finditer(DECOMPRESSION_PATTERN, text))
    for match in decompression_matches:
        index = match.end()

        # Get next decompression match
        match_length = len(match.group(0))
        number_of_characters = int(match.group(NUMBER_OF_CHARACTERS))
        repetitions = int(match.group(REPETITIONS))

        characters_to_repeat = text[index:index + number_of_characters]
        substring = characters_to_repeat * repetitions
        added_characters = len(characters_to_repeat) * (repetitions - 1)
        size_change += added_characters - match_length

        # Recursively decompress matches within the data field of the current decompression marker
        recursive_matches = text[index:index + number_of_characters].count(COMPRESSION_MARKER)

        if recursive_matches:
            consume(decompression_matches, recursive_matches)
            size_change += decompress_v2_length_increase(substring)

    return size_change


def main():
    for line in get_file_lines("input.txt"):
        decompressed = decompress(line)
        decompressed_v2_length = decompress_v2_length(line)
        print decompressed
        print "The length of the decompressed output is: %d" % len(decompressed)
        print "The length of the v2 decompressed output is : %d" % decompressed_v2_length


if __name__ == '__main__':
    main()
