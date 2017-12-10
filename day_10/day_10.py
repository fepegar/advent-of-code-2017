"""
Solutions for day 10.
"""

from collections import deque


def tie_knot(lengths, numbers):
    skip_size = 0
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
    return numbers[0] * numbers[1]


def main():
    INPUT = 165, 1, 255, 31, 87, 52, 24, 113, 0, 91, 148, 254, 158, 2, 73, 153
    EXAMPLE = 3, 4, 1, 5

    print('Part 1')
    hash_example = tie_knot(EXAMPLE, list(range(5)))
    print('{}: {}'.format(EXAMPLE, hash_example))
    solution1 = tie_knot(INPUT, list(range(256)))
    print('Solution to part 1: {}'.format(solution1))


if __name__ == '__main__':
    main()
