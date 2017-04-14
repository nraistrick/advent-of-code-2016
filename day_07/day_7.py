"""
Counts how many IPv7 IP addresses support certain protocols by validating
them against a provided set of rules.
"""

from common.common import \
    get_file_lines, \
    get_sliding_window_snapshots, \
    is_palindrome


def check_ip_supports_tls(ipv7_address):
    """
    An IP supports TLS if the following criteria are satisfied:
    * One ABBA is found outside of square brackets
    * No ABBA is found within square brackets

    :param str ipv7_address: An IPv7 IP address
    :rtype: bool
    """
    inside_bracket, outside_bracket = split_ip_address(ipv7_address)

    if any(find_abba(content) for content in inside_bracket):
        return False

    if any(find_abba(content) for content in outside_bracket):
        return True

    return False


def find_abba(input_text):
    """
    For a given input string, search for an ABBA (Autonomous Bridge Bypass Annotation).
    This is a palindromic sequence of four characters i.e. it contains a pair
    of two unique characters, followed by the reverse of that pair.

    e.g. ABBA, OXXO, YZZY

    :type input_text: str
    :return: The ABBA string
    :rtype: str
    """
    for snapshot in get_sliding_window_snapshots(input_text, 4):
        if is_palindrome(snapshot) and snapshot[0] != snapshot[1]:
            return snapshot


def check_ip_supports_ssl(ipv7_address):
    """
    Looks for an ABA (Area-Broadcast Accessor) outside square brackets
    and a BAB (Byte Allocation Block) inside square brackets.

    An ABA is a palindromic sequence of three characters for which has
    different first and second characters.
    e.g. aba, xyx, rtr

    A BAB is the same as an ABA, but with the characters reversed.
    e.g. aba -> bab, xyx -> yxy, rtr -> trt

    :type ipv7_address: str
    :rtype: bool
    """
    inside_bracket, outside_bracket = split_ip_address(ipv7_address)

    possible_aba_strings = []
    for string in outside_bracket:
        possible_aba_strings += find_all_aba(string)

    bab_characters = [(aba_string[0], aba_string[1])
                      for aba_string in possible_aba_strings]

    for string in inside_bracket:
        for inner, outer in bab_characters:
            if any(find_all_aba(string, inner, outer)):
                return True

    return False


def find_all_aba(input_text,
                 inner_character=None,
                 outer_character=None):
    """
    Looks for three-character strings that are symmetrical e.g. ABA, BAB, XYX

    :type inner_character: str
    :type outer_character: str
    :param str input_text: The input string of arbitrary length
    :return: A list of matching strings
    :rtype: list[str]
    """
    strings = []
    for section in get_sliding_window_snapshots(input_text, 3):
        if not is_palindrome(section):
            continue

        if outer_character and section[0] != outer_character:
            continue

        if inner_character and section[1] != inner_character:
            continue

        strings.append(section)

    return strings


def split_ip_address(ipv7_address):
    """
    We expect a string containing characters inside and outside of enclosing
    square brackets. We can process the content more easily if we split
    up the string into two character sets:

    1) Characters within square brackets.
    2) Characters outside of square brackets

    :type ipv7_address: str
    :return: The string content inside and outside of brackets respectively
    :rtype: (list[str], list[str])
    """
    # Splits the IP by the closing bracket and then splits each section into
    # two by opening bracket. This results in a list of string pairs where the
    # first elements are inside brackets and the second elements are outside
    # brackets
    split_ip = filter(None, [_.split('[') for _ in ipv7_address.split(']')])

    inside_bracket_content = []
    outside_bracket_content = []

    for section in split_ip:
        outside_bracket_content.append(section[0])
        if len(section) == 2:
            inside_bracket_content.append(section[1])

    return inside_bracket_content, outside_bracket_content


def main():
    input_file_path = "input.txt"

    tls_ips = [ip for ip in get_file_lines(input_file_path) if check_ip_supports_tls(ip)]
    print "The number of IPs that support TLS is: %s" % len(tls_ips)

    ssl_ips = [ip for ip in get_file_lines(input_file_path) if check_ip_supports_ssl(ip)]
    print "The number of IPs that support SSL is: %s" % len(ssl_ips)


if __name__ == '__main__':
    main()
