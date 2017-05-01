from unittest import TestCase

from day_11.building.elevator_movement_type import ElevatorMovementType
from day_11.floor.item import FloorItem, FloorItemType
from day_11.move.move import Move


class TestMove(TestCase):
    def test_create_invalid_move(self):
        with self.assertRaises(ValueError):
            Move("LEFT", set())

    def test_string_representation(self):
        items = {FloorItem("a", FloorItemType.GENERATOR)}
        move = Move(ElevatorMovementType.UP, items)
        self.assertEqual(str(move), "UP_AG")

        items = {FloorItem("a", FloorItemType.MICROCHIP)}
        move = Move(ElevatorMovementType.UP, items)
        self.assertEqual(str(move), "UP_AM")

        items = {FloorItem("b", FloorItemType.GENERATOR)}
        move = Move(ElevatorMovementType.DOWN, items)
        self.assertEqual(str(move), "DOWN_BG")

        items = {FloorItem("b", FloorItemType.MICROCHIP)}
        move = Move(ElevatorMovementType.DOWN, items)
        self.assertEqual(str(move), "DOWN_BM")

        items = {FloorItem("c", FloorItemType.MICROCHIP), FloorItem("c", FloorItemType.GENERATOR)}
        move = Move(ElevatorMovementType.UP, items)
        self.assertEqual(str(move), "UP_CG_CM")

        items = {FloorItem("c", FloorItemType.MICROCHIP), FloorItem("c", FloorItemType.GENERATOR)}
        move = Move(ElevatorMovementType.DOWN, items)
        self.assertEqual(str(move), "DOWN_CG_CM")

    def test_moving_generator_property(self):
        items = {FloorItem("a", FloorItemType.GENERATOR)}
        move = Move(ElevatorMovementType.UP, items)
        self.assertTrue(move.carrying_generator)

        items = {FloorItem("a", FloorItemType.MICROCHIP)}
        move = Move(ElevatorMovementType.UP, items)
        self.assertFalse(move.carrying_generator)

    def test_moving_microchip_property(self):
        items = {FloorItem("a", FloorItemType.MICROCHIP)}
        move = Move(ElevatorMovementType.UP, items)
        self.assertTrue(move.holding_microchip)

        items = {FloorItem("a", FloorItemType.GENERATOR)}
        move = Move(ElevatorMovementType.UP, items)
        self.assertFalse(move.holding_microchip)

    def test_move_equality(self):
        floor_item = FloorItem("makeupium", FloorItemType.MICROCHIP)
        floor_item_copy = FloorItem("makeupium", FloorItemType.MICROCHIP)
        move_items = {floor_item}
        move_items_copy = {floor_item_copy}

        move_1 = Move(ElevatorMovementType.UP, move_items)
        move_2 = Move(ElevatorMovementType.DOWN, move_items)
        move_1_copy = Move(ElevatorMovementType.UP, move_items_copy)

        self.assertNotEqual(id(move_1), id(move_2))
        self.assertFalse(move_1 == move_2)
        self.assertTrue(move_1 != move_2)

        self.assertNotEqual(id(move_1), id(move_1_copy))
        self.assertTrue(move_1 == move_1_copy)
        self.assertFalse(move_1 != move_1_copy)
