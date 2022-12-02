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
    day = 1
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    input_file = f"./inputs/input_day{day}.txt"
    inputs = aoc_tools.get_inputs(input_file)
    solution_part1(inputs)
    # solution_part2(inputs)