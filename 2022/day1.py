import os
import aoc_tools

def solution_part1(inputs):
    elves = []
    add = 0
    for line in inputs:
        if not line.strip():
            elves.append(add)
            add = 0
            continue
        add += int(line)
    
    elves.sort() # NlogN
    print(elves[-1], sum(elves[-3:]))


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(day)
    solution_part1(inputs)
    # solution_part2(inputs)