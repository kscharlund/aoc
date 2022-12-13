from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__} took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


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

    def __len__(self) -> int:
        return self._count


def dijkstra_with_bucket_queue(edges, size, src):
    # Edges should be a dict or list indexed by nodes, containing a list
    # of adjacent (node, weight) pairs.
    # Nodes are integers.
    max_dist = size
    bq = BucketQueue(max_dist)
    dist = [max_dist for _ in range(size)]
    prev = [-1 for _ in range(size)]
    bq.add_at(src, 0)
    dist[src] = 0
    for n in range(size):
        if n != src:
            bq.add_at(n, max_dist)

    while bq:
        u = bq.extract_min()
        for v, w in edges[u]:
            d = dist[u] + w
            if d < dist[v]:
                bq.move(v, dist[v], d)
                dist[v] = d
                prev[v] = u

    return dist, prev
