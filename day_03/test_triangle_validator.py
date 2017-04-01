import unittest
from unittest import TestCase

from mock import Mock, patch

from day_03.day_3 import \
    count_valid_triangles, \
    is_valid_triangle, \
    parse_triangle_data


class TestTriangleValidator(TestCase):
    def test_parse_triangle_data(self):
        data = ["1 2 3", "4 5 6", "7 8 9"]
        with patch('common.common.open') as mock_open:
            mock_open.return_value.__enter__ = mock_open
            mock_open.return_value.__iter__ = Mock(return_value=iter(data))
            lines = [line for line in parse_triangle_data("not_real.txt")]
            self.assertEqual(lines, [(1, 2, 3), (4, 5, 6), (7, 8, 9)])

    def test_is_not_valid_triangle(self):
        self.assertFalse(is_valid_triangle(5, 10, 25))
        self.assertFalse(is_valid_triangle(1, 4, 1))
        self.assertFalse(is_valid_triangle(5, 2, 3))

    def test_is_valid_triangle(self):
        self.assertTrue(is_valid_triangle(2, 3, 2))
        self.assertTrue(is_valid_triangle(70, 40, 50))
        self.assertTrue(is_valid_triangle(9, 9, 9))

    def test_incompatible_triangle_data(self):
        with self.assertRaises(ValueError):
            is_valid_triangle("a", "b", "c")

    def test_count_valid_triangles(self):
        data = [(1, 4, 1), (2, 3, 2), (3, 3, 3)]
        valid_triangles = count_valid_triangles(data)
        self.assertEqual(valid_triangles, 2)


if __name__ == '__main__':
    unittest.main()
