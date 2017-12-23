"""
Solutions for day 13.
"""

import re
from os.path import dirname, join



class Layer:

    def __init__(self, depth, range_):
        self.depth = depth
        self.range = range_


    def caught_at(self, t, delay=0):
        if self.range == 0:
            return False
        multiple = 2 * (self.range - 1)
        caught = (t + delay) % multiple == 0
        return caught


class Firewall:

    def __init__(self, input_path):
        self.layers = self.read_firewall(input_path)
        self.packet = -1


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


    def get_min_delay(self):
        delay = 0
        while True:
            caught = False
            for depth, layer in enumerate(self.layers):
                if layer.caught_at(depth, delay=delay):
                    caught = True
                    break
            if not caught:
                return delay
            delay += 1


def main():
    example = Firewall(join(dirname(__file__), 'example1.txt'))
    firewall = Firewall(join(dirname(__file__), 'input.txt'))

    print('Part 2')
    print('Solution to example: {}'.format(example.get_min_delay()))
    print('Solution to part 2: {}'.format(firewall.get_min_delay()))


if __name__ == '__main__':
    main()
