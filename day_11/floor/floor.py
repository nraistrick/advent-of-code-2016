from item import FloorItem
from item_type import FloorItemType


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
        self._check_safe(self.contents)

    @staticmethod
    def _check_safe(items):
        """Validate the floor"""
        def check_if_microchips_destroyed():
            generator_elements = set()
            microchip_elements = set()
            for i in items:
                if i.type == FloorItemType.GENERATOR:
                    generator_elements.add(i.element_id)
                else:
                    microchip_elements.add(i.element_id)

            destroyed_microchip_ids = microchip_elements - generator_elements
            if generator_elements and destroyed_microchip_ids:
                return True

            return False

        return not check_if_microchips_destroyed()

    def add_items(self, items):
        """
        :type items: set[FloorItem]
        """
        self.contents |= items

    def remove_items(self, items):
        """
        :param set[FloorItem] items: A collection of item names to remove
        :return: The removed items
        """
        if not items:
            raise ValueError("Could not find matching floor items: %s" % str(items))

        self.contents -= items

    def check_safe_to_add_items(self, items):
        updated_contents = self.contents | items
        return self._check_safe(updated_contents)

    def check_safe_to_remove_items(self, items):
        updated_contents = self.contents - items
        return self._check_safe(updated_contents)

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
        generators_or_microchips_only = [i.type for i in self.contents]
        return str(generators_or_microchips_only)

    def __hash__(self):
        return hash(repr(self))

    def __deepcopy__(self, memo=None):
        copied_contents = set(self.contents)
        return Floor(copied_contents)
