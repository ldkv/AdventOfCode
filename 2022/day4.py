import os
import aoc_tools
      
def solution_both_parts(inputs):
    res1 = 0
    res2 = 0
    for line in inputs:
        elves = line.split(',')
        # part 1
        p1 = [int(x) for x in elves[0].split('-')]
        p2 = [int(x) for x in elves[1].split('-')]
        if (p2[0] <= p1[0] <= p2[1] and p2[0] <= p1[1] <= p2[1]) \
        or (p1[0] <= p2[0] <= p1[1] and p1[0] <= p2[1] <= p1[1]):
            res1 += 1
        # part 2
        if p2[0] <= p1[0] <= p2[1] or p2[0] <= p1[1] <= p2[1] \
        or p1[0] <= p2[0] <= p1[1] or p1[0] <= p2[1] <= p1[1]:
            res2 += 1
    
    return (res1, res2)


def solution_part2(inputs):
    pass


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(day, test_file=False)
    sol1, sol2 = solution_both_parts(inputs)
    print(f"Solution for {day} part 1 = {sol1}")
    print(f"Solution for {day} part 2 = {sol2}")