import sys
from pprint import pprint
import math


def get_input():
    return [int(x) for x in sys.stdin.readline().split(',')]


def a(initial_fish, n_generations=80):
    n_in_generation = [0 for _ in range(9)]
    for fish in initial_fish:
        n_in_generation[fish] += 1
    for _ in range(n_generations):
        n_in_generation = n_in_generation[1:] + n_in_generation[:1]
        n_in_generation[6] += n_in_generation[8]
    print(sum(n_in_generation))


def b(initial_fish):
    a(initial_fish, 256)


def main():
    initial_fish = get_input()
    a(initial_fish)
    print()
    b(initial_fish)


if __name__ == '__main__':
    main()
