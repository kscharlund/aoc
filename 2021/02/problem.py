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


def parse_command(line):
    cmd, arg = line.split()
    return cmd, int(arg)


def a(commands):
    x, y = 0, 0
    for cmd, arg in commands:
        if cmd == 'forward':
            x += arg
        if cmd == 'down':
            y += arg
        if cmd == 'up':
            y -= arg
    print(x * y)


def b(commands):
    x, y, z = 0, 0, 0
    for cmd, arg in commands:
        if cmd == 'forward':
            x += arg
            z += arg * y
        if cmd == 'down':
            y += arg
        if cmd == 'up':
            y -= arg
    print(x * z)


def main():
    commands = [parse_command(line) for line in sys.stdin]
    a(commands)
    print()
    b(commands)


if __name__ == '__main__':
    main()
