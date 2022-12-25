import sys
from pprint import pprint
import math

FROM_SNAFU_MAP = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}

TO_SNAFU_MAP = {
    2: "2",
    1: "1",
    0: "0",
    -1: "-",
    -2: "=",
}


def from_snafu(line):
    res = 0
    for i, c in enumerate(reversed(line)):
        res += 5**i * FROM_SNAFU_MAP[c]
    return res


def to_snafu(val):
    res = ""
    while val > 0:
        val, dig = divmod(val, 5)
        res = "012=-"[dig] + res
        val += dig > 2
    return res


def get_data():
    return [from_snafu(line.strip()) for line in open(sys.argv[1])]


def a(data):
    print(to_snafu(sum(data)))


def b(data):
    pass


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
