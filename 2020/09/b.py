import sys


def pairwise_sums(numbers):
    sums = set()
    for ii in range(len(numbers)):
        for jj in range(ii + 1, len(numbers)):
            sums.add(numbers[ii] + numbers[jj])
    return sums


def main():
    numbers = [int(line.strip()) for line in sys.stdin.readlines()]
    needle = 552655238
    min_ii = 0
    max_ii = 0
    cur_sum = numbers[0]
    while True:
        if cur_sum == needle:
            print(min_ii, max_ii, numbers[min_ii], numbers[max_ii])
            print(min(numbers[min_ii:max_ii+1]) + max(numbers[min_ii:max_ii+1]))
            break
        max_ii += 1
        cur_sum += numbers[max_ii]
        while cur_sum > needle:
            cur_sum -= numbers[min_ii]
            min_ii += 1


if __name__ == '__main__':
    main()
