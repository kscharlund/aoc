import sys


def get_fields(line):
    return {elem.split(':')[0] for elem in line.split()}


def main():
    required_fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    }
    passport_fields = set()
    num_valid = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        if line:
            passport_fields |= get_fields(line)
        else:
            if not (required_fields - passport_fields):
                num_valid += 1
            passport_fields = set()
    if not (required_fields - passport_fields):
        num_valid += 1
    print(num_valid)


if __name__ == '__main__':
    main()
