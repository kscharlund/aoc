import sys
from pprint import pprint
import math


def get_data():
    galaxies = []
    populated_rows = set()
    populated_cols = set()
    for row, line in enumerate(open(sys.argv[1])):
        for col, c in enumerate(line.strip()):
            if c == '#':
                galaxies.append((row, col))
                populated_rows.add(row)
                populated_cols.add(col)
    n_rows = row + 1
    n_cols = col + 1
    return galaxies, populated_rows, populated_cols, n_rows, n_cols


def dist(p0, p1, empty_rows, empty_cols, exp_factor=1):
    y0, x0 = p0
    y1, x1 = p1
    # Galaxies are sorted by row, then col. y0 will always be <= y1,
    # but x0 and x1 may need swapping.
    if x0 > x1:
        x0, x1 = x1, x0
    yd = y1 - y0 + exp_factor * len([y for y in range(y0, y1) if y in empty_rows])
    xd = x1 - x0 + exp_factor * len([x for x in range(x0, x1) if x in empty_cols])
    return yd + xd


def a(data, exp_factor=1):
    galaxies, populated_rows, populated_cols, n_rows, n_cols = data
    empty_rows = set(range(n_rows)) - populated_rows
    empty_cols = set(range(n_cols)) - populated_cols
    res = 0
    for i, p0 in enumerate(galaxies):
        for p1 in galaxies[i+1:]:
            res += dist(p0, p1, empty_rows, empty_cols, exp_factor=exp_factor)
    print(res)


def b(data):
    a(data, exp_factor=999999)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
