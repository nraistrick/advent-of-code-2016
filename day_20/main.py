"""
For a given blacklist of IP ranges, find the lowest allowable IP and total IP
count which provides access through a firewall.
"""

from common.common import get_file_lines

MAX_ALLOWABLE_IP = 4294967296


def get_lowest_unblocked_ip(blacklisted_ip_ranges):
    """
    :type blacklisted_ip_ranges: list
    :rtype: int

    >>> get_lowest_unblocked_ip(["5-8", "0-2", "4-7"])
    3
    >>> get_lowest_unblocked_ip(["2-3", "0-4"])
    5
    >>> get_lowest_unblocked_ip(["0-2", "1-3"])
    4
    """
    lowest_ip = 0
    while True:
        start_lowest_ip = lowest_ip
        for ip_range in blacklisted_ip_ranges:

            lower_bound, upper_bound = [int(i) for i in ip_range.split("-")]

            # We're only interested in ranges that will change the lowest
            # available IP allowed through the firewall
            if lowest_ip < lower_bound or lowest_ip > upper_bound:
                continue

            lowest_ip = upper_bound + 1
            blacklisted_ip_ranges.remove(ip_range)

        if lowest_ip == start_lowest_ip:
            break

    return lowest_ip


def get_range(ip_rule):
    """
    :param str ip_rule: An IP range rule as defined in the blacklist
    :return A parsed IP range with the first value being the lowest IP
    and the second value being the highest IP
    :rtype: (int, int)

    >>> get_range("0-5")
    (0, 5)
    >>> get_range("5-0")
    (0, 5)
    >>> get_range("2-10")
    (2, 10)
    """
    lower, upper = sorted([int(i) for i in ip_rule.split("-")])
    return lower, upper


def create_rule(lowest_ip, highest_ip):
    """
    :type lowest_ip: int
    :type highest_ip: int
    :return: An IP range rule as defined in the blacklist
    :rtype: str

    >>> create_rule(0, 5)
    '0-5'
    >>> create_rule(2, 6)
    '2-6'
    >>> create_rule(1, 10)
    '1-10'
    """
    return "%d-%d" % (lowest_ip, highest_ip)


def check_ranges_overlap(first_range, second_range):
    """
    :param first_range: (int, int)
    :type second_range: (int, int)
    :rtype: bool

    >>> check_ranges_overlap((1, 2), (2, 3))
    True
    >>> check_ranges_overlap((1, 3), (2, 4))
    True
    >>> check_ranges_overlap((1, 2), (3, 4))
    True
    >>> check_ranges_overlap((3, 4), (1, 2))
    True
    >>> check_ranges_overlap((1, 2), (4, 5))
    False
    >>> check_ranges_overlap((4, 5), (1, 2))
    False
    """
    if first_range[0] <= second_range[1] + 1 and second_range[0] <= first_range[1] + 1:
        return True
    return False


def combine_ranges(first_range, second_range):
    """
    :type first_range: (int, int)
    :type second_range: (int, int)
    :rtype: (int, int)

    >>> combine_ranges((0, 1), (1, 2))
    (0, 2)
    >>> combine_ranges((0, 3), (1, 2))
    (0, 3)
    >>> combine_ranges((3, 4), (1, 2))
    (1, 4)
    """
    return min(first_range[0], second_range[0]), max(first_range[1], second_range[1])


def combine_blacklist_ranges(blacklisted_ip_ranges):
    """
    :type blacklisted_ip_ranges: list[str]
    :rtype: list[str]

    >>> combine_blacklist_ranges(["1-5"])
    ['1-5']
    >>> combine_blacklist_ranges(["1-5", "1-5"])
    ['1-5']
    >>> combine_blacklist_ranges(["1-5", "6-10"])
    ['1-10']
    >>> combine_blacklist_ranges(["1-3", "6-10"])
    ['1-3', '6-10']
    >>> combine_blacklist_ranges(["1-3", "4-10", "11-12"])
    ['1-12']
    >>> combine_blacklist_ranges(["11-12", "1-3", "4-10"])
    ['1-12']
    >>> combine_blacklist_ranges(["0-1", "1-3", "0-200"])
    ['0-200']
    """
    counter = 0
    while counter < len(blacklisted_ip_ranges):
        rule = blacklisted_ip_ranges[counter]
        following_rules = blacklisted_ip_ranges[counter + 1:]

        current_range = get_range(rule)

        for i, rule in enumerate(following_rules):
            other_range = get_range(rule)

            # Check if the two ranges need combining
            if not check_ranges_overlap(current_range, other_range):
                continue

            # Combine the ranges into one
            combined = combine_ranges(current_range, other_range)

            # We add the new rule to the end in case it needs combining again
            blacklisted_ip_ranges.append(create_rule(*combined))

            # Remove the original ranges
            del blacklisted_ip_ranges[counter]
            del blacklisted_ip_ranges[counter + i]

            counter -= 1
            break

        counter += 1

    return blacklisted_ip_ranges


def count_blacklisted_ips(blacklisted_ip_ranges):
    """
    :type blacklisted_ip_ranges: list
    :rtype: int

    >>> count_blacklisted_ips(["1-2"])
    2
    >>> count_blacklisted_ips(["1-2", "1-2"])
    2
    >>> count_blacklisted_ips(["1-2", "3-6"])
    6
    >>> count_blacklisted_ips(["3-15", "7-10", "1-2"])
    15
    >>> count_blacklisted_ips(["3-15", "22-25", "1-2"])
    19
    >>> count_blacklisted_ips(["9-10", "5-12", "6-8", "5-8", "3-4", "2-3", "1-2", "2-3", "1-9"])
    12
    >>> count_blacklisted_ips(['1-1000', '10000-11000'])
    2001
    >>> count_blacklisted_ips((['703998143-724929678']))
    20931536
    """
    count = 0
    for ip_range in combine_blacklist_ranges(blacklisted_ip_ranges):
        minimum, maximum = get_range(ip_range)
        count += (maximum - minimum) + 1

    return count


def main():
    blacklisted_ip_ranges = [line for line in get_file_lines("input.txt")]
    lowest_unblocked_ip = get_lowest_unblocked_ip(list(blacklisted_ip_ranges))
    print "Lowest allowable IP is: %d" % lowest_unblocked_ip

    allowable_ip_count = MAX_ALLOWABLE_IP - count_blacklisted_ips(list(blacklisted_ip_ranges))
    print "Total available IPs: %d" % allowable_ip_count


if __name__ == '__main__':
    main()
