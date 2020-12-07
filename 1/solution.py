#!/bin/env python3


def read_source(filename):
    with open(filename) as source:
        return set(int(line.strip()) for line in source)

def find_pair_sum(collection, target):
    for i in collection:
        complement = target - i
        if complement in collection:
            return i, complement
    return None

if __name__ == "__main__":
    TARGET = 2020
    numbers = read_source('sample')
    first, second = find_pair_sum(numbers, TARGET)
    assert(first * second == 514579)

    numbers = read_source('input')
    first, second = find_pair_sum(numbers, TARGET)
    assert(first * second == 658899)

    for i in numbers:
        complement = TARGET - i
        pair = find_pair_sum(numbers, complement)
        if pair is not None:
            print(i, pair[0], pair[1])
            print(i * pair[0] * pair[1])
            exit(0)
    exit(1)