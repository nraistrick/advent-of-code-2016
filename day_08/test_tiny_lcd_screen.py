import unittest
from day_08.tiny_lcd_screen import TinyLCDScreen


class TestTinyLcdScreen(unittest.TestCase):
    def test_initialise_empty_screen(self):
        self.assertEqual(TinyLCDScreen(1, 2).screen, [[0, 0]])
        self.assertEqual(TinyLCDScreen(2, 2).screen, [[0, 0],
                                                      [0, 0]])
        self.assertEqual(TinyLCDScreen(3, 3).screen, [[0, 0, 0],
                                                      [0, 0, 0],
                                                      [0, 0, 0]])

    def test_create_rectangle(self):
        display = TinyLCDScreen(2, 2)
        display.create_rectangle(1, 2)
        self.assertEqual(display.screen, [[1, 1], [0, 0]])

        display = TinyLCDScreen(2, 2)
        display.create_rectangle(2, 1)
        self.assertEqual(display.screen, [[1, 0], [1, 0]])

        display = TinyLCDScreen(2, 2)
        display.create_rectangle(2, 2)
        self.assertEqual(display.screen, [[1, 1], [1, 1]])

    def test_rotate_column(self):
        display = TinyLCDScreen(2, 1)
        display.screen[0][0] = 1
        self.assertEqual(display.screen, [[1],
                                          [0]])
        display.rotate_column(0, 1)
        self.assertEqual(display.screen, [[0],
                                          [1]])
        display.rotate_column(0, 1)
        self.assertEqual(display.screen, [[1],
                                          [0]])
        display.rotate_column(0, 2)
        self.assertEqual(display.screen, [[1],
                                          [0]])
        display.rotate_column(0, 3)
        self.assertEqual(display.screen, [[0],
                                          [1]])

    def test_rotate_row(self):
        display = TinyLCDScreen(1, 2)
        display.screen[0][0] = 1
        self.assertEqual(display.screen, [[1, 0]])

        display.rotate_row(0, 1)
        self.assertEqual(display.screen, [[0, 1]])

        display.rotate_row(0, 1)
        self.assertEqual(display.screen, [[1, 0]])

        display.rotate_row(0, 2)
        self.assertEqual(display.screen, [[1, 0]])

        display.rotate_row(0, 3)
        self.assertEqual(display.screen, [[0, 1]])

    def test_on_pixel_count(self):
        display = TinyLCDScreen(3, 3)
        self.assertEqual(display.on_pixel_count, 0)

        display.screen[0][0] = 1
        display.screen[1][1] = 1
        self.assertEqual(display.on_pixel_count, 2)

        display.screen[0][2] = 1
        display.screen[2][2] = 1
        self.assertEqual(display.on_pixel_count, 4)

    def test_call_instruction(self):
        display = TinyLCDScreen(3, 7)
        display.execute_instruction("rect 3x2")
        self.assertEqual(display.screen, [[1, 1, 1, 0, 0, 0, 0],
                                          [1, 1, 1, 0, 0, 0, 0],
                                          [0, 0, 0, 0, 0, 0, 0]])

        display.execute_instruction("rotate column x=1 by 1")
        self.assertEqual(display.screen, [[1, 0, 1, 0, 0, 0, 0],
                                          [1, 1, 1, 0, 0, 0, 0],
                                          [0, 1, 0, 0, 0, 0, 0]])

        display.execute_instruction("rotate row y=0 by 4")
        self.assertEqual(display.screen, [[0, 0, 0, 0, 1, 0, 1],
                                          [1, 1, 1, 0, 0, 0, 0],
                                          [0, 1, 0, 0, 0, 0, 0]])

        display.execute_instruction("rotate column x=1 by 1")
        self.assertEqual(display.screen, [[0, 1, 0, 0, 1, 0, 1],
                                          [1, 0, 1, 0, 0, 0, 0],
                                          [0, 1, 0, 0, 0, 0, 0]])


if __name__ == '__main__':
    unittest.main()
