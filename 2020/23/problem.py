import sys
from pprint import pprint
import math


def read_cups():
    return [int(x) - 1 for x in sys.stdin.readline().strip()]


def get_next_cups(cups):
    next_cup = [-1 for _ in range(len(cups))]
    for ii in range(len(cups) - 1):
        next_cup[cups[ii]] = cups[ii + 1]
    next_cup[cups[-1]] = cups[0]
    return next_cup


def print_next_cups(next_cup, cur):
    cups = [cur]
    cup = next_cup[cur]
    while cup != cur:
        cups.append(cup)
        cup = next_cup[cup]
    pprint([cup + 1 for cup in cups])


def move_cups(next_cup, cur, iters):
    # print_next_cups(next_cup, cur)
    for move in range(iters):
        if iters > 100 and (move % (iters // 72)) == 0:
            sys.stdout.write('-')
            sys.stdout.flush()
        moved_1 = next_cup[cur]
        moved_2 = next_cup[moved_1]
        moved_3 = next_cup[moved_2]
        next_cup[cur] = next_cup[moved_3]
        dst = (cur - 1) % len(next_cup)
        while dst in {moved_1, moved_2, moved_3}:
            dst = (dst - 1) % len(next_cup)
        next_cup[moved_3] = next_cup[dst]
        next_cup[dst] = moved_1
        cur = next_cup[cur]
        # print_next_cups(next_cup, cur)
    if iters > 100:
        print()
    return next_cup


def a(cups):
    next_cup = get_next_cups(cups)
    next_cup = move_cups(next_cup, cups[0], 100)
    output = []
    cup = next_cup[0]
    while cup != 0:
        output.append(str(cup + 1))
        cup = next_cup[cup]
    print(''.join(output))


def b(cups):
    next_cup = get_next_cups(cups)
    next_cup = move_cups(next_cup, cups[0], 10000000)
    lo = next_cup[0]
    hi = next_cup[lo]
    print(lo + 1, hi + 1)
    print((lo + 1) * (hi + 1))


def main():
    cups = read_cups()
    a(cups)
    print()
    b(cups + [cup for cup in range(9, 1000000)])


if __name__ == '__main__':
    main()
