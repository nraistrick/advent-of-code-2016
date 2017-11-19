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
    STARTING_KEY = "5"

    LAYOUT = (("1", "2", "3"),
              ("4", "5", "6"),
              ("7", "8", "9"))

    def __init__(self, row, column):
        """
        :param int row: The row to point to
        :param int column: The column to point to
        """
        self.row = row
        self.column = column
        self.move_in_direction = {"U": self.move_up,
                                  "D": self.move_down,
                                  "L": self.move_left,
                                  "R": self.move_right}
        self.max_row = len(self.LAYOUT) - 1
        self.max_column = len(self.LAYOUT[0]) - 1
        self.min_row = self.min_column = 0

    def move_up(self):
        self.row = self.decrement(self.row, self.min_row)

    def move_down(self):
        self.row = self.increment(self.row, self.max_row)

    def move_left(self):
        self.column = self.decrement(self.column, self.min_column)

    def move_right(self):
        self.column = self.increment(self.column, self.max_column)

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
        return self.LAYOUT[self.row][self.column]

    def move(self, direction):
        """
        Points to a new key on the keypad
        :param str direction: U, D, L or R
        """
        self.move_in_direction[direction]()
