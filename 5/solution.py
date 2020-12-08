#!/bin/env python3

def binary_search(left, right, lower_char, higher_char, chars):
    for char in chars:
        half = left + (right - left) // 2
        if char == lower_char:
            right = half
        if char == higher_char:
            left = half + 1
    assert(left == right)
    return left

def decode_seats(value):
    return (binary_search(0, 127, 'F', 'B', value[:7]), binary_search(0, 7, 'L', 'R', value[7:]))

def seat_id(row, column):
    return row * 8 + column

if __name__ == "__main__":
    row, column = decode_seats('BFFFBBFRRR')
    assert(row == 70 and column == 7 and seat_id(row, column) == 567)
    row, column = decode_seats('FFFBBBFRRR')
    assert(row == 14 and column == 7 and seat_id(row, column) == 119)
    row, column = decode_seats('BBFFBBFRLL')
    assert(row == 102 and column == 4 and seat_id(row, column) == 820)

    with open('input') as source:
        all_seats = set()
        for x in range(128):
            for y in range(8):
                all_seats.add( (x, y) )
        in_list = set(decode_seats(line.strip()) for line in source)
        possible = all_seats - in_list
        # filter out isle seats
        possible = filter(lambda pair: pair[1] != 0 and pair[1] != 7, possible)
        # left and right neighbours required
        for row, column in possible:
            if (row, column - 1) in in_list and (row, column + 1) in in_list:
                print(seat_id(row, column))
                break
