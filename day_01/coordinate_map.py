class CoordinateMap(object):
    """
    Represents a user moving around a two-dimensional coordinate map

            ^ y
            |
            |
            |
    ----- (0,0) -----> x
            |
            |
            |
    """
    NORTH, EAST, SOUTH, WEST = "N", "E", "S", "W"

    TURN_LEFT_LOOKUP = {NORTH: WEST, EAST: NORTH, SOUTH: EAST, WEST: SOUTH}
    TURN_RIGHT_LOOKUP = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}

    MOVE_LOOKUP = {NORTH: lambda x, y: (x, y + 1),
                   SOUTH: lambda x, y: (x, y-1),
                   EAST: lambda x, y: (x+1, y),
                   WEST: lambda x, y: (x-1, y)}

    def __init__(self):
        self.coordinates = (0, 0)
        self.direction = self.NORTH

    def turn_left(self):
        self.direction = self.TURN_LEFT_LOOKUP[self.direction]

    def turn_right(self):
        self.direction = self.TURN_RIGHT_LOOKUP[self.direction]

    def step_forward(self):
        move = self.MOVE_LOOKUP[self.direction]
        self.coordinates = move(*self.coordinates)
