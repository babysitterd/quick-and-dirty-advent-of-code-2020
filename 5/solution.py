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

def decode_seat(value):
    return (binary_search(0, 127, 'F', 'B', value[:7]), binary_search(0, 7, 'L', 'R', value[7:]))

def seat_id(row, column):
    return row * 8 + column

if __name__ == "__main__":
    row, column = decode_seat('BFFFBBFRRR')
    assert(row == 70 and column == 7 and seat_id(row, column) == 567)
    row, column = decode_seat('FFFBBBFRRR')
    assert(row == 14 and column == 7 and seat_id(row, column) == 119)
    row, column = decode_seat('BBFFBBFRLL')
    assert(row == 102 and column == 4 and seat_id(row, column) == 820)

    with open('input') as source:
        print(max(seat_id(*decode_seat(line.strip())) for line in source))

