import os
import aoc_tools
import bisect
from collections import defaultdict


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_inputs(line):
    sensor, beacon = line.split(': closest beacon is at x=')
    sensor = sensor.split('Sensor at x=')[1]
    sensor = sensor.split(', y=')
    beacon = beacon.split(', y=')
    sx, sy = int(sensor[0]), int(sensor[1])
    bx, by = int(beacon[0]), int(beacon[1])
    return sx, sy, bx, by


@aoc_tools.timeit
def solution_part1(inputs, depth=2000000):
    occupied = []
    for line in inputs:
        sx, sy, bx, by = parse_inputs(line)
        dist = manhattan_distance((sx, sy), (bx, by))
        remain_dist = dist - abs(sy - depth)
        # Add horizontal range of occupied cell
        bisect.insort(occupied, (sx - remain_dist, sx + remain_dist))

    # Merge the ranges to count all occupied cells
    count = 0
    prev = occupied[0]
    for i in range(1, len(occupied)):
        if occupied[i][0] > prev[1] + 1:
            count += prev[1] - prev[0] + 1
            prev = occupied[i]
            continue
        prev = (prev[0], max(prev[1], occupied[i][1]))
    count += prev[1] - prev[0]
    
    return count


@aoc_tools.timeit
def solution_part2(inputs, max_depth=20):
    occupied = defaultdict(list)
    for line in inputs:
        sx, sy, bx, by = parse_inputs(line)
        dist = manhattan_distance((sx, sy), (bx, by))
        # Limit the range on Y
        start_y = max(0, sy - dist)
        stop_y = min(max_depth, sy + dist)
        for depth in range(start_y, stop_y + 1):
            remain_dist = dist - abs(sy - depth)
            # Save the range of X for each depth and each sensor in ascending order
            bisect.insort(occupied[depth], (sx - remain_dist, sx + remain_dist))
    print("HERE", len(occupied))

    for depth in occupied:
        ranges = occupied[depth]
        if len(ranges) == 0:
            return 0
        # Merge the ranges to find hole => answer
        prev = ranges[0]
        for i in range(1, len(ranges)):
            if ranges[i][0] > prev[1] + 1:
                return ((prev[1] + 1) * max_depth + depth)
            prev = (prev[0], max(prev[1], ranges[i][1]))

    return -1


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    is_test = 0 
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=is_test
    )
    depth = 2_000_000
    max_depth = 4000000
    if is_test:
        depth = 10
        max_depth = 20
    print(f"Solution for {day} part 1 = {solution_part1(inputs, depth)}")
    print(f"Solution for {day} part 2 = {solution_part2(inputs, max_depth)}")
