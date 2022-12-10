import os
import aoc_tools

def solution_part1(inputs):
    check = [20, 60, 100, 140, 180, 220]
    cycle = 0
    add = 0
    idx = 0
    X = 1
    for line in inputs:
        val = 0
        if line == 'noop':
            cycle += 1
        else:
            val = int(line.split(' ')[1])
            cycle += 2
        if cycle == check[idx] or cycle == check[idx] + 1:
            add += X * check[idx]
            idx += 1
        X += val
        if idx >= len(check):
            break
    
    return add

# Part 2
def render(screen):
    for x in range(len(screen)):
        for y in range(len(screen[x])):
            print(screen[x][y], end='  ')
        print('\n')


def solution_part2(inputs):
    H = 6
    W = 40
    screen = [['.' for _ in range(W)] for _ in range(H)]
    
    X = 1
    row = 0
    col = 0
    for line in inputs:
        val = 0
        if line == 'noop':
            nb_cycle = 1
        else:
            val = int(line.split(' ')[1])
            nb_cycle = 2
        for _ in range(nb_cycle):
            if X-1 <= col <= X+1:
                screen[row][col] = '#'
            col += 1
            if col >= W:
                row += 1
                col = 0
        X += val
    render(screen)
    return 'PHLHJGZA'


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    print(f"Solution for {day} part 1 = {solution_part1(inputs)}")
    print(f"Solution for {day} part 2 = {solution_part2(inputs)}")