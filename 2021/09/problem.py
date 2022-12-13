import sys
from pprint import pprint
import math


class Grid:
    def __init__(self, vals):
        self._vals = vals
        self.sy = len(vals)
        self.sx = len(vals[0])
        self.component = [[-1 for _ in range(self.sx)] for _ in range(self.sy)]

    def get(self, y, x):
        return self._vals[y][x]

    def neighbors(self, y, x):
        if y > 0:
            yield y - 1, x
        if x > 0:
            yield y, x - 1
        if x < self.sx - 1:
            yield y, x + 1
        if y < self.sy - 1:
            yield y + 1, x

    def is_low(self, y, x):
        val = self.get(y, x)
        if all(self.get(ny, nx) > val for ny, nx in self.neighbors(y, x)):
            return True

    def mark_component(self, y, x, c, marked=0):
        self.component[y][x] = c
        marked += 1
        for ny, nx in self.neighbors(y, x):
            if self.component[ny][nx] < 0 and self.get(ny, nx) < 9:
                marked = self.mark_component(ny, nx, c, marked)
        return marked


def get_input():
    return Grid([[int(x) for x in line.strip()] for line in sys.stdin])


def a(grid):
    low_points = []
    for y in range(grid.sy):
        for x in range(grid.sx):
            if grid.is_low(y, x):
                low_points.append((y, x))
    print(sum(grid.get(y, x) + 1 for y, x in low_points))


def b(grid):
    component_sizes = []
    for y in range(grid.sy):
        for x in range(grid.sx):
            if grid.component[y][x] < 0 and grid.get(y, x) < 9:
                component_sizes.append(grid.mark_component(y, x, len(component_sizes)))
    print(math.prod(sorted(component_sizes)[-3:]))


def main():
    grid = get_input()
    a(grid)
    print()
    b(grid)


if __name__ == '__main__':
    main()
