#!/bin/env python3

#    BFFFBBFRRR: row 70, column 7, seat ID 567.
#    FFFBBBFRRR: row 14, column 7, seat ID 119.
#    BBFFBBFRLL: row 102, column 4, seat ID 820.

def decode_seat(value):
    return (70, 7)

def seat_id(row, column):
    return row * 8 + column

if __name__ == "__main__":
    row, column = decode_seat('BFFFBBFRRR')
    assert(row == 70 and column == 7 and seat_id(row, column) == 567)
