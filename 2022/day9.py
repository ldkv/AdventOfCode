import os
import aoc_tools

def calc_diff(x1, x2):
    if abs(x1-x2) <= 1:
        return 0
    return (x1 - x2) // 2


def move_tail(tx, ty, hx, hy):
    move_x = calc_diff(tx, hx)
    move_y = calc_diff(ty, hy)
    # Force diagonal moves
    if move_x != 0 and (move_y == 0 and ty != hy):
        return [tx - move_x, hy]
    if move_y != 0 and (move_x == 0 and tx != hx):
        return [hx, ty - move_y]

    return [tx - move_x, ty - move_y]


def solution_both_parts(inputs, nb_knots):
    moves = {
        'R': (1, 0),
        'L': (-1, 0),
        'D': (0, 1),
        'U': (0, -1)
    }
    knots = [[0, 0] for _ in range(nb_knots)]
    visited = {(0, 0)}
    for line in inputs:
        line = line.split(' ')
        dir = line[0]
        nb_move = int(line[1])
        for _ in range(nb_move):
            # Move head
            knots[0][0] += moves[dir][0]
            knots[0][1] += moves[dir][1]
            # Move all other knots
            for i in range(1, nb_knots):
                knots[i] = move_tail(knots[i][0], knots[i][1], knots[i-1][0], knots[i-1][1])
            # Add visited position of tail
            visited.add(tuple(knots[-1]))
    
    return len(visited)


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    print(f"Solution for {day} part 1 = {solution_both_parts(inputs, 2)}")
    print(f"Solution for {day} part 2 = {solution_both_parts(inputs, 10)}")