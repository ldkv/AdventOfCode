import os
import aoc_tools

def generate_bingo_boards_and_inputs(inputs):
    bingo_inputs = []
    for nb in inputs[0].split(','):
        bingo_inputs.append(int(nb))
    bingo_boards = []
    board = []
    for line in inputs[2:]:
        if not line:
            bingo_boards.append(board)
            board = []
        else:
            nbs = line.split(' ')
            row = []
            for n in nbs:
                if n.strip():
                    row.append(int(n))
            board.append(row)
    bingo_boards.append(board)
    return bingo_inputs, bingo_boards


def win_condition(board, x, y):
    # Check row
    found = True
    for i in range(5):
        if board[i][y] != -1:
            found = False
            break
    if found:
        return True
    # Check column
    found = True
    for i in range(5):
        if board[x][i] != -1:
            found = False
            break
    return found


def update_board(nb, board):
    found_win = False
    for x in range(5):
        for y in range(5):
            if board[x][y] == nb:
                board[x][y] = -1
                if win_condition(board, x, y):
                    found_win = True
                    return board, found_win
    return board, found_win


def calc_result(nb, board):
    add = 0
    for x in range(5):
        for y in range(5):
            if board[x][y] != -1:
                add += board[x][y]
    return add*nb


def solution_part1(inputs):
    bingo_inputs, bingo_boards = generate_bingo_boards_and_inputs(inputs)
    for nb in bingo_inputs:
        for id, _ in enumerate(bingo_boards):
            bingo_boards[id], found_win = update_board(nb, bingo_boards[id])
            if found_win:
                return calc_result(nb, bingo_boards[id])


def solution_part2(inputs):
    bingo_inputs, bingo_boards = generate_bingo_boards_and_inputs(inputs)
    won = set()
    for nb in bingo_inputs:
        for id, _ in enumerate(bingo_boards):
            if id in won:
                continue
            bingo_boards[id], found_win = update_board(nb, bingo_boards[id])
            if found_win:
                won.add(id)
                if len(won) == len(bingo_boards):
                    return calc_result(nb, bingo_boards[id])


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(day, test_file=False)
    print(solution_part1(inputs))
    print(solution_part2(inputs))