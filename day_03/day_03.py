import math

def spiral(x):
    if x == 1:
        return 0

    # x <= (2*levels - 1)**2
    min_levels = (math.sqrt(x) + 1) / 2
    levels = math.ceil(min_levels)
    largest = (2*levels - 1) ** 2

    steps_max = 2 * (levels - 1)
    steps_min = levels - 1
    sequence_down = list(range(steps_max, steps_min, -1))
    sequence_up = list(range(steps_min, steps_max))
    sequence_level = 4 * (sequence_down + sequence_up)
    return sequence_level[largest - x]


def main():
    print('Part 1')
    EXAMPLES_1 = 1, 12, 23, 1024
    for example in EXAMPLES_1:
        solution = spiral(example)
        print('Solution to {}: {}'.format(example, solution))
    solution1 = spiral(289326)
    print(solution1)

    print(2*'\n')


if __name__ == '__main__':
    main()
