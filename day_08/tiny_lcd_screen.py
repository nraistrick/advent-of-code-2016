class TinyLCDScreen(object):
    """
    Models the behaviour of a small LCD screen

    [c][r] ---------> (column)
      |
      |
      |
      |
      V
    (row)
    """
    PIXEL_OFF = 0
    PIXEL_ON = 1

    CREATE_RECTANGLE = "rect"
    ROTATE = "rotate"
    ROW = "row"
    COLUMN = "column"

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.screen = [[self.PIXEL_OFF] * self.width for _ in range(self.height)]

    def execute_instruction(self, instruction):
        """
        Executes the provided command on the screen

        :type instruction: str
        """
        line = instruction.split(" ")
        if line[0] == self.CREATE_RECTANGLE:
            width, height = line[1].split("x")
            self.create_rectangle(int(height), int(width))

        elif line[0] == self.ROTATE:
            pixels = int(line[4])
            index = int(line[2].split("=")[1])

            if line[1] == self.ROW:
                self.rotate_row(index, pixels)
            elif line[1] == self.COLUMN:
                self.rotate_column(index, pixels)

    def display(self):
        """
        Prints the LCD display
        """
        for row in xrange(len(self.screen)):
            for column in xrange(len(self.screen[row])):
                character = self.screen[row][column]
                if character == self.PIXEL_ON:
                    print character,
                else:
                    print " ",
            print ""

    def create_rectangle(self, height, width):
        """
        Creates a rectangle in the top-left corner of the screen

        :type height: int
        :type width: int
        """
        for i in xrange(height):
            for j in xrange(width):
                self.screen[i][j] = self.PIXEL_ON

    def rotate_column(self, column, pixels):
        """
        Rotates a column by a certain number of pixels

        :type column: int
        :type pixels: int
        """
        for i in xrange(pixels):
            column_snapshot = [self.screen[i][column] for i in xrange(self.height)]
            for j in xrange(self.height):
                try:
                    self.screen[j + 1][column] = column_snapshot[j]
                except IndexError:
                    self.screen[0][column] = column_snapshot[j]

    def rotate_row(self, row, pixels):
        """
        Rotates a row by a certain number of pixels

        :type row: int
        :type pixels: int
        """
        for _ in xrange(pixels):
            row_snapshot = self.screen[row][:]
            for j in xrange(self.width):
                try:
                    self.screen[row][j + 1] = row_snapshot[j]
                except IndexError:
                    self.screen[row][0] = row_snapshot[j]

    @property
    def on_pixel_count(self):
        """
        :rtype: int
        """
        pixel_count = 0
        for row in self.screen:
            pixel_count += row.count(self.PIXEL_ON)

        return pixel_count
