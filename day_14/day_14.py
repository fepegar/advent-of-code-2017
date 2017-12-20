"""
Solutions for day 14.
"""

import os
from functools import reduce
from collections import deque


def tie_knot(lengths, numbers, current_position=None, skip_size=None):
    if skip_size is None:
        skip_size = 0
    if current_position is None:
        current_position = 0
    n = len(numbers)
    for length in lengths:
        group_first = current_position
        group_last = group_first + length - 1
        if group_last + 1 > n:
            group_last = group_last - n
        rotated = deque(numbers)
        rotated.rotate(-group_first)
        rotated = list(rotated)
        group = rotated[:length]
        rest = rotated[length:]
        group.reverse()
        rotated = group + rest
        numbers = deque(rotated)
        numbers.rotate(group_first)
        numbers = list(numbers)
        current_position += (length + skip_size) % n
        skip_size += 1
    return numbers, current_position, skip_size


def get_dense_hash(sparse_hash):
    blocks = [sparse_hash[i * 16 : (i + 1) * 16] for i in range(16)]
    dense_hash = [reduce((lambda x, y: x ^ y), block) for block in blocks]
    return dense_hash


def dense_to_hex(dense_hash):
    hex_digits = [format(n, 'x').zfill(2) for n in dense_hash]
    return ''.join(hex_digits)


def get_knot_hash(string):
    current_position = None
    skip_size = None
    numbers = list(range(256))
    bytes_ascii = string_to_bytes(string)
    for _ in range(64):
        numbers, current_position, skip_size = tie_knot(
            bytes_ascii, numbers, current_position=current_position,
            skip_size=skip_size)
    sparse_hash = numbers
    dense_hash = get_dense_hash(sparse_hash)
    knot_hash = dense_to_hex(dense_hash)
    return knot_hash


def string_to_bytes(string):
    SUFFIX = [17, 31, 73, 47, 23]
    bytes_ascii = list(map(ord, string)) + SUFFIX
    return bytes_ascii


def get_grid(key):
    rows = []
    for i in range(128):
        row_hash = get_knot_hash('{}-{}'.format(key, i))
        row_bin = hex_to_bin(row_hash)
        rows.append(row_bin)
    return rows


def hex_to_bin(hex_string):
    num_bits = 4 * len(hex_string)
    bin_string = bin(int(hex_string, 16))[2:].zfill(num_bits)
    return bin_string


def get_num_squares(grid):
    return ''.join(grid).count('1')


def ind2sub(grid, index):
    size = len(grid)
    i = index // size
    j = index % size
    return i, j


def sub2ind(grid, i, j):
    size = len(grid)
    index = i * size + j
    return index


def get_neighbors(grid, i, j):
    size = len(grid)
    diffs = [
        (-1, 0),
        (1, 0),
        (0, 0),
        (0, -1),
        (0, 1),
    ]
    neighbors = []
    for di, dj in diffs:
        ti, tj = i + di, j + dj
        if ti >= size or ti < 0 or tj >= size or tj < 0:
            continue
        if grid[ti][tj] == '1':
            neighbors.append(sub2ind(grid, ti, tj))
    return neighbors


def make_pipes_file(grid, output_path):
    rows = cols = len(grid)
    with open(output_path, 'w') as f:
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    continue
                string = '{} <-> '.format(sub2ind(grid, i, j))
                neighbors = get_neighbors(grid, i, j)
                neighbors_string = ', '.join(map(str, neighbors))
                print(string + neighbors_string, file=f)


### From day 12 ###
import copy

class Program:
    def __init__(self, name):
        self.name = name
        self.links = []
        self.visited = False

    def __repr__(self):
        return str(self.name)


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


def get_number_of_connected_components(pipes):
    return len(connected_components(pipes))
###

def read_pipes(input_path):
    with open(input_path) as f:
        lines = f.read().splitlines()
    programs_map = {}
    for line in lines:
        this, others = line.split('<->')
        programs_map[int(this)] = Program(this)
    for line in lines:
        this, others = line.split('<->')
        this = programs_map[int(this)]
        for other in others.split(','):
            this.links.append(programs_map[int(other)])
    return list(programs_map.values())


def get_grid_number_of_cc(grid):
    output_path = 'grid.txt'
    make_pipes_file(grid, output_path)
    pipes = read_pipes(output_path)
    n = get_number_of_connected_components(pipes)
    os.remove(output_path)
    return n


def main():
    INPUT = 'ugkiagan'
    EXAMPLE_1 = 'flqrgnkx'

    print('Part 1')
    example = get_grid(EXAMPLE_1)
    print('Solution to {}: {}'.format(EXAMPLE_1, get_num_squares(example)))
    grid = get_grid(INPUT)
    print('Solution to part 1: {}'.format(get_num_squares(grid)))

    print()
    print('Part 2')
    print('Solution to {}: {}'.format(EXAMPLE_1, get_grid_number_of_cc(example)))
    print('Solution to part 2: {}'.format(get_grid_number_of_cc(grid)))


if __name__ == '__main__':
    main()
