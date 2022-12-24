from collections import defaultdict, deque
import sys
from pprint import pprint
import math


x_size = 0
y_size = 0


def get_data():
    global x_size, y_size
    lines = open(sys.argv[1]).read().splitlines()
    y_size = len(lines) - 2
    x_size = len(lines[0]) - 2
    src = (-1, 0)
    dst = (y_size, x_size - 1)
    assert lines[src[0] + 1][src[1] + 1] == "."
    assert lines[dst[0] + 1][dst[1] + 1] == "."
    blizzards = {d: set() for d in "^v<>"}
    for y, line in enumerate(lines[1:-1]):
        for x, char in enumerate(line[1:-1]):
            if char in blizzards:
                blizzards[char].add((y, x))
    return src, dst, blizzards


def is_free(pos, t, blizzards):
    y, x = pos
    if ((y - t) % y_size, x) in blizzards["v"]:
        return False
    if ((y + t) % y_size, x) in blizzards["^"]:
        return False
    if (y, (x - t) % x_size) in blizzards[">"]:
        return False
    if (y, (x + t) % x_size) in blizzards["<"]:
        return False
    return True


def within_bounds(pos, src, dst):
    y, x = pos
    return pos in {src, dst} or (0 <= y < y_size and 0 <= x < x_size)


def adj(pos, t, src, dst, blizzards):
    y, x = pos
    for dy in (1, -1, 0):
        for dx in (1, -1, 0):
            n_pos = (y + dy, x + dx)
            if not (dy and dx):
                if n_pos == src and pos != src:
                    continue
                free = is_free(n_pos, t + 1, blizzards)
                bds = within_bounds(n_pos, src, dst)
                if free and bds:
                    yield n_pos


def bfs_distance(src, dst, blizzards, t0=0):
    queue = deque([(src, t0)])
    visited = {(src, t0)}
    while queue:
        u, t = queue.popleft()
        for v in adj(u, t, src, dst, blizzards):
            if v == dst:
                return t + 1
            nxt = (v, t + 1)
            if nxt not in visited:
                queue.append(nxt)
                visited.add(nxt)
    return None


def a(data):
    src, dst, blizzards = data
    print(bfs_distance(src, dst, blizzards))


def b(data):
    src, dst, blizzards = data
    t = 0
    for _ in range(3):
        t = bfs_distance(src, dst, blizzards, t)
        print(t)
        src, dst = dst, src


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
