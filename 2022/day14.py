import os
import aoc_tools


def render(cave):
    H = len(cave)
    W = len(cave[0])
    for y in range(H):
        for x in range(W):
            print(cave[y][x], end = ' ')
        print('\n', end='')
    print('\n')


def parse_input(inputs):
    max_x = -1
    max_y = -1
    min_x = float('inf')
    rocks = []
    for line in inputs:
        coords = line.split(' -> ')
        for c in coords:
            x, y = c.split(',')
            x, y = int(x), int(y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            min_x = int(min(x, min_x))
            rocks.append((x, y))
        rocks.append((-1, -1))
    # print(min_x, max_x, max_y)
    
    offset_x = 2001
    width =  max_x - min_x + offset_x
    cave = [['.' for _ in range(width)] for _ in range(max_y + 3)]
    min_x -= offset_x // 2
    start = None
    # Fill cave with rocks
    for (x, y) in rocks:
        if x == -1:
            start = None
            continue 
        if start == None:
            start = (x, y)
            cave[y][x-min_x] = '#'
            continue
        start_x, stop_x = min(start[0], x+1), max(start[0], x+1)
        start_y, stop_y = min(start[1], y+1), max(start[1], y+1)
        for i in range(start_x, stop_x):
            cave[y][i-min_x] = '#'
        for j in range(start_y, stop_y):
            cave[j][x-min_x] = '#'
        start = (x, y)
        # render(cave)
    for x in range(width):
         cave[len(cave)-1][x] = '#'
    return (cave, min_x, max_y)

    
def solution_both_parts(inputs):
    cave, min_x, max_y = parse_input(inputs)
    s_x, s_y = (500 - min_x, 0)
    count_part1 = 0
    count_part2 = 0
    stop_count_part1 = False
    while True:
        if s_y > max_y:
            stop_count_part1 = True
        if cave[s_y][s_x] == 'o':
            break
        if cave[s_y+1][s_x] == '.':
            s_y = s_y + 1
        elif cave[s_y+1][s_x-1] == '.':
            s_x = s_x - 1
            s_y = s_y + 1
        elif cave[s_y+1][s_x+1] == '.':
            s_x = s_x + 1
            s_y = s_y + 1
        else:
            cave[s_y][s_x] = 'o'
            # render(cave)
            if not stop_count_part1:
                count_part1 += 1
            count_part2 += 1
            s_x, s_y = (500 - min_x, 0)
    
    return count_part1, count_part2


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    print(f"Solution for {day} part 1&2 = {solution_both_parts(inputs)}")