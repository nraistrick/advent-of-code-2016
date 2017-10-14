from unittest import TestCase

from day_11.building.building import Building
from day_11.building.elevator_movement_type import ElevatorMovementType
from day_11.floor.floor import Floor
from day_11.floor.item import FloorItem
from day_11.floor.item_type import FloorItemType
from day_11.main import \
    get_possible_moves, \
    execute_move, \
    puzzle_complete, \
    single_item_carry_options, \
    double_item_carry_options, \
    all_carry_options, \
    solve_puzzle
from day_11.move.move import Move


class TestAlgorithm(TestCase):
    DUMMY_ELEMENT_1 = "abarium"
    DUMMY_ELEMENT_2 = "bondium"
    DUMMY_ELEMENT_3 = "charium"

    DUMMY_MICROCHIP_1 = FloorItem(DUMMY_ELEMENT_1, FloorItemType.MICROCHIP)
    DUMMY_MICROCHIP_2 = FloorItem(DUMMY_ELEMENT_2, FloorItemType.MICROCHIP)
    DUMMY_MICROCHIP_3 = FloorItem(DUMMY_ELEMENT_3, FloorItemType.MICROCHIP)
    DUMMY_GENERATOR_1 = FloorItem(DUMMY_ELEMENT_1, FloorItemType.GENERATOR)
    DUMMY_GENERATOR_2 = FloorItem(DUMMY_ELEMENT_2, FloorItemType.GENERATOR)
    DUMMY_GENERATOR_3 = FloorItem(DUMMY_ELEMENT_3, FloorItemType.GENERATOR)

    def test_single_item_carry_options(self):
        items = [self.DUMMY_GENERATOR_1, self.DUMMY_MICROCHIP_1]
        carry_options = single_item_carry_options(items)
        self.assertEqual(carry_options, [(self.DUMMY_GENERATOR_1,),
                                         (self.DUMMY_MICROCHIP_1,)])

        items = [self.DUMMY_MICROCHIP_1, self.DUMMY_MICROCHIP_2, self.DUMMY_MICROCHIP_3]
        carry_options = single_item_carry_options(items)
        self.assertEqual(carry_options, [(self.DUMMY_MICROCHIP_1,),
                                         (self.DUMMY_MICROCHIP_2,),
                                         (self.DUMMY_MICROCHIP_3,)])

    def test_double_item_carry_options(self):
        items = [self.DUMMY_MICROCHIP_1, self.DUMMY_MICROCHIP_2, self.DUMMY_MICROCHIP_3]
        carry_options = double_item_carry_options(items)
        self.assertEqual(carry_options, [(self.DUMMY_MICROCHIP_1, self.DUMMY_MICROCHIP_2),
                                         (self.DUMMY_MICROCHIP_1, self.DUMMY_MICROCHIP_3),
                                         (self.DUMMY_MICROCHIP_2, self.DUMMY_MICROCHIP_3)])

        items = [self.DUMMY_MICROCHIP_1, self.DUMMY_GENERATOR_1, self.DUMMY_GENERATOR_2]
        carry_options = double_item_carry_options(items)
        self.assertEqual(carry_options, [(self.DUMMY_MICROCHIP_1, self.DUMMY_GENERATOR_1),
                                         (self.DUMMY_GENERATOR_1, self.DUMMY_GENERATOR_2)])

    def test_all_item_carry_options(self):
        items = [self.DUMMY_MICROCHIP_1, self.DUMMY_MICROCHIP_2, self.DUMMY_MICROCHIP_3]
        single_options = single_item_carry_options(items)
        double_options = double_item_carry_options(items)
        carry_options = all_carry_options(items)
        self.assertEqual(carry_options, double_options + single_options)

    def test_generate_possible_moves(self):
        items_one_and_two = {self.DUMMY_MICROCHIP_1, self.DUMMY_MICROCHIP_2}
        item_one = {self.DUMMY_MICROCHIP_1}
        item_two = {self.DUMMY_MICROCHIP_2}
        single_generator = {self.DUMMY_GENERATOR_1}

        empty_floor = Floor()
        floor_with_two_items = Floor(items_one_and_two)
        floor_with_one_generator = Floor(single_generator)

        building = Building([floor_with_two_items, empty_floor])
        expected_moves = [Move(ElevatorMovementType.UP, items_one_and_two),
                          Move(ElevatorMovementType.UP, item_one),
                          Move(ElevatorMovementType.UP, item_two)]
        self.verify_expected_moves(building, expected_moves)

        building = Building([empty_floor, floor_with_two_items, empty_floor])
        building._elevator_floor_id = 2
        expected_moves = [Move(ElevatorMovementType.UP, items_one_and_two),
                          Move(ElevatorMovementType.UP, item_one),
                          Move(ElevatorMovementType.UP, item_two),
                          Move(ElevatorMovementType.DOWN, items_one_and_two),
                          Move(ElevatorMovementType.DOWN, item_one),
                          Move(ElevatorMovementType.DOWN, item_two)]
        self.verify_expected_moves(building, expected_moves)

        building = Building([empty_floor, empty_floor, floor_with_two_items])
        building._elevator_floor_id = building.top_floor_id
        expected_moves = [Move(ElevatorMovementType.DOWN, items_one_and_two),
                          Move(ElevatorMovementType.DOWN, item_one),
                          Move(ElevatorMovementType.DOWN, item_two)]
        self.verify_expected_moves(building, expected_moves)

        building = Building([empty_floor, floor_with_one_generator, empty_floor])
        building._elevator_floor_id = 2
        expected_moves = [Move(ElevatorMovementType.UP, single_generator),
                          Move(ElevatorMovementType.DOWN, single_generator)]
        self.verify_expected_moves(building, expected_moves)

    def verify_expected_moves(self, building, expected_moves):
        moves = [m for m in get_possible_moves(building)]
        self.assertEqual(moves, expected_moves)

    def test_puzzle_complete(self):
        empty_floor = Floor()
        populated_floor = Floor({self.DUMMY_MICROCHIP_1, self.DUMMY_GENERATOR_1})
        building = Building([empty_floor, empty_floor, populated_floor])
        building._elevator_floor_id = building.top_floor_id
        self.assertTrue(puzzle_complete(building, len(building.get_all_items())))

        building = Building([empty_floor, populated_floor])
        building._elevator_floor_id = building.top_floor_id
        self.assertTrue(puzzle_complete(building, len(building.get_all_items())))

    def test_execute_move(self):
        floor_item_combination_1 = {self.DUMMY_MICROCHIP_1, self.DUMMY_MICROCHIP_2}

        empty_floor = Floor()
        floor_with_two_items = Floor(floor_item_combination_1)

        building = Building([floor_with_two_items, empty_floor])
        self.assertFalse(puzzle_complete(building, len(building.get_all_items())))

        possible_moves = [m for m in get_possible_moves(building)]
        self.assertEqual(len(possible_moves), 3)

        execute_move(building, possible_moves[0])
        self.assertTrue(puzzle_complete(building, len(building.get_all_items())))

    def test_solve_easiest_problem(self):
        hydrogen_element = "hydrogen"

        floor_1 = Floor({FloorItem(hydrogen_element, FloorItemType.MICROCHIP),
                         FloorItem(hydrogen_element, FloorItemType.GENERATOR)})
        floor_2 = Floor()
        floors = [floor_1, floor_2]
        building = Building(floors)
        building.print_floor_map()

        minimum_solution_steps = solve_puzzle(building)
        self.assertEqual(minimum_solution_steps, 1)

    def test_solve_easier_problem(self):
        hydrogen_element = "hydrogen"
        lithium_element = "lithium"

        floor_1 = Floor({FloorItem(hydrogen_element, FloorItemType.MICROCHIP),
                         FloorItem(lithium_element, FloorItemType.MICROCHIP),
                         FloorItem(hydrogen_element, FloorItemType.GENERATOR),
                         FloorItem(lithium_element, FloorItemType.GENERATOR)})
        floor_2 = Floor()
        floors = [floor_1, floor_2]

        building = Building(floors)
        building.print_floor_map()

        minimum_solution_steps = solve_puzzle(building)
        self.assertEqual(minimum_solution_steps, 5)

    def test_solve_easy_problem(self):
        hydrogen_element = "hydrogen"
        lithium_element = "lithium"

        floor_1 = Floor({FloorItem(hydrogen_element, FloorItemType.MICROCHIP),
                         FloorItem(lithium_element, FloorItemType.MICROCHIP)})
        floor_2 = Floor({FloorItem(hydrogen_element, FloorItemType.GENERATOR)})
        floor_3 = Floor({FloorItem(lithium_element, FloorItemType.GENERATOR)})
        floor_4 = Floor()
        floors = [floor_1, floor_2, floor_3, floor_4]

        building = Building(floors)
        building.print_floor_map()

        minimum_solution_steps = solve_puzzle(building)
        self.assertEqual(minimum_solution_steps, 11)

    def test_solve_intermediate_problem(self):
        ruthenium_element = "ruthenium"
        strontium_element = "strontium"
        thulium_element = "thulium"

        floor_1 = Floor({FloorItem(ruthenium_element, FloorItemType.GENERATOR),
                         FloorItem(ruthenium_element, FloorItemType.MICROCHIP),
                         FloorItem(strontium_element, FloorItemType.GENERATOR),
                         FloorItem(strontium_element, FloorItemType.MICROCHIP),
                         FloorItem(thulium_element, FloorItemType.GENERATOR)})
        floor_2 = Floor({FloorItem(thulium_element, FloorItemType.MICROCHIP)})
        floor_3 = Floor()
        floor_4 = Floor()
        floors = [floor_1, floor_2, floor_3, floor_4]

        building = Building(floors)
        building.print_floor_map()

        self.assertEqual(solve_puzzle(building), 25)

    def test_solve_hard_problem(self):
        plutonium_element = "plutonium"
        ruthenium_element = "ruthenium"
        strontium_element = "strontium"
        thulium_element = "thulium"

        floor_1 = Floor({FloorItem(strontium_element, FloorItemType.GENERATOR),
                         FloorItem(strontium_element, FloorItemType.MICROCHIP),
                         FloorItem(plutonium_element, FloorItemType.GENERATOR),
                         FloorItem(plutonium_element, FloorItemType.MICROCHIP)})
        floor_2 = Floor({FloorItem(thulium_element, FloorItemType.GENERATOR),
                         FloorItem(ruthenium_element, FloorItemType.GENERATOR),
                         FloorItem(ruthenium_element, FloorItemType.MICROCHIP)})
        floor_3 = Floor({FloorItem(thulium_element, FloorItemType.MICROCHIP)})
        floors = [floor_1, floor_2, floor_3]

        building = Building(floors)
        building.print_floor_map()

        self.assertEqual(solve_puzzle(building), 16)
