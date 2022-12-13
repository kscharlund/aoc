import sys
from pprint import pprint
import math

def get_input():
    lines = []
    for line in sys.stdin:
        p1, p2 = line.split(' -> ')
        lines.append((
            tuple(int(v) for v in p1.split(',')),
            tuple(int(v) for v in p2.split(',')),
        ))
    return lines


def a(lines):
    board = {}
    crossings = set()

    for p1, p2 in lines:
        x1, y1 = p1
        x2, y2 = p2
        if x1 != x2 and y1 != y2:
            continue
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                board[(x, y)] = board.get((x, y), 0) + 1
                if board[(x, y)] > 1:
                    crossings.add((x, y))

    print(len(crossings))


def b(lines):
    board = {}
    crossings = set()

    for p1, p2 in lines:
        x1, y1 = p1
        x2, y2 = p2
        dx = -1 if x2 < x1 else (1 if x2 > x1 else 0)
        dy = -1 if y2 < y1 else (1 if y2 > y1 else 0)
        x, y = x1, y1
        while True:
            board[(x, y)] = board.get((x, y), 0) + 1
            if board[(x, y)] > 1:
                crossings.add((x, y))
            if x == x2 and y == y2:
                break
            x, y = x + dx, y + dy

    print(len(crossings))


def main():
    lines = get_input()
    a(lines)
    print()
    b(lines)


if __name__ == '__main__':
    main()
