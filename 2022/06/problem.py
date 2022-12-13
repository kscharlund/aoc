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
    return [line.strip() for line in open(sys.argv[1])]


def find_marker(line, window_size):
    for start in range(len(line)):
        end = start + window_size
        if len(set(line[start:end])) == window_size:
            return end
    return None


def a(data):
    for line in data:
        print(find_marker(line, 4))


def b(data):
    for line in data:
        print(find_marker(line, 14))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
