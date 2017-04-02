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
