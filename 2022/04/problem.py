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
    return [
        [tuple(int(n) for n in p.split("-")) for p in line.strip().split(",")]
        for line in open(sys.argv[1])
    ]


def overlap_a(lp, rp):
    return (lp[0] <= rp[0] and lp[1] >= rp[1]) or (lp[0] >= rp[0] and lp[1] <= rp[1])


def overlap_b(lp, rp):
    return (rp[0] <= lp[0] <= rp[1]) or (lp[0] <= rp[0] <= lp[1])


def a(data):
    print(sum(overlap_a(lp, rp) for lp, rp in data))


def b(data):
    print(sum(overlap_b(lp, rp) for lp, rp in data))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
