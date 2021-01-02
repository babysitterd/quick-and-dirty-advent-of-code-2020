#!/bin/env python3

import re
import functools

REQUIRED_KEYS = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def is_byr_valid(value):
    return re.match(r'^\d{4}$', value) and 1920 <= int(value) <= 2002

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def is_iyr_valid(value):
    return re.match(r'^\d{4}$', value) and 2010 <= int(value) <= 2020

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def is_eyr_valid(value):
    return re.match(r'^\d{4}$', value) and 2020 <= int(value) <= 2030

# hgt (Height) - a number followed by either cm or in:
#
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
def is_hgt_valid(value):
    cm_pattern = re.compile(r'^(\d{3})cm$')
    match = cm_pattern.match(value)
    if match and 150 <= int(match.group(1)) <= 193:
        return True

    in_pattern = re.compile(r'^(\d{2})in$')
    match = in_pattern.match(value)
    if match and 59 <= int(match.group(1)) <= 76:
        return True

    return False

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def is_hcl_valid(value):
    return bool(re.match(r'^#[\da-f]{6}$', value))

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def is_ecl_valid(value):
    return value in { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }

# pid (Passport ID) - a nine-digit number, including leading zeroes.
def is_pid_valid(value):
    return bool(re.match(r'^\d{9}$', value))

def is_valid_part_one(collection):
    return REQUIRED_KEYS.issubset(collection.keys())

def is_valid_part_two(collection):
    if not is_valid_part_one(collection):
        return False

    return functools.reduce(lambda x, y: x and globals()[f'is_{y}_valid'](collection[y]), REQUIRED_KEYS)

if __name__ == "__main__":
    with open('input') as source:
        valid_count = 0
        current = { }
        for line in source:
            pairs = line.split()
            if not pairs:
                if is_valid_part_two(current):
                    valid_count += 1
                current = { }
                continue
            current = { **current, **{ pair[0]:pair[1] for pair in [ x.split(':') for x in pairs ] } }
        if is_valid_part_two(current):
            valid_count += 1
        print(valid_count)
