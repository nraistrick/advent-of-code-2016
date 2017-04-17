from output import Output


class Bot(Output):
    """
    A bot which makes decisions on where to pass microchips based on value
    """
    def __init__(self):
        super(Bot, self).__init__()
        self.low_chip_destination = None
        self.high_chip_destination = None

    def move_microchips(self):
        """
        If the bot has the maximum number of microchips,
        pass them to the appropriate container
        """
        if len(self) < self.MAX_MICROCHIPS:
            raise ValueError("Must have %d microchips to move" % self.MAX_MICROCHIPS)

        self.sort()
        self.low_chip_destination.append(self.pop(0))
        self.high_chip_destination.append(self.pop(0))
