import os
import aoc_tools

def is_visible(matrix, x, y):
    h = matrix[x][y]
    found_higher = False
    for i in range(x-1, -1, -1):
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
    for j in range(y-1, -1, -1):
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


def find_distance(matrix, x, y):
    h = matrix[x][y]
    dist = 1
    count = 0
    for i in range(x-1, -1, -1):
        count += 1
        if matrix[i][y] >= h:
            break
    dist *= count

    count = 0
    for i in range(x+1, len(matrix)):
        count += 1
        if matrix[i][y] >= h:
            break
    dist *= count

    count = 0
    for j in range(y-1, -1, -1):
        count += 1
        if matrix[x][j] >= h:
            break
    dist *= count

    count = 0
    for j in range(y+1, len(matrix[0])):
        count += 1
        if matrix[x][j] >= h:
            break
    dist *= count
    return dist


def solution(inputs):
    rows = len(inputs)
    cols = len(inputs[0])
    count = 0
    maxi = 0
    for x in range(1, len(inputs)-1):
        for y in range(1, len(inputs[0])-1):
            if not is_visible(matrix, x, y):
                count += 1
            maxi = max(find_distance(matrix, x, y), maxi)
    
    return (rows*cols - count, maxi)


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    matrix = [[int(x) for x in row] for row in inputs]
    part1, part2 = solution(matrix)
    print(f"Solution for {day} part 1 = {part1}")
    print(f"Solution for {day} part 2 = {part2}")