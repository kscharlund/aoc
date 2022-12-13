from functools import cmp_to_key
import sys
from pprint import pprint
import math


def get_packet_pairs():
    packet_pairs = []
    for lines in open(sys.argv[1]).read().split("\n\n"):
        lp, rp = lines.splitlines()
        packet_pairs.append((eval(lp), eval(rp)))
    return packet_pairs


def get_packet_list():
    packets = []
    for line in open(sys.argv[1]):
        if not line.strip():
            continue
        packets.append(eval(line.strip()))
    packets.append([[2]])
    packets.append([[6]])
    return packets


def cmp(li, ri):
    return (li > ri) - (li < ri)


def cmp_packets(lp, rp):
    if isinstance(lp, int) and isinstance(rp, int):
        return cmp(lp, rp)
    if isinstance(lp, int):
        return cmp_packets([lp], rp)
    if isinstance(rp, int):
        return cmp_packets(lp, [rp])
    for i in range(min(len(lp), len(rp))):
        c = cmp_packets(lp[i], rp[i])
        if c:
            return c
    return cmp(len(lp), len(rp))


def a(data):
    right_order = []
    for i, (lp, rp) in enumerate(data):
        if cmp_packets(lp, rp) < 0:
            right_order.append(i + 1)
    print(sum(right_order))


def b(data: list):
    data.sort(key=cmp_to_key(cmp_packets))
    res = 1
    for i, p in enumerate(data):
        if p in [[[2]], [[6]]]:
            res *= i + 1
    print(res)


def main():
    data = get_packet_pairs()
    a(data)
    print()
    data = get_packet_list()
    b(data)


if __name__ == "__main__":
    main()
