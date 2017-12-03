
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

    s = 0
    i = 0

    while True:
        i += 1
        x, y, dx, dy, new_level = update_xy(x, y, dx, dy, new_level)
        s = 0
        if i == 1:
            s = 1
        for otherX, otherY, otherS in coords.values():
            # print(n, k, otherX, otherY, otherS)
            diffX = otherX - x
            diffY = otherY - y
            if abs(diffX) < 2 and abs(diffY) < 2:  # in range
                s += otherS
        coords[i] = x, y, s
        if s > n:
            return s


def main():
    my_input = 289326
    print('Part 1')
    EXAMPLES_1 = 1, 12, 23, 1024
    for example in EXAMPLES_1:
        solution = spiral_steps(example)
        print('Solution to {}: {}'.format(example, solution))
    solution1 = spiral_steps(my_input)
    print('Solution to part 1: {}'.format(solution1))

    print(2*'\n')

    print('Part 2')
    EXAMPLES_2 = 4, 15, 23, 800
    for example in EXAMPLES_2:
        solution = spiral_stress(example)
        print('Solution to {}: {}'.format(example, solution))
    solution2 = spiral_stress(my_input)
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
