import sys
from pprint import pprint
import math
from copy import deepcopy


class Grid:
    def __init__(self, vals):
        self.vals = vals
        self.sy = len(vals)
        self.sx = len(vals[0])
        self.flashed = set()

    def neighbors(self, y, x):
        for dy in -1, 0, 1:
            for dx in -1, 0, 1:
                if dy == 0 and dx == 0:
                    continue
                if 0 <= y + dy < self.sy and 0 <= x + dx < self.sx:
                    yield y + dy, x + dx

    def increment(self):
        self.flashed.clear()
        to_flash = set()
        for y in range(self.sy):
            for x in range(self.sx):
                self.vals[y][x] += 1
                if self.vals[y][x] > 9:
                    to_flash.add((y, x))
        return to_flash

    def flash(self, to_flash):
        to_flash_next = set()
        for y, x in to_flash:
            self.flashed.add((y, x))
            self.vals[y][x] = 0
            for ny, nx in self.neighbors(y, x):
                if (ny, nx) in self.flashed.union(to_flash):
                    continue
                self.vals[ny][nx] += 1
                if self.vals[ny][nx] > 9:
                    to_flash_next.add((ny, nx))
        return to_flash_next


def get_input():
    return [[int(x) for x in line.strip()] for line in sys.stdin]


def a(vals):
    grid = Grid(deepcopy(vals))
    n_flashes = 0
    for _ in range(100):
        to_flash = grid.increment()
        while to_flash:
            to_flash = grid.flash(to_flash)
        n_flashes += len(grid.flashed)
    print(n_flashes)

def b(vals):
    grid = Grid(deepcopy(vals))
    i = 0
    while True:
        i += 1
        to_flash = grid.increment()
        while to_flash:
            to_flash = grid.flash(to_flash)
        n_flashes = len(grid.flashed)
        if n_flashes == grid.sy * grid.sx:
            print(i)
            break


def main():
    vals = get_input()
    a(vals)
    print()
    b(vals)


if __name__ == '__main__':
    main()
