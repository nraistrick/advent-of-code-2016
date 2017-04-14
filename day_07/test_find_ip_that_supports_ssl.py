import unittest
from day_07.day_7 import check_ip_supports_ssl, find_all_aba


class TestFindIPThatSupportsSSL(unittest.TestCase):
    ip_1 = "aba[bab]xyz"
    ip_1_supports_ssl = True

    ip_2 = "xyx[xyx]xyx"
    ip_2_supports_ssl = False

    ip_3 = "aaa[kek]eke"
    ip_3_supports_ssl = True

    ip_4 = "zazbz[bzb]cdb"
    ip_4_supports_ssl = True

    def test_find_all_aba(self):
        self.assertEqual(find_all_aba("aba", "b", "a"), ['aba'])
        self.assertEqual(find_all_aba("abakek", "b", "a"), ['aba'])
        self.assertEqual(find_all_aba("xyx", "z", "x"), [])

    def test_ip_supports_ssl(self):
        """
        Checks if an IPv7 address supports ssl
        """
        self.assertEqual(self.ip_1_supports_ssl, check_ip_supports_ssl(self.ip_1))
        self.assertEqual(self.ip_2_supports_ssl, check_ip_supports_ssl(self.ip_2))
        self.assertEqual(self.ip_3_supports_ssl, check_ip_supports_ssl(self.ip_3))
        self.assertEqual(self.ip_4_supports_ssl, check_ip_supports_ssl(self.ip_4))


if __name__ == '__main__':
    unittest.main()
