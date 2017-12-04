"""
Solutions for day 4.
"""

from os.path import dirname, join


def is_valid(passphrase, anagram=False):
    split = passphrase.split()
    unique = set(split)
    if not anagram:
        return len(split) == len(unique)

    sorted_words = [''.join(sorted(word)) for word in split]
    sorted_set = set(sorted_words)
    return len(sorted_words) == len(sorted_set)


def valid_passphrases(passphrases, anagram=False):
    valid = 0
    for passphrase in passphrases:
        if is_valid(passphrase, anagram=anagram):
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

    print('Part 2')
    EXAMPLES_2 = ['abcde fghij', 'abcde xyz ecdab', 'a ab abc abd abf abj',
                  'iiii oiii ooii oooi oooo', 'oiii ioii iioi iiio']
    for example in EXAMPLES_2:
        solution = is_valid(example, anagram=True)
        print('{} is valid: {}'.format(example, solution))
    solution2 = valid_passphrases(passphrases, anagram=True)
    print('Solution to part 2: {}'.format(solution2))



if __name__ == '__main__':
    main()
