"""
Solutions for day 4.
"""

from os.path import dirname, join


def is_valid(passphrase):
    split = passphrase.split()
    unique = set(split)
    return len(split) == len(unique)


def valid_passphrases(passphrases):
    valid = 0
    for passphrase in passphrases:
        if is_valid(passphrase):
            valid += 1
    return valid


def main():
    input_path = join(dirname(__file__), 'passphrases.txt')
    with open(input_path) as f:
        passphrases = f.readlines()

    print('Part 1')
    EXAMPLES_1 = 'aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa'
    for example in EXAMPLES_1:
        solution = is_valid(example)
        print('{} is valid: {}'.format(example, solution))
    solution1 = valid_passphrases(passphrases)
    print('Solution to part 1: {}'.format(solution1))

    print()



if __name__ == '__main__':
    main()
