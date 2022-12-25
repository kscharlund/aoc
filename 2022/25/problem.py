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
    l5 = math.floor(math.log(val, 5))
    res = ""
    snafu_sum = 0
    if val / 5**l5 >= 2.5:
        # TODO: if val / 5**l5 == 2.5 due to float precision, need to handle.
        res = "1"
        snafu_sum = 5 ** (l5 + 1)
    for i in range(l5, -1, -1):
        rem = val - snafu_sum
        dig = round(rem / 5**i)
        res += TO_SNAFU_MAP[dig]
        snafu_sum += dig * 5**i
        # print(val, snafu_sum, res, rem / 5**i)
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
