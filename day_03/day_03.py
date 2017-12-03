"""
Solutions for day 3.
"""

def update_xy(x, y, dx, dy, new_level):
    x += dx
    y += dy
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
    return x, y, dx, dy, new_level


def spiral_steps(n):
    x, y = -1, 0
    dx, dy = 1, 0
    new_level = False
    for _ in range(1, n+1):
        x, y, dx, dy, new_level = update_xy(x, y, dx, dy, new_level)
    return abs(x) + abs(y)


def spiral_stress(n):
    x, y = -1, 0
    dx, dy = 1, 0
    coords = {}
    new_level = False

    i = 1
    while True:
        x, y, dx, dy, new_level = update_xy(x, y, dx, dy, new_level)
        s = 1 if i == 1 else 0
        for otherX, otherY, otherS in coords.values():
            diffX = otherX - x
            diffY = otherY - y
            if abs(diffX) < 2 and abs(diffY) < 2:  # in range
                s += otherS
        if s > n:
            return s
        coords[i] = x, y, s
        i += 1


def main():
    MY_INPUT = 289326

    print('Part 1')
    EXAMPLES_1 = 1, 12, 23, 1024
    for example in EXAMPLES_1:
        solution = spiral_steps(example)
        print('Solution to {}: {}'.format(example, solution))
    solution1 = spiral_steps(MY_INPUT)
    print('Solution to part 1: {}'.format(solution1))

    print()

    print('Part 2')
    EXAMPLES_2 = 4, 15, 23, 800
    for example in EXAMPLES_2:
        solution = spiral_stress(example)
        print('Solution to {}: {}'.format(example, solution))
    solution2 = spiral_stress(MY_INPUT)
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
