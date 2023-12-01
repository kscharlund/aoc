import sys
from pprint import pprint
import math


def get_data():
    return sys.stdin.read().splitlines()


def a(data):
    digits = [[x for x in line if x.isdigit()] for line in data]
    print(sum(int(d[0] + d[-1]) for d in digits))


def find_digit(line, start, delta):
    digit_mapping = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    i = start
    while True:
        for s, d in digit_mapping.items():
            if line[i:].startswith(s):
                return d
        i += delta


def b(data):
    vals = [
        10 * find_digit(line, 0, 1) + find_digit(line, -1, -1)
        for line in data
    ]
    print(sum(vals))


def main():
    data = get_data()
    #a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
