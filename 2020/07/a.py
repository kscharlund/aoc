import sys


def parse_rule(line):
    parent, rest = line.split(' bags contain ')
    if rest == 'no other bags.':
        children = set()
    else:
        children = {' '.join(x.split()[1:3]) for x in rest.split(', ')}
    return (parent, children)


def main():
    contains = {}
    for line in sys.stdin.readlines():
        parent, children = parse_rule(line.strip())
        for child in children:
            contains.setdefault(child, set()).add(parent)
    result = set()
    visited = set()
    result |= contains['shiny gold']
    while True:
        remaining = result - visited
        if not remaining:
            break
        for child in remaining:
            result |= contains.get(child, set())
            visited.add(child)
    print(len(result))


if __name__ == '__main__':
    main()
