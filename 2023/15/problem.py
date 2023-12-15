from collections import defaultdict
import sys
from pprint import pprint
import math


def get_data():
    return [x.strip() for x in open(sys.argv[1]).read().split(',')]


def hash_a(s):
    res = 0
    for c in s:
        res = ((res + ord(c)) * 17) & 0xFF
    return res


def a(data):
    pprint(sum([hash_a(v) for v in data]))


def b(data):
    hash_table = defaultdict(dict)
    for item in data:
        if item.endswith('-'):
            label = item[:-1]
            hash_table[hash_a(label)].pop(label, 0)
        else:
            label, val = item.split('=')
            hash_table[hash_a(label)][label] = int(val)
    res = 0
    for box, contents in hash_table.items():
        for i, (label, focal_length) in enumerate(contents.items()):
            res += (box + 1) * (i + 1) * focal_length
    print(res)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
