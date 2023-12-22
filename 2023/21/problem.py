import sys
from pprint import pprint
import math


def get_data():
    blocks = set()
    start = None
    for row, line in enumerate(open(sys.argv[1])):
        for col, c in enumerate(line.strip()):
            if c == "#":
                blocks.add((row, col))
            if c == "S":
                start = (row, col)
    return blocks, start, row + 1, col + 1


def a(data):
    blocks, start, n_rows, n_cols = data

    def neighbors(pt):
        y, x = pt
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < n_rows and 0 <= nx < n_cols and (ny, nx) not in blocks:
                yield (ny, nx)

    positions = {start}
    for _ in range(64):
        positions = {n for p in positions for n in neighbors(p)}
    print(len(positions))


def b(data):
    blocks, start, n_rows, n_cols = data

    def neighbors(pt):
        y, x = pt
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if (ny % n_rows, nx % n_cols) not in blocks:
                yield (ny, nx)

    positions = {start}
    iters = 0
    while True:
        iters += 1
        positions = {n for p in positions for n in neighbors(p)}
        if ((iters - 65) % 131) == 0:
            print(len(positions))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
