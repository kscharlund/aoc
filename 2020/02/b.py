import sys


def is_char(pwd, ii, char):
    if ii <= len(pwd):
        return pwd[ii-1] == char
    return False


def main():
    count = 0
    for line in sys.stdin.readlines():
        num, char, pwd = line.split()
        i1, i2 = (int(x) for x in num.split('-'))
        char = char[0]
        count += (is_char(pwd, i1, char) ^ is_char(pwd, i2, char))
    print(count)


if __name__ == '__main__':
    main()
