import sys
from pprint import pprint
from math import prod


def a(adapters):
    diffs = [b - a for a, b in zip([0] + adapters, adapters + [adapters[-1]+3])]
    hist = {}
    for diff in diffs:
        hist[diff] = hist.get(diff, 0) + 1
    print(hist[1] * hist[3])


num_combs = [1, 1, 2, 4, 7]


def b(adapters):
    # Note: this solution does not work if there are 2-diffs.
    diffs = [b - a for a, b in zip([0] + adapters, adapters + [adapters[-1]+3])]
    runs = []
    rlen = 0
    for diff in diffs:
        if diff == 1:
            rlen += 1
        else:
            if rlen:
                runs.append(rlen)
            rlen = 0
    print(prod(num_combs[run] for run in runs))


def b_dp(adapters):
    diffs = [b - a for a, b in zip([0] + adapters, adapters + [adapters[-1]+3])]
    # w_n is the number of paths to (J_i - n) where J_i is the joltage of the i:th adapter.
    # Starting at J_0 = 0, there is one way (the outlet). There are 0 ways to -1 and -2.
    w_0, w_1, w_2 = (1, 0, 0)
    for diff in diffs:
        if diff == 1:
            # J_{i+1} := J_i + 1
            w_0, w_1, w_2 = (w_0 + w_1 + w_2,
                             w_0,
                             w_1)
        elif diff == 2:
            # J_{i+1} := J_i + 2
            w_0, w_1, w_2 = (w_0 + w_1,
                             0,
                             w_0)
        elif diff == 3:
            # J_{i+1} := J_i + 3
            w_0, w_1, w_2 = (w_0,
                             0,
                             0)
        else:
            raise ValueError('Impossible input')
    print(w_0)


def b_rec(adapters):
    output = adapters[-1]
    adapters = set(adapters)
    cache = {}
    def ways(joltage):
        if joltage in cache:
            return cache[joltage]
        if joltage == 0:
            return 1
        if joltage < 0:
            return 0
        if joltage in adapters:
            res = ways(joltage - 1) + ways(joltage - 2) + ways(joltage - 3)
            cache[joltage] = res
            return res
        return 0
    print(ways(output))


def main():
    adapters = list(sorted(int(line.strip()) for line in sys.stdin.readlines()))
    a(adapters)
    print()
    b(adapters)
    print()
    b_dp(adapters)
    print()
    b_rec(adapters)


if __name__ == '__main__':
    main()
