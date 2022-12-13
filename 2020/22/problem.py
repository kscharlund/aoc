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


def read_input():
    p1, p2 = sys.stdin.read().split('\n\n')
    return [[int(line) for line in p.split('\n')[1:]] for p in (p1, p2)]


def a(hand1, hand2):
    while hand1 and hand2:
        c1, c2 = hand1.pop(0), hand2.pop(0)
        if c1 < c2:
            hand2 += [c2, c1]
        else:
            hand1 += [c1, c2]
    print(sum(c * (i + 1) for i, c in enumerate(reversed(hand1 if hand1 else hand2))))


def b(hand1, hand2):
    @memoize
    def recursive_combat(state):
        h1, h2 = state
        seen_states = {state}
        while h1 and h2:
            c1, c2, h1, h2 = h1[0], h2[0], h1[1:], h2[1:]
            if c1 <= len(h1) and c2 <= len(h2):
                winner, _ = recursive_combat((h1[:c1], h2[:c2]))
                if winner == 1:
                    h1 = h1 + (c1, c2)
                else:
                    h2 = h2 + (c2, c1)
            elif c2 < c1:
                winner = 1
                h1 = h1 + (c1, c2)
            else:
                winner = 2
                h2 = h2 + (c2, c1)
            next_state = (h1, h2)
            if next_state in seen_states:
                winner = 1
                break
            seen_states.add(next_state)
        return winner, h1 if winner == 1 else h2
    _, winning_hand = recursive_combat((hand1, hand2))
    print(sum(c * (i + 1) for i, c in enumerate(reversed(winning_hand))))


def main():
    hand1, hand2 = read_input()
    a(hand1[:], hand2[:])
    print()
    b(tuple(hand1), tuple(hand2))


if __name__ == '__main__':
    main()
