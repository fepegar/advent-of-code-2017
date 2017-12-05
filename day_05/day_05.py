"""
Solutions for day 4.
"""

from os.path import dirname, join

def read_maze(input_path):
    with open(input_path) as f:
        maze = [int(n.strip()) for n in f.readlines()]
    return maze


def steps_maze(maze, second=False):
    maze = maze[:]  # don't modify input list
    current = 0
    steps = 0
    while True:
        if second and maze[current] >= 3:
            maze[current] -= 1
            current += maze[current] + 1
        else:
            maze[current] += 1
            current += maze[current] - 1
        steps += 1
        if current < 0 or current >= len(maze):
            return steps


def main():
    input_path = join(dirname(__file__), 'maze.txt')
    maze = read_maze(input_path)

    print('Part 1')
    EXAMPLES_1 = [[0, 3, 0, 1, -3]]
    for example in EXAMPLES_1:
        solution = steps_maze(example)
        print('Steps to leave {}: {}'.format(example, solution))
    solution1 = steps_maze(maze)
    print('Solution to part 1: {}'.format(solution1))

    print()

    print('Part 2')
    for example in EXAMPLES_1:
        solution = steps_maze(example, second=True)
        print('Steps to leave {}: {}'.format(example, solution))
    solution2 = steps_maze(maze, second=True)
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
