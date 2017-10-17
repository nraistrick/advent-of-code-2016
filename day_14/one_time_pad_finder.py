from common.common import get_md5_hash, get_sliding_window_snapshots


def get_hash(salt, number):
    """
    :type salt: str
    :type number: int
    :rtype: str

    >>> get_hash("abc", 18) #doctest: +ELLIPSIS
    '...cc38887a5...'
    >>> get_hash("abc", 39) #doctest: +ELLIPSIS
    '...eee...'
    >>> get_hash("abc", 816) #doctest: +ELLIPSIS
    '...eeeee...'
    >>> get_hash("abc", 92) #doctest: +ELLIPSIS
    '...999...'
    >>> get_hash("abc", 200) #doctest: +ELLIPSIS
    '...99999...'
    """
    return get_md5_hash("%s%s" % (salt, str(number)))


def find_first_repeating_hex_digit(sequence, repetitions, digit=None):
    """
    :type sequence: str
    :type repetitions: int
    :param str digit: A specific character to look for
    :rtype: str

    >>> find_first_repeating_hex_digit("aaa", 3)
    'a'
    >>> find_first_repeating_hex_digit("abbbc", 3)
    'b'
    >>> find_first_repeating_hex_digit("bbbaaa", 3)
    'b'
    >>> find_first_repeating_hex_digit("bbbaaa", 3, 'a')
    'a'
    >>> find_first_repeating_hex_digit("abcde", 3)
    >>> find_first_repeating_hex_digit("yyy", 3)
    """
    hex_digits = "0123456789abcdef"

    if digit:
        assert digit in hex_digits

    digits = hex_digits if not digit else digit

    for chunk in get_sliding_window_snapshots(sequence, repetitions):
        for d in digits:
            if d * repetitions in chunk:
                return d

    return None


def get_one_time_pad_values(salt, count):
    """
    :type salt: str
    :type count: int
    :rtype list[(str, int)]

    >>> values = get_one_time_pad_values("abc", 2)
    >>> values[0]
    ('347dac6ee8eeea4652c7476d0f97bee5', 39)
    >>> values[1]
    ('ae2e85dd75d63e916a525df95e999ea0', 92)
    """
    i = 0
    values = []
    while len(values) != count:
        hash_value = get_hash(salt, i)
        digit = find_first_repeating_hex_digit(hash_value, 3)

        if digit:
            for j in xrange(i + 1, i + 1001):
                if find_first_repeating_hex_digit(get_hash(salt, j), 5, digit):
                    values.append((hash_value, i))
                    break

        i += 1

    return values
