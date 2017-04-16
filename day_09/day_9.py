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


def main():
    for line in get_file_lines("input.txt"):
        decompressed = decompress(line)
        print decompressed
        print "The length of the decompressed output is: %d" % len(decompressed)


if __name__ == '__main__':
    main()
