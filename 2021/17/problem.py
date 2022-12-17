import re
import sys
from pprint import pprint
import math


def get_data():
    return tuple(
        int(s)
        for s in re.match(
            r"\D*?(-?\d+)\D*?(-?\d+)\D*?(-?\d+)\D*?(-?\d+)",
            open(sys.argv[1]).read(),
        ).groups()
    )


def a(data):
    x_min, x_max, y_min, y_max = data
    for xv in range(1, x_min):
        if x_min <= sum(range(xv + 1)) <= x_max:
            break

    yv = -y_min - 1
    print(sum(range(yv + 1)))


def b(data):
    x_min, x_max, y_min, y_max = data
    solutions = set()
    for xv in range(1, x_max + 1):
        for yv in range(y_min, -y_min):
            x, y = 0, 0
            xvt, yvt = xv, yv
            while y >= y_min:
                x += xvt
                y += yvt
                xvt = max(0, xvt - 1)
                yvt -= 1
                if x_min <= x <= x_max and y_min <= y <= y_max:
                    solutions.add((xv, yv))
    print(len(solutions))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
