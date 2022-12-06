import os
import aoc_tools

def solution(line, nb_distinct):
    char_set = []
    for idx, c in enumerate(line):
        if c in char_set:
            char_set = char_set[char_set.index(c)+1:]
        char_set.append(c)
        if len(char_set) == nb_distinct:
            return idx+1
    return -1


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    print(f"Solution for {day} part 1 = {solution(inputs[0], 4)}")
    print(f"Solution for {day} part 2 = {solution(inputs[0], 14)}")