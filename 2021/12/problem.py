import sys
from pprint import pprint
import math


def get_input():
    adj = {}
    for line in sys.stdin:
        src, dst = line.strip().split('-')
        if dst != 'start':
            adj.setdefault(src, []).append(dst)
        if src != 'start':
            adj.setdefault(dst, []).append(src)
    return adj


def visit(adj, src, results, path, dual_node=None):
    path = path + (src,)
    for dst in adj[src]:
        if dst == 'end':
            results.add(path + ('end',))
        elif (
            dst.isupper()
            or dst not in path
            or (dst == dual_node and sum(v == dst for v in path) < 2)
        ):
            visit(adj, dst, results, path, dual_node)


def a(adj):
    results = set()
    visit(adj, 'start', results, tuple())
    print(len(results))


def b(adj):
    results = set()
    for node in adj:
        if node.islower() and node not in {'start', 'end'}:
            visit(adj, 'start', results, tuple(), node)
    print(len(results))


def main():
    adj = get_input()
    a(adj)
    print()
    b(adj)


if __name__ == '__main__':
    main()
