class FloorItemType(object):
    """Represents all allowable item types"""
    GENERATOR = "G"
    MICROCHIP = "M"

    @staticmethod
    def items():
        """
        :return: Floor item types
        :rtype: list[str]
        """
        return [getattr(FloorItemType, attr) for attr in dir(FloorItemType)
                if not callable(getattr(FloorItemType, attr)) and not attr.startswith("__")]
