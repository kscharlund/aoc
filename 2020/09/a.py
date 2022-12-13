import sys


def pairwise_sums(numbers):
    sums = set()
    for ii in range(len(numbers)):
        for jj in range(ii + 1, len(numbers)):
            sums.add(numbers[ii] + numbers[jj])
    return sums


def main():
    numbers = [int(line.strip()) for line in sys.stdin.readlines()]
    window_size = 25
    for ii in range(window_size, len(numbers)):
        prev_sums = pairwise_sums(numbers[ii-window_size:ii])
        if numbers[ii] not in prev_sums:
            print(ii, numbers[ii])
            break


if __name__ == '__main__':
    main()
