import operator
from common.common import count_characters, get_file_lines


def get_columns(file_path):
    """
    Get the columns from a square block of text

    :type: file_path: str
    :rtype: list
    """
    file_lines = get_file_lines(file_path)

    columns = list(next(file_lines))
    for line in file_lines:
        characters = list(line)
        for index, char in enumerate(characters):
            columns[index] += char

    return columns


def sort_characters(characters, most_common_first=True):
    """
    Sorts a dictionary of characters by number of occurrences

    :param dict characters: A dictionary of characters against count
    :param bool most_common_first: Order the dictionary by most common
    character first
    :rtype: dict
    """
    return sorted(characters.items(),
                  key=operator.itemgetter(1),
                  reverse=most_common_first)


def get_most_common_character(characters):
    """
    :type characters: list
    :rtype: str
    """
    character_count = count_characters(characters)
    sorted_characters = sort_characters(character_count)

    return sorted_characters[0][0]


def get_least_common_character(characters):
    """
    :type characters: list
    :rtype: str
    """
    character_count = count_characters(characters)
    sorted_characters = sort_characters(character_count, False)

    return sorted_characters[0][0]


def recover_original_text(file_path, most_common=True):
    """
    :type file_path: str
    :param bool most_common: Whether to use the most or least common character
    :rtype: str
    """
    if most_common is True:
        decoding_algorithm = get_most_common_character
    else:
        decoding_algorithm = get_least_common_character

    characters = [decoding_algorithm(characters)
                  for characters in get_columns(file_path)]

    return "".join(characters)


def main():
    file_path = "input/scrambled_input.txt"

    print "The original message was: %s" % \
          recover_original_text(file_path)
    print "The actual original message was: %s" % \
          recover_original_text(file_path, False)


if __name__ == '__main__':
    main()
