"""
Solutions for day 13.
"""

import re
from os.path import dirname, join



class Layer:

    def __init__(self, depth, range_):
        self.depth = depth
        self.range = range_
        self.scanner = 0
        self.DOWN = 1
        self.UP = -1
        self.direction = self.DOWN
        self.packet = False


    def __repr__(self):
        strings = [str(self.depth).center(3)]
        if self.range == 0:
            if self.packet:
                strings.append('(.)')
            else:
                strings.append('...')
        for n in range(self.range):
            if n == 0 and self.packet:
                brackets = '(', ')'
            else:
                brackets = '[', ']'
            if n == self.scanner:
                inside = 'S'
            else:
                inside = ' '
            strings.append(brackets[0] + inside + brackets[1])
        return ' '.join(strings)


    def update(self):
        self.scanner += self.direction
        if self.scanner == self.range - 1 or self.scanner == 0:
            self.toggle_direction()


    def toggle_direction(self):
        if self.direction == self.DOWN:
            self.direction = self.UP
        else:
            self.direction = self.DOWN


    def reset(self):
        self.scanner = 0
        self.direction = self.DOWN
        self.packet = False


def read_firewall(input_path):
    layers = []
    pattern = r'(\d+): (\d+)'
    with open(input_path) as f:
        for line in f:
            groups = re.match(pattern, line).groups()
            layer_depth, layer_range = list(map(int, groups))
            for depth in range(len(layers), layer_depth):
                layers.append(Layer(depth, 0))
            layers.append(Layer(layer_depth, layer_range))
    return layers



class Firewall:

    def __init__(self, input_path):
        self.layers = read_firewall(input_path)
        self.packet = -1


    def __repr__(self):
        strings = []
        for layer in self.layers:
            strings.append(repr(layer))
        return '\n'.join(strings)


    def update(self):
        for layer in self.layers:
            layer.update()


    def run(self, delay=None):
        severity = 0
        caught = False

        if delay is None:
            delay = 0
            return_if_caught = False
        else:
            return_if_caught = True

        for _ in range(delay):
            self.update()

        # print(self)
        current_layer = None
        for _ in range(len(self.layers)):
            if current_layer is not None:
                current_layer.packet = False
            self.packet += 1
            current_layer = self.layers[self.packet]
            current_layer.packet = True
            caught = current_layer.scanner == 0
            if caught:
                # print('caught!')
                if return_if_caught:
                    self.reset()
                    return caught, severity
                severity += current_layer.depth * current_layer.range
            # print()
            # print(self)
            self.update()
        self.reset()
        print('not caught!')
        return caught, severity


    def get_min_delay(self):
        caught = True
        delay = -1
        while caught:
            print('Try delay', delay+1)
            delay += 1
            caught = self.run(delay=delay)[0]
        return delay


    def reset(self):
        self.packet = -1
        for layer in self.layers:
            layer.reset()



def main():
    example = Firewall(join(dirname(__file__), 'example1.txt'))
    firewall = Firewall(join(dirname(__file__), 'input.txt'))

    print('Part 1')
    # print('Solution to example: {}'.format(example.run()[1]))
    # print('Solution to part 1: {}'.format(firewall.run()[1]))

    print('Part 2')
    print('Solution to example: {}'.format(example.get_min_delay()))
    print('Solution to part 2: {}'.format(firewall.get_min_delay()))


if __name__ == '__main__':
    main()
