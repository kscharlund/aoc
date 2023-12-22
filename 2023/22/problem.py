from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass, field
import sys
from pprint import pprint
import math


@dataclass
class Range:
    lo: int
    hi: int

    def coords(self):
        return range(self.lo, self.hi + 1)


@dataclass
class Brick:
    x: Range
    y: Range
    z: Range
    above: set[int] = field(default_factory=set)
    below: set[int] = field(default_factory=set)


def get_data():
    data = []
    for line in open(sys.argv[1]):
        lo, hi = line.strip().split("~")
        lo_x, lo_y, lo_z = (int(c) for c in lo.split(","))
        hi_x, hi_y, hi_z = (int(c) for c in hi.split(","))
        data.append(Brick(Range(lo_x, hi_x), Range(lo_y, hi_y), Range(lo_z, hi_z)))
    return data


def a(data: list[Brick]):
    # Settle bricks
    data.sort(key=lambda b: b.z.lo)
    brick_index = {}
    max_z = defaultdict(int)
    for i, brick in enumerate(data):
        floor_z = 0
        for x in brick.x.coords():
            for y in brick.y.coords():
                floor_z = max(max_z[(x, y)], floor_z)
        dz = brick.z.lo - (floor_z + 1)
        assert dz >= 0
        brick.z.lo -= dz
        brick.z.hi -= dz
        for x in brick.x.coords():
            for y in brick.y.coords():
                for z in brick.z.coords():
                    brick_index[(x, y, z)] = i
                if z > max_z[(x, y)]:
                    max_z[(x, y)] = z
                if (x, y, floor_z) in brick_index:
                    j = brick_index[(x, y, floor_z)]
                    data[j].above.add(i)
                    brick.below.add(j)

    count = 0
    for brick in data:
        if not brick.above or all(len(data[bi].below) > 1 for bi in brick.above):
            count += 1
    print(count)


def b(data: list[Brick]):
    # Bricks already settled by a()
    count = 0
    for i in range(len(data)):
        fallen = set()
        prop = deque([i])
        while prop:
            u = prop.popleft()
            fallen.add(u)
            for v in data[u].above:
                if not data[v].below - fallen:
                    prop.append(v)
        count += len(fallen) - 1
    print(count)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
