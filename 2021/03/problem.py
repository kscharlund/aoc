import sys
from pprint import pprint
import math


def get_input():
    lines = [line.strip() for line in sys.stdin]
    n_bits = len(lines[0])
    for line in lines:
        assert len(line) == n_bits
    numbers = [int(line, 2) for line in lines]
    return numbers, n_bits


def most_common_at(numbers, bit):
    ones = sum((x >> bit) & 1 for x in numbers)
    return 1 if ones >= len(numbers) / 2 else 0


def a(numbers, n_bits):
    gamma, epsilon = 0, 0
    for bit in range(n_bits):
        most_common = most_common_at(numbers, bit)
        if most_common:
            gamma += 1 << bit
        else:
            epsilon += 1 << bit
    print(gamma, epsilon, bin(gamma), bin(epsilon), gamma * epsilon)


def b(numbers, n_bits):
    o_numbers, c_numbers = numbers[:], numbers[:]
    for bit in range(n_bits - 1, -1, -1):
        if len(o_numbers) == 1:
            break
        o_most_common = most_common_at(o_numbers, bit)
        o_numbers = [x for x in o_numbers if ((x >> bit) & 1) == o_most_common]

    for bit in range(n_bits - 1, -1, -1):
        if len(c_numbers) == 1:
            break
        c_most_common = most_common_at(c_numbers, bit)
        c_numbers = [x for x in c_numbers if ((x >> bit) & 1) != c_most_common]

    print(o_numbers[0] * c_numbers[0])


def main():
    numbers, n_bits = get_input()
    a(numbers, n_bits)
    print()
    b(numbers, n_bits)


if __name__ == '__main__':
    main()
