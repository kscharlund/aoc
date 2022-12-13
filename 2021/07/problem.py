import sys
from pprint import pprint
import math


def get_input():
    return [int(x) for x in sys.stdin.readline().split(',')]


def a(positions, cost=lambda x: x):
    x_min, x_max = min(positions), max(positions)
    costs = [
        sum(cost(abs(p - x)) for p in positions) for x in range(x_min, x_max + 1)
    ]
    print(min(costs))


def b(positions):
    a(positions, lambda c: c * (c + 1) // 2)


def main():
    positions = get_input()
    a(positions)
    print()
    b(positions)


if __name__ == '__main__':
    main()
