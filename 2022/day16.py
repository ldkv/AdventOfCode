import os
import functools
from collections import deque
import aoc_tools

# Global input to be use in functools cache without passing in parameters
grid = {}
all_valves = {}

def parse_input(inputs):
    graph = {}
    positive_valves = {}
    for line in inputs:
        line = line.split('Valve ')[1]
        valve = line[:2]
        line = line.split('has flow rate=')[1].split(';')
        pressure = int(line[0])
        if 'tunnels' in line[1]:
            tunnels = line[1].split('tunnels lead to valves ')[1].split(', ')
        else:
            tunnels = line[1].split('tunnel leads to valve ')[1].split(', ')
        if pressure > 0:
            positive_valves[valve] = pressure
        graph[valve] = {
            'to' : set(tunnels)
        }
    return graph, positive_valves


# Shortest distance map from a valve to all other valves (NxN)
def generate_dist_grid(inputs):
    graph, pressures = parse_input(inputs)
    grid = {}
    for src in graph:
        grid[src] = {}
        for dst in graph:
            queue = deque([(src, 0)])
            visited = set()
            while queue:
                v, dist = queue.popleft()
                if v == dst:
                    grid[src][dst] = dist
                    break
                if v in visited:
                    continue
                visited.add(v)
                for tun in graph[v]['to']:
                    if tun not in visited:
                        queue.append((tun, dist+1))
    return grid, pressures


@functools.cache
def find_fastest_route(mn_left, start, valves_left, elephant=False):
    global grid, all_valves
    # Initiate list with 0 to avoid error when call max function
    all_next_valves = [0]
    for v in valves_left:
        if grid[start][v] < mn_left:
            mn = mn_left - grid[start][v] - 1
            next_valve = find_fastest_route(mn, v, valves_left - {v}, elephant)
            all_next_valves.append(all_valves[v] * mn + next_valve)
    if elephant:
        all_next_valves.append(find_fastest_route(26, 'AA', valves_left))
    
    return max(all_next_valves)


@aoc_tools.timeit
def solution_part1():
    return find_fastest_route(30, 'AA', frozenset(all_valves))


# 13s with functools.cache / 3 minutes without
@aoc_tools.timeit
def solution_part2():
    return find_fastest_route(26, 'AA', frozenset(all_valves), True)


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=0
    )
    grid, all_valves = generate_dist_grid(inputs)
    print(f"Solution for {day} part 1 = {solution_part1()}")
    print(find_fastest_route.cache_info())
    print(f"Solution for {day} part 2 = {solution_part2()}")
    print(find_fastest_route.cache_info())