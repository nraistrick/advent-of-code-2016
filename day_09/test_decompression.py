import unittest
from day_09.day_9 import decompress


class TestDecompression(unittest.TestCase):
    def test_decompressing_string(self):
        self.assertEqual("ADVENT", decompress("ADVENT"))
        self.assertEqual("ABBBBBC", decompress("A(1x5)BC"))
        self.assertEqual("XYZXYZXYZ", decompress("(3x3)XYZ"))
        self.assertEqual("ABCBCDEFEFG", decompress("A(2x2)BCD(2x2)EFG"))
        self.assertEqual("(1x3)A", decompress("(6x1)(1x3)A"))
        self.assertEqual("X(3x3)ABC(3x3)ABCY", decompress("X(8x2)(3x3)ABCY"))


if __name__ == '__main__':
    unittest.main()
