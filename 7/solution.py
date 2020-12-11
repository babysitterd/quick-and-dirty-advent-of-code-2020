#!/bin/env python3

import re

def bag_contained_in(bag, result, tree):
    if bag not in tree:
        return

    for i in tree[bag]:
        result.add(i)
        bag_contained_in(i, result, tree)

def bag_contains(bag, tree):
    if bag not in tree:
        return 0

    result = 0
    for bag, count in tree[bag]:
        result += count * (bag_contains(bag, tree) + 1)
    return result

if __name__ == "__main__":
    with open('input') as source:
        contained_in = { }
        contains = { }
        pattern = re.compile(r'(\d*) ?(\w+) (\w+) bag')
        for line in source:
            match = pattern.findall(line)
            if not match or match[1][1:] == ('no', 'other'):
                continue
            large = ' '.join(match[0][1:])
            contains[large] = set()
            for bag in match[1:]:
                small = ' '.join(bag[1:])
                contains[large].add((small, int(bag[0]) if bag[0] else 1))
                if small in contained_in:
                    contained_in[small].add(large)
                else:
                    contained_in[small] = { large }
        # part one
        result = set()
        bag_contained_in('shiny gold', result, contained_in)
        print(len(result))
        # part two
        print(bag_contains('shiny gold', contains))

#        tests for sample dataset
#        bag_contained_in('shiny gold', result, contained_in)
#        assert(len(result) == 4)
#        assert(bag_contains('faded blue', contains) == 0)
#        assert(bag_contains('dotted black', contains) == 0)
#        assert(bag_contains('vibrant plum', contains) == 11)
#        assert(bag_contains('dark olive', contains) == 7)
#        assert(bag_contains('shiny gold', contains) == 32)
