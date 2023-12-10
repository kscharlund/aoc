from collections import deque
import sys
from pprint import pprint
import math


EDGE_TEMPLATES = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((1, 0), (0, -1)),
    'F': ((1, 0), (0, 1)),
}


def get_data():
    edges, start, n_rows, n_cols = {}, None, 0, 0

    for row, line in enumerate(open(sys.argv[1]), start=1):
        for col, node in enumerate(line.strip(), start=1):
            for dy, dx in EDGE_TEMPLATES.get(node, ()):
                edges.setdefault((row, col), set()).add((row + dy, col + dx))
            if node == 'S':
                start = (row, col)
            n_cols = max(col, n_cols)
        n_rows = max(row, n_rows)

    row, col = start
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if start in edges.get((row + dy, col + dx), set()):
            edges.setdefault(start, set()).add((row + dy, col + dx))

    return edges, start, n_rows, n_cols


def bfs_distance(adj, src):
    # When adj is a dict of lists (nodes can be anything):
    dist = {node: -1 for node in adj}
    # When adj is a list of lists (nodes are int from 0 to len(adj)-1):
    # dist = [-1 for node in range(len(adj))]
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
    edges, start, _, _ = data
    print(max(bfs_distance(edges, start).values()))


def b(data):
    edges, start, n_rows, n_cols = data
    loop_nodes = set(node for node, dist in bfs_distance(edges, start).items() if dist >= 0)

    # Algorithm from https://stackoverflow.com/questions/14685739/find-all-inner-grid-points-of-a-polygon-made-up-from-neighbouring-grid-points
    vertical_edges = {}
    for row in range(1, n_rows + 1, 2):
        for col in range(1, n_cols + 1):
            if (row, col) in loop_nodes and (row + 1, col) in edges[(row, col)]:
                vertical_edges.setdefault(row, []).append(col)

    interior_points = set()
    for row in range(1, n_rows + 1, 2):
        if row not in vertical_edges:
            continue
        inside = False
        e0 = vertical_edges[row][0]
        for e1 in vertical_edges[row][1:]:
            inside = not inside
            if inside:
                for col in range(e0, e1 + 1):
                    if (row, col) not in loop_nodes:
                        interior_points.add((row, col))
                    if (row + 1, col) not in loop_nodes:
                        interior_points.add((row + 1, col))
            e0 = e1
    pprint(len(interior_points))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
