from collections import defaultdict
import sys
from pprint import pprint
import math
from typing import Any


class BucketQueue:
    def __init__(self, max_dist: int):
        self._buckets = [set() for _ in range(max_dist + 1)]
        self._count = 0
        self._min_p = 0

    def extract_min(self) -> int:
        assert self._count
        self._count -= 1
        for p in range(self._min_p, len(self._buckets)):
            if self._buckets[p]:
                self._min_p = p
                return self._buckets[p].pop()

    def add_at(self, u: Any, p: int) -> None:
        self._count += 1
        self._buckets[p].add(u)
        if p < self._min_p:
            self._min_p = p

    def move(self, u: Any, p_old: int, p_new: int) -> None:
        self._buckets[p_old].remove(u)
        self._buckets[p_new].add(u)
        if p_new < self._min_p:
            self._min_p = p_new

    def __len__(self) -> int:
        return self._count


def shortest_allowed_path(edges, src, max_dist, is_b=False):
    bq = BucketQueue(max_dist)
    dist = {}
    max_n = 3 if not is_b else 10

    for node in edges:
        if node == src:
            continue
        for du in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for n in range(max_n):
                bq.add_at((node, du, n), max_dist)
                dist[(node, du, n)] = max_dist

    bq.add_at((src, (0, 0), 0), 0)
    dist[(src, (0, 0), 0)] = 0
    for du in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        for n in range(max_n):
            dist[(src, du, n)] = 0

    while bq:
        us = bq.extract_min()
        u, du, nu = us
        for v, w in edges[u]:
            dv = (v[0] - u[0], v[1] - u[1])
            nv = (nu + 1) if du == dv else 0
            if nv >= max_n:
                continue
            if du[0] == -dv[0] and du[1] == -dv[1]:
                continue
            if is_b and nu < 3 and du != dv and u != src:
                continue

            vs = (v, dv, nv)
            d = dist[us] + w
            if d < dist[vs]:
                bq.move(vs, dist[vs], d)
                dist[vs] = d

    return dist


def get_data():
    grid = open(sys.argv[1]).read().splitlines()
    n_rows = len(grid)
    n_cols = len(grid[0])
    edges = defaultdict(list)
    for row, line in enumerate(grid):
        for col, ws in enumerate(line):
            v = (row, col)
            w = int(ws)
            if row - 1 >= 0:
                edges[(row - 1, col)].append((v, w))
            if row + 1 < n_rows:
                edges[(row + 1, col)].append((v, w))
            if col - 1 >= 0:
                edges[(row, col - 1)].append((v, w))
            if col + 1 < n_cols:
                edges[(row, col + 1)].append((v, w))
    return edges, n_rows, n_cols


def a(data):
    edges, n_rows, n_cols = data
    dist = shortest_allowed_path(edges, (0, 0), n_rows * n_cols * 9)
    print(min(cost for u, cost in dist.items() if u[0] == (n_rows - 1, n_cols - 1)))


def b(data):
    edges, n_rows, n_cols = data
    dist = shortest_allowed_path(edges, (0, 0), n_rows * n_cols * 9, True)
    print(min(cost for u, cost in dist.items() if u[0] == (n_rows - 1, n_cols - 1)))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
