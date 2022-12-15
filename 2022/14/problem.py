from collections import defaultdict
import sys
from pprint import pprint
import math


def get_data():
    columns = defaultdict(set)
    y_max = -1
    for line in open(sys.argv[1]):
        points = line.split(" -> ")
        x_prev, y_prev = -1, -1
        for point in points:
            x_curr, y_curr = [int(p) for p in point.split(",")]
            if y_curr > y_max:
                y_max = y_curr
            if x_curr == x_prev:
                for y in range(min(y_prev, y_curr), max(y_prev, y_curr) + 1):
                    columns[x_curr].add(y)
            if y_curr == y_prev:
                for x in range(min(x_prev, x_curr), max(x_prev, x_curr) + 1):
                    columns[x].add(y_curr)
            x_prev, y_prev = x_curr, y_curr
            # pprint(columns)
    return columns, y_max + 2


def a(data):
    columns, _ = data
    n_at_rest = 0
    try:
        while True:
            x_pos, y_pos = 500, 0
            at_rest = False
            while not at_rest:
                y_next = min(y for y in columns[x_pos] if y > y_pos)
                if not y_next in columns[x_pos - 1]:
                    x_pos, y_pos = x_pos - 1, y_next
                elif not y_next in columns[x_pos + 1]:
                    x_pos, y_pos = x_pos + 1, y_next
                else:
                    columns[x_pos].add(y_next - 1)
                    at_rest = True
                    n_at_rest += 1
    except ValueError:
        print(n_at_rest)


def b(data):
    columns, floor = data
    for x in range(0, 1000):
        columns[x].add(floor)
    n_at_rest = 0
    try:
        while True:
            x_pos, y_pos = 500, 0
            at_rest = False
            while not at_rest:
                y_next = min(y for y in columns[x_pos] if y >= y_pos)
                if not y_next in columns[x_pos - 1]:
                    x_pos, y_pos = x_pos - 1, y_next
                elif not y_next in columns[x_pos + 1]:
                    x_pos, y_pos = x_pos + 1, y_next
                else:
                    columns[x_pos].add(y_next - 1)
                    at_rest = True
                    n_at_rest += 1
                    if x_pos == 500 and y_next == 1:
                        raise ValueError("cave full")
    except ValueError:
        print(n_at_rest)


def main():
    data = get_data()
    a(data)
    print()
    data = get_data()
    b(data)


if __name__ == "__main__":
    main()
