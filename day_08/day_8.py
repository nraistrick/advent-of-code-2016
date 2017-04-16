"""
Creates a printed message by lighting up pixels on a tiny LCD display
"""

from common.common import get_file_lines
from day_08.tiny_lcd_screen import TinyLCDScreen


def main():
    screen = TinyLCDScreen(6, 50)
    for line in get_file_lines("input.txt"):
        screen.execute_instruction(line)

    screen.display()
    print "The number of pixels turned on is: %d" % screen.on_pixel_count


if __name__ == '__main__':
    main()
