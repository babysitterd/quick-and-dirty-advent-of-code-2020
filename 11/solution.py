#!/bin/env python3

import functools

def get_adjacent(position):
    x, y = position
    return [ (x - 1, y) ,
             (x + 1, y) ,
             (x, y - 1) ,
             (x, y + 1) ,
             (x - 1, y - 1) ,
             (x - 1, y + 1) ,
             (x + 1, y - 1) ,
             (x + 1, y + 1) ]

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
            adjacent_people = 0
            for adjacent in get_adjacent(position):
                if adjacent in current and current[adjacent] == '#':
                    adjacent_people += 1
            if current[position] == 'L' and adjacent_people == 0:
                new[position] = '#'
            if current[position] == '#' and adjacent_people >= 4:
                new[position] = 'L'

        current, new = new, current

    print(list(current.values()).count('#'))