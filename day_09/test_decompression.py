import unittest
from day_09.day_9 import decompress, decompress_v2_length


class TestDecompression(unittest.TestCase):
    def test_decompressing_string(self):
        self.assertEqual("ADVENT", decompress("ADVENT"))
        self.assertEqual("ABBBBBC", decompress("A(1x5)BC"))
        self.assertEqual("XYZXYZXYZ", decompress("(3x3)XYZ"))
        self.assertEqual("ABCBCDEFEFG", decompress("A(2x2)BCD(2x2)EFG"))
        self.assertEqual("(1x3)A", decompress("(6x1)(1x3)A"))
        self.assertEqual("X(3x3)ABC(3x3)ABCY", decompress("X(8x2)(3x3)ABCY"))

    def test_get_decompressed_v2_length(self):
        compressed = "X(8x2)(3x3)ABCY"
        length = decompress_v2_length(compressed)
        self.assertEqual(length, len("XABCABCABCABCABCABCY"))

        compressed = "(27x12)(20x12)(13x14)(7x10)(1x12)A"
        length = decompress_v2_length(compressed)
        self.assertEqual(length, 241920)

        compressed = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
        length = decompress_v2_length(compressed)
        self.assertEqual(length, 445)


if __name__ == '__main__':
    unittest.main()
