#!/bin/env python3

if __name__ == "__main__":
    with open('input') as source:
        data = source.readlines()

    timepoint = startpoint = int(data[0])
    buses = [ int(i) for i in filter(lambda x: x != 'x', data[1].split(',')) ]
    while True:
        bus = next((bus for bus in buses if timepoint % bus == 0), None)
        if bus:
            to_wait = timepoint - startpoint
            print(to_wait * bus)
            break
        timepoint += 1

    requirements = [ ]
    buses = data[1].split(',')
    for i in range(len(buses)):
        if buses[i] != 'x':
            requirements.append((i, int(buses[i])))
    _, jump = requirements[0]
    candidate = 0
    looking_for = 1
    while looking_for != len(requirements):
        shift, divisor = requirements[looking_for]
        if (candidate + shift) % divisor == 0:
            jump *= divisor
            looking_for += 1
            continue

        candidate += jump

    print(candidate)