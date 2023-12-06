import sys
from pprint import pprint
import math


def get_data():
    with open(sys.argv[1]) as input:
        times = [int(t) for t in input.readline().split(':')[-1].strip().split()]
        dists = [int(d) for d in input.readline().split(':')[-1].strip().split()]
    return list(zip(times, dists))


def a(data):
    res = 1
    for t, d in data:
        dis = t**2 - 4*(d + 1e-9)
        assert dis > 0
        tmp = math.sqrt(dis)
        res *= math.floor((t + tmp) / 2) - math.ceil((t - tmp) / 2) + 1
    # pprint(data)
    print(res)


def b(data):
    with open(sys.argv[1]) as input:
        time = int("".join(input.readline().split(':')[-1].strip().split()))
        dist = int("".join(input.readline().split(':')[-1].strip().split()))
        a([(time, dist)])


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
