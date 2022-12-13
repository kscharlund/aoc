from collections import defaultdict
import sys
from pprint import pprint
import math


def memoize(func):
    """
    Memoization decorator for a function taking a single argument.
    """

    class Memodict(dict):
        """Memoization dictionary."""

        def __missing__(self, key):
            ret = self[key] = func(key)
            return ret

    return Memodict().__getitem__


def get_data():
    stacks = defaultdict(list)
    moves = []
    for line in open(sys.argv[1]):
        line = line.rstrip()
        if "[" in line:
            for ii in range(1, len(line), 4):
                if line[ii].strip():
                    stacks[ii // 4 + 1].append(line[ii])
        if line.startswith("move"):
            moves.append(tuple(int(x) for x in line.split()[1::2]))
    for stack in stacks.values():
        stack.reverse()
    pprint(stacks)
    return stacks, moves


def a(data):
    stacks, moves = data
    for nn, src, dst in moves:
        for _ in range(nn):
            v = stacks[src].pop()
            stacks[dst].append(v)
    print("".join(stacks[ii][-1] for ii in sorted(stacks.keys())))


def b(data):
    stacks, moves = data
    for nn, src, dst in moves:
        tmp = []
        for _ in range(nn):
            v = stacks[src].pop()
            tmp.append(v)
        tmp.reverse()
        stacks[dst] += tmp
    print("".join(stacks[ii][-1] for ii in sorted(stacks.keys())))


def main():
    data = get_data()
    a(data)
    print()
    data = get_data()
    b(data)


if __name__ == "__main__":
    main()
