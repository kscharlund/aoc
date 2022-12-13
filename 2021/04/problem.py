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


def parse_board(lines):
    rows = [set(line) for line in lines]
    cols = [set(line[col] for line in lines) for col in range(5)]
    return rows + cols


def get_input():
    draws = [int(num) for num in sys.stdin.readline().split(',')]
    lines = [
        [int(x) for x in line.split()] for line in sys.stdin if line.strip()
    ]
    assert not (len(lines) % 5)
    boards = [parse_board(lines[i:i+5]) for i in range(0, len(lines), 5)]
    return draws, boards


def is_winner(board, drawn):
    return any((x & drawn) == x for x in board)


def remaining_numbers(board, drawn):
    remaining = set()
    for x in board:
        remaining |= x - drawn
    return remaining


def a(draws, boards):
    drawn = set()
    for num in draws:
        drawn.add(num)
        for board in boards:
            if is_winner(board, drawn):
                print(num * sum(remaining_numbers(board, drawn)))
                return


def b(draws, boards):
    drawn = set()
    has_won = set()
    for num in draws:
        drawn.add(num)
        for i, board in enumerate(boards):
            if is_winner(board, drawn):
                has_won.add(i)
                if len(has_won) == len(boards):
                    print(num * sum(remaining_numbers(board, drawn)))
                    return


def main():
    draws, boards = get_input()
    a(draws, boards)
    print()
    b(draws, boards)


if __name__ == '__main__':
    main()
