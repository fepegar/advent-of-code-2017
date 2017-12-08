"""
Solutions for day 7.
"""


from os.path import dirname, join

from tower import Tower


def main():
    tower = Tower(join(dirname(__file__), 'tower.txt'))
    tower_example = Tower(join(dirname(__file__), 'example.txt'))

    print('Part 1')
    print('Bottom program: {}'.format(tower_example.get_bottom()))
    print('Solution to part 1: {}'.format(tower.get_bottom()))

    print()

    print('Part 2')
    solution = tower_example.weight_to_balance()
    print('Correct weight: {}'.format(solution))
    solution2 = tower.weight_to_balance()
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
