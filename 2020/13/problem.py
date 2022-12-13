import sys
from pprint import pprint
import math
from sympy.ntheory.modular import crt


def a(start_ts, buses):
    moduli = [bus - (start_ts % bus) for i, bus in buses]
    mini = moduli.index(min(moduli))
    print(buses[mini][1] * moduli[mini])


def b(buses):
    """
    find n such that:
    - n % buses[0] == 0
    - (n + 1) % buses[1] == 0
    - ...
    - (n + i) % buses[i] == 0


    n % 7 == 0
    (n + 1) % 13 == 0
    """
    ms = [m for _, m in buses]
    vs = [m - v for v, m in buses]
    print(ms)
    print(vs)
    print(crt(ms, vs)[0])

    nn = 0
    while not all([(nn + ii) % mm == 0 for ii, mm in buses]):
        nn += math.prod([mm for ii, mm in buses if (nn + ii) % mm == 0])
    print(nn)


def main():
    start_ts = int(sys.stdin.readline())
    buses = [(i, int(x)) for i, x in enumerate(sys.stdin.readline().split(',')) if x != 'x']
    a(start_ts, buses)
    print()
    b(buses)


if __name__ == '__main__':
    main()
