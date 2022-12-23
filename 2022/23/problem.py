from collections import Counter, defaultdict
import sys
from pprint import pprint
import math


def get_data():
    pos = set()
    for y, line in enumerate(open(sys.argv[1])):
        for x, char in enumerate(line):
            if char == "#":
                pos.add((y, x))
    return pos


def all_neighbors(pos):
    y, x = pos
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy or dx:
                yield y + dy, x + dx


def y_neighbors(pos, dy):
    y, x = pos
    for dx in (-1, 0, 1):
        yield y + dy, x + dx


def x_neighbors(pos, dx):
    y, x = pos
    for dy in (-1, 0, 1):
        yield y + dy, x + dx


def print_grid(curr):
    ys = {y for y, x in curr}
    xs = {x for y, x in curr}
    print("-" * (max(xs) - min(xs) + 1))
    for y in range(min(ys), max(ys) + 1):
        for x in range(min(xs), max(xs) + 1):
            sys.stdout.write("#" if (y, x) in curr else " ")
        print()
    print()


def a(data, n_iters=10):
    curr: set[tuple[int, int]] = data
    size = len(curr)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n_iters):
        prop = Counter()
        back = defaultdict(list)
        for pos in curr:
            if any(n in curr for n in all_neighbors(pos)):
                for dy, dx in moves:
                    y, x = pos
                    n_pos = y + dy, x + dx
                    if (dy and not any(n in curr for n in y_neighbors(pos, dy))) or (
                        dx and not any(n in curr for n in x_neighbors(pos, dx))
                    ):
                        prop[n_pos] += 1
                        back[n_pos].append(pos)
                        break
                else:
                    prop[pos] += 1
            else:
                prop[pos] += 1

        next = set()
        for pos, count in prop.items():
            if count > 1:
                for b_pos in back[pos]:
                    next.add(b_pos)
            else:
                assert count == 1
                next.add(pos)

        assert len(next) == size
        # print_grid(next)
        if curr == next:
            return i + 1
        curr = next
        moves = moves[1:] + moves[:1]

    ys = {y for y, x in curr}
    xs = {x for y, x in curr}
    h, w = max(ys) - min(ys) + 1, max(xs) - min(xs) + 1
    print(h * w - size)
    return i + 1


def b(data):
    iters = a(data, 10000000)
    print(iters)


def main():
    data = get_data()
    a(data)
    print()
    data = get_data()
    b(data)


if __name__ == "__main__":
    main()
