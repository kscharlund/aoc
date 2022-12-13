from collections import deque
import sys
from pprint import pprint
import math


def height(cc):
    if cc == "S":
        return ord("a")
    if cc == "E":
        return ord("z")
    return ord(cc)


def get_data():
    grid = open(sys.argv[1]).read().splitlines()
    rows, cols = len(grid), len(grid[0])
    adj = [[] for _ in range(rows * cols)]
    src = dst = -1
    srcs = []
    for row in range(rows):
        for col in range(cols):
            idx = row * cols + col
            cc = grid[row][col]
            if cc == "S":
                src = idx
                cc = "a"
            elif cc == "E":
                dst = idx
                cc = "z"
            if cc == "a":
                srcs.append(idx)
            hh = ord(cc) - 1
            if row > 0 and hh <= height(grid[row - 1][col]):
                adj[idx].append((row - 1) * cols + col)
            if row + 1 < rows and hh <= height(grid[row + 1][col]):
                adj[idx].append((row + 1) * cols + col)
            if col > 0 and hh <= height(grid[row][col - 1]):
                adj[idx].append(row * cols + col - 1)
            if col + 1 < cols and hh <= height(grid[row][col + 1]):
                adj[idx].append(row * cols + col + 1)
    return adj, src, dst, srcs


def bfs_distance(adj, src):
    dist = [-1 for _ in range(len(adj))]
    dist[src] = 0
    queue = deque([src])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def a(data):
    adj, src, dst, _ = data
    b((adj, src, dst, [src]))


def b(data):
    adj, _, dst, srcs = data
    dists = []
    dist = bfs_distance(adj, dst)
    for src in srcs:
        dists.append(dist[src])
    print(min(dist for dist in dists if dist >= 0))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
