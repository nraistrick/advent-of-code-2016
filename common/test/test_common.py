import unittest
from mock import Mock, patch

from common.common import get_file_lines


class CommonTester(unittest.TestCase):
    def test_reading_file_lines(self):
        data = ["abc", "def", "hij"]

        with patch('common.common.open') as mock_open:
            mock_open.return_value.__enter__ = mock_open
            mock_open.return_value.__iter__ = Mock(return_value=iter(data))
            lines = [line for line in get_file_lines("not_real.txt")]
            self.assertEqual(lines, data)


if __name__ == '__main__':
    unittest.main()
