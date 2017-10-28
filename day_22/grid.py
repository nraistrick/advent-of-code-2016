from day_22.node import Node


class Grid(object):
    """
    Represents a distributed grid of computers with varying storage capacity
    """
    ACCESSIBLE_COORDINATES = (0, 0)

    def __init__(self, nodes):
        """
        :type nodes: list[Node]
        """
        self.nodes = self.indexed_nodes(nodes)
        self.max_x = self.get_max_x()
        self.max_y = self.get_max_y()

        self.empty = self.get_empty_node_coordinates()
        self.target = (self.max_x, 0)

    @staticmethod
    def indexed_nodes(nodes):
        """
        :type nodes: list[Node]
        :rtype: list[list[Node]]
        """
        indexed_nodes = []
        for n in sorted(nodes, key=lambda node: node.x):
            if n.y == 0:
                column = []
                indexed_nodes.append(column)
            column.append(n)
        return indexed_nodes

    def get_max_x(self):
        """
        :rtype: int

        >>> nodes = [Node("/dev/grid/node-x0-y0", 0, 0),
        ...          Node("/dev/grid/node-x1-y0", 0, 0),
        ...          Node("/dev/grid/node-x2-y0", 0, 0),
        ...          Node("/dev/grid/node-x0-y1", 0, 0)]
        >>> Grid(nodes).get_max_x()
        2
        """
        return len(self.nodes) - 1

    def get_max_y(self):
        """
        :rtype: int

        >>> nodes = [Node("/dev/grid/node-x0-y0", 0, 0), Node("/dev/grid/node-x1-y0", 0, 0),
        ...          Node("/dev/grid/node-x0-y1", 0, 0), Node("/dev/grid/node-x1-y1", 0, 0),
        ...          Node("/dev/grid/node-x0-y2", 0, 0), Node("/dev/grid/node-x1-y2", 0, 0)]
        >>> Grid(nodes).get_max_y()
        2
        """
        return len(self.nodes[0]) - 1

    def get_empty_node_coordinates(self):
        """
        :rtype: (int, int)
        """
        for y in range(self.max_y + 1):
            for x in range(self.max_x + 1):
                if self.nodes[x][y].is_empty:
                    return x, y

    def solve(self):
        """
        1) Find available moves for the target data (preferred movements left, up, down, right)
             * Move to node is available provided it's not 'very large and very full'
               as these are not interchangeable with 'empty' nodes
        2) Find distance from 'empty' node to available move position
             * Avoid 'very large and very full' nodes
        3) Move data into empty node
        4) Repeat until target data is located in accessible coordinates

        :rtype: int
        :return: Minimum number of moves taken
        """
        move_count = 0

        # Assume only moving left for the moment
        target_moves = [(self.target[0] - 1, self.target[1])]

        while target_moves:
            move = target_moves.pop(0)
            empty_to_target_move_count = self.find_shortest_path(self.empty, move)

            # Move the empty node
            self.empty = move
            move_count += empty_to_target_move_count

            # Switch the target and empty
            self.target, self.empty = self.empty, self.target
            move_count += 1

            # Check if we can access the data
            if self.target == self.ACCESSIBLE_COORDINATES:
                return move_count

            # Add the next move
            target_moves.append((self.target[0] - 1, self.target[1]))

    def find_shortest_path(self, start_coordinates, end_coordinates):
        """
        Finds the shortest allowable path in a grid between two points

        :type start_coordinates: (int, int)
        :type end_coordinates: (int, int)
        :rtype: int
        """
        visited = []
        locations = [(start_coordinates[0], start_coordinates[1], 0)]
        while locations:
            x, y, move_count = locations.pop(0)

            if (x, y) == end_coordinates:
                return move_count

            if (x, y) in visited:
                continue

            visited.append((x, y))

            move_count += 1
            for x, y in self.available_node_coordinates(x, y):
                if (x, y) in visited:
                    continue
                locations += [(x, y, move_count)]

    def available_node_coordinates(self, x, y):
        """
        :rtype: list[(int, int)]
        """
        moves = []
        if self.can_move_node_up(x, y):
            moves.append((x, y-1))
        if self.can_move_node_down(x, y):
            moves.append((x, y+1))
        if self.can_move_node_left(x, y):
            moves.append((x-1, y))
        if self.can_move_node_right(x, y):
            moves.append((x+1, y))

        return moves

    def can_move_node_up(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        if y == 0:
            return False

        new_node = self.nodes[x][y-1]
        if new_node.is_large_and_full or (new_node.x, new_node.y) == self.target:
            return False

        return True

    def can_move_node_down(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        if y == self.max_y:
            return False

        new_node = self.nodes[x][y+1]
        if new_node.is_large_and_full or (new_node.x, new_node.y) == self.target:
            return False

        return True

    def can_move_node_left(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        if x == 0:
            return False

        new_node = self.nodes[x-1][y]
        if new_node.is_large_and_full or (new_node.x, new_node.y) == self.target:
            return False

        return True

    def can_move_node_right(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        if x == self.max_x:
            return False

        new_node = self.nodes[x+1][y]
        if new_node.is_large_and_full or (new_node.x, new_node.y) == self.target:
            return False

        return True

    def print_map(self):
        """
        Prints a grid map of all the nodes
        """
        for y in range(self.max_y + 1):
            print ""
            for x in range(self.max_x + 1):
                print str(self.nodes[x][y]),

    def print_simplified_map(self):
        """
        Prints a simplified map of all the nodes where types of node are
        represented by specific characters
        """
        for y in range(self.max_y + 1):
            print ""
            for x in range(self.max_x + 1):
                n = self.nodes[x][y]
                if (x, y) == self.target:
                    print "G",
                elif n.is_interchangeable:
                    print ".",
                elif n.is_large_and_full:
                    print "#",
                elif n.is_empty:
                    print "_",
                else:
                    raise ValueError("Found unexpected node type in grid")
        print ""
