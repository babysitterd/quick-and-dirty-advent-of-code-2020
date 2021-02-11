#!/bin/env python3

import re

def is_in_bounds(value, bounds_list):
    for bounds in bounds_list:
        left, right = bounds
        if left <= value <= right:
            return True
    return False

def is_valid(value, requirements):
    for bounds_list in requirements.values():
        if is_in_bounds(value, bounds_list):
            return True
    return False

def possible_categories(value, requirements):
    result = set()
    for category in requirements:
        if is_in_bounds(value, requirements[category]):
            result.add(category)
    return result

if __name__ == "__main__":
    with open('input') as source:
        data = source.readlines()

    # requirements
    requirements = { }
    pattern = re.compile(r'(^[^:]+): (\d+)-(\d+) or (\d+)-(\d+)$')
    n = 0
    while data[n].strip():
        match = re.match(pattern, data[n])
        if not match:
            n += 1
            continue

        field, x_left, x_right, y_left, y_right = match.groups()
        requirements[field] = [ (int(x_left), int(x_right)),
                                (int(y_left), int(y_right)) ]
        n += 1

    error_rate = 0
    valid_tickets = [ ]
    for i in range(n, len(data)):
        if not data[i][0].isnumeric():
            continue
        ticket = [ int(x) for x in data[i].split(',') ]
        invalid_sum = sum(k for k in ticket if not is_valid(k, requirements))
        if invalid_sum == 0:
            valid_tickets.append(ticket)
        else:
            error_rate += invalid_sum

    print(error_rate)

    possible_solutions = []
    for i in range(len(valid_tickets[0])):
        possible_solutions.append(set(requirements.keys()))

    for ticket in valid_tickets:
        for i in range(len(ticket)):
            possible_solutions[i] = possible_solutions[i].intersection(possible_categories(ticket[i], requirements))

    field_to_index = { }
    while len(field_to_index) != len(valid_tickets[0]):
        for i in range(len(possible_solutions)):
            if len(possible_solutions[i]) == 1:
                cached = possible_solutions[i]
                field_to_index[list(cached)[0]] = i
                for j in range(len(possible_solutions)):
                    possible_solutions[j] = possible_solutions[j] - cached

    my_ticket = valid_tickets[0]
    result = 1
    for field in field_to_index:
        if field.startswith('departure'):
            result *= my_ticket[field_to_index[field]]

    print(result)