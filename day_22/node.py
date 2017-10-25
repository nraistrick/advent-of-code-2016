class Node(object):
    """
    Represents a node in a computer grid
    """
    def __init__(self, node_string):
        """
        :type node_string: str

        >>> n = Node("/dev/grid/node-x0-y0     92T   73T    19T   79%")
        >>> n.name, n.size, n.used, n.available
        ('/dev/grid/node-x0-y0', 92, 73, 19)
        """
        split = [a for a in node_string.split(" ") if a != ""]
        self.name = split[0]
        self.size = int(split[1].strip("T"))
        self.used = int(split[2].strip("T"))
        self.available = int(split[3].strip("T"))
        self.x, self.y = self.get_coordinates(self.name)

    @staticmethod
    def get_coordinates(name):
        """
        :type name: str
        :rtype: (int, int)

        >>> Node.get_coordinates("/dev/grid/node-x0-y0")
        (0, 0)
        >>> Node.get_coordinates("/dev/grid/node-x1-y6")
        (1, 6)
        >>> Node.get_coordinates("/dev/grid/node-x14-y1")
        (14, 1)
        >>> Node.get_coordinates("/dev/grid/node-x2-y32")
        (2, 32)
        """
        x_index = name.index("x") + 1
        y_index = name.index("y") + 1
        x = int(name[x_index:y_index - 2])
        y = int(name[y_index:])
        return x, y

    def __repr__(self):
        return "%s,%s" % (self.x, self.y)
