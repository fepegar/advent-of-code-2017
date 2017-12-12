"""
Solutions for day 12.
"""

from os.path import dirname, join


def read_pipes(input_path):
    with open(input_path) as f:
        lines = f.read().splitlines()
    pipes = {}
    for line in lines:
        this, others = line.split('<->')
        this = int(this)
        pipes[this] = []
        for other in others.split(','):
            pipes[this].append(int(other))
    return pipes


def is_connected(pipes, program, group, stack=None):
    if stack is None:
        stack = []
    stack.append(program)
    for connection in pipes[program]:
        if connection in group:
            return True
        elif connection in stack:
            continue
        else:
            connected = is_connected(pipes, connection, group, stack)
            if connected:
                return True
    return False


def programs_in_group(pipes, group_number=0):
    group = []
    for program in pipes:
        if program == group_number:
            group.append(program)
        elif is_connected(pipes, program, group):
            group.append(program)
    return len(group)


def number_of_groups(pipes):
    programs_without_group = list(pipes.keys())
    groups = {}
    while programs_without_group:
        group_number = programs_without_group[0]
        group = []
        for program in pipes:
            if program == group_number or is_connected(pipes, program, group):
                group.append(program)
        for program in group:
            programs_without_group.pop(programs_without_group.index(program))
        groups[group_number] = group
    return len(groups)


def main():
    pipes = read_pipes(join(dirname(__file__), 'input.txt'))
    example1 = read_pipes(join(dirname(__file__), 'example1.txt'))

    print('Part 1')
    programs = programs_in_group(example1)
    print('Solution to example: {}'.format(programs))
    solution1 = programs_in_group(pipes)
    print('Solution to part 1: {}'.format(solution1))

    print()

    print('Part 2')
    programs = number_of_groups(example1)
    print('Solution to example: {}'.format(programs))
    solution2 = number_of_groups(pipes)
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
