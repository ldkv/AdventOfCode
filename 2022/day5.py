import os
import aoc_tools

def parse_inputs(inputs):
    # Find line with number order of the stacks
    stack_line = 0
    while not (inputs[stack_line][0]==' ' and inputs[stack_line][1]=='1'):
        stack_line += 1
    
    # Calculate space (number of characters) between each cargo then parse stacks
    nb_stacks = int(inputs[stack_line].split(' ')[-1])
    stacks = [[] for _ in range(nb_stacks)]
    spaces = len(inputs[stack_line]) // nb_stacks
    for i in range(stack_line):
        line = inputs[i]
        for idx in range(1, len(line), spaces):
            if line[idx].strip():
                stacks[idx // spaces].append(line[idx])
    reverse_stacks = [s[::-1] for s in stacks]

    # Parse commands
    commands = []
    for line in inputs[stack_line+2:]:
        line = line.replace('move ', '').replace('from ', '').replace('to ', '')
        commands.append([int(x) for x in line.split(' ')])

    return (reverse_stacks, commands)


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
        test_file=True
    )
    print(f"Solution for {day} part 1 = {solution_part1(inputs)}")
    print(f"Solution for {day} part 2 = {solution_part2(inputs)}")