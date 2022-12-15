import re
import sys
from pprint import pprint
import math


def get_data():
    coords = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    return [
        tuple(int(c) for c in coords.match(line).groups()) for line in open(sys.argv[1])
    ]


def merge_ranges(ranges: list[tuple[int, int]]):
    ranges.sort()
    lo_0, hi_0 = ranges[0]
    for lo, hi in ranges[1:]:
        if lo <= hi_0 + 1:
            hi_0 = max(hi, hi_0)
        else:
            yield (lo_0, hi_0)
            lo_0, hi_0 = lo, hi
    yield (lo_0, hi_0)


def a(data):
    target_row = 10 if "tiny" in sys.argv[1] else 2000000
    target_beacons = set()
    excluded_ranges = []
    for sx, sy, bx, by in data:
        max_dist = abs(sx - bx) + abs(sy - by)
        target_dist = abs(sy - target_row)
        n_cols = max_dist - target_dist
        if n_cols >= 0:
            excluded_ranges.append((sx - n_cols, sx + n_cols))
        if by == target_row:
            target_beacons.add(bx)
    excluded = 0
    for lo, hi in merge_ranges(excluded_ranges):
        excluded += hi - lo + 1 - sum(lo <= bx <= hi for bx in target_beacons)
    print(excluded)


def b(data):
    size = 20 if "tiny" in sys.argv[1] else 4000000
    for row in range(size + 1):
        excluded_ranges = []
        for sx, sy, bx, by in data:
            max_dist = abs(sx - bx) + abs(sy - by)
            target_dist = abs(sy - row)
            n_cols = max_dist - target_dist
            if n_cols >= 0:
                excluded_ranges.append((max(0, sx - n_cols), min(sx + n_cols, size)))
        merged = list(merge_ranges(excluded_ranges))
        if len(merged) > 1:
            r1, r2 = merged
            x1 = r2[0] - 1
            x2 = r1[1] + 1
            assert x1 == x2
            print(x1, row, row + x1 * 4000000)
            break


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
