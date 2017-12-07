"""
Solutions for day 7.
"""

import re
from os.path import dirname, join


def bottom(input_path):
    with open(input_path) as f:
        lines = f.readlines()
    parents = []
    children = []
    for line in lines:
        info = re.findall(r'(\w+)', line)
        parent = info[0]
        parents.append(parent)
        holds_disk = len(info) > 2
        if holds_disk:
            children += info[2:]
    return set(parents) - set(children)


def main():
    input_path = join(dirname(__file__), 'tower.txt')
    example_path = join(dirname(__file__), 'example.txt')

    print('Part 1')
    solution = bottom(example_path)
    print('Bottom program: {}'.format(solution))
    solution1 = bottom(input_path)
    print('Solution to part 1: {}'.format(solution1))


if __name__ == '__main__':
    main()
