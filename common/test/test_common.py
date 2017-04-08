import unittest
from mock import Mock, patch

from common.common import get_file_lines, grouper, count_characters, \
    rotate_character, get_md5_hash


class CommonTester(unittest.TestCase):
    def test_reading_file_lines(self):
        data = ["abc", "def", "hij"]

        with patch('common.common.open') as mock_open:
            mock_open.return_value.__enter__ = mock_open
            mock_open.return_value.__iter__ = Mock(return_value=iter(data))
            lines = [line for line in get_file_lines("not_real.txt")]
            self.assertEqual(lines, data)

    def test_grouper(self):
        output = [i for i in grouper([1, 2, 3, 4], 2)]
        self.assertEqual(output, [(1, 2), (3, 4)])

        output = [i for i in grouper([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)]
        self.assertEqual(output, [(1, 2, 3), (4, 5, 6), (7, 8, 9)])

        output = [i for i in grouper([1, 2, 3], 2)]
        self.assertEqual(output, [(1, 2), (3, None)])

        output = [i for i in grouper([1, 2, 3], 2, 0)]
        self.assertEqual(output, [(1, 2), (3, 0)])

        output = [i for i in grouper([1, 2, 3], 2, "a")]
        self.assertEqual(output, [(1, 2), (3, "a")])

    def test_count_characters(self):
        self.assertEqual(count_characters("abc"), {"a": 1, "b": 1, "c": 1})
        self.assertEqual(count_characters("aba"), {"a": 2, "b": 1})
        self.assertEqual(count_characters("zzz"), {"z": 3})

    def test_rotate_character(self):
        self.assertEqual(rotate_character('a', 1), 'b')
        self.assertEqual(rotate_character('z', 1), 'a')
        self.assertEqual(rotate_character('b', 3), 'e')
        self.assertEqual(rotate_character('x', 10), 'h')
        self.assertEqual(rotate_character('c', 52), 'c')

    def test_get_md5_hash(self):
        self.assertEqual(get_md5_hash("abc"),
                         "900150983cd24fb0d6963f7d28e17f72")
        self.assertEqual(get_md5_hash("a1b2c3d4e5"),
                         "cb3bae31bb1c443fbf3db8889055f2fe")
        self.assertEqual(get_md5_hash("a very slightly longer string"),
                         "62dbba1fbe158598e7176b7a2085ba23")


if __name__ == '__main__':
    unittest.main()
