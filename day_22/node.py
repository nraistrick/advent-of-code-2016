class Node(object):
    """
    Represents a node in a computer grid
    """
    def __init__(self, name, size, used, available=None):
        """
        :type name: str
        :type size: int
        :type used: int
        """
        self.name = name
        self.used = used
        self.size = size

        if not available:
            self.available = self.size - self.used
        else:
            self.available = available

        self.x, self.y = Node.get_coordinates(name)

    @classmethod
    def from_string(cls, node_string):
        """
        :type node_string: str
        :rtype: Node

        >>> n = Node.from_string("/dev/grid/node-x0-y0     92T   73T    19T   79%")
        >>> n.name, n.size, n.used
        ('/dev/grid/node-x0-y0', 92, 73)
        """
        split = [a for a in node_string.split(" ") if a != ""]
        return cls(split[0],
                   int(split[1].strip("T")),
                   int(split[2].strip("T")),
                   int(split[3].strip("T")))

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

    @property
    def is_large_and_full(self):
        """
        :rtype: bool

        >>> Node('/dev/grid/node-x0-y0', 500, 495).is_large_and_full
        True
        >>> Node('/dev/grid/node-x0-y0', 50, 30).is_large_and_full
        False
        """
        if self.size >= 500 and self.used >= 490:
            return True
        return False

    @property
    def is_empty(self):
        """
        :rtype: bool

        >>> Node('/dev/grid/node-x0-y0', 8, 0).is_empty
        True
        >>> Node('/dev/grid/node-x0-y0', 8, 5).is_empty
        False
        """
        if self.used == 0:
            return True
        return False

    @property
    def is_interchangeable(self):
        """
        :rtype: bool

        >>> Node('/dev/grid/node-x0-y0', 11, 7).is_interchangeable
        True
        >>> Node('/dev/grid/node-x0-y0', 8, 0).is_interchangeable
        False
        >>> Node('/dev/grid/node-x0-y0', 500, 495).is_interchangeable
        False
        """
        if not self.is_empty and not self.is_large_and_full:
            return True
        return False

    def __str__(self):
        """
        :rtype: str

        >>> str(Node('/dev/grid/node-x0-y0', 20, 10))
        ' 10/20 '
        """
        return "%3s/%-3s" % (self.used, self.size)

    def __repr__(self):
        """
        :rtype: str

        >>> repr(Node('/dev/grid/node-x0-y0', 10, 20))
        '0,0'
        """
        return "%s,%s" % (self.x, self.y)
