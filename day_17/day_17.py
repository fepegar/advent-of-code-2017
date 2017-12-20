"""
Solutions for day 17.
"""

def spinlock(step, iterations=2017):
    state = [0]
    current_position = 0
    print_state(state, current_position)
    for i in range(iterations):
        end = (current_position + step) % len(state) + 1
        state.insert(end, i+1)
        current_position = end
        if i < 9:
            print_state(state, current_position)
    return state[current_position + 1]


def print_state(state, position):
    for i, n in enumerate(state):
        if i == position:
            print('({}) '.format(n), end='')
        else:
            print('{} '.format(n), end='')
    print()


def main():
    EXAMPLE = 3
    INPUT = 359

    print('Part 1')
    print('Solution to example: {}'.format(spinlock(EXAMPLE)))
    print('Solution to part 1: {}'.format(spinlock(INPUT)))


if __name__ == '__main__':
    main()
