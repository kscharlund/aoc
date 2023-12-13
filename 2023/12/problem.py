from collections import Counter
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
    data = []
    for line in open(sys.argv[1]):
        line, groups_str = line.split()
        groups = tuple(int(x) for x in groups_str.split(','))
        data.append((line, groups))
    return data


@memoize
def count_valid_combinations(arg):
    line, groups, prefix = arg
    # print(line, groups, prefix)
    if not groups:
        # Nothing more to match, make sure we have no more '#':s.
        return 1 if not prefix and '#' not in line else 0
    if not line:
        # Still want matches, but no more string. Make sure we have the right prefix.
        return 1 if len(groups) == 1 and groups[0] == prefix else 0
    if prefix > groups[0]:
        # Early out from impossible situations.
        return 0

    if line[0] == '.':
        return (count_valid_combinations((line[1:], groups[1:], 0)) if prefix == groups[0] else 0) if prefix else count_valid_combinations((line[1:], groups, 0))
    if line[0] == '#':
        return count_valid_combinations((line[1:], groups, prefix + 1))
    return count_valid_combinations((line[1:], groups, prefix + 1)) + ((count_valid_combinations((line[1:], groups[1:], 0)) if prefix == groups[0] else 0) if prefix else count_valid_combinations((line[1:], groups, 0)))


def a(data):
    print(sum(count_valid_combinations((line, groups, 0)) for line, groups in data))


def b(data):
    print(sum(count_valid_combinations((f'{line}?{line}?{line}?{line}?{line}', groups * 5, 0)) for line, groups in data))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
