import sys
from pprint import pprint
import math


def get_input():
    data = []
    for line in sys.stdin:
        inputs, outputs = line.split(' | ')
        data.append(
            (
                [set(x) for x in inputs.split()],
                [set(x) for x in outputs.split()]
            )
        )
    return data


def a(data):
    unique_lens = {2, 3, 4, 7}
    print(sum(len([
        o for o in outputs if len(o) in unique_lens
    ]) for _, outputs in data))


def b(data):
    result = 0
    for inputs, outputs in data:
        digits = [None for _ in range(10)]
        inputs.sort(key=len)
        digits[1] = inputs[0]
        digits[7] = inputs[1]
        digits[4] = inputs[2]
        digits[8] = inputs[9]
        cf = digits[1]
        bd = digits[4] - cf
        for input in inputs[3:6]:
            if input.intersection(cf) == cf:
                digits[3] = input
            elif input.intersection(bd) == bd:
                digits[5] = input
            else:
                digits[2] = input
        for input in inputs[6:9]:
            if input.intersection(cf) != cf:
                digits[6] = input
            elif input.intersection(digits[5]) == digits[5]:
                digits[9] = input
            else:
                digits[0] = input
        scale = 1000
        for output in outputs:
            result += digits.index(output) * scale
            scale //= 10

    print(result)


def main():
    data = get_input()
    a(data)
    print()
    b(data)


if __name__ == '__main__':
    main()
