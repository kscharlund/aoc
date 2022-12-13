import sys


def get_id(bp: str):
    row = int(bp[:7].replace('F', '0').replace('B', '1'), base=2)
    col = int(bp[-3:].replace('R', '1').replace('L', '0'), base=2)
    return row * 8 + col


def main():
    ids = list(sorted(get_id(line.strip()) for line in sys.stdin.readlines()))
    p_id = ids[0]
    for c_id in ids[1:]:
        if p_id + 1 != c_id:
            print(c_id - 1)
        p_id = c_id


if __name__ == '__main__':
    main()
