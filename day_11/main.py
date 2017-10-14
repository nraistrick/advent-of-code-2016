"""
Solves a puzzle to safely move a collection of radioactive generators and
microchips to the top of a building.
"""

import itertools
import time
from copy import deepcopy

from anytree import Node, RenderTree

from day_11.building.building import Building
from day_11.building.elevator_movement_type import ElevatorMovementType
from day_11.floor.floor import Floor
from day_11.floor.item import FloorItem
from day_11.floor.item_type import FloorItemType
from day_11.floor.microchip_destroyed import MicrochipDestroyed
from day_11.move.move import Move


def all_carry_options(floor_items):
    """
    :rtype: list[(FloorItem, FloorItem)]
    """
    return double_item_carry_options(floor_items) + single_item_carry_options(floor_items)


def single_item_carry_options(floor_items):
    """
    :type floor_items: list[FloorItem]
    :rtype: list[(FloorItem, _)]
    """
    return [(item,) for item in floor_items]


def double_item_carry_options(floor_items):
    """
    :type floor_items: list[FloorItem]
    :rtype: list[(FloorItem, FloorItem)]
    """
    return [choice for choice in itertools.combinations(floor_items, 2)
            if valid_carry_combination(choice[0], choice[1])]


def valid_carry_combination(first_floor_item, second_floor_item):
    """
    :type first_floor_item: FloorItem
    :type second_floor_item: FloorItem
    :rtype: bool
    """
    if first_floor_item.element_id != second_floor_item.element_id and \
            first_floor_item.type != second_floor_item.type:
        return False
    return True


def get_possible_moves(building):
    """
    :type building: Building
    :rtype: set[Move]
    """
    floor_items = sorted(building.current_floor_items, key=lambda x: x.element_id)
    item_combinations = all_carry_options(floor_items)

    for direction in building.available_elevator_directions:
        for items in item_combinations:
            yield Move(direction, set(items))


def puzzle_complete(building, total_building_items):
    """
    :type building: Building
    :type total_building_items: int
    :rtype: bool
    """
    if building.elevator_floor_id == building.top_floor_id and \
            len(building.current_floor_items) == total_building_items:
        return True
    return False


def execute_move(building, move):
    """
    :type building: Building
    :type move: Move
    :raises: ValueError
    """
    building.grab_items(move.items)

    if move.direction == ElevatorMovementType.UP:
        building.go_up_in_elevator()
    elif move.direction == ElevatorMovementType.DOWN:
        building.go_down_in_elevator()
    else:
        raise ValueError("Invalid elevator movement type")


def print_tree(root_node):
    """
    Prints a prettified version of a node tree

    :type root_node: Node
    """
    for pre, _, node in RenderTree(root_node):
        print "%s%s" % (pre, node.name)


def create_valid_move_tree(start_building):
    """
    Recursively creates a tree to try find the best possible solution
    for a given building.

    :type start_building: Building
    """
    start_node = "START"
    root_node = Node(start_node)
    total_building_items = len(start_building.get_all_items())
    used_building_versions = set()

    buildings = [(start_building, root_node)]
    while buildings:
        building, parent_node = buildings.pop(0)
        if building in used_building_versions:
            continue

        for move in get_possible_moves(building):
            copied_building = deepcopy(building)
            try:
                execute_move(copied_building, move)
                if copied_building in used_building_versions:
                    continue

                child = Node(str(move), parent=parent_node)

                if puzzle_complete(copied_building, total_building_items):
                    solution_depth = parent_node.depth + 1
                    return solution_depth

                buildings.append((copied_building, child))

            except MicrochipDestroyed:
                pass

        used_building_versions.add(building)


def solve_puzzle(building):
    """
    For a given building, tries all possible ways of finding a solution

    :param Building building: The building to solve the problem for
    :rtype: int
    """
    minimum_solution_steps = create_valid_move_tree(building)
    print "Best Solution: %s" % minimum_solution_steps

    return minimum_solution_steps


def solve_complex_problem():
    curium_element = "curium"
    dilithium_element = "dilithium"
    elerium_element = "elerium"
    plutonium_element = "plutonium"
    ruthenium_element = "ruthenium"
    strontium_element = "strontium"
    thulium_element = "thulium"

    floor_1 = Floor({FloorItem(dilithium_element, FloorItemType.GENERATOR),
                     FloorItem(dilithium_element, FloorItemType.MICROCHIP),
                     FloorItem(elerium_element, FloorItemType.GENERATOR),
                     FloorItem(elerium_element, FloorItemType.MICROCHIP),
                     FloorItem(strontium_element, FloorItemType.GENERATOR),
                     FloorItem(strontium_element, FloorItemType.MICROCHIP),
                     FloorItem(plutonium_element, FloorItemType.GENERATOR),
                     FloorItem(plutonium_element, FloorItemType.MICROCHIP)})
    floor_2 = Floor({FloorItem(thulium_element, FloorItemType.GENERATOR),
                     FloorItem(ruthenium_element, FloorItemType.GENERATOR),
                     FloorItem(ruthenium_element, FloorItemType.MICROCHIP),
                     FloorItem(curium_element, FloorItemType.GENERATOR),
                     FloorItem(curium_element, FloorItemType.MICROCHIP)})
    floor_3 = Floor({FloorItem(thulium_element, FloorItemType.MICROCHIP)})
    floor_4 = Floor()
    floors = [floor_1, floor_2, floor_3, floor_4]

    building = Building(floors)
    building.print_floor_map()

    solution_depth = solve_puzzle(building)
    print "Solution found in %s steps" % str(solution_depth)


def main():
    start = time.time()
    solve_complex_problem()
    end = time.time()
    print "Total time taken: %.2f" % (end - start)


if __name__ == '__main__':
    main()
