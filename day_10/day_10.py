"""
Solutions for day 10.
"""

from functools import reduce
from collections import deque
from os.path import dirname, join
import yaml


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
        current_position += length + skip_size
        if current_position > n:
            current_position -= n
        skip_size += 1
    return numbers, current_position, skip_size


def one_knot(lengths, numbers):
    numbers = tie_knot(lengths, numbers)[0]
    return numbers[0] * numbers[1]


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


def numbers_to_string(lengths):
    string = ','.join(map(str, lengths))
    return string


def main():
    INPUT = 165, 1, 255, 31, 87, 52, 24, 113, 0, 91, 148, 254, 158, 2, 73, 153
    EXAMPLE_1 = 3, 4, 1, 5

    print('Part 1')
    hash_example = one_knot(EXAMPLE_1, list(range(5)))
    print('Solution to {}: {}'.format(EXAMPLE_1, hash_example))
    solution1 = one_knot(INPUT, list(range(256)))
    print('Solution to part 1: {}'.format(solution1))

    print()

    print('Part 2')
    with open(join(dirname(__file__), 'examples2.yaml')) as f:
        examples = yaml.load(f)
    for example in examples:
        knot_hash = get_knot_hash(example['string'])
        print('Solution to "{}": {}. Is it right? {}'.format(
            example['string'], knot_hash, knot_hash == example['hash']))
    solution2 = get_knot_hash(numbers_to_string(INPUT))
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
