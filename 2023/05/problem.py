import sys
from pprint import pprint
import math


def get_data():
    data = open(sys.argv[1]).read().splitlines()
    seeds = []
    maps = []
    current_map = None
    for line in data:
        if line.startswith("seeds:"):
            seeds = [int(s) for s in line.split(": ")[-1].split()]
        elif line.endswith("map:"):
            if current_map:
                maps.append(current_map)
            current_map = []
        elif not line.strip():
            continue
        else:
            current_map.append([int(s) for s in line.split()])
    maps.append(current_map)
    return seeds, maps


def a(data):
    seeds, maps = data
    min_val = -1
    for seed in seeds:
        for map in maps:
            for ds, ss, ml in map:
                if seed in range(ss, ss + ml):
                    seed = ds + (seed - ss)
                    break
        min_val = min(seed, min_val) if min_val >= 0 else seed
    print(min_val)


def map_ranges(src_ranges, map):
    dst_ranges = []
    for ds, ss, ml in map:
        me = ss + ml - 1
        remaining = []
        for rs, rl in src_ranges:
            re = rs + rl - 1
            if rs < ss:
                remaining.append((rs, min(rl, ss - rs + 1)))
            s = max(rs, ss)
            e = min(re, me)
            if e - s + 1 > 0:
                dst_ranges.append((ds + s - ss, e - s + 1))
            if re > me:
                s = max(me + 1, rs)
                remaining.append((s, re - s + 1))
        src_ranges = remaining
    dst_ranges += src_ranges
    dst_ranges.sort()
    return dst_ranges


def b(data):
    seeds, maps = data
    seed_ranges = [(s, l) for s, l in zip(seeds[::2], seeds[1::2])]
    for map in maps:
        seed_ranges = map_ranges(seed_ranges, map)
    print(seed_ranges[0][0])


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
