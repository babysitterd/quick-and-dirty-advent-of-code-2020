#!/bin/env python3

# recursive, _super_ ineffective
def hop_count(n, data):
    if n < 0:
        return 0
    
    if n == 0:
        return 1

    if n not in data:
        return 0

    return hop_count(n - 1, data) + hop_count(n - 2, data) + hop_count(n - 3, data)

if __name__ == "__main__":
    with open('input') as source:
        data = source.readlines()

    data = list(int(x) for x in data)
    data = [0] + data + [max(data) + 3]
    data.sort()

    stats = { }
    for i in range(1, len(data)):
        diff = data[i] - data[i - 1]
        if diff in stats:
            stats[diff] += 1
        else:
            stats[diff] = 1

    print(stats[1] * stats[3])

    # iterative approach, we don't have to store all results though
    cache = { 0 : 1 }
    def next_hop_count(n):
        if n < 0:
            return 0
        if n not in cache:
            return 0
        return cache[n]

    for i in data[1:]:
        cache[i] = next_hop_count(i - 1) + \
                   next_hop_count(i - 2) + \
                   next_hop_count(i - 3)

    # assert(cache[data[-1]] == hop_count(data[-1], set(data)))
    print(cache[data[-1]])
