from collections import Counter, defaultdict
import sys
from pprint import pprint
import math


def get_data():
    return open(sys.argv[1]).read().strip()


ROCKS = [
    ((0, 3),),
    ((1, 1), (0, 2), (1, 1)),
    ((0, 2), (2, 2), (2, 2)),
    ((0, 0), (0, 0), (0, 0), (0, 0)),
    ((0, 1), (0, 1)),
]


def repeat(seq):
    pos = 0
    while True:
        yield seq[pos], pos
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


def height(columns):
    return max(max(col) for col in columns)


def a(data):
    columns = [{0} for _ in range(7)]
    rock_gen = repeat(ROCKS)
    push_gen = repeat(data)
    for _ in range(2022):
        rock, _ = next(rock_gen)
        at_rest = False
        x, y = 2, height(columns) + 4
        while not at_rest:
            dir, _ = next(push_gen)
            x, y = push(x, y, rock, dir, columns)
            x, y, at_rest = fall(x, y, rock, columns)
            if at_rest:
                for dy, (lo, ro) in enumerate(rock):
                    for dx in range(lo, ro + 1):
                        columns[x + dx].add(y + dy)
    print(height(columns))


def b(data):
    columns = [{0} for _ in range(7)]
    rock_gen = repeat(ROCKS)
    push_gen = repeat(data)
    cycle_len = 0
    rocks_before_cycle = 0
    happenings = {}
    for rock_n in range(15000):
        if cycle_len:
            break
        rock, rt = next(rock_gen)
        at_rest = False
        x, y = 2, height(columns) + 4
        while not at_rest:
            dir, dt = next(push_gen)
            x, y = push(x, y, rock, dir, columns)
            x, y, at_rest = fall(x, y, rock, columns)
            if at_rest:
                for dy, (lo, ro) in enumerate(rock):
                    for dx in range(lo, ro + 1):
                        columns[x + dx].add(y + dy)
                if (rt, dt, x) in happenings:
                    rocks_before_cycle, height_before_cycle = happenings[(rt, dt, x)]
                    cycle_len = rock_n - rocks_before_cycle
                    cycle_height = height(columns) - height_before_cycle
                else:
                    happenings[(rt, dt, x)] = (rock_n, height(columns))

    full_iters = (1000000000000 - rocks_before_cycle) // cycle_len
    remaining_rocks = 1000000000000 - full_iters * cycle_len
    print(f"{rocks_before_cycle=}, {cycle_len=}, {cycle_height=}, {remaining_rocks=}")

    columns = [{0} for _ in range(7)]
    rock_gen = repeat(ROCKS)
    push_gen = repeat(data)
    for rock_n in range(remaining_rocks):
        rock, _ = next(rock_gen)
        at_rest = False
        x, y = 2, height(columns) + 4
        while not at_rest:
            dir, _ = next(push_gen)
            x, y = push(x, y, rock, dir, columns)
            x, y, at_rest = fall(x, y, rock, columns)
            if at_rest:
                for dy, (lo, ro) in enumerate(rock):
                    for dx in range(lo, ro + 1):
                        columns[x + dx].add(y + dy)
    rows = height(columns)

    print(rows + full_iters * cycle_height)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
