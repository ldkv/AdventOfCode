import os
from collections import deque 
import aoc_tools

def parse_inputs(inputs):
    stacks = [deque() for _ in range((len(inputs[0]) + 1) // 4)]
    i = 0
    while inputs[i][1] != '1':
        line = inputs[i]
        for idx in range(1, len(line), 4):
            if line[idx].strip():
                stacks[idx // 4].appendleft(line[idx])
        i += 1
    
    commands = []
    for line in inputs[i+2:]:
        line = line.replace('move ', '').replace('from ', '').replace('to ', '')
        commands.append([int(x) for x in line.split(' ')])
    
    return (stacks, commands)


def solution_part1(inputs):
    stacks, commands = parse_inputs(inputs)
    for (nb, start, dest) in commands:
        start -= 1
        dest -= 1
        for _ in range(nb):
            cargo = stacks[start].pop()
            stacks[dest].append(cargo)
    
    res1 = ''
    for cargo in stacks:
        res1 += cargo.pop()

    return res1


def solution_part2(inputs):
    stacks, commands = parse_inputs(inputs)
    for (nb, start, dest) in commands:
        start -= 1
        dest -= 1
        stack_to_move = [stacks[start].pop() for _ in range(nb)]
        for s in stack_to_move[::-1]:
            stacks[dest].append(s)
    
    res2 = ''
    for cargo in stacks:
        res2 += cargo.pop()

    return res2


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=True,
        test_file=False
    )
    print(f"Solution for {day} part 1 = {solution_part1(inputs)}")
    print(f"Solution for {day} part 2 = {solution_part2(inputs)}")