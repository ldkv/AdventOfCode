import os
import aoc_tools
from collections import deque

def find_start_end(grid):
    start = None
    end = None
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'S':
                start = (x, y)#, 'a', 0)
                if end:
                    return(start, end)
                continue
            if grid[x][y] == 'E':
                end = (x, y)#, 'z', -1)
                if start:
                    return(start, end)
                continue
    return start, end


def find_neighbors(pos, grid):
    (x, y, h, depth) = pos
    height = ord(h)
    neighbors = []
    if x > 0 and abs(ord(grid[x-1][y]) - height) <= 1:
        neighbors.append((x-1, y, grid[x-1][y], depth+1))
    if x < len(grid)-1 and abs(ord(grid[x+1][y]) - height) <= 1:
        neighbors.append((x+1, y, grid[x+1][y], depth+1))
    if y > 0 and abs(ord(grid[x][y-1]) - height) <= 1:
        neighbors.append((x, y-1, grid[x][y-1], depth+1))
    if y < len(grid[0])-1 and abs(ord(grid[x][y+1]) - height) <= 1:
        neighbors.append((x, y+1, grid[x][y+1], depth+1))
    return neighbors


def height(letter):
    if letter == 'S':
        return ord('a')
    if letter == 'E':
        return ord('z')
    return ord(letter)


def solution_part1(grid):
    H = len(grid)
    W = len(grid[0])
    start, end = find_start_end(grid)
    print(start, end, H, W)
    visited = set([start])
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[x][y] == 'E':
            return len(path) - 1
        curr_height = height(grid[x][y])
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < H and 0 <= y2 < W:
                h = height(grid[x2][y2])
                if (h - curr_height) <= 1 and (x2, y2) not in visited:
                    queue.append(path + [(x2, y2)])
                    visited.add((x2, y2))
    return -1

def find_possible_starts(grid):
    starts = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'a':
                starts.append((x, y))
    return starts

def solution_part2(grid):
    H = len(grid)
    W = len(grid[0])
    start, end = find_start_end(grid)
    print(start, end, H, W)
    starts = find_possible_starts(grid)
    start = end
    print(len(starts), start)
    min_path = H*W + 1
    for end in starts:
        visited = set([start])
        queue = deque([[start]])
        while queue:
            path = queue.popleft()
            if len(path) - 1 > min_path:
                continue
            x, y = path[-1]
            if grid[x][y] == grid[end[0]][end[1]] and len(path) - 1 < min_path:
                min_path = len(path) - 1
                break
            curr_height = height(grid[x][y])
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < H and 0 <= y2 < W:
                    h = height(grid[x2][y2])
                    if (curr_height - h) <= 1 and (x2, y2) not in visited:
                        queue.append(path + [(x2, y2)])
                        visited.add((x2, y2))
    return min_path

if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    grid = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    print(f"Solution for {day} part 1 = {solution_part1(grid)}")
    print(f"Solution for {day} part 2 = {solution_part2(grid)}")