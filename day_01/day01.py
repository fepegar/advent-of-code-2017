"""
Solution for day 1.
"""

from os.path import dirname, join

def solve_inverse_captcha(captcha):
    numbers = [int(n) for n in captcha]
    numbers.append(numbers[0])  # list is circular
    pairs = zip(numbers[:-1], numbers[1:])
    diffs = [b - a for (a, b) in pairs]
    repeated = [numbers[i] for (i, diff) in enumerate(diffs) if diff == 0]
    solution = sum(repeated)
    return solution

def main():
    EXAMPLES = '1122', '1111', '1234', '91212129'
    for example in EXAMPLES:
        solution = solve_inverse_captcha(example)
        print('Solution to {}: {}'.format(example, solution))

    input_path = join(dirname(__file__), 'input.txt')
    with open(input_path) as f:
        text = f.read()
    captcha = text.strip()
    solution = solve_inverse_captcha(captcha)
    print(solution)

if __name__ == '__main__':
    main()
