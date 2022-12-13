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
    return [line.split() for line in open(sys.argv[1])]


def a(data):
    wanted_cycles = {20, 60, 100, 140, 180, 220}
    reg, cycle = 1, 1
    results = []
    for op in data:
        if cycle in wanted_cycles:
            results.append(reg)

        if len(op) > 1:
            if cycle + 1 in wanted_cycles:
                results.append(reg)
            reg += int(op[1])
            cycle += 2
        else:
            cycle += 1
    pprint(results)
    print(sum(r * c for r, c in zip(results, sorted(wanted_cycles))))


def b(data):
    calc = []
    reg = 1
    output = ["" for _ in range(6)]
    for cycle in range(240):
        row = cycle // 40
        col = cycle % 40
        if abs(reg - col) <= 1:
            output[row] += "#"
        else:
            output[row] += " "
        if not calc:
            op, data = data[0], data[1:]
            if len(op) > 1:
                calc.append(int(op[1]))
        else:
            reg += calc.pop()
        cycle += 1
    print("\n".join(output))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
