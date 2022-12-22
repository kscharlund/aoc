from __future__ import annotations

import sys
from pprint import pprint
import math


class Op:
    def __init__(self, operation, args):
        self.operation = operation
        self.args = args

    def eval(self, names: dict[str, Op], name, humn=None, part_b=False):
        if part_b:
            lhs, rhs = self.args
            left = names[lhs].eval(names, lhs, humn)
            right = names[rhs].eval(names, rhs, humn)
            return left - right

        if name == "humn" and humn is not None:
            return humn

        match self.operation:
            case "c":
                return self.args
            case "+":
                lhs, rhs = self.args
                return names[lhs].eval(names, lhs, humn) + names[rhs].eval(
                    names, rhs, humn
                )
            case "-":
                lhs, rhs = self.args
                return names[lhs].eval(names, lhs, humn) - names[rhs].eval(
                    names, rhs, humn
                )
            case "*":
                lhs, rhs = self.args
                return names[lhs].eval(names, lhs, humn) * names[rhs].eval(
                    names, rhs, humn
                )
            case "/":
                lhs, rhs = self.args
                return names[lhs].eval(names, lhs, humn) / names[rhs].eval(
                    names, rhs, humn
                )


def make_op(line):
    parts = line.split()
    if len(parts) == 1:
        return Op("c", int(parts[0]))
    assert len(parts) == 3
    return Op(parts[1], (parts[0], parts[2]))


def get_data():
    return {
        name: make_op(rest)
        for name, rest in map(lambda line: line.split(": "), open(sys.argv[1]))
    }


def a(data):
    print(int(data["root"].eval(data, "root")))


def b(data):
    fn = lambda x: data["root"].eval(data, "root", x, True)

    lo, hi = [1e10, 1e13]
    for _ in range(1000):
        mi = (hi + lo) // 2
        if abs(fn(mi)) < 1e-5:
            print(int(mi))
            break

        if fn(mi) * fn(lo) < 0:
            hi = mi
        else:
            lo = mi


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
