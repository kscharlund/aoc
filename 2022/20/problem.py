from __future__ import annotations
from dataclasses import dataclass
import sys
from pprint import pprint
import math


@dataclass
class Node:
    val: int
    prev: Node | None = None
    next: Node | None = None

    def __str__(self) -> str:
        return f"Node({self.val}, prev={self.prev.val if self.prev else self.prev}, next={self.next.val if self.next else self.next})"


def get_data():
    nodes = [Node(int(line.strip())) for line in open(sys.argv[1])]
    for ii in range(len(nodes)):
        nodes[ii].prev = nodes[ii - 1]
        nodes[ii - 1].next = nodes[ii]
    return nodes


def print_nodes(start: Node, factor: int) -> None:
    tmp = start
    while True:
        sys.stdout.write(f"{tmp.val*factor} ")
        tmp = tmp.next
        if tmp == start:
            print()
            break


def a(data: list[Node], factor=1, iters=1):
    mod = len(data) - 1
    zero_node = None
    for node in data:
        if not node.val:
            zero_node = node
    assert zero_node

    for _ in range(iters):
        for node in data:
            moves = (node.val * factor) % mod
            if moves > len(data) // 2:
                moves = moves - mod
            if not moves:
                continue
            prev, next = node.prev, node.next
            # Remove node from list
            prev.next, next.prev = node.next, node.prev
            # Execute moves
            if moves < 0:
                for _ in range(-moves):
                    prev = prev.prev
                next = prev.next
            else:
                for _ in range(moves):
                    next = next.next
                prev = next.prev
            # Insert node into list
            # print(f"Inserting {node} between {prev} and {next}")
            node.prev, node.next = prev, next
            prev.next, next.prev = node, node

    tmp = zero_node
    res = 0
    for _ in range(3):
        for _ in range(1000):
            tmp = tmp.next
        res += tmp.val * factor

    print(res)


def b(data):
    a(data, 811589153, 10)


def main():
    data = get_data()
    a(data)
    print()
    data = get_data()
    b(data)


if __name__ == "__main__":
    main()
