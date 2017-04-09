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


def get_most_common_character(characters):
    """
    :type characters: list
    :rtype: str
    """
    character_count = count_characters(characters)
    sorted_characters = sorted(character_count.items(),
                               key=operator.itemgetter(1),
                               reverse=True)

    return sorted_characters[0][0]


def recover_original_text(file_path):
    characters = [get_most_common_character(characters)
                  for characters in get_columns(file_path)]
    return "".join(characters)


def main():
    file_path = "input/scrambled_input.txt"
    print "The original message was: %s" % recover_original_text(file_path)


if __name__ == '__main__':
    main()
