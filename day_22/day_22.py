"""
Solutions for day 22.
"""

import sys
from os.path import dirname, join

CLEAN = '.'
INFECTED = '#'
FLAGGED = 'F'
WEAKENED = 'W'

UP = complex(-1, 0)
TURN_RIGHT = -1j
TURN_LEFT = 1j


class Cluster:
    def __init__(self, grid_path):
        self.grid = {}
        # for i in range(-10, 10):
        #     for j in range(-10, 10):
        #         self.grid[(i, j)] = CLEAN
        self.position = self.read_grid(grid_path)
        self.direction = UP
        self.infections = 0


    def __repr__(self):
        s = ''
        imax = jmax = sys.float_info.min
        imin = jmin = sys.float_info.max
        for i, j in self.grid:
            imax = max(imax, i)
            jmax = max(jmax, j)
            imin = min(imin, i)
            jmin = min(jmin, i)

        for i in range(imin, imax + 1):
            for j in range(jmin, jmax + 1):
                position = i, j
                if position in self.grid:
                    value = self.grid[position]
                else:
                    value = CLEAN

                if self.position == (i, j+1):
                    suffix = '['
                elif self.position == (i, j):
                    suffix = ']'
                else:
                    suffix = ' '
                s += value + suffix
            s += '\n'
        return s


    @property
    def current_node(self):
        return self.grid[self.position]


    @current_node.setter
    def current_node(self, status):
        self.grid[self.position] = status


    def read_grid(self, grid_path):
        with open(grid_path) as f:
            lines = [line.strip() for line in f.readlines()]
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                self.grid[(i, j)] = char
        center = int((len(lines) - 1) / 2)
        position = center, center
        return position


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
