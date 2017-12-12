"""
Solutions for day 12.
"""

import copy
from os.path import dirname, join


class Program:

    def __init__(self, name):
        self.name = name
        self.links = []
        self.visited = False

    def __repr__(self):
        return str(self.name)


def read_pipes(input_path):
    with open(input_path) as f:
        lines = f.read().splitlines()
    programs = [Program(n) for n in range(len(lines))]
    for line in lines:
        this, others = line.split('<->')
        this = programs[int(this)]
        for other in others.split(','):
            this.links.append(programs[int(other)])
    return programs


def dfs(program, group):
    program.visited = True
    group.append(program)
    for neighbor in program.links:
        if not neighbor.visited:
            dfs(neighbor, group)


def connected_components(pipes):
    groups = []
    pipes = copy.deepcopy(pipes)
    for program in pipes:
        if not program.visited:
            group = []
            groups.append(group)
            dfs(program, group)
    return groups


def get_number_of_components(pipes, group_number):
    return len(connected_components(pipes)[group_number])


def get_number_of_connected_components(pipes):
    return len(connected_components(pipes))


def main():
    pipes = read_pipes(join(dirname(__file__), 'input.txt'))
    example1 = read_pipes(join(dirname(__file__), 'example1.txt'))

    print('Part 1')
    programs = get_number_of_components(example1, 0)
    print('Solution to example: {}'.format(programs))
    solution1 = get_number_of_components(pipes, 0)
    print('Solution to part 1: {}'.format(solution1))

    print()

    print('Part 2')
    programs = get_number_of_connected_components(example1)
    print('Solution to example: {}'.format(programs))
    solution2 = get_number_of_connected_components(pipes)
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
