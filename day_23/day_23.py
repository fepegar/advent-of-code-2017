"""
Solutions for day 23.
"""

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


class Program:
    def __init__(self, input_path):
        self.instructions, registers_set = self.read_instructions(input_path)
        self.registers = {}
        for register in registers_set:
            self.registers[register] = 0
        self.current_index = 0
        self.num_mul = 0
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

    def run_instruction(self, instruction):
        function, x, y = instruction.get_parts()
        jump = 1
        if function == 'set':
            self.registers[x] = self.translate(y)
        elif function == 'sub':
            self.registers[x] -= self.translate(y)
        elif function == 'mul':
            self.registers[x] *= self.translate(y)
            self.num_mul += 1
        elif function == 'jnz' and self.translate(x) != 0:
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
        return self.num_mul

    def run_next_instruction(self):
        self.terminated = self.current_index < 0 or \
                          self.current_index >= len(self.instructions)
        if self.terminated:
            return False
        instruction = self.instructions[self.current_index]
        self.run_instruction(instruction)
        return True


def main():
    print('Part 1')
    program = Program(join(dirname(__file__), 'program.txt'))
    print('Solution to part 1: {}'.format(program.run()))


if __name__ == '__main__':
    main()
