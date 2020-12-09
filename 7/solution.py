#!/bin/env python3

import re

def check_branch(bag, result, tree):
    if bag not in tree:
        return

    for i in tree[bag]:
        result.add(i)
        check_branch(i, result, tree)

if __name__ == "__main__":
    with open('input') as source:
        contained_in = { }
        pattern = re.compile(r'(\w+) (\w+) bag')
        for line in source:
            match = pattern.findall(line)
            if not match or match[1] == ('no', 'other'):
                continue
            for bag in match[1:]:
                if bag in contained_in:
                    contained_in[bag].add(match[0])
                else:
                    contained_in[bag] = { match[0] }
        result = set()
        check_branch(('shiny', 'gold'), result, contained_in)
        print(len(result))
