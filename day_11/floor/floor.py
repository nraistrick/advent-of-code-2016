from day_11.floor.item import FloorItem
from day_11.floor.item_type import FloorItemType
from day_11.floor.microchip_destroyed import MicrochipDestroyed


class Floor(object):
    """Models one level of a building"""

    def __init__(self, contents=None):
        """
        :type contents set[FloorItem]
        """
        if contents is None:
            contents = set()

        for item in contents:
            assert isinstance(item, FloorItem)

        self.contents = contents
        self._check_safe()

    def _check_safe(self):
        """Validate the floor"""
        def check_if_microchips_destroyed():
            generator_elements = set()
            microchip_elements = set()
            for i in self.contents:
                if i.type == FloorItemType.GENERATOR:
                    generator_elements.add(i.element_id)
                else:
                    microchip_elements.add(i.element_id)

            destroyed_microchip_ids = microchip_elements - generator_elements
            if generator_elements and destroyed_microchip_ids:
                raise MicrochipDestroyed("Microchip(s) destroyed with element ID(s): %s" %
                                         str(destroyed_microchip_ids))

        check_if_microchips_destroyed()

    def add_items(self, items):
        """
        :type items: set[FloorItem]
        """
        self.contents |= items
        self._check_safe()

    def remove_items(self, items):
        """
        :param set[FloorItem] items: A collection of item names to remove
        :return: The removed items
        """
        if not items:
            raise ValueError("Could not find matching floor items: %s" % str(items))

        self.contents -= items
        self._check_safe()

    @staticmethod
    def sort_items(items):
        """
        :type: list[day_11.floor.item.FloorItem]
        """
        items_sorted_by_type = sorted(items, key=lambda x: x.type)
        items_sorted_by_element = sorted(items_sorted_by_type, key=lambda x: x.element_id)
        return items_sorted_by_element

    def __eq__(self, floor):
        if set(self.contents) == set(floor.contents):
            return True

    def __ne__(self, floor):
        return not self.__eq__(floor)

    def __repr__(self):
        return str(self.contents)

    def __deepcopy__(self, memo=None):
        copied_contents = set(self.contents)
        return Floor(copied_contents)
