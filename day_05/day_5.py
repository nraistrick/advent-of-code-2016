"""
Generates the required password for a door based on a given input
"""

import itertools
from common.common import get_md5_hash

DOOR_INPUT = "wtnhxymk"
PASSWORD_LENGTH = 8


def calculate_password(door_id):
    """
    :type door_id: str
    :rtype: str
    """
    password = ""

    for i in itertools.count():
        value_to_hash = "%s%s" % (door_id, str(i))
        hash_value = get_md5_hash(value_to_hash)
        if not hash_value.startswith("00000"):
            # Not a hash value of interest
            continue

        password += hash_value[5]
        if len(password) == PASSWORD_LENGTH:
            break

    return password


def main():
    return calculate_password(DOOR_INPUT)


if __name__ == "__main__":
    print main()
