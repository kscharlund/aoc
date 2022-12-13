import itertools
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
        (line[: len(line) // 2], line[len(line) // 2 :].strip())
        for line in open(sys.argv[1])
    ]


def get_prio(common):
    assert len(common) == 1
    c = ord(common.pop())
    return c - 64 + 26 if c <= 90 else c - 96


def a(data):
    pprint(sum([get_prio(set(lh) & set(rh)) for lh, rh in data]))


def b(data):
    res = 0
    for ii in range(0, len(data), 3):
        common = set(data[ii][0] + data[ii][1])
        for offset in range(1, 3):
            common &= set(data[ii + offset][0] + data[ii + offset][1])
        res += get_prio(common)
    print(res)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
