import sys
from pprint import pprint
import math


DELTAS = {
    'e': (0, 1),
    'w': (0, -1),
    'ne': (1, 0.5),
    'se': (-1, 0.5),
    'nw': (1, -0.5),
    'sw': (-1, -0.5),
}

def split_directions(line):
    ii = 0
    directions = []
    while ii < len(line):
        if line[ii] in {'s', 'n'}:
            directions.append(DELTAS[line[ii:ii+2]])
            ii += 2
        else:
            directions.append(DELTAS[line[ii]])
            ii += 1
    return directions


def read_input():
    return [split_directions(line.strip()) for line in sys.stdin]


def a(tiles):
    black = set()
    for tile in tiles:
        yy, xx = 0, 0
        for dy, dx in tile:
            yy += dy
            xx += dx
        coord = (yy, xx)
        if coord in black:
            black.remove(coord)
        else:
            black.add(coord)
    print(len(black))
    return black


def iterate(black):
    neighbors = {}
    for yy, xx in black:
        for dy, dx in DELTAS.values():
            coord = (yy + dy, xx + dx)
            neighbors[coord] = neighbors.get(coord, 0) + 1
    return {
        coord for coord, count in neighbors.items()
        if (
            (coord in black and 1 <= count <= 2)
            or (coord not in black and count == 2)
        )
    }


def b(black):
    for _ in range(100):
        black = iterate(black)
    print(len(black))


def main():
    tiles = read_input()
    black = a(tiles)
    print()
    b(black)


if __name__ == '__main__':
    main()
