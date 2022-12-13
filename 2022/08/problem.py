import itertools
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
    return [[int(x) for x in line.strip()] for line in open(sys.argv[1])]


def scan_row(data, visible, row, iter):
    max_seen = -1
    for col in iter:
        if data[row][col] > max_seen:
            visible[row][col] = True
            max_seen = data[row][col]


def scan_col(data, visible, col, iter):
    max_seen = -1
    for row in iter:
        if data[row][col] > max_seen:
            visible[row][col] = True
            max_seen = data[row][col]


def a(data):
    rows = len(data)
    cols = len(data[0])
    visible = [[False for c in range(cols)] for r in range(rows)]
    for row in range(rows):
        scan_row(data, visible, row, range(cols))
        scan_row(data, visible, row, reversed(range(cols)))
    for col in range(cols):
        scan_col(data, visible, col, range(rows))
        scan_col(data, visible, col, reversed(range(rows)))
    # pprint(visible)
    print(sum(itertools.chain.from_iterable(visible)))


def get_score(data, row, col):
    u, d, l, r = 0, 0, 0, 0
    h = data[row][col]
    for y in range(row - 1, -1, -1):
        u += 1
        if data[y][col] >= h:
            break
    for y in range(row + 1, len(data)):
        d += 1
        if data[y][col] >= h:
            break
    for x in range(col - 1, -1, -1):
        l += 1
        if data[row][x] >= h:
            break
    for x in range(col + 1, len(data[0])):
        r += 1
        if data[row][x] >= h:
            break
    return u * d * l * r


def b(data):
    rows = len(data)
    cols = len(data[0])
    scores = [
        [get_score(data, row, col) for col in range(1, cols - 1)]
        for row in range(1, rows - 1)
    ]
    # pprint(scores)
    print(max(itertools.chain.from_iterable(scores)))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
