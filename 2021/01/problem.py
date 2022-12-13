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


def a(measurements):
    prev = None
    increases = 0
    for val in measurements:
        if prev is not None and val > prev:
            increases += 1
        prev = val
    print(increases)


def b(measurements):
    windows = [
        sum(t)
        for t in zip(measurements[:-2], measurements[1:-1], measurements[2:])
    ]
    a(windows)


def main():
    measurements = [int(line) for line in sys.stdin]
    a(measurements)
    print()
    b(measurements)


if __name__ == '__main__':
    main()
