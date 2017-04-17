class Output(list):
    """
    A marked output bin which holds microchips
    """
    MAX_MICROCHIPS = 2

    def __iadd__(self, microchips):
        """
        :type microchips: list[int]
        """
        self.extend(microchips)
        return self

    def append(self, microchip):
        """
        :type microchip: int
        """
        if len(self) == self.MAX_MICROCHIPS:
            raise MicrochipLimitExceeded(self.MAX_MICROCHIPS)
        super(Output, self).append(microchip)

    def extend(self, microchips):
        """
        :type microchips: list[int]
        """
        updated_microchips = list(self)
        updated_microchips.extend(microchips)
        if len(updated_microchips) > self.MAX_MICROCHIPS:
            raise MicrochipLimitExceeded(self.MAX_MICROCHIPS)
        super(Output, self).extend(microchips)


class MicrochipLimitExceeded(Exception):
    def __init__(self, microchip_limit):
        """
        :type microchip_limit: int
        """
        error = "Can't hold more than %d microchip(s)" % microchip_limit
        super(MicrochipLimitExceeded, self).__init__(error)
