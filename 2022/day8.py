import os
import aoc_tools

def is_visible(matrix, h, x, y):
    found_higher = False
    for i in range(x-1, 0, -1):
        if matrix[i][y] >= h:
            found_higher = True
            break
    if not found_higher:
        return True 
    
    found_higher = False
    for i in range(x+1, len(matrix)):
        if matrix[i][y] >= h:
            found_higher = True
            break
    if not found_higher:
        return True 
    
    found_higher = False
    for j in range(y-1, 0, -1):
        if matrix[x][j] >= h:
            found_higher = True
            break
    if not found_higher:
        return True 
    
    found_higher = False
    for j in range(y+1, len(matrix[0])):
        if matrix[x][j] >= h:
            found_higher = True
            break
    if not found_higher:
        return True
    return False

def solution_part1(inputs):
    rows = len(inputs)
    cols = len(inputs[0])
    count = 0
    matrix = []
    for x in range(rows):
        row = []
        for y in range(cols):
            row.append(int(inputs[x][y]))
        matrix.append(row)

    for x in range(1, rows-1):
        for y in range(1, cols-1):
            print(matrix[x][y])
            if is_visible(matrix, matrix[x][y], x, y):
                count += 1
    
    return count + (rows-1)*(cols-1)


def solution_part2(inputs):
    return -1


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=True
    )
    print(f"Solution for {day} part 1 = {solution_part1(inputs)}")
    print(f"Solution for {day} part 2 = {solution_part2(inputs)}")