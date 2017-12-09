"""
Solutions for day 9.
"""

from os.path import dirname, join

OPEN_GROUP = '{'
CLOSE_GROUP = '}'
OPEN_GARBAGE = '<'
CLOSE_GARBAGE = '>'
IGNORE = '!'


def stream_score(stream, remove_garbage=False):
    score = 0
    removed = 0
    i = 0
    group_depth = 0
    garbage = False
    while True:
        char = stream[i]
        if char == IGNORE:
            i += 1
        elif garbage:
            if char == CLOSE_GARBAGE:
                garbage = False
            else:
                removed += 1
        elif char == OPEN_GROUP:
            group_depth += 1
        elif char == CLOSE_GROUP:
            score += group_depth
            group_depth -= 1
        elif char == OPEN_GARBAGE:
            garbage = True
        i += 1

        if i >= len(stream):
            return removed if remove_garbage else score


def main():
    input_path = join(dirname(__file__), 'input.txt')
    with open(input_path) as f:
        stream = f.read()

    print('Part 1')
    with open(join(dirname(__file__), 'examples1.txt')) as f:
        for example in [line.strip() for line in f]:
            score = stream_score(example)
            print('{}: {}'.format(example, score))
    solution1 = stream_score(stream)
    print('Solution to part 1: {}'.format(solution1))

    print()

    print('Part 2')
    with open(join(dirname(__file__), 'examples2.txt')) as f:
        for example in [line.strip() for line in f]:
            removed = stream_score(example, remove_garbage=True)
            print('{}: {}'.format(example, removed))
    solution2 = stream_score(stream, remove_garbage=True)
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
