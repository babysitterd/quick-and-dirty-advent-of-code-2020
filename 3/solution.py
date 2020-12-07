#!/bin/env python3

def eval_tree_count(filename, delta_x, delta_y):
    with open(filename) as source:
        lines = source.readlines()
    length = len(lines[0].strip())

    tree_count = x = 0
    for y in range(0, len(lines), delta_y):
        if lines[y][x] == '#':
            tree_count += 1

        # a little faster than modulo?
        x = x + delta_x if x + delta_x < length else x + delta_x - length
    return tree_count


if __name__ == "__main__":
    assert(eval_tree_count('sample', 1, 1) == 2)
    assert(eval_tree_count('sample', 3, 1) == 7)
    assert(eval_tree_count('sample', 5, 1) == 3)
    assert(eval_tree_count('sample', 7, 1) == 4)
    assert(eval_tree_count('sample', 1, 2) == 2)
    assert(eval_tree_count('sample', 1, 1) *
           eval_tree_count('sample', 3, 1) *
           eval_tree_count('sample', 5, 1) *
           eval_tree_count('sample', 7, 1) *
           eval_tree_count('sample', 1, 2) == 336)

    assert(eval_tree_count('input', 3, 1) == 276)
    print(eval_tree_count('input', 1, 1) *
          eval_tree_count('input', 3, 1) *
          eval_tree_count('input', 5, 1) *
          eval_tree_count('input', 7, 1) *
          eval_tree_count('input', 1, 2))
