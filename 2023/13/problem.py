import sys
from pprint import pprint
import math


def get_data():
    data = []
    for grid in open(sys.argv[1]).read().split('\n\n'):
        rows = grid.splitlines()
        cols = [
            ''.join(row[i] for row in rows)
            for i in range(len(rows[0]))
        ]
        data.append((rows, cols))
    return data


def find_symmetry_line(grid: list[str], wanted_err_count=0):
    for i in range(1, len(grid[0])):
        err_count = 0
        for line in grid:
            a, b = line[:i][::-1], line[i:]
            if not (a.startswith(b) or b.startswith(a)):
                err_count += 1
            if err_count > wanted_err_count:
                break
        else:
            if err_count == wanted_err_count:
                return i
    return 0


def a(data, wanted_err_count=0):
    res = 0
    for rows, cols in data:
        if rs := find_symmetry_line(rows, wanted_err_count):
            res += rs
        else:
            res += 100 * find_symmetry_line(cols, wanted_err_count)
    print(res)


def b(data):
    a(data, 1)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
