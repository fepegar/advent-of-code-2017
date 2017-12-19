"""
Solutions for day 15.
"""

FACTOR_A = 16807
FACTOR_B = 48271


def match(a, b):
    return (a & 0xFFFF) == (b & 0xFFFF)


class Generator:
    def __init__(self, factor, starting_value, multiple=1):
        self.factor = factor
        self.value = starting_value
        self.multiple = multiple

    def __next__(self):
        while True:
            self.value = (self.value * self.factor) % 2147483647
            if self.value % self.multiple == 0:
                return self.value


def judge_count(a, b, iterations=40000000, multiples=False):
    count = 0
    if multiples:
        genA = Generator(FACTOR_A, a, multiple=4)
        genB = Generator(FACTOR_B, b, multiple=8)
    else:
        genA = Generator(FACTOR_A, a)
        genB = Generator(FACTOR_B, b)

    for step in range(iterations):
        if step % 1000000 == 0:
            print(step/1000000, '/', iterations/1000000 - 1)
        if match(next(genA), next(genB)):
            count += 1
    return count


def main():
    INPUT = 699, 124
    EXAMPLE_1 = 65, 8921

    print('Part 1')
    print('Solution to example: {}'.format(judge_count(*EXAMPLE_1)))
    print('Solution to part 1: {}'.format(judge_count(*INPUT)))

    print()

    print('Part 2')
    kwargs = {'iterations': 5000000, 'multiples': True}
    print('Solution to example: {}'.format(judge_count(*EXAMPLE_1, **kwargs)))
    print('Solution to part 2: {}'.format(judge_count(*INPUT, **kwargs)))

if __name__ == '__main__':
    main()
