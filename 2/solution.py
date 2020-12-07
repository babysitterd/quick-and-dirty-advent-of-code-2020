#!/bin/env python3

import re

if __name__ == "__main__":
    pattern = re.compile(r'^(\d+)-(\d+)\s(\S):\s(\S+)')
    with open('input') as source:
        result = 0
        for line in source:
            match = pattern.match(line)
#            part one
#            left, right, needle, haystack = match.groups()
#            occurences = haystack.count(needle)
#            if int(left) <= occurences <= int(right):
#                result += 1
#           part two
            first, second, needle, haystack = match.groups()
            first, second = [ int(x) - 1 for x in (first, second) ]
            if (haystack[first] == needle and haystack[second] != needle) or \
               (haystack[first] != needle and haystack[second] == needle):
                result += 1
        print(result)
