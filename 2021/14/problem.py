import sys
from pprint import pprint
import math


def get_input():
    start = sys.stdin.readline().strip()
    sys.stdin.readline()
    mapping = {}
    for line in sys.stdin:
        src, add = [x.strip() for x in line.split(' -> ')]
        mapping[src] = add
    return mapping, start


def a(mapping, start, n=10):
    hist = {}
    for c in start:
        hist[c] = hist.get(c, 0) + 1
    pair_hist = {}
    for pair in [x + y for x, y in zip(start[:-1], start[1:])]:
        pair_hist[pair] = pair_hist.get(pair, 0) + 1

    for _ in range(n):
        it = pair_hist.copy()
        for pair, count in it.items():
            add = mapping[pair]
            hist[add] = hist.get(add, 0) + count
            p1, p2 = pair[0] + add, add + pair[1]
            pair_hist[p1] = pair_hist.get(p1, 0) + count
            pair_hist[p2] = pair_hist.get(p2, 0) + count
            pair_hist[pair] = pair_hist.get(pair, 0) - count

    rank = sorted(hist, key=lambda x: hist[x])
    print(hist[rank[-1]] - hist[rank[0]])


def b(mapping, start):
    a(mapping, start, 40)


def main():
    mapping, start = get_input()
    a(mapping, start)
    print()
    b(mapping, start)


if __name__ == '__main__':
    main()
