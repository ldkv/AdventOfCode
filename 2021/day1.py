import os
import aoc_tools

def solution_part1(inputs):
    prev = float('inf')
    res = 0
    for line in inputs:
        curr = int(line)
        if curr > prev:
            res += 1
        prev = curr

    print(res)


def solution_part2(inputs):
    res = 0
    curr = prev = 0
    count = 0
    for idx, line in enumerate(inputs):
        line = int(line)
        if count < 3:
            curr += line
            prev += line
            count += 1
            continue
        curr = curr + line - int(inputs[idx-3])
        if prev < curr + line - int(inputs[idx-3]):
            res += 1
        prev = curr
            
    print(res)


if __name__ == '__main__':
    day = 1
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    input_file = f"./inputs/input_day{day}.txt"
    inputs = aoc_tools.get_inputs(input_file)
    solution_part1(inputs)
    solution_part2(inputs)