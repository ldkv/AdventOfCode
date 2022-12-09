import os
import aoc_tools

moves = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1)
}

def calc_diff(x1, x2):
    if x1-x2 == -1:
        return 0
    return (x1 - x2) // 2

def move_tail(pos_tail, pos_head):
    if abs(pos_tail[0] - pos_head[0]) <= 1 \
        and abs(pos_tail[1] - pos_head[1]) <= 1:
        return pos_tail
    
    # return [
    #     pos_tail[0] - calc_diff(pos_tail[0], pos_head[0]),
    #     pos_tail[1] - calc_diff(pos_tail[1], pos_head[1])
    # ]
    if pos_tail[0] - pos_head[0] == 2:
        if pos_tail[1] - pos_head[1] == 2:
            return [pos_tail[0]-1, pos_tail[1]-1]
        if pos_tail[1] - pos_head[1] == -2:
            return [pos_tail[0]-1, pos_tail[1]+1]
        return [pos_tail[0]-1, pos_head[1]]
    if pos_tail[0] - pos_head[0] == -2:
        if pos_tail[1] - pos_head[1] == 2:
            return [pos_tail[0]+1, pos_tail[1]-1]
        if pos_tail[1] - pos_head[1] == -2:
            return [pos_tail[0]+1, pos_tail[1]+1]
        return [pos_tail[0]+1, pos_head[1]]
    if pos_tail[1] - pos_head[1] == 2:
        if pos_tail[0] - pos_head[0] == 2:
            return [pos_tail[0]-1, pos_tail[1]-1]
        if pos_tail[0] - pos_head[0] == -2:
            return [pos_tail[0]+1, pos_tail[1]-1]
        return [pos_head[0], pos_tail[1]-1]
    if pos_tail[1] - pos_head[1] == -2:
        if pos_tail[0] - pos_head[0] == 2:
            return [pos_tail[0]-1, pos_tail[1]+1]
        if pos_tail[0] - pos_head[0] == -2:
            return [pos_tail[0]+1, pos_tail[1]+1]
        return [pos_head[0], pos_tail[1]+1]
    # print(pos_tail, pos_head)
    return None


def solution_part1(inputs):
    print(move_tail((0,0), (-1,2)))
    curr_head = [0, 0]
    curr_tail = [0, 0]
    visited = {(0, 0)}
    for line in inputs:
        line = line.split(' ')
        dir = line[0]
        nb_move = int(line[1])
        for i in range(nb_move):
            curr_head[0] += moves[dir][0]
            curr_head[1] += moves[dir][1]
            curr_tail = move_tail(curr_tail, curr_head)
            visited.add(tuple(curr_tail))
    return len(visited)


def solution_part2(inputs):
    nb_knots = 10
    knots = [[0, 0] for _ in range(nb_knots)]
    print(knots)
    visited = {(0, 0)}
    for line in inputs:
        line = line.split(' ')
        dir = line[0]
        nb_move = int(line[1])
        for _ in range(nb_move):
            knots[0][0] += moves[dir][0]
            knots[0][1] += moves[dir][1]
            for i in range(1, nb_knots):
                try:
                    knots[i] = move_tail(knots[i], knots[i-1])
                except:
                    print(line)
                    print(knots)
                    return
            visited.add(tuple(knots[-1]))
        # print(knots)
    return len(visited)


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=True
    )
    print(f"Solution for {day} part 1 = {solution_part1(inputs)}")
    print(f"Solution for {day} part 2 = {solution_part2(inputs)}")