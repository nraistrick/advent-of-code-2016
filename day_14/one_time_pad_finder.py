from common.common import get_md5_hash, get_sliding_window_snapshots

# This programs runs under the assumption that the salt will
# not change mid-way through the one-time-pad key calculations
HASH_CACHE = {}


def get_hash(salt, number, key_stretch=False):
    """
    :type salt: str
    :type number: int
    :type key_stretch: bool
    :rtype: str
    """
    if number not in HASH_CACHE:
        HASH_CACHE[number] = calculate_hash(salt, number, key_stretch)

    return HASH_CACHE[number]


def calculate_hash(salt, number, key_stretch=False):
    """
    :type salt: str
    :type number: int
    :type key_stretch: bool
    :rtype: str

    >>> calculate_hash("abc", 18) #doctest: +ELLIPSIS
    '...cc38887a5...'
    >>> calculate_hash("abc", 39) #doctest: +ELLIPSIS
    '...eee...'
    >>> calculate_hash("abc", 816) #doctest: +ELLIPSIS
    '...eeeee...'
    >>> calculate_hash("abc", 92) #doctest: +ELLIPSIS
    '...999...'
    >>> calculate_hash("abc", 200) #doctest: +ELLIPSIS
    '...99999...'
    >>> calculate_hash("abc", 0, key_stretch=True) #doctest: +ELLIPSIS
    'a107ff...
    """
    hash_value = get_md5_hash("%s%s" % (salt, str(number)))
    if key_stretch:
        hash_value = key_stretch_hash(hash_value)

    return hash_value


def key_stretch_hash(value, iterations=2016):
    """
    :type value: str
    :type iterations: int
    :rtype: str

    >>> key_stretch_hash("577571be4de9dcce85a041ba0410f29f") #doctest: +ELLIPSIS
    'a107ff...
    """
    for _ in range(iterations):
        value = get_md5_hash(value)

    return value


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


def get_one_time_pad_values(salt, count, key_stretch=False):
    """
    :type salt: str
    :type count: int
    :type key_stretch: bool
    :rtype list[(str, int)]

    >>> values = get_one_time_pad_values("abc", 2)
    >>> values[0]
    ('347dac6ee8eeea4652c7476d0f97bee5', 39)
    >>> values[1]
    ('ae2e85dd75d63e916a525df95e999ea0', 92)
    """
    global HASH_CACHE
    HASH_CACHE = {}

    i = 0
    values = []
    while len(values) != count:
        hash_value = get_hash(salt, i, key_stretch)
        digit = find_first_repeating_hex_digit(hash_value, 3)

        if digit:
            for j in xrange(i + 1, i + 1001):
                if find_first_repeating_hex_digit(get_hash(salt, j, key_stretch), 5, digit):
                    values.append((hash_value, i))
                    break

        i += 1

    return values
