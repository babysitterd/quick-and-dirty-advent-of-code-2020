#!/bin/env python3

import functools

if __name__ == "__main__":
    with open('input') as source:
        unique_answers_sum = 0
        dataset = []
        current = []
        for line in source:
            if not line.strip():
                dataset.append(current)
                current = []
                continue
            current.append(line.strip())
        dataset.append(current)
        # part one
        print(sum(len(k) for k in [ functools.reduce(lambda x, y: set(x) | set(y), i) for i in dataset ]))
        # part two
        print(sum(len(k) for k in [ functools.reduce(lambda x, y: set(x).intersection(y), i) for i in dataset ]))
