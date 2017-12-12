"""
Solutions for day 11.
"""

from os.path import dirname, join

# Using cube coordinates
# See https://www.redblobgames.com/grids/hexagons/#coordinates-cube
DIRECTIONS = {
    # disable convention messages
    # pylint: disable=C
    'n' : ( 0,  1, -1),
    'ne': ( 1,  0, -1),
    'se': ( 1, -1,  0),
    's' : ( 0, -1,  1),
    'sw': (-1,  0,  1),
    'nw': (-1,  1,  0),
}


def add(coordsA, coordsB):
    return [a + b for a, b in zip(coordsA, coordsB)]


def steps_to_return(line):
    steps = line.split(',')
    coordinates = [0, 0, 0]
    for step in steps:
        coordinates = add(coordinates, DIRECTIONS[step])
    return max(map(abs, coordinates))


def main():
    with open(join(dirname(__file__), 'input.txt')) as f:
        input_steps = f.read().strip()
    with open(join(dirname(__file__), 'examples1.txt')) as f:
        examples = f.read().splitlines()
    print('Part 1')
    for example in examples:
        steps = steps_to_return(example)
        print('Solution to {}: {}'.format(example, steps))
    solution1 = steps_to_return(input_steps)
    print('Solution to part 1: {}'.format(solution1))


if __name__ == '__main__':
    main()
