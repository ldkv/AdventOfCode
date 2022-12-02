import os
import aoc_tools

def solution_part1(inputs):
    hor = 0
    dep = 0
    for line in inputs:
        move = line.split(' ')
        move[1] = int(move[1])
        if move[0] == 'forward':
            hor += move[1]
        if move[0] == 'up':
            dep -= move[1]
        if move[0] == 'down':
            dep += move[1]

    print(hor*dep)


def solution_part2(inputs):
    hor = 0
    dep = 0
    aim = 0
    for line in inputs:
        move = line.split(' ')
        move[1] = int(move[1])
        if move[0] == 'up':
            aim -= move[1]
        if move[0] == 'down':
            aim += move[1]
        if move[0] == 'forward':
            hor += move[1]
            dep += aim*move[1]

    print(hor*dep)


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(day)
    solution_part1(inputs)
    solution_part2(inputs)