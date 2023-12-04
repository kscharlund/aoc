from collections import deque
import sys
from pprint import pprint
import math


def get_data():
    data = []
    for line in open(sys.argv[1]):
        header, rest = line.split(": ")
        winners, drawn = rest.split(" | ")
        data.append(
            (set(int(x) for x in winners.split()), set(int(x) for x in drawn.split()))
        )
    return data


def a(data):
    print(
        sum(
            (1 << len(winners & drawn) - 1) if (winners & drawn) else 0
            for winners, drawn in data
        )
    )


def b(data):
    factors = [1 for _ in range(len(data))]
    n_cards = 0
    for i, (winners, drawn) in enumerate(data):
        factor = factors[i]
        for j in range(len(winners & drawn)):
            factors[i + j + 1] += factor
        n_cards += factor
        print(factor, n_cards, factors)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
