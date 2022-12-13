import sys
from pprint import pprint


HEADINGS = ['E', 'S', 'W', 'N']


HANDLERS = {
    'L': lambda val, heading, position: ((heading - (val // 90)) % 4, position),
    'R': lambda val, heading, position: ((heading + (val // 90)) % 4, position),
    'F': lambda val, heading, position: HANDLERS[HEADINGS[heading]](val, heading, position),
    'E': lambda val, heading, position: (heading, (position[0], position[1] + val)),
    'S': lambda val, heading, position: (heading, (position[0] - val, position[1])),
    'W': lambda val, heading, position: (heading, (position[0], position[1] - val)),
    'N': lambda val, heading, position: (heading, (position[0] + val, position[1])),
}


def a(instructions):
    heading = 0
    position = (0, 0)
    for op, val in instructions:
        heading, position = HANDLERS[op](val, heading, position)
        print(HEADINGS[heading], position)
    print(sum(abs(x) for x in position))


def handle_r(val, position):
    if val == 90:
        return (-position[1], position[0])
    elif val == 180:
        return (-position[0], -position[1])
    else:
        return (position[1], -position[0])


def b(instructions):
    HANDLERS['L'] = lambda val, heading, position: (heading, handle_r(360 - val, position))
    HANDLERS['R'] = lambda val, heading, position: (heading, handle_r(val, position))
    position = (0, 0)
    delta = (1, 10)
    heading = 0
    for op, val in instructions:
        if op == 'F':
            position = (position[0] + delta[0] * val, position[1] + delta[1] * val)
        else:
            heading, delta = HANDLERS[op](val, heading, delta)
        print(delta, position)
    print(sum(abs(x) for x in position))


def main():
    instructions = [(line[0], int(line[1:].strip())) for line in sys.stdin]
    a(instructions)
    print()
    b(instructions)


if __name__ == '__main__':
    main()
