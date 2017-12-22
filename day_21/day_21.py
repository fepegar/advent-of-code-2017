"""
Solutions for day 21.
"""

from os.path import dirname, join
import numpy as np


class Image:
    def __init__(self, rules_path):
        self.rules = self.read_rules(rules_path)
        self.grid = self.str2grid('.#./..#/###')


    def __repr__(self):
        return repr(self.grid)

    @property
    def size(self):
        return self.grid.shape[0]


    def str2grid(self, string):
        binary = string.replace('.', '0').replace('#', '1')
        rows = binary.split('/')
        size = len(rows[0])
        elements = [int(c) for row in rows for c in row]
        grid = np.array(elements).reshape(size, size)
        return grid


    def read_rules(self, rules_path):
        rules = {}
        with open(rules_path) as f:
            for line in f:
                input_pattern, output = line.split(' => ')
                rules[input_pattern] = output.strip()
        return rules


    def iterate(self):
        enhanced_chunks = []
        for chunk in self.split():
            enhanced_chunks.append(self.enhance(chunk))
        self.grid = self.merge(enhanced_chunks)


    def merge(self, chunks):
        rows = []
        n = np.sqrt(len(chunks)).astype(int)
        rows = self.split_list(chunks, n)
        rows = [np.hstack(row) for row in rows]
        merged = np.vstack(rows)
        return merged


    def split_list(self, l, n):
        """
        Yield successive n-sized chunks from l.
        https://stackoverflow.com/a/312464/3956024
        """
        for i in range(0, len(l), n):
            yield l[i:i + n]


    def enhance(self, chunk):
        for rule in self.rules:
            rule_grid = self.str2grid(rule)
            if self.match(chunk, rule_grid):
                return self.str2grid(self.rules[rule])


    def match(self, grid1, grid2):
        if grid1.shape != grid2.shape:
            return False
        for n in range(4):
            if (grid1 == np.rot90(grid2, n)).all():
                return True
            if (grid1 == np.rot90(np.fliplr(grid2), n)).all():
                return True
        return False


    def split(self):
        chunks = []
        if self.size % 2 == 0:
            pattern_size = 2
        elif self.size % 3 == 0:
            pattern_size = 3
        n = self.size / pattern_size
        rows = np.split(self.grid, n, axis=0)
        for row in rows:
            cols = np.split(row, n, axis=1)
            chunks.extend(cols)
        return chunks


    def run(self, iterations=1):
        for _ in range(iterations):
            self.iterate()


    def on_after(self, iterations):
        self.run(iterations=iterations)
        return self.grid.sum()


def main():
    print('Part 1')
    example = Image(join(dirname(__file__), 'example.txt'))
    print('Solution to example: {}'.format(example.on_after(2)))
    image = Image(join(dirname(__file__), 'artist_book.txt'))
    print('Solution to part 1: {}'.format(image.on_after(5)))


if __name__ == '__main__':
    main()
