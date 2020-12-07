#!/bin/env python3

if __name__ == "__main__":
    REQUIRED_KEYS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    with open('input') as source:
        valid_count = 0
        current = set()
        for line in source:
            pairs = line.split()
            if not pairs:
                if REQUIRED_KEYS.issubset(current):
                    valid_count += 1
                current = set()
                continue
            current |= set(x.split(':')[0] for x in pairs)
        print(valid_count + 1 if REQUIRED_KEYS.issubset(current) else valid_count)