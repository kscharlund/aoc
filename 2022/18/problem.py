from collections import deque
import sys
from pprint import pprint
import math


def get_data():
    return {tuple(int(c) for c in line.split(",")) for line in open(sys.argv[1])}


def neighbors(point):
    z, y, x = point
    yield (z - 1, y, x)
    yield (z + 1, y, x)
    yield (z, y - 1, x)
    yield (z, y + 1, x)
    yield (z, y, x - 1)
    yield (z, y, x + 1)


def a(data):
    sides = 0
    for point in data:
        sides += sum(n not in data for n in neighbors(point))
    print(sides)


def flood_fill_internal(data, src):
    assert src not in data
    queue = deque([src])
    fill = set()
    fill.add(src)
    while queue:
        u = queue.popleft()
        for v in neighbors(u):
            if any(c < 0 or c > 21 for c in v):
                # Reached the border, this point is not internal.
                # Throw away the fill.
                return
            if v not in data and v not in fill:
                fill.add(v)
                queue.append(v)
    data |= fill


def flood_fill_all_internal(data):
    max_z, max_y, max_x = (
        max(z for z, y, x in data),
        max(y for z, y, x in data),
        max(x for z, y, x in data),
    )
    mid = (max_z // 2 + 1, max_y // 2 + 1, max_x // 2 + 1)
    if mid not in data:
        flood_fill_internal(data, mid)
    for z in range(max_z + 1):
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                p = (z, y, x)
                if p in data:
                    continue
                flood_fill_internal(data, p)


def b(data):
    flood_fill_all_internal(data)

    # max_z, max_y, max_x = (
    #     max(z for z, y, x in data),
    #     max(y for z, y, x in data),
    #     max(x for z, y, x in data),
    # )
    # print(f"{max_z=} {max_y=} {max_x=}")
    # for z in range(max_z + 1):
    #     print(f"{z=}")
    #     for y in range(max_y + 1):
    #         line = "".join("#" if (z, y, x) in data else " " for x in range(max_x + 1))
    #         print(line)
    #     print()

    a(data)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
