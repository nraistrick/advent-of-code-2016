"""
Finds the shortest route through a grid of small rooms, similar to the below:

               x
   ------------>
  |
  |   #########
  |   #S| | | #
  |   #-#-#-#-#
  |   # | | | #
  |   #-#-#-#-#
  |   # | | | #
  |   #-#-#-#-#
  |   # | | |E
y v   #######

Fixed walls are marked with #, and doors are marked with - or |

There is a door connecting each room which is locked based on both a passcode
and the previous directions taken to enter the room.
"""

from day_17.room import Room


START_COORDINATES = (0, 0)


def maze_solver(passcode, end_coordinates=(3, 3)):
    """
    :type passcode: str
    :type end_coordinates: (int, int)
    :return: The shortest path i.e. the actual path, not just the length
    :rtype: str

    >>> maze_solver("ihgpwlah")
    'DDRRRD'
    >>> maze_solver("kglvqrro")
    'DDUDRLRRUDRD'
    >>> maze_solver("ulqzkmiv")
    'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
    """
    right_wall = end_coordinates[0]
    bottom_wall = end_coordinates[1]

    locations = [(START_COORDINATES, "")]
    while True:
        coordinates, directions = locations.pop(0)

        if coordinates == end_coordinates:
            return directions

        x, y = coordinates
        room = Room(passcode, directions)

        if room.can_go_right and x < right_wall:
            locations.append(((x + 1, y), directions + "R"))
        if room.can_go_down and y < bottom_wall:
            locations.append(((x, y + 1), directions + "D"))
        if room.can_go_left and x > 0:
            locations.append(((x - 1, y), directions + "L"))
        if room.can_go_up and y > 0:
            locations.append(((x, y - 1), directions + "U"))


def main():
    passcode = "edjrjqaa"
    shortest_route = maze_solver(passcode)

    print "The shortest route to reach the end of the maze is: %s" % shortest_route


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
