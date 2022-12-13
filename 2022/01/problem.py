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


def read_sorted_inventory_sums() -> list[int]:
    inventories = []
    current_inventory = []
    for line in open(sys.argv[1]):
        if not line.strip():
            inventories.append(current_inventory)
            current_inventory = []
        else:
            current_inventory.append(int(line))
    inventories.append(current_inventory)
    return sorted(sum(inv) for inv in inventories)


def sum_of_n_largest(elems: list[int], n: int) -> int:
    return sum(elems[-n:])


def a():
    print(sum_of_n_largest(read_sorted_inventory_sums(), 1))


def b():
    print(sum_of_n_largest(read_sorted_inventory_sums(), 3))


def main():
    a()
    print()
    b()


if __name__ == "__main__":
    main()
