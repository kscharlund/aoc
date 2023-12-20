from collections import defaultdict, deque
import sys
from pprint import pprint
import math


def get_data():
    data = []
    for line in open(sys.argv[1]):
        d, n, r = line.split()
        data.append((d, int(n), r))
    return data


def neighbors(y, x):
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        yield (y + dy, x + dx)


def flood_fill(data, src):
    assert src not in data
    queue = deque([src])
    fill = set()
    fill.add(src)
    while queue:
        u = queue.popleft()
        for v in neighbors(*u):
            if v not in data and v not in fill:
                fill.add(v)
                queue.append(v)
    data |= fill


def a(data):
    dys = {'U': -1, 'D': 1}
    dxs = {'L': -1, 'R': 1}
    pos = (0, 0)
    visited = {pos}
    for d, n, _ in data:
        y, x = pos
        dy = dys.get(d, 0)
        dx = dxs.get(d, 0)
        if dy:
            ny = n * dy + y
            for ty in range(y + 1, ny + 1) if dy > 0 else range(ny, y):
                visited.add((ty, x))
            pos = (ny, x)
        else:
            nx = n * dx + x
            for tx in range(x + 1, nx + 1) if dx > 0 else range(nx, x):
                visited.add((y, tx))
            pos = (y, nx)
    max_y = max(p[0] for p in visited)
    max_x = max(p[1] for p in visited)
    min_y = min(p[0] for p in visited)
    min_x = min(p[1] for p in visited)
    print(f'{min_y=} {max_y=} {min_x=} {max_x=}')
    #flood_fill(visited, (-168, 40))
    print(len(visited))
    # for y in range(min_y, max_y + 1):
    #     for x in range(min_x, max_x + 1):
    #         if (y, x) in visited:
    #             sys.stdout.write('#')
    #         else:
    #             sys.stdout.write('.')
    #     sys.stdout.write('\n')


def polygon_area(corners, distances):
    ys = [p[0] for p in corners]
    xs = [p[1] for p in corners]
    yps = list(zip(ys[:-1], ys[1:]))
    xps = list(zip(xs[:-1], xs[1:]))
    # TODO: Verify even sums here?
    shoelace_area = sum((y0 + y1) * (x0 - x1) for (y0, y1), (x0, x1) in zip(yps, xps)) // 2
    edge_area = sum(distances) // 2 + 1
    return shoelace_area + edge_area


def b(data):
    dys = {'U': -1, 'D': 1}
    dxs = {'L': -1, 'R': 1}
    dmap = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    pos = (0, 0)
    corners = [pos]
    distances = []
    for _, _, i in data:
        d = dmap[i[-2]]
        n = int(i[2:-2], 16)

        y, x = pos
        dy = dys.get(d, 0)
        dx = dxs.get(d, 0)
        if dy:
            pos = (n * dy + y, x)
        else:
            pos = (y, n * dx + x)
        corners.append(pos)
        distances.append(n)

    print(polygon_area(corners, distances))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
