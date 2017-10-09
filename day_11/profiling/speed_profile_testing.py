import cProfile

from day_11.building.building import Building
from day_11.floor.floor import Floor
from day_11.floor.item import FloorItem
from day_11.floor.item_type import FloorItemType
from day_11.main import solve_puzzle


def profile_easy_problem():
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

    return solve_puzzle(building)


def profile_hard_problem():
    plutonium_element = "plutonium"
    ruthenium_element = "ruthenium"
    strontium_element = "strontium"
    curium_element = "curium"

    floor_1 = Floor({FloorItem(strontium_element, FloorItemType.GENERATOR),
                     FloorItem(strontium_element, FloorItemType.MICROCHIP),
                     FloorItem(plutonium_element, FloorItemType.GENERATOR),
                     FloorItem(plutonium_element, FloorItemType.MICROCHIP),
                     FloorItem(curium_element, FloorItemType.GENERATOR),
                     FloorItem(curium_element, FloorItemType.MICROCHIP)})
    floor_2 = Floor({FloorItem(ruthenium_element, FloorItemType.GENERATOR),
                     FloorItem(ruthenium_element, FloorItemType.MICROCHIP)})
    floor_3 = Floor()
    floor_4 = Floor()
    floors = [floor_1, floor_2, floor_3, floor_4]

    building = Building(floors)
    building.print_floor_map()

    return solve_puzzle(building)


def main():
    cProfile.run("profile_easy_problem()")
    cProfile.run("profile_hard_problem()")


if __name__ == '__main__':
    main()
