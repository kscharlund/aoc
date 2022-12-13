import sys
from pprint import pprint


def a(sequence, stop = 2020):
    occurrences = {x: i for i, x in enumerate(sequence[:-1])}
    prev = sequence[-1]
    for step in range(len(sequence), stop):
        if prev in occurrences:
            curr = step - 1 - occurrences[prev]
        else:
            curr = 0
        occurrences[prev] = step - 1
        prev = curr
    print(prev)


def b(sequence):
    a(sequence, 30000000)


def main():
    sequence = [int(x) for x in sys.stdin.readline().split(',')]
    a(sequence)
    print()
    b(sequence)


if __name__ == '__main__':
    main()
