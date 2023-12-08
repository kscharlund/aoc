import itertools
import sys
from pprint import pprint
import math


def get_data():
    with open(sys.argv[1]) as input:
        steps = input.readline().strip()
        nodes = {}
        for line in input:
            if ' = ' not in line:
                continue
            lhs, rhs = line.strip().split(' = ')
            l, r = rhs.split(', ')
            nodes[lhs] = (l[1:], r[:-1])
        return steps, nodes


def a(data):
    steps, nodes = data
    curr = 'AAA'
    step_count = 0
    for dir in itertools.cycle(steps):
        curr = nodes[curr][0 if dir == 'L' else 1]
        step_count += 1
        if curr == 'ZZZ':
            break
    print(step_count)


def b(data):
    steps, nodes = data
    starts = [node for node in nodes if node.endswith('A')]
    pprint(starts)
    step_counts = [0 for _ in starts]
    for i, curr in enumerate(starts):
        for dir in itertools.cycle(steps):
            curr = nodes[curr][0 if dir == 'L' else 1]
            step_counts[i] += 1
            if curr.endswith('Z'):
                # NOTE: Only works if there is only one end node in each cycle.
                break
    pprint(step_counts)
    a = step_counts[0]
    for b in step_counts[1:]:
        a = b * (a // math.gcd(a, b))
    print(a)


def main():
    data = get_data()
    # a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
