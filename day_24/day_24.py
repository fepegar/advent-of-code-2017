"""
Solutions for day 24.
"""

from os.path import dirname, join


class Components:
    def __init__(self, input_path):
        self.components = self.read_components(input_path)


    def read_components(self, input_path):
        components = []
        with open(input_path) as f:
            for line in f:
                components.append(tuple(map(int, line.split('/'))))
        return components


    def get_strongest_bridge(self):
        initials = self.get_compatible_components(0)
        for initial in initials:
            pass
            

    def get_compatible_components(self, n):
        return [component for component in self.components if n in component]


def main():
    print('Part 1')
    example = Components(join(dirname(__file__), 'example.txt'))
    print('Solution to example:', example.get_strongest_bridge())
    # print('Solution to part 1:', program.run())


if __name__ == '__main__':
    main()
