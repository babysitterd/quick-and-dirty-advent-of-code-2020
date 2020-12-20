#!/bin/env python3

#   N
# W   E
#   S

def move_N(x, y, delta):
    return (x - delta, y)

def move_S(x, y, delta):
    return (x + delta, y)

def move_W(x, y, delta):
    return (x, y - delta)

def move_E(x, y, delta):
    return (x, y + delta)

DIRECTIONS = [ 'E', 'S', 'W', 'N' ]

if __name__ == "__main__":
    with open('input') as source:
        x = y = 0
        direction = 0
        for line in source:
            if line[0] == 'F':
                direction %= len(DIRECTIONS)
                x, y = globals()[f'move_{DIRECTIONS[direction]}'](x, y, int(line[1:]))
            elif line[0] == 'L':
                direction -= int(line[1:]) // 90
            elif line[0] == 'R':
                direction += int(line[1:]) // 90
            else:
                x, y = globals()[f'move_{line[0]}'](x, y, int(line[1:]))
        print(abs(x) + abs(y))