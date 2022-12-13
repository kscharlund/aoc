import sys
from pprint import pprint
import math


matching_closers = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
rem_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
OPEN, CLOSE = range(2)


def get_input():
    return [line.strip() for line in sys.stdin]


def a(lines):
    errors = []
    remaining = []
    for line in lines:
        state = OPEN
        expected = []
        for char in line:
            if char in matching_closers:
                expected.append(matching_closers[char])
            else:
                exp = expected.pop()
                if exp != char:
                    errors.append(char)
                    break
        else:
            remaining.append(''.join(reversed(expected)))
    print(sum(scores[e] for e in errors))
    return remaining


def b(lines):
    remaining = a(lines)
    scores = []
    for rem in remaining:
        score = 0
        for char in rem:
            score *= 5
            score += rem_scores[char]
        scores.append(score)
    scores.sort()
    print(scores[len(scores) // 2])


def main():
    lines = get_input()
    a(lines)
    print()
    b(lines)


if __name__ == '__main__':
    main()
