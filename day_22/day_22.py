"""
Solutions for day 22.
"""

from os.path import dirname, join

INFECTED = True
CLEAN = False
UP = complex(-1, 0)
TURN_RIGHT = -1j
TURN_LEFT = 1j


class Cluster:
    def __init__(self, grid_path):
        self.grid, self.position = self.read_grid(grid_path)
        self.direction = UP
        self.infections = 0


    @property
    def current_node(self):
        return self.grid[self.position]


    @current_node.setter
    def current_node(self, status):
        self.grid[self.position] = status


    def read_grid(self, grid_path):
        grid = {}
        with open(grid_path) as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                grid[(i, j)] = char == '#'
        center = int((len(lines) - 1) / 2)
        position = center, center
        return grid, position


    def turn(self, turn_direction):
        self.direction *= turn_direction


    def burst(self):
        if self.current_node is INFECTED:
            self.turn(TURN_RIGHT)
        else:
            self.turn(TURN_LEFT)

        if self.current_node is CLEAN:
            self.current_node = INFECTED
            self.infections += 1
        else:
            self.current_node = CLEAN
        self.move()


    def move(self):
        i, j = self.position
        i += int(self.direction.real)
        j += int(self.direction.imag)
        position = i, j
        if position not in self.grid:
            self.grid[position] = CLEAN
        self.position = position


    def run(self, iterations):
        for _ in range(iterations):
            self.burst()
        return self.infections


def main():
    print('Part 1')
    example = Cluster(join(dirname(__file__), 'example.txt'))
    print('Solution to example:', example.run(10000))
    cluster = Cluster(join(dirname(__file__), 'grid.txt'))
    print('Solution to part 1:', cluster.run(10000))


if __name__ == '__main__':
    main()
