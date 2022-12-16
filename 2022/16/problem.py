from collections import deque
import re
import sys
from pprint import pprint
import math


def get_data():
    pattern = re.compile(r"Valve (\w+) has flow rate=(\d+);")
    adj = {}
    cap = {}
    for line in open(sys.argv[1]):
        node_name, flow_rate = pattern.match(line).groups()
        edges = {node.replace(",", "") for node in line.split(";")[-1].split()[4:]}
        adj[node_name] = edges
        cap[node_name] = int(flow_rate)

    return adj, cap


def bfs_distance(adj, src):
    dist = {node: -1 for node in adj}
    dist[src] = 0
    queue = deque([src])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def get_distances(adj):
    dist = {}
    for node in adj:
        dist[node] = bfs_distance(adj, node)
    return dist


def possible_paths(dist, nodes, path, pos, time=30):
    for node in nodes:
        cost = dist[pos][node] + 1
        if cost < time:
            yield from possible_paths(
                dist, nodes - {node}, path + [node], node, time - cost
            )
    yield path


def total_release(visit_orders, dist, cap, time_limit=30):
    release = 0
    for visit_order in visit_orders:
        pos = "AA"
        time = time_limit
        for node in visit_order:
            time -= dist[pos][node] + 1
            assert time > 0
            release += time * cap[node]
            pos = node
    return release


def a(data):
    adj, cap = data
    dist = get_distances(adj)
    nodes = {node for node, flow in cap.items() if flow}
    max_release = max(
        total_release([path], dist, cap)
        for path in possible_paths(dist, nodes, [], "AA")
    )
    print(max_release)


def b(data):
    adj, cap = data
    dist = get_distances(adj)
    nodes = {node for node, flow in cap.items() if flow}
    max_release = max(
        total_release([path_a, path_b], dist, cap, 26)
        for path_a in possible_paths(dist, nodes, [], "AA", 26)
        for path_b in possible_paths(dist, nodes - set(path_a), [], "AA", 26)
    )
    print(max_release)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
