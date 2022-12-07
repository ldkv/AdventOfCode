import os
import aoc_tools

def calc_priority(letter):
    if ord(letter) >= 97:
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27


def solution_part1(inputs):
    res = 0
    for line in inputs:
        # Find same character in 1st and 2nd parts of same line
        ln = len(line)
        for let in line[:ln//2]:
            if let in line[ln//2:]:
                res += calc_priority(let)
                break
    return res
    

def solution_part2(inputs):
    res = 0
    idx = 0
    while idx < len(inputs):
        # Find same character in 3 consecutive lines
        first = ''
        for let in inputs[idx]:
            if let in inputs[idx + 1]:
                first += let
        for let in first:
            if let in inputs[idx + 2]:
                res += calc_priority(let)
                break
        idx += 3
    return res

    
if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(day, test_file=False)
    print(f"Solution for {day} part 1 = {solution_part1(inputs)}")
    print(f"Solution for {day} part 2 = {solution_part2(inputs)}")