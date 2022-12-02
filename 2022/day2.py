import os
import aoc_tools

def solution_part1(f):
    strat_part1 = {
        'X' : {
            'point': 1,
            'A': 3,
            'B': 0,
            'C': 6
        },
        'Y' : {
            'point': 2,
            'A': 6,
            'B': 3,
            'C': 0
        },
        'Z' : {
            'point': 3,
            'A': 0,
            'B': 6,
            'C': 3
        }
    }
    strat_part2 = {
        'X' : {
            'point': 0,
            'A': 3,
            'B': 1,
            'C': 2
        },
        'Y' : {
            'point': 3,
            'A': 1,
            'B': 2,
            'C': 3
        },
        'Z' : {
            'point': 6,
            'A': 2,
            'B': 3,
            'C': 1
        }
    }

    res1 = 0
    res2 = 0

    for line in f:
        a = line.strip().split(' ')
        left = a[0]
        right = a[1]
        res1 += strat_part1[right]['point'] + strat_part1[right][left]
        res2 += strat_part2[right]['point'] + strat_part2[right][left]

    print(res1, res2)

if __name__ == '__main__':
    day = 2
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    input_file = f"./inputs/input_day{day}.txt"
    inputs = aoc_tools.get_inputs(input_file)
    solution_part1(inputs)
    # solution_part2(inputs)