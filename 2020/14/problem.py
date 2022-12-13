import sys
from pprint import pprint
from math import prod


def parse_mask(mask):
    or_mask = sum(2**(35-i) if bit == '1' else 0 for i, bit in enumerate(mask))
    and_mask = sum(2**(35-i) if bit != '0' else 0 for i, bit in enumerate(mask))
    return or_mask, and_mask


def a(writes):
    or_mask = 0
    and_mask = 2**36 - 1
    mem = {}
    for target, value in writes:
        if target == 'mask':
            or_mask, and_mask = parse_mask(value)
        else:
            value = int(value)
            mem[target] = or_mask | (and_mask & value)
    print(sum(val for val in mem.values()))


def get_concrete_addresses(mask, target):
    n_writes = mask.count('X')
    for nn in range(2**n_writes):
        address = 0
        nx = 0
        for ii, bit in enumerate(reversed(mask)):
            if bit == 'X':
                address |= (1 << ii) if (nn & (1 << nx)) else 0
                nx += 1
            elif bit == '1':
                address |= (1 << ii)
            else:
                address |= (target & (1 << ii))
        yield address


def b(writes):
    mask = '0' * 36
    mem = {}
    for target, value in writes:
        if target == 'mask':
            mask = value
        else:
            target = int(target.replace('mem[', '').replace(']', ''))
            value = int(value)
            for address in get_concrete_addresses(mask, target):
                mem[address] = value
    print(sum(val for val in mem.values()))


def main():
    writes = [x.strip().split(' = ') for x in sys.stdin.readlines()]
    a(writes)
    print()
    b(writes)


if __name__ == '__main__':
    main()
