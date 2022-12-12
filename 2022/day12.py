import os
import aoc_tools
from collections import deque

def find_start_end(grid):
    start = None
    end = None
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'S':
                start = (x, y)
                if end:
                    return(start, end)
                continue
            if grid[x][y] == 'E':
                end = (x, y)
                if start:
                    return(start, end)
                continue
    return start, end


def height(letter):
    if letter == 'S':
        return ord('a')
    if letter == 'E':
        return ord('z')
    return ord(letter)


@aoc_tools.timeit
def find_shortest_path(grid: list, start: tuple, ends: set, go_up=True):
    H = len(grid)
    W = len(grid[0])
    visited = set(start)
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        # Stop condition
        if grid[x][y] in ends:
            return len(path) - 1

        curr_height = height(grid[x][y])
        # Check valid neighbors
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < H and 0 <= y2 < W:
                h = height(grid[x2][y2])
                check_elevation = h - curr_height if go_up else curr_height - h
                if check_elevation <= 1 and (x2, y2) not in visited:
                    queue.append(path + [(x2, y2)])
                    visited.add((x2, y2))
    return -1


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    grid = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    start, end = find_start_end(grid)
    print(f"Solution for {day} part 1 = {find_shortest_path(grid, start, {'E'})}")
    # Searching back from E => the first 'a' or 'S' found is the closest from E
    print(f"Solution for {day} part 2 = {find_shortest_path(grid, end, {'S', 'a'}, False)}")