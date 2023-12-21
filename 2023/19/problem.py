from dataclasses import dataclass, replace
import sys
from pprint import pprint
import math
import operator


def get_data():
    expect_workflow = True
    workflows = {}
    parts = []
    for line in open(sys.argv[1]):
        if not line.strip():
            expect_workflow = False
        elif expect_workflow:
            name, rest = line.split("{")
            node = []
            rules = rest.strip()[:-1].split(",")
            for rule in rules[:-1]:
                cond, next = rule.split(":")
                var, op, val = (
                    cond[0],
                    cond[1],
                    int(cond[2:]),
                )
                node.append(((var, op, val), next))
            node.append((None, rules[-1]))
            workflows[name] = node
        else:
            part = {}
            for rating in line.strip()[1:-1].split(","):
                var, val = rating.split("=")
                part[var] = int(val)
            parts.append(part)
    return workflows, parts


def a(data):
    workflows, parts = data
    count = 0
    for part in parts:
        wf = "in"
        while wf not in {"A", "R"}:
            workflow = workflows[wf]
            for rule, next in workflow:
                if rule is None:
                    wf = next
                    break
                var, op, val = rule
                fn = operator.lt if op == "<" else operator.gt
                if fn(part[var], val):
                    wf = next
                    break
        if wf == "A":
            count += sum(part.values())
    print(count)


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


@dataclass(frozen=True)
class Ranges:
    x: tuple[int, int]
    m: tuple[int, int]
    a: tuple[int, int]
    s: tuple[int, int]

    def apply(self, rule):
        var, op, val = rule
        min_val, max_val = getattr(self, var)
        next_r = (min_val, val - 1) if op == "<" else (val + 1, max_val)
        return replace(self, **{var: next_r})

    def inverse(self, rule):
        var, op, val = rule
        min_val, max_val = getattr(self, var)
        next_r = (min_val, val) if op == ">" else (val, max_val)
        return replace(self, **{var: next_r})

    def __len__(self):
        res = 1
        for mi, ma in (self.x, self.m, self.a, self.s):
            p = ma - mi + 1
            if p <= 0:
                return 0
            res *= p
        return res


def b(data):
    workflows = data[0]

    @memoize
    def accepted_ranges(args):
        ranges, node = args
        if not ranges:
            return []
        if node == "R":
            return []
        if node == "A":
            return [ranges]

        accepted = []
        workflow = workflows[node]
        for rule, target in workflow:
            if rule is None:
                return accepted + accepted_ranges((ranges, target))
            accepted += accepted_ranges((ranges.apply(rule), target))
            ranges = ranges.inverse(rule)
            if not ranges:
                return accepted

    pprint(
        sum(
            len(r)
            for r in accepted_ranges(
                (Ranges(x=(1, 4000), m=(1, 4000), a=(1, 4000), s=(1, 4000)), "in")
            )
        )
    )


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
