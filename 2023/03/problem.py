import sys
from pprint import pprint
import math


def get_data():
    data = open(sys.argv[1]).read().splitlines()
    grid = {}
    numbers = []
    symbols = []
    for row, line in enumerate(data):
        curr_num = []
        start, end = -1, -1
        for col, sym in enumerate(line):
            if curr_num:
                if sym.isdigit():
                    curr_num.append(sym)
                    end = col
                else:
                    for x in range(start, end + 1):
                        grid[(row, x)] = ("n", len(numbers))
                    numbers.append((int("".join(curr_num)), row, (start, end + 1)))
                    curr_num = []
                    if sym != ".":
                        grid[(row, col)] = ("s", len(symbols))
                        symbols.append((sym, row, col))
            elif sym.isdigit():
                start = end = col
                curr_num.append(sym)
            elif sym != ".":
                grid[(row, col)] = ("s", len(symbols))
                symbols.append((sym, row, col))
        if curr_num:
            for x in range(start, end + 1):
                grid[(row, x)] = ("n", len(numbers))
            numbers.append((int("".join(curr_num)), row, (start, end + 1)))
    return grid, numbers, symbols


def include_number(grid, row, sc, ec):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            for x in range(sc, ec):
                t = (row + dy, x + dx)
                if t in grid and grid[t][0] == "s":
                    return True
    return False


def a(data):
    grid, numbers, _ = data
    included_numbers = [
        val for val, row, (sc, ec) in numbers if include_number(grid, row, sc, ec)
    ]
    print(sum(included_numbers))


def adjacent_numbers(grid, row, col):
    number_indices = set()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            t = (row + dy, col + dx)
            if t in grid and grid[t][0] == "n":
                number_indices.add(grid[t][1])
    return number_indices


def b(data):
    grid, numbers, symbols = data
    res = 0
    for symbol, row, col in symbols:
        if symbol != "*":
            continue
        number_indices = adjacent_numbers(grid, row, col)
        if len(number_indices) == 2:
            res += math.prod(numbers[i][0] for i in number_indices)
    print(res)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
