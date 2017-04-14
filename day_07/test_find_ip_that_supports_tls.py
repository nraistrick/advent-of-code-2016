import unittest
from day_07.day_7 import split_ip_address, find_abba, check_ip_supports_tls


class TestFindIPThatSupportsTLS(unittest.TestCase):
    """
    Tests the day_7 module for finding IPv7 addresses that support TLS
    """
    ip_1 = "abba[mnop]qrst"
    ip_1_split_input = ["mnop"], ["abba", "qrst"]
    ip_1_abba_section = "abba"
    ip_1_abba = "abba"
    ip_1_supports_tls = True

    ip_2 = "ioxxoj[asdfgh]zxcvbn"
    ip_2_split_input = ["asdfgh"], ["ioxxoj", "zxcvbn"]
    ip_2_abba_section = "ioxxoj"
    ip_2_abba = "oxxo"
    ip_2_supports_tls = True

    ip_3 = "abcd[bddb]xyyx"
    ip_3_split_input = ["bddb"], ["abcd", "xyyx"]
    ip_3_abba_section = "bddb"
    ip_3_abba = "bddb"
    ip_3_supports_tls = False

    ip_4 = "aaaa[qwer]tyui"
    ip_4_split_input = ["qwer"], ["aaaa", "tyui"]
    ip_4_invalid_abba_section = "aaaa"
    ip_4_supports_tls = False

    def test_separate_input(self):
        self.assertEqual(self.ip_1_split_input, split_ip_address(self.ip_1))
        self.assertEqual(self.ip_2_split_input, split_ip_address(self.ip_2))
        self.assertEqual(self.ip_3_split_input, split_ip_address(self.ip_3))
        self.assertEqual(self.ip_4_split_input, split_ip_address(self.ip_4))

    def test_finding_abbas(self):
        self.assertEqual(self.ip_1_abba, find_abba(self.ip_1_abba_section))
        self.assertEqual(self.ip_2_abba, find_abba(self.ip_2_abba_section))
        self.assertEqual(self.ip_3_abba, find_abba(self.ip_3_abba_section))
        self.assertEqual(None, find_abba(self.ip_4_invalid_abba_section))

    def test_ip_supports_tls(self):
        self.assertEqual(self.ip_1_supports_tls, check_ip_supports_tls(self.ip_1))
        self.assertEqual(self.ip_2_supports_tls, check_ip_supports_tls(self.ip_2))
        self.assertEqual(self.ip_3_supports_tls, check_ip_supports_tls(self.ip_3))
        self.assertEqual(self.ip_4_supports_tls, check_ip_supports_tls(self.ip_4))


if __name__ == '__main__':
    unittest.main()
