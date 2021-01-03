#!/bin/env python3

if __name__ == "__main__":
#    input = [ 0, 3, 6 ]
    input = [ 8, 13, 1, 0, 18, 9 ]
    history = { x: [ i + 1 ] for i, x in enumerate(input) }

    last_spoken = input[-1]
    for index in range(len(input) + 1, 30000001):
        occurrences = history[last_spoken]
        if len(occurrences) < 2:
            next_number = 0
        else:
            next_number = occurrences[-1] - occurrences[-2]

        if next_number in history:
            history[next_number].append(index)
        else:
            history[next_number] = [ index ]

        last_spoken = next_number

    print(last_spoken)