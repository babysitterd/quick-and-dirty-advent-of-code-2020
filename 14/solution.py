#!/bin/env python3

import re

def get_variants(template):
    result = [ '' ]
    for ch in template:
        if ch == 'X':
            result = [ '0' + x for x in result ] + [ '1' + y for y in result ]
        else:
            result = [ ch + x for x in result ]
    return result

if __name__ == "__main__":
    with open('input') as source:
        data = source.readlines()

    memory = { }
    for line in data:
        lhs, rhs = [ i.strip() for i in line.split('=') ]
        if lhs == 'mask':
            zero_mask = int(rhs.replace('X', '1'), 2)
            one_mask = int(rhs.replace('X', '0'), 2)
            x_mask = [ i for i, ch in enumerate(reversed(rhs)) if ch == 'X' ]
            continue

        address = int(re.match(r'^mem\[(\d+)\]', lhs).group(1))
#       part one
#        memory[address] = int(rhs) & zero_mask | one_mask
#       part two
        template = list(reversed(str(bin(address | one_mask))[2:].rjust(max(x_mask) + 1, '0')))
        for position in x_mask:
            template[position] = 'X'
        addresses = get_variants(template)
        for addr in addresses:
            memory[int(addr, 2)] = int(rhs)
    print(sum(i for i in memory.values()))