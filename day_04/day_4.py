"""
Finds information regarding north pole objects using a collection of
room identifiers
"""

import operator
from common.common import count_characters, get_file_lines, rotate_character


def get_encrypted_room_name(room_identifier):
    """
    Extract a room name from a full room string such as:
    "aaaaa-bbb-z-y-x-123[abxyz]"

    :param str room_identifier: The raw room data
    :rtype: str
    """
    room_name_end_position = room_identifier.rfind("-")
    if room_name_end_position == -1:
        raise ValueError("Couldn't find room name in: %s" % room_identifier)

    return room_identifier[:room_name_end_position]


def get_sector_id(room_identifier):
    """
    :param str room_identifier: The raw room data
    :rtype: int
    """
    start_position = room_identifier.rfind("-")
    if start_position == -1:
        raise ValueError("Couldn't find sector ID in: %s" % room_identifier)
    end_position = room_identifier.index("[")

    return int(room_identifier[start_position+1:end_position])


def get_hash_value(room_identifier):
    """
    :param str room_identifier: The raw room data
    :rtype: str
    """
    start_position = room_identifier.index("[")
    return room_identifier[start_position+1:-1]


def calculate_room_hash_value(room_identifier):
    """
    :type room_identifier: str
    :rtype: str
    """
    counts = count_characters(room_identifier.replace("-", ""))
    alphabetically_sorted = sorted(counts.items(),
                                   key=operator.itemgetter(0))
    most_common_characters = sorted(alphabetically_sorted,
                                    key=operator.itemgetter(1),
                                    reverse=True)

    return ''.join(c[0] for c in most_common_characters[:5])


def validate_room_name(room_identifier):
    """
    :type room_identifier: str
    :rtype: bool
    """
    room_name = get_encrypted_room_name(room_identifier)
    expected_hash_value = calculate_room_hash_value(room_name)
    hash_value = get_hash_value(room_identifier)

    return True if expected_hash_value == hash_value else False


def calculate_sector_id_sum(file_path):
    """
    :type file_path: str
    :rtype: int
    """
    sector_id_sum = 0
    for room_string in get_file_lines(file_path):
        if validate_room_name(room_string):
            sector_id_sum += get_sector_id(room_string)

    return sector_id_sum


def decrypt_room_name(encrypted_name, sector_id):
    """
    :param str encrypted_name: The encrypted room name
    :param int sector_id: The sector ID of the room
    :rtype: str
    """
    decrypted_name = ""
    for character in encrypted_name:
        if character == '-':
            decrypted_name += " "
        else:
            decrypted_name += rotate_character(character, sector_id)

    return decrypted_name


def get_north_pole_room(file_path):
    """
    Finds a decrypted room name that contains the north pole objects

    :param file_path: The path to the raw data
    :return: The decrypted room name and sector ID
    :rtype: (str, int)
    """
    for room_string in get_file_lines(file_path):
        if not validate_room_name(room_string):
            continue

        encrypted_room_name = get_encrypted_room_name(room_string)
        sector_id = get_sector_id(room_string)
        room_name = decrypt_room_name(encrypted_room_name, sector_id)
        if "pole" in room_name:
            return room_name, get_sector_id(room_string)


def main():
    """
    Sum all valid sector IDs then find the location of the north pole objects
    """
    input_file = "input/raw_room_data.txt"

    print "Sum of valid sector IDs: %d" % calculate_sector_id_sum(input_file)
    print "North pole objects are stored at: %s %d" % get_north_pole_room(input_file)


if __name__ == "__main__":
    main()
