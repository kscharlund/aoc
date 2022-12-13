import sys
from pprint import pprint
import math


def memoize(func):
    """
    Memoization decorator for a function taking a single argument.
    """
    class Memodict(dict):
        """Memoization dictionary."""
        def __missing__(self, key):
            ret = self[key] = func(key)
            return ret
    return Memodict().__getitem__


def create_graph(lines, nd=3):
    return {
        (xx, yy) + (0,) * (nd - 2)
        for yy, line in enumerate(lines)
        for xx, char in enumerate(line.strip())
        if char == '#'
    }


@memoize
def adjacent_nodes(coords):
    xx, yy, zz = coords
    return {
        (xx + dx, yy + dy, zz + dz)
        for dz in (-1, 0, 1)
        for dy in (-1, 0, 1)
        for dx in (-1, 0, 1)
        if any((dx, dy, dz))
    }


@memoize
def adjacent_nodes_4d(coords):
    xx, yy, zz, ww = coords
    return {
        (xx + dx, yy + dy, zz + dz, ww + dw)
        for dw in (-1, 0, 1)
        for dz in (-1, 0, 1)
        for dy in (-1, 0, 1)
        for dx in (-1, 0, 1)
        if any((dx, dy, dz, dw))
    }


def iterate(active_nodes, neighbor_func):
    active_neighbors = {}
    for node in active_nodes:
        for neighbor in neighbor_func(node):
            active_neighbors[neighbor] = active_neighbors.get(neighbor, 0) + 1
    return {
        node
        for node, nn in active_neighbors.items()
        if nn == 3 or (node in active_nodes and nn == 2)
    }


def a(lines):
    active_nodes = create_graph(lines)
    for _ in range(6):
        active_nodes = iterate(active_nodes, adjacent_nodes)
    print(len(active_nodes))


def b(lines):
    active_nodes = create_graph(lines, 4)
    for _ in range(6):
        active_nodes = iterate(active_nodes, adjacent_nodes_4d)
    print(len(active_nodes))


def main():
    lines = sys.stdin.readlines()
    a(lines)
    print()
    b(lines)


if __name__ == '__main__':
    main()
