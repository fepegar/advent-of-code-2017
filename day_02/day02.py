"""
Solutions for day 2.
"""

from os.path import dirname, join

def read_spreadsheet(path):
    with open(path) as f:
        lines = f.readlines()
    rows_str = [line.split() for line in lines]
    rows = []
    for row in rows_str:
        rows.append([int(n) for n in row])
    return rows


def even_division(row):
    for dividend in row:
        for divisor in row:
            if dividend == divisor:
                continue
            if dividend % divisor == 0:
                return dividend / divisor

def checksum(spreadsheet, evenly=False):
    if evenly:
        numbers = [even_division(row) for row in spreadsheet]
    else:
        numbers = [max(row) - min(row) for row in spreadsheet]
    solution = int(sum(numbers))
    return solution


def main():
    input_path = join(dirname(__file__), 'spreadsheet.txt')
    spreadsheet = read_spreadsheet(input_path)

    # Part 1
    print('Part 1')
    example_path = join(dirname(__file__), 'example1.txt')
    solution_example = checksum(read_spreadsheet(example_path))
    print('Solution to example 1: {}'.format(solution_example))
    solution1 = checksum(spreadsheet)
    print('Solution to part 1: {}'.format(solution1))

    print(2*'\n')

    # Part 2
    print('Part 2')
    example_path = join(dirname(__file__), 'example2.txt')
    solution_example = checksum(read_spreadsheet(example_path), evenly=True)
    print('Solution to example 2: {}'.format(solution_example))
    solution2 = checksum(spreadsheet, evenly=True)
    print('Solution to part 2: {}'.format(solution2))




if __name__ == '__main__':
    main()
