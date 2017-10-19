"""
Creates a set of randomised data and its corresponding checksum to overwrite
existing data on a disk.
"""


def add_random_data(current_data):
    """
    Takes some data and extends it with some additional random data.

    :type current_data: str
    :return: The input data with the additional random data appended
    :rtype: str

    >>> add_random_data("1")
    '100'
    >>> add_random_data("0")
    '001'
    >>> add_random_data("11111")
    '11111000000'
    >>> add_random_data("111100001010")
    '1111000010100101011110000'
    """
    reversed_data = current_data[::-1]
    inverted_bits = "".join(["0" if b == "1" else "1" for b in reversed_data])
    return "%s0%s" % (current_data, inverted_bits)


def calculate_checksum(data):
    """
    :type data: str

    >>> calculate_checksum("110010110100")
    '100'
    >>> calculate_checksum("10000011110010000111")
    '01100'
    """
    checksum = ""
    for i in range(0, len(data), 2):
        pair = data[i:i+2]
        checksum += "1" if pair[0] == pair[1] else "0"

    if len(checksum) % 2 == 0:
        checksum = calculate_checksum(checksum)

    return checksum


def create_disk_data(initial_state, length):
    """
    :type initial_state: str
    :type length: int
    :return: Randomised data of the correct length
    :rtype: str

    >>> create_disk_data("10000", 20)
    '10000011110010000111'
    """
    data = initial_state
    while len(data) < length:
        data = add_random_data(data)

    return data[:length]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
