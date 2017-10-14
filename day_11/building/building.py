from copy import deepcopy
from day_11.building.elevator_movement_type import ElevatorMovementType
from day_11.floor.floor import Floor


class Building(object):
    """
    Represents a building with multiple floors
    """
    _MAX_CARRY_ITEMS = 2
    _BOTTOM_FLOOR_ID = 1

    def __init__(self, floors):
        """
        :type floors: list[day_11.floor.floor.Floor]
        """
        self.floors = floors
        self._elevator_items = set()

        self.bottom_floor_id = self._BOTTOM_FLOOR_ID
        self.top_floor_id = len(self.floors)
        self._elevator_floor_id = self.bottom_floor_id

    def get_all_items(self):
        """
        :return: A list of all available items
        :rtype: list[day_11.floor.item.FloorItem]
        """
        all_items = []
        for floor in self.floors:
            all_items += floor.contents
        return Floor.sort_items(all_items)

    def go_up_in_elevator(self):
        """
        Take the current items up one floor in the elevator, then drop them
        """
        if not self.elevator_items:
            raise ValueError("Must be holding at least one item to move the elevator")

        new_floor = self.elevator_floor_id + 1
        if new_floor > self.top_floor_id:
            raise ValueError("The elevator cannot go higher than the top floor")

        self._elevator_floor_id = new_floor
        self.drop_items()

    def go_down_in_elevator(self):
        """
        Take the current items down one floor in the elevator, then drop them
        """
        new_floor = self.elevator_floor_id - 1

        if not self.elevator_items:
            raise ValueError("Must be holding at least one item to move the elevator")

        if new_floor < self.bottom_floor_id:
            raise ValueError("The elevator cannot go lower than the first floor")

        self._elevator_floor_id = new_floor
        self.drop_items()

    def drop_items(self):
        self._current_floor.add_items(self.elevator_items)
        self._elevator_items = set()

    def check_safe_to_go_up_in_elevator(self, items):
        safe_to_remove = self._current_floor.check_safe_to_remove_items(items)
        if not safe_to_remove:
            return False
        new_floor = self.elevator_floor_id + 1
        safe_to_add = self.floors[new_floor - 1].check_safe_to_add_items(items)
        return safe_to_add

    def check_safe_to_go_down_in_elevator(self, items):
        safe_to_remove = self._current_floor.check_safe_to_remove_items(items)
        if not safe_to_remove:
            return False
        new_floor = self.elevator_floor_id - 1
        safe_to_add = self.floors[new_floor - 1].check_safe_to_add_items(items)
        return safe_to_add

    def grab_items(self, items):
        """
        :type items: set[day_11.floor.item.FloorItem]
        """
        if len(items) > self._MAX_CARRY_ITEMS:
            raise ValueError("Cannot pick up more than %s items at once" % self._MAX_CARRY_ITEMS)

        if self.elevator_items:
            raise ValueError("Must drop items before picking more up")

        self._current_floor.remove_items(items)
        self._elevator_items |= items

    def print_floor_map(self):
        def print_elevator_location_marker(number):
            if number == self.elevator_floor_id:
                print "E",
            else:
                print " ",

        def print_floor_number(number):
            print "F" + str(number),

        def print_floor_items(number):
            for item in self.get_all_items():
                if item in self.floors[number - 1].contents:
                    print " " + str(item),
                else:
                    print " . ",

        for floor_number in reversed(self.floor_numbers):
            print_elevator_location_marker(floor_number)
            print_floor_number(floor_number)
            print_floor_items(floor_number)
            print ""

    @property
    def elevator_floor_id(self):
        """
        :rtype: int
        """
        return self._elevator_floor_id

    @property
    def _current_floor(self):
        """
        :rtype: day_11.floor.floor.Floor
        """
        return self.floors[self.elevator_floor_id - 1]

    @property
    def floor_numbers(self):
        """
        :rtype: list[int]
        """
        return range(self.bottom_floor_id, len(self.floors) + 1)

    @property
    def current_floor_items(self):
        """
        :rtype: set[day_11.floor.item.FloorItem]
        """
        return self.floors[self.elevator_floor_id - 1].contents

    @property
    def elevator_items(self):
        """
        :rtype: set
        """
        return self._elevator_items

    @property
    def items_on_floors_below(self):
        """
        Checks if there are any items on the floors below the current
        :rtype: bool
        """
        for floor in self.floors[:self.elevator_floor_id - 1]:
            if floor.contents:
                return True

        return False

    @property
    def available_elevator_directions(self):
        """
        :rtype: list[ElevatorMovementType]
        """
        if self.elevator_floor_id == self.top_floor_id:
            possible_directions = [ElevatorMovementType.DOWN]
        elif self.elevator_floor_id == self.bottom_floor_id:
            possible_directions = [ElevatorMovementType.UP]
        else:
            possible_directions = [ElevatorMovementType.UP, ElevatorMovementType.DOWN]

        return possible_directions

    def __eq__(self, building):
        """
        :type building: Building
        """
        return True if hash(self) == hash(building) else False

    def __ne__(self, building):
        """
        :type building: Building
        """
        return not self.__eq__(building)

    def __hash__(self):
        return hash(self.elevator_floor_id) ^ hash(repr(self.floors))

    def __repr__(self):
        return "%s%s" % (str(self.elevator_floor_id), repr(self.floors))

    def __deepcopy__(self, memo=None):
        copied_floors = [deepcopy(f) for f in self.floors]
        copied_building = Building(copied_floors)
        copied_building._elevator_floor_id = self.elevator_floor_id
        return copied_building
