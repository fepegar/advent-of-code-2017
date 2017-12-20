"""
Solutions for day 16.
"""

from os.path import dirname, join

SPIN = 's'
EXCHANGE = 'x'
PARTNER = 'p'


def read_moves(input_path):
    with open(input_path) as f:
        return f.read().split(',')


class Programs:
    def __init__(self, length, moves):
        self.length = length
        self.programs = self.get_programs()
        self.moves = moves

    def get_programs(self):
        a = ord('a')
        return list(map(chr, range(a, a + self.length)))

    def dance_move(self, move):
        move_type = move[0]
        move_args = move[1:]
        if move_type == SPIN:
            n = int(move_args)
            end = self.programs[-n:]
            start = self.programs[:-n]
            self.programs = end + start
        elif move_type == EXCHANGE:
            posA, posB = move_args.split('/')
            self.swap(posA, posB)
        elif move_type == PARTNER:
            programA, programB = move_args.split('/')
            posA = self.programs.index(programA)
            posB = self.programs.index(programB)
            self.swap(posA, posB)

    def swap(self, posA, posB):
        posA = int(posA)
        posB = int(posB)
        self.programs[posA], self.programs[posB] = (self.programs[posB],
                                                    self.programs[posA])

    def dance(self):
        for move in self.moves:
            self.dance_move(move)
        return self.beautify()

    def long_dance(self, times=int(1e9)):
        record = []
        step = 0
        while True:
            self.dance()
            if self.programs in record:
                period = step
                break
            else:
                record.append(self.programs[:])
                step += 1
        index = times % period - 1
        result = record[index]
        return self.beautify(result)

    def beautify(self, programs=None):
        if programs is None:
            programs = self.programs
        return ''.join(programs)


def main():
    moves = read_moves(join(dirname(__file__), 'input.txt'))
    EXAMPLE_1 = 's1', 'x3/4', 'pe/b'

    print('Part 1')
    example = Programs(5, EXAMPLE_1)
    print('Solution to example: {}'.format(example.dance()))
    programs = Programs(16, moves)
    print('Solution to part 1: {}'.format(programs.dance()))

    print()

    print('Part 2')
    example = Programs(5, EXAMPLE_1)
    print('Solution to example: {}'.format(example.long_dance()))
    programs = Programs(16, moves)
    print('Solution to part 1: {}'.format(programs.long_dance()))


if __name__ == '__main__':
    main()
