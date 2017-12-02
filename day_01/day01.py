"""
Solution for day 1.
"""

from os.path import dirname, join
from collections import deque

def solve_inverse_captcha(captcha, halfway=False):
    if halfway:
        even = len(captcha) % 2 == 0
        if not even:
            raise ValueError('Number of digits must be even')
    numbers = [int(n) for n in captcha]
    steps = int(len(numbers)/2) if halfway else 1
    rotated = deque(numbers)
    rotated.rotate(steps)
    pairs = zip(numbers, rotated)
    diffs = [b - a for (a, b) in pairs]
    repeated = [numbers[i] for (i, diff) in enumerate(diffs) if diff == 0]
    solution = sum(repeated)
    return solution

def main():
    input_path = join(dirname(__file__), 'sequence.txt')
    with open(input_path) as f:
        text = f.read()
    captcha = text.strip()
    print(len(captcha))

    # Part 1
    print('Part 1')
    EXAMPLES_1 = '1122', '1111', '1234', '91212129'
    for example in EXAMPLES_1:
        solution = solve_inverse_captcha(example)
        print('Solution to {}: {}'.format(example, solution))
    solution1 = solve_inverse_captcha(captcha)
    print(solution1)

    print(2*'\n')

    # Part 2
    print('Part 2')
    EXAMPLES_2 = '1212', '1221', '123425', '123123', '12131415'
    for example in EXAMPLES_2:
        solution = solve_inverse_captcha(example, halfway=True)
        print('Solution to {}: {}'.format(example, solution))
    solution2 = solve_inverse_captcha(captcha, halfway=True)
    print(solution2)

if __name__ == '__main__':
    main()
