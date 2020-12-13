#!/bin/env python3

if __name__ == "__main__":
    with open('input') as source:
        program = list( line.split() for line in source)

    accumulator = 0
    executed_lines = set()
    current_line = 0
    while current_line not in executed_lines:
        executed_lines.add(current_line)

        if program[current_line][0] == 'acc':
            accumulator += int(program[current_line][1])
            current_line += 1
        elif program[current_line][0] == 'nop':
            current_line += 1
        elif program[current_line][0] == 'jmp':
            current_line += int(program[current_line][1])
    
    print(accumulator)