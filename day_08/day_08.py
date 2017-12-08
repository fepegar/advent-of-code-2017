"""
Solutions for day 8.
"""

import csv
import sys
import operator
from os.path import dirname, join

def read_instructions(input_path):
    FIELDNAMES = 'name', 'operation', 'n', '', 'a', 'condition', 'b'
    instructions = []
    registers = {}
    with open(input_path) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=' ', fieldnames=FIELDNAMES)
        for row in reader:
            instructions.append(row)
            name = row['name']
            if name not in registers:
                registers[name] = 0
    return instructions, registers


def get_largest_after_run(instructions, registers, track=False):
    operators = {
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '>': operator.gt,
    }

    if track:
        max_register_total = sys.float_info.min

    for instruction in instructions:
        a = registers[instruction['a']]
        b = int(instruction['b'])
        condition = instruction['condition']
        satisfied = operators[condition](a, b)
        if satisfied:
            if instruction['operation'] == 'inc':
                registers[instruction['name']] += int(instruction['n'])
            elif instruction['operation'] == 'dec':
                registers[instruction['name']] -= int(instruction['n'])
        max_register_now = max(registers.values())

        if track:
            max_register_total = max(max_register_total, max_register_now)

    if track:
        return max_register_total
    else:
        return max(registers.values())


def main():
    example_path = join(dirname(__file__), 'example.csv')
    input_path = join(dirname(__file__), 'input.csv')

    print('Part 1')
    largest = get_largest_after_run(*read_instructions(example_path))
    print('Largest registry: {}'.format(largest))
    solution1 = get_largest_after_run(*read_instructions(input_path))
    print('Solution to part 1: {}'.format(solution1))

    print()

    print('Part 2')
    largest = get_largest_after_run(*read_instructions(example_path), track=True)
    print('Largest registry: {}'.format(largest))
    solution2 = get_largest_after_run(*read_instructions(input_path), track=True)
    print('Solution to part 2: {}'.format(solution2))

if __name__ == '__main__':
    main()
