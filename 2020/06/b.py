import sys


def main():
    group = set('abcdefghijklmnopqrstuvwxyz')
    count = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        if line:
            group &= set(line)
        else:
            count += len(group)
            group = set('abcdefghijklmnopqrstuvwxyz')
    print(count + len(group))


if __name__ == '__main__':
    main()
