import sys
from pprint import pprint
import math


def get_data():
    return open(sys.argv[1]).read().strip()


ROCKS = [
    [(0, 3)],
    [(1, 1), (0, 2), (1, 1)],
    [(0, 2), (2, 2), (2, 2)],
    [(0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 1), (0, 1)],
]


def repeat(seq):
    pos = 0
    while True:
        yield seq[pos]
        pos = (pos + 1) % len(seq)


def push(x, y, rock, direction, columns):
    dx = -1 if direction == "<" else 1
    # Handle wall
    if x + dx < 0 or x + dx + max(ro for _, ro in rock) > 6:
        return x, y
    # Handle rocks at rest
    for dy, (lo, ro) in enumerate(rock):
        offset = lo if direction == "<" else ro
        if y + dy in columns[x + dx + offset]:
            return x, y
    return x + dx, y


def fall(x, y, rock, columns):
    for dy, (lo, ro) in enumerate(rock):
        for dx in range(lo, ro + 1):
            if y + dy - 1 in columns[x + dx]:
                return x, y, True
    return x, y - 1, False


def a(data):
    columns = [{0} for _ in range(7)]
    rock_gen = repeat(ROCKS)
    push_gen = repeat(data)
    for _ in range(2022):
        rock = next(rock_gen)
        at_rest = False
        x, y = 2, max(max(col) for col in columns) + 4
        while not at_rest:
            x, y = push(x, y, rock, next(push_gen), columns)
            x, y, at_rest = fall(x, y, rock, columns)
            if at_rest:
                for dy, (lo, ro) in enumerate(rock):
                    for dx in range(lo, ro + 1):
                        columns[x + dx].add(y + dy)
    print(max(max(col) for col in columns))


def b(data):
    columns = [{0} for _ in range(7)]
    rock_gen = repeat(ROCKS)
    push_gen = repeat(data)
    floor_y = [0]
    floor_r = [0]
    cycle_len = 0
    for rock_n in range(500000):
        if cycle_len:
            break
        rock = next(rock_gen)
        at_rest = False
        x, y = 2, max(max(col) for col in columns) + 4
        while not at_rest:
            x, y = push(x, y, rock, next(push_gen), columns)
            x, y, at_rest = fall(x, y, rock, columns)
            if at_rest:
                for dy, (lo, ro) in enumerate(rock):
                    for dx in range(lo, ro + 1):
                        columns[x + dx].add(y + dy)
                    if all(y + dy in col for col in columns):
                        print(f"Created a floor at {y+dy} with rock {rock_n+1}")
                        floor_y.append(y + dy)
                        floor_r.append(rock_n)
                        for pcl in range(2, len(floor_y) // 2):
                            yd = [y2 - y1 for y2, y1 in zip(floor_y[1:], floor_y[:-1])]
                            c1 = [r for r in yd[-pcl:]]
                            c2 = [r for r in yd[-(2 * pcl) : -pcl]]
                            if c1 == c2:
                                cycle_len = len(c1)
                                break

    rocks_before_cycle = floor_r[-2 * (cycle_len + 1)]
    rows_before_cycle = floor_y[-2 * (cycle_len + 1)]
    print(f"{rocks_before_cycle=}, {rows_before_cycle=}")
    rocks_in_cycle = floor_r[-1] - floor_r[-cycle_len - 1]
    rows_in_cycle = floor_y[-1] - floor_y[-cycle_len - 1]
    print(f"{rocks_in_cycle=}, {rows_in_cycle=}")
    full_iters = (1000000000000 - rocks_before_cycle) // rocks_in_cycle
    remaining_rocks = 1000000000000 - full_iters * rocks_in_cycle
    print(remaining_rocks)

    columns = [{0} for _ in range(7)]
    rock_gen = repeat(ROCKS)
    push_gen = repeat(data)
    for rock_n in range(remaining_rocks):
        rock = next(rock_gen)
        at_rest = False
        x, y = 2, max(max(col) for col in columns) + 4
        while not at_rest:
            x, y = push(x, y, rock, next(push_gen), columns)
            x, y, at_rest = fall(x, y, rock, columns)
            if at_rest:
                for dy, (lo, ro) in enumerate(rock):
                    for dx in range(lo, ro + 1):
                        columns[x + dx].add(y + dy)
    rows = max(max(col) for col in columns)

    print(rows + full_iters * rows_in_cycle)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
