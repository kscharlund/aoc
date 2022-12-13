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


def get_data():
    return [line.split() for line in open(sys.argv[1])]


def move_head(h_pos, dir):
    y, x = h_pos
    match dir:
        case "U":
            return (y - 1, x)
        case "D":
            return (y + 1, x)
        case "L":
            return (y, x - 1)
        case "R":
            return (y, x + 1)


def cmp(a, b):
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


def move_tail(h_pos, t_pos):
    hy, hx = h_pos
    ty, tx = t_pos
    dy, dx = hy - ty, hx - tx
    if abs(dy) <= 1 and abs(dx) <= 1:
        return (ty, tx)
    return (ty + cmp(dy, 0), tx + cmp(dx, 0))


def a(data):
    h_pos = t_pos = (0, 0)
    visited = set()
    for dir, n in data:
        for i in range(int(n)):
            h_pos = move_head(h_pos, dir)
            t_pos = move_tail(h_pos, t_pos)
            visited.add(t_pos)
    print(len(visited))


def b(data):
    positions = [(0, 0) for _ in range(10)]
    visited = set()
    for dir, n in data:
        for i in range(int(n)):
            positions[0] = move_head(positions[0], dir)
            for p in range(1, 10):
                positions[p] = move_tail(positions[p - 1], positions[p])
            visited.add(positions[-1])
    print(len(visited))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
