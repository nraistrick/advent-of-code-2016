import unittest
from mock import Mock, patch

from common.common import get_file_lines, grouper, count_characters, \
    rotate_character, get_md5_hash, get_sliding_window_snapshots, \
    is_palindrome, consume, is_even


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

    def test_sliding_window(self):
        snapshots = [s for s in get_sliding_window_snapshots("abc", 1, 1)]
        self.assertEqual(snapshots, ['a', 'b', 'c'])

        snapshots = [s for s in get_sliding_window_snapshots("abcd", 2, 1)]
        self.assertEqual(snapshots, ['ab', 'bc', 'cd'])

        snapshots = [s for s in get_sliding_window_snapshots("abcdefgh", 4, 4)]
        self.assertEqual(snapshots, ['abcd', 'efgh'])

        snapshots = [s for s in get_sliding_window_snapshots("abcdef", 1, 2)]
        self.assertEqual(snapshots, ['a', 'c', 'e'])

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("aba"))
        self.assertTrue(is_palindrome("aaaa"))
        self.assertTrue(is_palindrome("rotor"))

        self.assertFalse(is_palindrome("ab"))
        self.assertFalse(is_palindrome("cost"))
        self.assertFalse(is_palindrome("snowman"))

    def test_consume(self):
        iterator = iter(xrange(15))
        self.assertEqual(next(iterator), 0)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)

        consume(iterator, 1)
        self.assertEqual(next(iterator), 4)

        consume(iterator, 2)
        self.assertEqual(next(iterator), 7)

        consume(iterator, 4)
        self.assertEqual(next(iterator), 12)

        consume(iterator)
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(14))
        self.assertTrue(is_even(368))

        self.assertFalse(is_even(3))
        self.assertFalse(is_even(19))
        self.assertFalse(is_even(295))


if __name__ == '__main__':
    unittest.main()
