"""
Solutions for day 15.
"""

FACTOR_A = 16807
FACTOR_B = 48271


def match(a, b):
    return (a & 0xFFFF) == (b & 0xFFFF)


class Generator:
    def __init__(self, factor, starting_value):
        self.factor = factor
        self.value = starting_value

    def __next__(self):
        self.value = (self.value * self.factor) % 2147483647
        return self.value


def judge_count(a, b):
    count = 0
    genA = Generator(FACTOR_A, a)
    genB = Generator(FACTOR_B, b)
    for _ in range(40000000):
        if match(next(genA), next(genB)):
            count += 1
    return count


def main():
    INPUT = 699, 124
    EXAMPLE_1 = 65, 8921

    print('Part 1')
    print('Solution to example: {}'.format(judge_count(*EXAMPLE_1)))
    print('Solution to part 1: {}'.format(judge_count(*INPUT)))


if __name__ == '__main__':
    main()
