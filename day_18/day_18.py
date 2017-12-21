"""
Solutions for day 18.
"""

from collections import deque
from os.path import dirname, join


class Instruction:
    def __init__(self, line):
        self.function, self.x, self.y = self.read_instruction(line)

    def __repr__(self):
        l = [self.function, self.x]
        if self.y is not None:
            l += [self.y]
        return ' '.join(l) + '\n'

    def read_instruction(self, line):
        split = line.strip().split()
        function, parameters = split[0], split[1:]
        number_of_parameters = len(parameters)
        x = parameters[0]
        if number_of_parameters == 1:
            y = None
        else:
            y = ''.join(parameters[1:])
        return function, x, y

    def get_parts(self):
        return self.function, self.x, self.y


class Duet:
    def __init__(self, input_path):
        self.program0 = Program(input_path)
        self.program1 = Program(input_path)
        self.program0.set_id(0)
        self.program1.set_id(1)
        self.program0.set_partner(self.program1)
        self.program1.set_partner(self.program0)

    def run(self):
        deadlock = False
        end = False
        while not end:
            self.program0.run_next_instruction(duet=True)
            self.program1.run_next_instruction(duet=True)
            deadlock = self.program0.deadlock and self.program1.deadlock
            terminated = self.program0.terminated and self.program1.terminated
            end = deadlock or terminated# or self.program1.sent > 1000
        return self.program1.sent


class Program:
    def __init__(self, input_path):
        self.instructions, registers_set = self.read_instructions(input_path)
        self.registers = {}
        for register in registers_set:
            self.registers[register] = 0
        self.current_index = 0
        self.last_played = 0
        self.recovered = None
        self.partner = None
        self.rcv_buffer = deque()
        self.deadlock = False
        self.sent = 0
        self.id = None
        self.terminated = False

    def __repr__(self):
        s = ''
        for instruction in self.instructions:
            s += repr(instruction)
        return repr(self.registers)

    def read_instructions(self, input_path):
        instructions = []
        registers = set()
        with open(input_path) as f:
            for line in f:
                instruction = Instruction(line)
                instructions.append(instruction)
                x = instruction.x
                if x.isalpha():
                    registers.add(instruction.x)
        return instructions, registers

    def run_instruction(self, instruction, duet=False):
        function, x, y = instruction.get_parts()
        jump = 1
        if function == 'snd':
            x = self.translate(x)
            if duet:
                self.send(x)
                self.sent += 1
            else:
                self.last_played = x
        elif function == 'set':
            self.registers[x] = self.translate(y)
        elif function == 'add':
            self.registers[x] += self.translate(y)
        elif function == 'mul':
            self.registers[x] *= self.translate(y)
        elif function == 'mod':
            self.registers[x] %= self.translate(y)
        elif function == 'rcv':
            if duet:
                received = self.receive(x)
                if not received:
                    jump = 0
            else:
                if self.translate(x) != 0:
                    self.recovered = self.last_played
        elif function == 'jgz' and self.translate(x) > 0:
            jump = self.translate(y)
        self.current_index += jump

    def translate(self, n):
        if n.isalpha():
            n = self.registers[n]
        else:
            n = int(n)
        return n

    def run(self):
        while self.current_index >= 0 and \
                self.current_index < len(self.instructions):
            self.run_next_instruction()
            if self.recovered is not None:
                return self.recovered

    def run_next_instruction(self, duet=False):
        self.terminated = self.current_index < 0 or \
                          self.current_index >= len(self.instructions)
        if self.terminated:
            return False
        instruction = self.instructions[self.current_index]
        self.run_instruction(instruction, duet=duet)
        return True

    def set_id(self, p):
        self.id = p
        self.registers['p'] = p

    def set_partner(self, program):
        self.partner = program

    def send(self, n):
        self.partner.rcv_buffer.appendleft(n)

    def receive(self, register):
        try:
            n = self.rcv_buffer.pop()
            self.registers[register] = n
            self.deadlock = False
            received = True
        except IndexError:
            self.deadlock = True
            received = False
        return received


def main():
    print('Part 1')
    example = Program(join(dirname(__file__), 'example.txt'))
    print('Solution to example: {}'.format(example.run()))
    duet = Program(join(dirname(__file__), 'duet.txt'))
    print('Solution to part 1: {}'.format(duet.run()))

    print()

    print('Part 2')
    example = Duet(join(dirname(__file__), 'example2.txt'))
    print('Solution to example: {}'.format(example.run()))
    duet = Duet(join(dirname(__file__), 'duet.txt'))
    print('Solution to part 2: {}'.format(duet.run()))


if __name__ == '__main__':
    main()
