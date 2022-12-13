from collections import deque
from dataclasses import dataclass
import sys
from pprint import pprint
import math
from typing import Callable


class Monkey:
    def __init__(self, desc: str):
        for line in desc.splitlines():
            if "Starting items" in line:
                self.items = deque(
                    [int(x) for x in line.split(":")[-1].strip().split(", ")]
                )
            elif "Operation" in line:
                expr = line.split(" = ")[-1]
                self.worry = lambda old: eval(expr)
            elif "Test" in line:
                self.test = int(line.split()[-1])
            elif "If true" in line:
                self.next_t = int(line.split()[-1])
            elif "If false" in line:
                self.next_f = int(line.split()[-1])


def get_data():
    return [Monkey(desc) for desc in open(sys.argv[1]).read().split("\n\n")]


def a(monkeys):
    counts = [0 for _ in monkeys]
    for round in range(20):
        for ii, monkey in enumerate(monkeys):
            while monkey.items:
                counts[ii] += 1
                item = monkey.items.popleft()
                new_item = monkey.worry(item) // 3
                next = monkey.next_f if (new_item % monkey.test) else monkey.next_t
                monkeys[next].items.append(new_item)
                print(ii, item, "->", new_item, "to", next)
    pprint(counts)
    a, b = sorted(counts)[-2:]
    print(a * b)


def b(monkeys):
    counts = [0 for _ in monkeys]
    mod = 1
    for monkey in monkeys:
        mod *= monkey.test

    for round in range(10000):
        for ii, monkey in enumerate(monkeys):
            while monkey.items:
                counts[ii] += 1
                item = monkey.items.popleft()
                new_item = monkey.worry(item) % mod
                next = monkey.next_f if (new_item % monkey.test) else monkey.next_t
                monkeys[next].items.append(new_item)
                # print(ii, item, "->", new_item, "to", next)
    pprint(counts)
    a, b = sorted(counts)[-2:]
    print(a * b)


def main():
    data = get_data()
    a(data)
    print()
    data = get_data()
    b(data)


if __name__ == "__main__":
    main()
