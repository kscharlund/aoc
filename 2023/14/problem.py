from collections import defaultdict
import sys
from pprint import pprint
import math


def get_data():
    rocks, blocks = set(), set()
    for row, line in enumerate(open(sys.argv[1])):
        for col, c in enumerate(line.strip()):
            if c == '#':
                blocks.add((row, col))
            if c == 'O':
                rocks.add((row, col))
    return frozenset(rocks), blocks, row + 1, col + 1

class Grid:
    def __init__(self, blocks, N, M):
        self.blocks = blocks
        self.N = N
        self.M = M

    def tilt_north(self, rocks):
        new_rocks = set()
        for col in range(self.M):
            block = 0
            for row in range(self.N):
                if (row, col) in self.blocks:
                    block = row + 1
                if (row, col) in rocks:
                    new_rocks.add((block, col))
                    block += 1
        return frozenset(new_rocks)

    def tilt_west(self, rocks):
        new_rocks = set()
        for row in range(self.N):
            block = 0
            for col in range(self.M):
                if (row, col) in self.blocks:
                    block = col + 1
                if (row, col) in rocks:
                    new_rocks.add((row, block))
                    block += 1
        return frozenset(new_rocks)

    def tilt_south(self, rocks):
        new_rocks = set()
        for col in range(self.M):
            block = self.N - 1
            for row in reversed(range(self.N)):
                if (row, col) in self.blocks:
                    block = row - 1
                if (row, col) in rocks:
                    new_rocks.add((block, col))
                    block -= 1
        return frozenset(new_rocks)

    def tilt_east(self, rocks):
        new_rocks = set()
        for row in range(self.N):
            block = self.M - 1
            for col in reversed(range(self.M)):
                if (row, col) in self.blocks:
                    block = col - 1
                if (row, col) in rocks:
                    new_rocks.add((row, block))
                    block -= 1
        return frozenset(new_rocks)

    def print_rocks(self, rocks):
        for row in range(self.N):
            for col in range(self.M):
                if (row, col) in rocks:
                    sys.stdout.write('O')
                elif (row, col) in self.blocks:
                    sys.stdout.write('#')
                else:
                    sys.stdout.write('.')
            sys.stdout.write('\n')


def a(data):
    rocks, blocks, N, M = data
    grid = Grid(blocks, N, M)
    new_rocks = grid.tilt_north(rocks)
    print(sum(N - row for row, col in new_rocks))


def tilt_cycle(rocks, grid):
    return grid.tilt_east(grid.tilt_south(grid.tilt_west(grid.tilt_north(rocks))))


def b(data):
    rocks, blocks, N, M = data
    grid = Grid(blocks, N, M)
    iter = 0
    states = {rocks: 0}
    cycle_start = cycle_end = -1
    while True:
        iter += 1
        rocks = tilt_cycle(rocks, grid)
        if rocks in states:
            print(f'Cycle found, {iter} same as {states[rocks]}')
            cycle_start = states[rocks]
            cycle_end = iter - 1
            break
        states[rocks] = iter
    idx = (1000000000 - cycle_start) % (cycle_end - cycle_start + 1) + cycle_start
    final_rocks = list(states)[idx]
    print(sum(N - row for row, col in final_rocks))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
