"""
Solutions for day 9.
"""

from os.path import dirname, join

OPEN_GROUP = '{'
CLOSE_GROUP = '}'
OPEN_GARBAGE = '<'
CLOSE_GARBAGE = '>'
IGNORE = '!'


def stream_score(stream):
    score = 0
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
        elif char == OPEN_GROUP:
            group_depth += 1
        elif char == CLOSE_GROUP:
            score += group_depth
            group_depth -= 1
        elif char == OPEN_GARBAGE:
            garbage = True
        i += 1
        if i >= len(stream):
            return score


def main():
    example_path = join(dirname(__file__), 'examples.txt')
    input_path = join(dirname(__file__), 'input.txt')
    with open(example_path) as f:
        examples = [line.strip() for line in f]
    with open(input_path) as f:
        stream = f.read()

    print('Part 1')
    for example in examples:
        score = stream_score(example)
        print('{}: {}'.format(example, score))
    solution1 = stream_score(stream)
    print('Solution to part 1: {}'.format(solution1))

    print()


if __name__ == '__main__':
    main()
