from day_11.floor.item_type import FloorItemType


class FloorItem(object):
    def __init__(self, element_name, item_type):
        """
        :type element_name: str
        :type item_type: FloorItemType
        """
        self.element_name = element_name
        self.type = item_type
        self._validate()

    def _validate(self):
        if not self.element_name:
            raise ValueError("An element name must be specified")

        if self.type not in FloorItemType.items():
            raise ValueError("%s must be one of the valid floor item types: %s"
                             % (self.type, FloorItemType))

    @property
    def element_id(self):
        """
        :return: The unique identifying element character
        :rtype: str
        """
        return self.element_name[0].upper()

    def __eq__(self, other):
        """
        :type other: FloorItem
        """
        if self.element_name == other.element_name and self.type == other.type:
            return True
        return False

    def __ne__(self, other):
        """
        :type other: FloorItem
        """
        return not self.__eq__(other)

    def __repr__(self):
        return "%s%s" % (self.element_id, self.type)

    def __hash__(self):
        return hash(repr(self))
