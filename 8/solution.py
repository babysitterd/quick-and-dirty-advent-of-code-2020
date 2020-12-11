#!/bin/env python3

import re

if __name__ == "__main__":
    with open('input') as source:
#        pattern = re.compile(r'(\d*) ?(\w+) (\w+) bag')
        program = list( line.split() for line in source)

        accumulator = 0
        executed_lines = set()
        current_line = 0
        while current_line not in executed_lines:
#            print(f'line: {current_line}, accumulator: {accumulator}')
            executed_lines.add(current_line)

            if program[current_line][0] == 'acc':
                accumulator += int(program[current_line][1])
                current_line += 1
            elif program[current_line][0] == 'nop':
                current_line += 1
            elif program[current_line][0] == 'jmp':
                current_line += int(program[current_line][1])
        
        print(accumulator)