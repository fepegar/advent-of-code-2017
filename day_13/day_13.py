"""
Solutions for day 13.
"""

import re
import copy
from os.path import dirname, join




class Layer:

    def __init__(self, depth, range_):
        self.depth = depth
        self.range = range_
        self.scanner = 0
        self.DOWN = 1
        self.UP = -1
        self.direction = self.DOWN


    def __repr__(self):
        return '{}: {}'.format(self.depth, self.range)


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



class Firewall:

    def __init__(self, input_path):
        self.layers = self.read_firewall(input_path)
        self.depth = -1


    # def __repr__(self):
    #     lines = []
    #     line1 = ' '.join(' {} '.format(layer.depth) for layer in self.layers)
    #     lines.append(line1)
    #
    #     line2 = ' '.join('[{}]'.format(layer))
    #     return '\n'.join(lines)


    def read_firewall(self, input_path):
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


    def update(self):
        for layer in self.layers:
            layer.update()


    def run(self):
        firewall = copy.copy(self)
        severity = 0
        for _ in range(len(self.layers)):
            self.depth += 1
            current_layer = self.layers[self.depth]
            caught = current_layer.scanner == 0
            if caught:
                severity += current_layer.depth * current_layer.range
            for layer in self.layers:
                layer.update()
        self.reset()
        return severity


    def reset(self):
        self.depth = -1
        for layer in self.layers:
            layer.reset()



def main():
    example = Firewall(join(dirname(__file__), 'example1.txt'))
    firewall = Firewall(join(dirname(__file__), 'input.txt'))

    print('Part 1')
    print('Solution to example: {}'.format(example.run()))
    print('Solution to part 1: {}'.format(firewall.run()))


if __name__ == '__main__':
    main()
