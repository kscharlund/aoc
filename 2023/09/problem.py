import sys
from pprint import pprint
import math


def get_data():
    return [
        [int(x) for x in line.split()]
        for line in open(sys.argv[1])
    ]


def diff(seq):
    return [n - m for m, n in zip(seq[:-1], seq[1:])]


def a(data):
    res = 0
    for seq in data:
        ends = [seq[-1]]
        while not all(n == seq[-1] for n in seq):
            seq = diff(seq)
            ends.append(seq[-1])
        res += sum(ends)
    print(res)


def b(data):
    res = 0
    for seq in data:
        firsts = [seq[0]]
        while not all(n == seq[0] for n in seq):
            seq = diff(seq)
            firsts.append(seq[0])
        f = 0
        for n in reversed(firsts):
            f = n - f
        res += f
    print(res)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
