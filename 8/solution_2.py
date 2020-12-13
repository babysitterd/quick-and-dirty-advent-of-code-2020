#!/bin/env python3

if __name__ == "__main__":
    with open('input') as source:
        program = list( line.split() for line in source)

    last_fixed_instruction = -1

    while True:
        fix_applied = False
        infintite_loop_detected = False

        accumulator = 0
        executed_lines = set()
        current_line = 0
        program_counter = 0
        while current_line not in executed_lines:
            if current_line == len(program):
                print(f'Program fixed by changing {last_fixed_instruction}, accumulator: {accumulator}')
                exit(0)

            executed_lines.add(current_line)

            instruction = program[current_line][0]
            if instruction in ['nop', 'jmp'] and not fix_applied and program_counter > last_fixed_instruction:
                fix_applied = True
                last_fixed_instruction = program_counter
                instruction = 'nop' if instruction == 'jmp' else 'jmp'


            if instruction == 'acc':
                accumulator += int(program[current_line][1])
                current_line += 1
            elif instruction == 'nop':
                current_line += 1
            elif instruction == 'jmp':
                current_line += int(program[current_line][1])
            
            program_counter += 1
