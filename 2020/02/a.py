import sys


def hist_chars(pwd):
    hist = {}
    for c in pwd:
        hist[c] = hist.get(c, 0) + 1
    return hist


def main():
    count = 0
    for line in sys.stdin.readlines():
        num, char, pwd = line.split()
        min_num, max_num = (int(x) for x in num.split('-'))
        char = char[0]
        hist = hist_chars(pwd)
        if min_num <= hist.get(char, 0) <= max_num:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
