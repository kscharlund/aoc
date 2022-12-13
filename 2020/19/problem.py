import sys
from pprint import pprint
import math
import re


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


def parse_input(lines):
    rules = {}
    for ii in range(len(lines)):
        if not lines[ii]:
            break
        num, rule = lines[ii].split(': ')
        if rule in {'"a"', '"b"'}:
            rules[num] = rule[1]
        elif '|' in rule:
            rules[num] = rule.split(' | ')
        else:
            rules[num] = rule
    messages = set(lines[ii+1:])
    return rules, messages


def a(lines):
    rules, messages = parse_input(lines)

    @memoize
    def get_matches_for_rule(num):
        rule = rules[num]
        if isinstance(rule, list):
            all_matches = []
            for part in rule:
                matches = None
                for subrule in part.split():
                    submatches = get_matches_for_rule(subrule)
                    if matches is None:
                        matches = submatches
                    else:
                        if isinstance(submatches, list):
                            if isinstance(matches, list):
                                matches = [x + y for x in matches for y in submatches]
                            else:
                                matches = [matches + y for y in submatches]
                        else:
                            if isinstance(matches, list):
                                matches = [x + submatches for x in matches]
                            else:
                                matches += submatches
                if isinstance(matches, list):
                    all_matches += matches
                else:
                    all_matches.append(matches)
            return all_matches

        if rule in {'a', 'b'}:
            return rule

        matches = None
        for subrule in rule.split():
            submatches = get_matches_for_rule(subrule)
            if matches is None:
                matches = submatches
            else:
                if isinstance(submatches, list):
                    if isinstance(matches, list):
                        matches = [x + y for x in matches for y in submatches]
                    else:
                        matches = [matches + y for y in submatches]
                else:
                    if isinstance(matches, list):
                        matches = [x + submatches for x in matches]
                    else:
                        matches += submatches
        return matches

    valid_matches = get_matches_for_rule('0')
    print(sum(vm in messages for vm in valid_matches))


def b(lines):
    rules = {}
    for ii in range(len(lines)):
        if not lines[ii]:
            break
        num, rule = lines[ii].split(': ')
        rules[num] = rule
    messages = lines[ii+1:]

    rules['8'] = '42+'
    rules['11'] = '|'.join('42 ' * i + '31 ' * i for i in range(1, 10))

    while len(rules) > 1:
        k, v = next((k, v) for k, v in rules.items() if not re.search(r'\d', v))
        rules = {
            k1: re.sub(rf'\b{k}\b', f'({v})', v1)
            for k1, v1 in rules.items() if k1 != k
        }

    reg = re.compile('^' + re.sub('[ "]', '', rules['0']) + '$')
    print(sum(bool(reg.match(line)) for line in messages))


def main():
    lines = [line.strip() for line in sys.stdin]
    a(lines)
    print()
    b(lines)


if __name__ == '__main__':
    main()
