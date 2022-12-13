import re
import sys
from pprint import pprint


def int_validator(min_val, max_val):
    def validator(s_val):
        try:
            i_val = int(s_val)
            return min_val <= i_val <= max_val
        except:
            return False
    return validator


def hgt_validator(s_val: str):
    if s_val.endswith('cm'):
        return int_validator(150, 193)(s_val[:-2])
    if s_val.endswith('in'):
        return int_validator(59, 76)(s_val[:-2])
    return False


def hcl_validator(s_val):
    return re.match(r'#[0-9a-f]{6}', s_val)


def ecl_validator(s_val):
    return s_val in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def pid_validator(s_val):
    return re.match(r'^\d{9}$', s_val)


def get_fields(line):
    return {elem.split(':')[0]: elem.split(':')[1] for elem in line.split()}


required_fields_validators = {
    'byr': int_validator(1920, 2002),
    'iyr': int_validator(2010, 2020),
    'eyr': int_validator(2020, 2030),
    'hgt': hgt_validator,
    'hcl': hcl_validator,
    'ecl': ecl_validator,
    'pid': pid_validator,
}


def validate(passport_fields):
    for field, validator in required_fields_validators.items():
        if not validator(passport_fields.get(field, '')):
            return False
    return True


def main():
    passport_fields = {}
    num_valid = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        if line:
            passport_fields.update(get_fields(line))
        else:
            if validate(passport_fields):
                num_valid += 1
            passport_fields = {}
    if validate(passport_fields):
        num_valid += 1
    print(num_valid)


if __name__ == '__main__':
    main()
