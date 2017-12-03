
def spiral_coords(n):
    x, y = -1, 0
    dx, dy = 1, 0
    coords = {}
    new_level = False
    for i in range(1, n+1):
        x += dx
        y += dy
        coords[i] = x, y

        if new_level:
            dx = 0
            dy = 1
            new_level = False
        elif x + y == 0:
            if dx > 0:  # go right to next level
                dx = 1
                dy = 0
                new_level = True
            else:  # go down
                dx = 0
                dy = -1
        elif x == y:  # left if upper right, right if bottom left
            dx = -1 if x > 0 else 1
            dy = 0

    return coords


def spiral_steps(n):
    coords = spiral_coords(n)
    coords_n = coords[n]
    return abs(coords_n[0]) + abs(coords_n[1])


def main():
    print('Part 1')
    EXAMPLES_1 = 1, 12, 23, 1024
    for example in EXAMPLES_1:
        solution = spiral_steps(example)
        print('Solution to {}: {}'.format(example, solution))
    solution1 = spiral_steps(289326)
    print('Solution to part 1: {}'.format(solution1))

    print(2*'\n')


if __name__ == '__main__':
    main()
