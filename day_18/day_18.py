"""
Solutions for day 18.
"""

from os.path import dirname, join


class Instruction:
    def __init__(self, line):
        self.function, self.x, self.y = self.read_instruction(line)

    def __repr__(self):
        l = [self.function, self.x]
        if self.y is not None:
            l += self.y
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
        self.instructions, registers_set = self.read_instructions(input_path)
        self.registers = {}
        for register in registers_set:
            self.registers[register] = 0
        self.current_index = 0
        self.last_played = 0
        self.recovered = None

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

    def run_instruction(self, instruction):
        function, x, y = instruction.get_parts()
        jump = 1
        if function == 'snd':
            self.last_played = self.translate(x)
        elif function == 'set':
            self.registers[x] = self.translate(y)
        elif function == 'add':
            self.registers[x] += self.translate(y)
        elif function == 'mul':
            self.registers[x] *= self.translate(y)
        elif function == 'mod':
            self.registers[x] %= self.translate(y)
        elif function == 'rcv' and self.translate(x) != 0:
            self.recovered = self.last_played
        elif function == 'jgz' and self.translate(x) != 0:
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
            instruction = self.instructions[self.current_index]
            self.run_instruction(instruction)
            if self.recovered is not None:
                return self.recovered
        print('Jumped off!')


def main():
    example = Duet(join(dirname(__file__), 'example.txt'))
    duet = Duet(join(dirname(__file__), 'duet.txt'))

    print('Part 1')
    print('Solution to example: {}'.format(example.run()))
    print('Solution to part 1: {}'.format(duet.run()))


if __name__ == '__main__':
    main()
