import sys


def main():
    data = list(int(x.strip()) for x in sys.stdin.readlines() if int(x.strip()) < 2021)
    for ii, xx in enumerate(data):
        for yy in data[ii+1:]:
            if xx + yy == 2020:
                print(xx * yy)


if __name__ == '__main__':
    main()
