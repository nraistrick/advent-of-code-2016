"""
For a given blacklist of IP ranges, find the lowest allowable IP that provides
access through a firewall
"""

from common.common import get_file_lines


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


def main():
    blacklisted_ip_ranges = [line for line in get_file_lines("input.txt")]
    lowest_unblocked_ip = get_lowest_unblocked_ip(blacklisted_ip_ranges)
    print "Lowest allowable IP is: %d" % lowest_unblocked_ip


if __name__ == '__main__':
    main()
