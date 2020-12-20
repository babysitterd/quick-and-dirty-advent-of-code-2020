#!/bin/env python3

#   N
# W   E
#   S

def get_N(x, y):
    return (x - 1, y)

def get_S(x, y):
    return (x + 1, y)

def get_W(x, y):
    return (x, y - 1)

def get_E(x, y):
    return (x, y + 1)

def get_NE(x, y):
    return get_N(*get_E(x, y))

def get_NW(x, y):
    return get_N(*get_W(x, y))

def get_SE(x, y):
    return get_S(*get_E(x, y))

def get_SW(x, y):
    return get_S(*get_W(x, y))

DIRECTIONS = [ get_N, get_S, get_W, get_E, get_NE, get_NW, get_SE, get_SW ]

def get_immediate_occupied(position, field):
    occupied = 0
    for adjacent in [ foo(*position) for foo in DIRECTIONS ]:
        if adjacent in field and field[adjacent] == '#':
            occupied += 1
    return occupied

def get_in_sight_occupied(position, field):
    occupied = 0
    for foo in DIRECTIONS:
        candidate = position
        while True:
            candidate = foo(*candidate)
            if candidate not in field or field[candidate] == 'L':
                break
            if field[candidate] == '#':
                occupied += 1
                break

    return occupied

if __name__ == "__main__":
    with open('input') as source:
        data = source.readlines()

    data = list(list(x.strip()) for x in data)

    current = { }
    for i in range(len(data)):
        for j in range(len(data[0])):
            current[ (i, j) ] = data[i][j]
    new = { }

    while current != new:
        new = current.copy()
        for position in current:
#            occupied = get_immediate_occupied(position, current)
            occupied = get_in_sight_occupied(position, current)
            if current[position] == 'L' and occupied == 0:
                new[position] = '#'

#            if current[position] == '#' and occupied >= 4:
            if current[position] == '#' and occupied >= 5:
                new[position] = 'L'

        current, new = new, current

    print(list(current.values()).count('#'))