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
