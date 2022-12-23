from itertools import zip_longest
import re
import sys
from pprint import pprint
import math


def get_data():
    grid_data, move_data = open(sys.argv[1]).read().split("\n\n")
    grid = grid_data.splitlines()
    y_size = len(grid)
    x_size = max(len(row) for row in grid)
    blockages = set()
    x_starts = []
    x_ends = []
    y_starts = [None for _ in range(x_size)]
    y_ends = [None for _ in range(x_size)]
    for y, row in enumerate(grid):
        xs = None
        for x, char in enumerate(row):
            if char == "#":
                blockages.add((y, x))
            if char in ".#" and xs is None:
                xs = x - 1
            if char in ".#" and y_starts[x] is None:
                y_starts[x] = y - 1
            if char == " " and y_starts[x] is not None and y_ends[x] is None:
                y_ends[x] = y
        x_starts.append(xs)
        x_ends.append(x + 1)
        for x in range(x + 1, x_size):
            if y_ends[x] is None:
                y_ends[x] = y
    for x in range(x_size):
        if y_ends[x] is None:
            y_ends[x] = y + 1

    moves = [int(x) for x in re.split("[RL]", move_data)]
    rotations = [x for x in re.split("\d+", move_data) if x.strip()]

    return (
        blockages,
        list(zip(x_starts, x_ends)),
        list(zip(y_starts, y_ends)),
        moves,
        rotations,
        (0, x_starts[0] + 1),
    )


def execute_moves(blockages, warps, moves, rotations, start):
    y, x = start
    dy, dx = 0, 1
    for i, (move, rotation) in enumerate(zip_longest(moves, rotations, fillvalue="")):
        for _ in range(move):
            ny, nx = y + dy, x + dx
            ny, nx, ndy, ndx = warps.get((ny, nx, dy, dx), (ny, nx, dy, dx))
            # if ny >= 200 or nx >= 150:
            #     print()
            #     print(f"{x=:3d}, {y=:3d}  {dx=:2d}, {dy=:2d}")
            #     print(f"{nx=:3d}, {ny=:3d}  {ndx=:2d}, {ndy=:2d}")
            #     return
            if (ny, nx) in blockages:
                break
            y, x, dy, dx = ny, nx, ndy, ndx
        if rotation == "L":
            dy, dx = -1 * dx, dy
        if rotation == "R":
            dy, dx = dx, -1 * dy
        print(f"{x=:3d}, {y=:3d}  {dx=:2d}, {dy=:2d}")
    return y, x, dy, dx


def build_planar_warps(x_limits, y_limits):
    warps = {}
    for y, (xs, xe) in enumerate(x_limits):
        warps[(y, xs, 0, -1)] = (y, xe - 1, 0, -1)
        warps[(y, xe, 0, 1)] = (y, xs + 1, 0, 1)
    for x, (ys, ye) in enumerate(y_limits):
        warps[(ys, x, -1, 0)] = (ye - 1, x, -1, 0)
        warps[(ye, x, 1, 0)] = (ys + 1, x, 1, 0)
    return warps


def a(data):
    blockages, x_limits, y_limits, moves, rotations, start = data
    warps = build_planar_warps(x_limits, y_limits)
    y, x, dy, dx = execute_moves(blockages, warps, moves, rotations, start)
    heading_scores = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
    print((y + 1) * 1000 + (x + 1) * 4 + heading_scores[(dy, dx)])


def build_cubic_warps(x_limits, y_limits):
    warps = {}
    for x in range(50, 100):
        warps[(-1, x, -1, 0)] = (100 + x, 0, 0, 1)
        warps[(100 + x, -1, 0, -1)] = (0, x, 1, 0)
    for x in range(100, 150):
        warps[(-1, x, -1, 0)] = (199, x - 100, -1, 0)
        warps[(200, x - 100, 1, 0)] = (0, x, 1, 0)
    for y in range(0, 50):
        warps[(y, 49, 0, -1)] = (149 - y, 0, 0, 1)
        warps[(149 - y, -1, 0, -1)] = (y, 50, 0, 1)
        warps[(y, 150, 0, 1)] = (149 - y, 99, 0, -1)
        warps[(149 - y, 100, 0, 1)] = (y, 149, 0, -1)
    for y in range(50, 100):
        warps[(y, 49, 0, -1)] = (100, y - 50, 1, 0)
        warps[(99, y - 50, -1, 0)] = (y, 50, 0, 1)
        warps[(y, 100, 0, 1)] = (49, y + 50, -1, 0)
        warps[(50, y + 50, 1, 0)] = (y, 99, 0, -1)
    for x in range(50, 100):
        warps[(150, x, 1, 0)] = (x + 100, 49, 0, -1)
        warps[(x + 100, 50, 0, 1)] = (149, x, -1, 0)
    return warps


def b(data):
    blockages, x_limits, y_limits, moves, rotations, start = data
    warps = build_cubic_warps(x_limits, y_limits)
    y, x, dy, dx = execute_moves(blockages, warps, moves, rotations, start)
    heading_scores = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
    print((y + 1) * 1000 + (x + 1) * 4 + heading_scores[(dy, dx)])


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
