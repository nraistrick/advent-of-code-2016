"""
Find statistics about the number of viable nodes in a computer grid
"""

from common.common import get_file_lines
from day_22.node import Node


def get_viable_nodes(nodes):
    """
    :type nodes: list[Node]
    :rtype: list[(Node, Node)]

    >>> n0 = Node("/dev/grid/node-x0-y0      7T    2T    5T   ..%")
    >>> n1 = Node("/dev/grid/node-x1-y1     30T   10T   20T   ..%")
    >>> get_viable_nodes([n0, n1])
    [(0,0, 1,1)]

    >>> n0 = Node("/dev/grid/node-x0-y0     30T   10T   20T   ..%")
    >>> n1 = Node("/dev/grid/node-x1-y1     30T    2T    5T   ..%")
    >>> get_viable_nodes([n0, n1])
    [(1,1, 0,0)]

    >>> n0 = Node("/dev/grid/node-x0-y0     5T     0T    5T   ..%")
    >>> n1 = Node("/dev/grid/node-x1-y1     30T   10T   20T   ..%")
    >>> get_viable_nodes([n0, n1])
    []

    >>> n0 = Node("/dev/grid/node-x0-y0     30T   10T   20T   ..%")
    >>> n1 = Node("/dev/grid/node-x1-y1     30T   10T   20T   ..%")
    >>> get_viable_nodes([n0, n1])
    [(0,0, 1,1), (1,1, 0,0)]
    """
    viable_nodes = []
    for i, node in enumerate(nodes):
        for further_node in nodes[i+1:]:
            if node.used != 0 and node.used <= further_node.available:
                viable_nodes.append(tuple((node, further_node)))
            if further_node.used != 0 and further_node.used <= node.available:
                viable_nodes.append(tuple((further_node, node)))

    return list(viable_nodes)


def main():
    input_text = [line for line in get_file_lines("input.txt")]
    nodes = [Node(line) for line in input_text[2:]]
    viable_nodes = get_viable_nodes(nodes)
    print "Number of viable nodes: %s" % len(viable_nodes)


if __name__ == '__main__':
    main()
