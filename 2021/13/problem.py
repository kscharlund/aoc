import sys
from pprint import pprint
import math


def get_input():
    dots = set()
    for line in sys.stdin:
        if not line.strip():
            break
        x, y = map(int, line.split(','))
        dots.add((x, y))
    folds = []
    for line in sys.stdin:
        assert line.startswith('fold along ')
        axis, coord = line.split()[-1].split('=')
        folds.append((axis, int(coord)))
    return dots, folds


def mirror(c, f):
    return c if c < f else 2 * f - c


def fold(dots, axis, coord):
    return {
        (
            mirror(x, coord) if axis == 'x' else x,
            mirror(y, coord) if axis == 'y' else y,
        ) for x, y in dots
    }


def print_dots(dots):
    max_x = max(x for x, _ in dots)
    max_y = max(y for _, y in dots)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in dots:
                sys.stdout.write('#')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')


def a(dots, folds):
    axis, coord = folds[0]
    folded_dots = fold(dots, axis, coord)
    print(len(folded_dots))


def b(dots, folds):
    for axis, coord in folds:
        dots = fold(dots, axis, coord)
    print_dots(dots)


def main():
    dots, folds = get_input()
    a(dots, folds)
    print()
    b(dots, folds)


if __name__ == '__main__':
    main()
