"""
Generates the required password for a door based on a given input
"""

import itertools
from common.common import get_md5_hash

DOOR_INPUT = "wtnhxymk"
PASSWORD_LENGTH = 8
HEXADECIMAL_BASE = 16


def password_hash_values(door_id):
    """
    Generates a list of valid hashes for password values

    :type door_id: str
    :return: A hash representing the door ID appended with an incrementing integer
    :rtype: str
    """
    password_hash_identifier = "00000"

    for i in itertools.count():
        value_to_hash = "%s%s" % (door_id, str(i))
        hash_value = get_md5_hash(value_to_hash)

        if hash_value.startswith(password_hash_identifier):
            # Not a hash value of interest
            yield hash_value


def calculate_password(door_id):
    """
    Calculate the basic password

    :param door_id: The door ID
    :return: The password
    :rtype: str
    """
    index_of_password_character = 5

    password_store = [""] * PASSWORD_LENGTH
    for hash_value in password_hash_values(door_id):
        character = hash_value[index_of_password_character]
        password_store[password_store.index("")] = character

        if "" not in password_store:
            # If we have all the characters
            break

    # There should be only characters in the password store
    return "".join(password_store)


def calculate_advanced_password(door_id):
    """
    Calculate the advanced password

    :param door_id: The door ID
    :return: The password
    :rtype: str
    """
    password_store = [""] * PASSWORD_LENGTH
    for hash_value in password_hash_values(door_id):
        character_position = int(hash_value[5], HEXADECIMAL_BASE)
        if character_position >= PASSWORD_LENGTH:
            # Character position doesn't fit within password length limits
            continue

        if password_store[character_position]:
            # We only use the first character found for each position
            continue

        password_store[character_position] = hash_value[6]
        if "" not in password_store:
            # If we have all the characters
            break

    # There should be only characters in the password store
    return "".join(password_store)


def main():
    print "The simple password is: %s" % calculate_password(DOOR_INPUT)
    print "The advanced password is %s" % calculate_advanced_password(DOOR_INPUT)


if __name__ == "__main__":
    main()
