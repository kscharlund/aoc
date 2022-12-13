import sys
from pprint import pprint
import math


def get_input():
    in_file = (
        open(sys.argv[1])
        if len(sys.argv) > 1 and sys.argv[1] != '-'
        else sys.stdin
    )
    return ''.join(f'{int(h, 16):04b}' for h in in_file.readline().strip())


def parse_packet(packet_str):
    v, t, rest = (
        int(packet_str[0:3], 2), int(packet_str[3:6], 2), packet_str[6:]
    )
    if t == 4:
        parse_literal(rest)
    else:
        lt, rest = rest[0], rest[1:]
        if lt == '0':
            packet_bits, rest = int(rest[:15], 2), rest[15:]
            return (t, parse_packet(rest[:packet_bits]))
        else:
            n_packets, rest = int(rest[:11], 2), rest[11:]
            pass


def a(bin_packet_str):
    v, t, rest = (
        int(bin_packet_str[0:3], 2),
        int(bin_packet_str[3:6], 2),
        bin_packet_str[6:]
    )
    if t == 4:
        parse_literal(rest)
    else:
        lt, rest = rest[0], rest[1:]
        if lt == '0':
            packet_bits, rest = int(rest[:15], 2), rest[15:]
            pass
        else:
            n_packets, rest = int(rest[:11], 2), rest[11:]
            pass


def b(bin_packet_str):
    pass


def main():
    bin_packet_str = get_input()
    a(bin_packet_str)
    print()
    b(bin_packet_str)


if __name__ == '__main__':
    main()
