#!/bin/env python3

#   N
# W   E
#   S

def move_N(x, y, delta):
    return (x, y + delta)

def move_S(x, y, delta):
    return (x, y - delta)

def move_W(x, y, delta):
    return (x - delta, y)

def move_E(x, y, delta):
    return (x + delta, y)

def apply_waypoint(ship_x, ship_y, waypoint_x, waypoint_y, multiplier):
    return ( ship_x + waypoint_x * multiplier,
             ship_y + waypoint_y * multiplier )

DIRECTIONS = [ 'E', 'S', 'W', 'N' ]

if __name__ == "__main__":
    with open('input') as source:
        ship_x = ship_y = 0

        x = 10
        y = 1

        direction = 0
        for line in source:
            if line[0] == 'F':
#                part one
#                direction %= len(DIRECTIONS)
#                ship_x, ship_y = globals()[f'move_{DIRECTIONS[direction]}'](ship_x, ship_y, int(line[1:]))
#                part two
                ship_x, ship_y = apply_waypoint(ship_x, ship_y, x, y, int(line[1:]))
            elif line[0] == 'L':
#                part one
#                direction -= int(line[1:]) // 90
#                part two
                for i in range(int(line[1:]) // 90):
                    x, y = -y, x
            elif line[0] == 'R':
#                part one
#                direction += int(line[1:]) // 90
#                part two
                for i in range(int(line[1:]) // 90):
                    x, y = y, -x
            else:
#                part one
#                ship_x, ship_y = globals()[f'move_{line[0]}'](ship_x, ship_y, int(line[1:]))
#                part two
                x, y = globals()[f'move_{line[0]}'](x, y, int(line[1:]))
        print(abs(ship_x) + abs(ship_y))