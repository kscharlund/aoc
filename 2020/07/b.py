import sys


def parse_rule(line):
    parent, rest = line.split(' bags contain ')
    if rest == 'no other bags.':
        children = set()
    else:
        children = {(int(x.split()[0]), ' '.join(x.split()[1:3])) for x in rest.split(', ')}
    return (parent, children)


def num_inside(contains, parent):
    result = 0
    for num, child in contains[parent]:
        result += num * (1 + num_inside(contains, child))
    return result


def main():
    contains = {}
    for line in sys.stdin.readlines():
        parent, children = parse_rule(line.strip())
        contains[parent] = children
    print(num_inside(contains, 'shiny gold'))


if __name__ == '__main__':
    main()
