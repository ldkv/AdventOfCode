import os
from collections import defaultdict
import aoc_tools
from aoc_tools import timeit

# Bad time complexity: N * w
# N=300k | w=100k => 70s
@timeit
def bad_solution(line, nb_distinct):
    char_set = []
    for idx, c in enumerate(line):
        c = int(c)
        try:
            id = char_set.index(c)
            char_set = char_set[id+1:]
        except:
            pass
        char_set.append(c)
        if len(char_set) == nb_distinct:
            return idx+1
    return -1


# N=300k | w=100k => 60ms
# N=3M   | w=1M   => 600ms
# Best case scenario: O(w) => w = length of sliding window
# Worst case scenario: O( (N - w + 1) * w )
# Average time complexity: depends on inputs arrangement, I don't know...
@timeit
def solution_big_inputs(lines, nb_distinct):
    distinct = {}
    i = 0
    while i < len(lines):
        nb = lines[i]
        if nb not in distinct:
            distinct[nb] = i
            i += 1
            if len(distinct) >= nb_distinct:
                return i
        else:
            i = distinct[nb] + 1
            distinct = {}
    
    return -1


if __name__ == '__main__':
    # Real input
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        convert_to_int=False,
        test_file=False
    )
    print(f"Solution for {day} part1 = {solution_big_inputs(inputs[0], 4)}")
    print(f"Solution for {day} part2 = {solution_big_inputs(inputs[0], 14)}")

    # Big inputs (N=300k | w=100k)
    day = os.path.basename(__file__).split('.')[0] + "_small"
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        convert_to_int=True,
        test_file=True
    )
    w = 100_000
    # print(f"Bad solution for small inputs = {bad_solution(inputs, w)}")
    print(f"Small inputs = {solution_big_inputs(inputs, w)}")
    
    # REALLY BIG inputs (N=3M | w=1M)
    day = os.path.basename(__file__).split('.')[0] + "_big"
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        convert_to_int=True,
        test_file=True
    )
    w = 1_000_000
    print(f"Big inputs = {solution_big_inputs(inputs, w)}")