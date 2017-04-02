import operator
from common.common import count_characters


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
