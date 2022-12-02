import os
import aoc_tools

def solution_part1(inputs):
    prev = float('inf')
    res = 0
    for line in inputs:
        curr = line
        if curr > prev:
            res += 1
        prev = curr

    print(res)


def solution_part2(inputs):
    res = 0
    curr = prev = 0
    count = 0
    for idx, line in enumerate(inputs):
        line = line
        if count < 3:
            curr += line
            prev += line
            count += 1
            continue
        curr = curr + line - inputs[idx-3]
        if prev < curr:
            res += 1
        prev = curr

    print(res)


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(day, convert_to_int=True)
    solution_part1(inputs)
    solution_part2(inputs)