from collections import Counter
import sys
from pprint import pprint
import math


CARD_VALUES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
}


def card_value(card):
    return CARD_VALUES[card] if card in CARD_VALUES else int(card)


def get_data():
    data = []
    for line in open(sys.argv[1]):
        hand, bet = line.split()
        data.append(([card_value(c) for c in hand], int(bet)))
    return data


def hand_value(hand):
    counts = Counter(hand)
    if len(counts) == 5:
        return 0
    if len(counts) == 4:
        return 1
    if len(counts) == 3:
        if any(c > 2 for c in counts.values()):
            # Three of a kind
            return 3
        # Two pair
        return 2
    if len(counts) == 2:
        if any(c > 3 for c in counts.values()):
            # Four of a kind
            return 5
        # Full house
        return 4
    return 6


def sort_key_a(item):
    hand = item[0]
    return (hand_value(hand), hand)


def a(data):
    res = 0
    data.sort(key=sort_key_a)
    for i, (hand, bet) in enumerate(data, start=1):
        print(hand_value(hand), hand, i * bet)
        res += i * bet
    print(res)


def substitute_jokers(hand):
    counts = Counter(hand)
    n_jokers = counts[11]
    del counts[11]
    best_key = counts.most_common(1)[0][0] if counts else 11
    counts[best_key] += n_jokers
    return list(counts.elements())


def reduce_joker_values(hand):
    return [1 if h == 11 else h for h in hand]


def sort_key_b(item):
    hand = item[0]
    return (hand_value(substitute_jokers(hand)), reduce_joker_values(hand))


def b(data):
    res = 0
    data.sort(key=sort_key_b)
    for i, (hand, bet) in enumerate(data, start=1):
        print(hand, substitute_jokers(hand))
        res += i * bet
    print(res)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
