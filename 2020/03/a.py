import sys


def main():
    trees = list(x.strip() for x in sys.stdin.readlines())
    count_prod = 1
    for dx, dy in ((3, 1),):
        count = 0
        col = dx
        row = dy
        while row < len(trees):
            line = trees[row]
            count += (line[col] == '#')
            row += dy
            col = (col + dx) % len(line)
        count_prod *= count
    print(count_prod)

if __name__ == '__main__':
    main()
