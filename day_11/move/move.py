from day_11.building.elevator_movement_type import ElevatorMovementType
from day_11.floor.item_type import FloorItemType


class Move(object):
    """
    The next move to take when solving the puzzle
    """
    def __init__(self, direction, items):
        """
        :type direction: day_11.building.elevator_movement.ElevatorMovementType
        :type items: set[day_11.floor.item.FloorItem]
        """
        if direction != ElevatorMovementType.UP and direction != ElevatorMovementType.DOWN:
            raise ValueError("Not a valid move direction: %s" % str(direction))

        self.direction = direction
        self.items = items

    def __repr__(self):
        readable_move = str(self.direction)
        for i in sorted(self.items, key=lambda x: x.element_id):
            readable_move += "_" + str(i)
        return readable_move

    @property
    def carrying_generator(self):
        if any(i for i in self.items if i.type == FloorItemType.GENERATOR):
            return True
        return False

    @property
    def holding_microchip(self):
        if any(i for i in self.items if i.type == FloorItemType.MICROCHIP):
            return True
        return False

    def __eq__(self, move):
        if self.direction == move.direction and set(self.items) == set(move.items):
            return True
        return False

    def __ne__(self, move):
        return not self.__eq__(move)
