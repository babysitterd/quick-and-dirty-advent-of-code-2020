#!/bin/env python3

# n^2, that's just disgusting, sorry
def all_possible_sums(last_n):
    all_sums = set()
    for i in range(len(last_n)):
        for j in range(i + 1, len(last_n)):
            all_sums.add(last_n[i] + last_n[j])
    return all_sums

if __name__ == "__main__":
    with open('input') as source:
        data = source.readlines()

    data = list(int(x) for x in data)

    # part one
    PREAMBULE_SIZE = 25

    for i in range(PREAMBULE_SIZE, len(data)):
        if data[i] not in all_possible_sums(data[i - PREAMBULE_SIZE: i]):
            goal = data[i]
            break

    print(goal)

    # part two
    for i in range(len(data)):
        sum = 0
        k = i
        while sum < goal:
            sum += data[k]
            k += 1

        if sum == goal:
            print(f"from {i} to {k}")
            print(min(data[i:k]) + max(data[i:k]))
            exit(0)

