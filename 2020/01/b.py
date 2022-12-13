import sys


def main():
    data = list(int(x.strip()) for x in sys.stdin.readlines() if int(x.strip()) < 2021)
    for ii, xx in enumerate(data):
        for jj, yy in enumerate(data[ii+1:]):
            for zz in data[ii+jj+1:]:
                if xx + yy +zz == 2020:
                    print(xx * yy * zz)


if __name__ == '__main__':
    main()
