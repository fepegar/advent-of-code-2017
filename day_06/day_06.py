"""
Solutions for day 6.
"""

import copy
from os.path import dirname, join


def read_blocks(input_path):
    with open(input_path) as f:
        blocks = [int(n.strip()) for n in f.read().split()]
    return blocks


def steps_blocks(blocks, curiosity=False):
    seen = []
    steps = 0
    blocks = copy.deepcopy(blocks)
    while True:
        seen.append(blocks[:])
        largest_value = max(blocks)
        largest_index = blocks.index(largest_value)
        dst_index = largest_index + 1
        blocks[largest_index] = 0
        while largest_value > 0:
            if dst_index == len(blocks):
                dst_index = 0
            blocks[dst_index] += 1
            largest_value -= 1
            dst_index += 1
        steps += 1
        if blocks in seen:
            if curiosity:
                return steps - seen.index(blocks)
            else:
                return steps


def main():
    input_path = join(dirname(__file__), 'blocks.txt')
    blocks = read_blocks(input_path)
    EXAMPLE = [0, 2, 7, 0]

    print('Part 2')
    solution = steps_blocks(EXAMPLE)
    print('Steps to leave {}: {}'.format(EXAMPLE, solution))
    solution1 = steps_blocks(blocks)
    print('Solution to part 1: {}'.format(solution1))

    print()

    print('Part 2')
    solution = steps_blocks(EXAMPLE, curiosity=True)
    print('Steps to leave {}: {}'.format(EXAMPLE, solution))
    solution2 = steps_blocks(blocks, curiosity=True)
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
