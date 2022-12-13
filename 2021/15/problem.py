import sys
from pprint import pprint
import math
from copy import deepcopy


def get_input():
    in_file = (
        open(sys.argv[1])
        if len(sys.argv) > 1 and sys.argv[1] != '-'
        else sys.stdin
    )
    return [[int(x) for x in line.strip()] for line in in_file]


def make_graph(weights):
    edges = {}
    sx = len(weights[0])
    sy = len(weights)

    for y in range(sy):
        for x in range(sx):
            n = sx * y + x
            w = weights[y][x]
            if x > 0:
                edges.setdefault(n - 1, []).append((n, w))
            if x < sx - 1:
                edges.setdefault(n + 1, []).append((n, w))
            if y > 0:
                edges.setdefault(n - sx, []).append((n, w))
            if y < sy - 1:
                edges.setdefault(n + sx, []).append((n, w))

    return edges, sx, sy


def bellman_ford(edges, sx, sy):
    # Bellman-Ford
    inf_distance = 100000000
    dist = [inf_distance for _ in range(sx * sy)]
    prev = [-1 for _ in range(sx * sy)]
    dist[0] = 0
    for _ in range(sx * sy):
        for u, u_edges in edges.items():
            for v, w in u_edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
    return dist, prev


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

    def add_at(self, u: int, p: int) -> None:
        self._count += 1
        self._buckets[p].add(u)
        if p < self._min_p:
            self._min_p = p

    def move(self, u: int, p_old: int, p_new: int) -> None:
        self._buckets[p_old].remove(u)
        self._buckets[p_new].add(u)
        if p_new < self._min_p:
            self._min_p = p_new

    def empty(self) -> bool:
        return self._count == 0


def dijkstra_with_bucket_queue(edges, sx, sy):
    # Dijkstra with bucket queue
    max_dist = (sx + sy) * 9
    bq = BucketQueue(max_dist)
    dist = [max_dist for _ in range(sx * sy)]
    prev = [-1 for _ in range(sx * sy)]
    bq.add_at(0, 0)
    dist[0] = 0
    for n in range(1, sx * sy):
        bq.add_at(n, max_dist)

    while not bq.empty():
        u = bq.extract_min()
        for v, w in edges[u]:
            d = dist[u] + w
            if d < dist[v]:
                bq.move(v, dist[v], d)
                dist[v] = d
                prev[v] = u

    return dist, prev


def a(weights):
    edges, sx, sy = make_graph(weights)
    # dist, _ = bellman_ford(edges, sx, sy)
    dist, _ = dijkstra_with_bucket_queue(edges, sx, sy)
    dst = sx * sy - 1
    print(dist[dst])


def augment_weights(weights: list):
    sy = len(weights)
    sx = len(weights[0])
    new_weights = [[0 for _ in range(sx * 5)] for _ in range(sy * 5)]
    for dy in range(5):
        for dx in range(5):
            for y in range(sy):
                for x in range(sx):
                    new_weights[sy*dy + y][sx*dx + x] = (
                        ((weights[y][x] - 1 + dy + dx) % 9) + 1
                    )
    return new_weights


def print_weights(weights):
    for row in weights:
        print(''.join(map(str, row)))


def b(weights):
    large_weights = augment_weights(weights)
    edges, sx, sy = make_graph(large_weights)
    dist, _ = dijkstra_with_bucket_queue(edges, sx, sy)
    print(dist[sx * sy - 1])


def main():
    weights = get_input()
    a(weights)
    print()
    b(weights)


if __name__ == '__main__':
    main()
