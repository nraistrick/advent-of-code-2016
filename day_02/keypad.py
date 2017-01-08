class Keypad(object):
    """
    (0, 0) ---------> (column)
      |
      |
      |
      |
      V
    (row)
    """
    INVALID_KEY = "0"
    STARTING_KEY = "5"

    LAYOUT = (("1", "2", "3"),
              ("4", "5", "6"),
              ("7", "8", "9"))

    COMPLEX_LAYOUT = (("0", "0", "1", "0", "0"),
                      ("0", "2", "3", "4", "0"),
                      ("5", "6", "7", "8", "9"),
                      ("0", "A", "B", "C", "0"),
                      ("0", "0", "D", "0", "0"))

    def __init__(self, layout):
        """
        :param str layout: The layout of the keypad
        """
        self.move_in_direction = {"U": self.move_up,
                                  "D": self.move_down,
                                  "L": self.move_left,
                                  "R": self.move_right}
        self.layout = layout
        self.max_row = len(self.layout) - 1
        self.max_column = len(self.layout[0]) - 1
        self.row, self.column = self.starting_coordinates()

    def check_valid_button(self, row, column):
        """
        Checks if there is a button on the current coordinate.

        :param int row: The row in the matrix
        :param int column: The column in the matrix
        :return: If the coordinate pair match a valid button
        :rtype: bool
        """
        if self.layout[row][column] != Keypad.INVALID_KEY:
            return True
        return False

    def move_up(self):
        value = self.decrement(self.row, 0)
        if self.check_valid_button(value, self.column):
            self.row = value

    def move_down(self):
        value = self.increment(self.row, self.max_row)
        if self.check_valid_button(value, self.column):
            self.row = value

    def move_left(self):
        value = self.decrement(self.column, 0)
        if self.check_valid_button(self.row, value):
            self.column = value

    def move_right(self):
        value = self.increment(self.column, self.max_column)
        if self.check_valid_button(self.row, value):
            self.column = value

    @staticmethod
    def decrement(value, minimum=0, step=1):
        """
        Decrease a value by an amount unless it falls below a minimum limit.

        :param int step: The amount to decrease the value by
        :param int minimum: A limit on how small the value can be
        :param int value: The initial value
        :return: The decreased value
        :rtype: int
        """
        if value > minimum:
            value -= step
        return value

    @staticmethod
    def increment(value, maximum, step=1):
        """
        Increase a value by an amount unless it exceeds a maximum limit.

        :param int step: The amount to decrease the value by
        :param int maximum: A limit on how small the value can be
        :param int value: The initial value
        :return: The increased value
        :rtype: int
        """
        if value < maximum:
            value += step
        return value

    @property
    def key(self):
        """
        :return: The value of the currently selected key
        :rtype: str
        """
        return self.layout[self.row][self.column]

    def starting_coordinates(self, value=STARTING_KEY):
        """
        Find the coordinates of the starting key.

        :param str value: The value of the starting key
        :return: Starting key coordinates
        :rtype: tuple(int, int)
        """
        for row in xrange(self.max_row + 1):
            for column in xrange(self.max_column + 1):
                if self.layout[row][column] == value:
                    return row, column

    def move(self, direction):
        """
        Points to a new key on the keypad
        :param str direction: U, D, L or R
        """
        self.move_in_direction[direction]()
