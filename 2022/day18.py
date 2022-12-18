import os
from collections import defaultdict
import aoc_tools


def adjacent(cube):
    x, y, z = cube
    return {
        (x, y, z-1),
        (x, y, z+1),
        (x, y-1, z),
        (x, y+1, z),
        (x-1, y, z),
        (x+1, y, z)
    }
    
    

def solution_part1(inputs):
    cubes = set()
    for line in inputs:
        cubes.add(tuple([int(n) for n in line.split(',')]))
    surface = 0
    for cube in cubes:
        for adj in adjacent(cube):
            if adj not in cubes:
                surface += 1
    
    return surface


def solution_part2(inputs):
    return -1


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=1
    )
    print(f"Solution for {day} part 1 = {solution_part1(inputs)}")
    print(f"Solution for {day} part 2 = {solution_part2(inputs)}")