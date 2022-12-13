import sys
from pprint import pprint
import math


def memoize(func):
    """
    Memoization decorator for a function taking a single argument.
    """

    class Memodict(dict):
        """Memoization dictionary."""

        def __missing__(self, key):
            ret = self[key] = func(key)
            return ret

    return Memodict().__getitem__


shape_scores = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
outcome_scores = {
    "X": {"A": 3, "B": 0, "C": 6},
    "Y": {"A": 6, "B": 3, "C": 0},
    "Z": {"A": 0, "B": 6, "C": 3},
}
shape_selections = {
    "X": {"A": "C", "B": "A", "C": "B"},
    "Y": {"A": "A", "B": "B", "C": "C"},
    "Z": {"A": "B", "B": "C", "C": "A"},
}


def score(left, right):
    return shape_scores[right] + outcome_scores[right][left]


def get_data():
    return [line.split() for line in open(sys.argv[1])]


def a(data):
    print(sum(score(*hand) for hand in data))


def b(data):
    score = 0
    for them, outcome in data:
        you = shape_selections[outcome][them]
        score += shape_scores[you] + {"X": 0, "Y": 3, "Z": 6}[outcome]
    print(score)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
