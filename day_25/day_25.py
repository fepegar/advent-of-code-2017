"""
Solutions for day 25.
"""

from collections import deque
from os.path import dirname, join


class State:
    def __init__(self, lines):
        self.instructions = self.read_state(lines)

    def __repr__(self):
        return self.name

    def read_state(self, lines):
        self.name = lines[0][-3]
        instructions = {}
        instructions[0] = self.read_instructions(lines[1:5])
        instructions[1] = self.read_instructions(lines[5:9])
        return instructions

    def read_instructions(self, lines):
        write = int(lines[1][-3])
        move = 1 if 'right' in lines[2] else -1
        go = lines[3][-3]
        return write, move, go


class Turing:
    def __init__(self, blueprints_path):
        self.tape = deque([0])
        self.checksum_steps, self.states = self.read_blueprints(blueprints_path)
        self.current_index = 0
        self.current_state = self.states[0]

    def __repr__(self):
        s = ''
        for i, n in enumerate(self.tape):
            if i == self.current_index:
                s += '[{}]'.format(n)
            else:
                s += ' {} '.format(n)
        s += ' Current idx: ' + str(self.current_index)
        return s

    @property
    def length(self):
        return len(self.tape)

    def read_blueprints(self, blueprints_path):
        with open(blueprints_path) as f:
            lines = f.readlines()
        num_states = int((len(lines) - 2) / 10)
        checksum_steps = int(lines[1].split()[5])
        l = 10
        states = []
        for i in range(num_states):
            index_ini = 3 + i * l
            state_lines = lines[index_ini : index_ini + l]
            states.append(State(state_lines))
        return checksum_steps, states

    def checksum(self):
        return self.tape.count(1)

    def build(self):
        for _ in range(self.checksum_steps):
            current_value = self.tape[self.current_index]
            write, move, go = self.current_state.instructions[current_value]
            self.tape[self.current_index] = write
            next_index = self.current_index + move
            if next_index < 0:
                self.tape.appendleft(0)
                self.current_index = 0
            elif next_index >= self.length:
                self.tape.append(0)
                self.current_index = next_index
            else:
                self.current_index = next_index
            self.current_state = self.get_state(go)
        return self.checksum()

    def get_state(self, name):
        for state in self.states:
            if state.name == name:
                return state


def main():
    print('Part 1')
    example = Turing(join(dirname(__file__), 'example.txt'))
    print('Solution to example:', example.build())
    turing = Turing(join(dirname(__file__), 'blueprints.txt'))
    print('Solution to part 1:', turing.build())


if __name__ == '__main__':
    main()
