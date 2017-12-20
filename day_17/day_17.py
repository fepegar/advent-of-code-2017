"""
Solutions for day 17.
"""

from collections import deque

class Spinlock:
    def __init__(self, step):
        self.value = 0
        self.state = deque([self.value])
        self.current_position = 0
        self.step = step

    def __getitem__(self, index):
        index = self.get_circular_index(index)
        return self.state[index]

    def __len__(self):
        return len(self.state)

    def __repr__(self):
        s = ''
        for i, n in enumerate(self.state):
            if i == self.current_position:
                s += '({}) '.format(n)
            else:
                s += '{} '.format(n)
        return s

    def index(self, item):
        return self.state.index(item)

    def get_circular_index(self, index):
        return index % len(self)

    def rotate(self, n):
        self.state.rotate(n)

    def append(self, item):
        self.state.append(item)

    def iterate(self, iterations=1):
        for i in range(iterations):
            if i % 1000000 == 0: print(int(i/1000000))
            new_index = self.get_circular_index(self.current_position + self.step)
            self.rotate(len(self) - self.index(self[new_index]) - 1)
            self.value += 1
            self.append(self.value)
            self.current_position = self.value

    def reset(self):
        self.value = 0
        self.state = deque([self.value])
        self.current_position = 0

    def get_item_after(self, iterations, element=None):
        self.reset()
        self.iterate(iterations=iterations)
        if element is None:  # part 1
            return self[0]
        else:
            return self[self.index(element) + 1]


def main():
    EXAMPLE = 3
    INPUT = 359
    N1 = 2017
    N2 = 50000000
    example = Spinlock(EXAMPLE)
    spinlock = Spinlock(INPUT)
    print('Part 1')
    print('Solution to example: {}'.format(example.get_item_after(N1)))
    print('Solution to part 1: {}'.format(spinlock.get_item_after(N1)))

    print()

    print('Part 2')
    print('Solution to part 2: {}'.format(spinlock.get_item_after(N2, element=0)))


if __name__ == '__main__':
    main()
