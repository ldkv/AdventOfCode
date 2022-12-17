import os
from collections import deque
import aoc_tools

class Rock:
    figures = [
        [23, 24, 25, 26],       # @@@@
        [10, 16, 17, 18, 24],   # Cross
        [11, 18, 23, 24, 25],   # L reverse
        [2, 9, 16, 23],         # Vertical
        [16, 17, 23, 24]        # Square
    ]
    
    def __init__(self, rock_figure) -> None:
        self.rock = self.figures[rock_figure]
        self.height = (self.rock[-1] - self.rock[0]) // 7 + 1
    
    def push_rock(self, push_direction, depth, floor):
        """
        Floor : 4 levels or fewer based on depth
        - True  : there is obstacle
        - False : free floor
        """
        push = 1
        if push_direction == '<':
            push = -1
        pushable = True
        for r in self.rock:
            dx = r % 7 + push
            if dx < 0 or dx >= 7:
                pushable = False
                break
            if depth <= 0:
                rock_level = r // 7
                floor_level = 3 - rock_level + depth
                if floor_level < 0 and floor[floor_level][dx] == True:
                    pushable = False
                    break

        if pushable:
            self.rock = [r+push for r in self.rock]

    def droppable(self, depth, floor):
        if depth > 0:
            return True
        for r in self.rock:
            rock_level = r // 7 # 0-3
            next_floor_level = 2 - rock_level + depth
            if next_floor_level < 0:
                if floor[next_floor_level][r % 7] == True:
                    return False
        return True

    def drop_rock(self, jets, jet_index, floor):
        for depth in range(3):
            curr_jet = jets[jet_index]
            self.push_rock(curr_jet, depth, floor)
            jet_index = (jet_index + 1) % len(jets)
        
        depth = 0
        while True:
            curr_jet = jets[jet_index]
            self.push_rock(curr_jet, depth, floor)
            jet_index = (jet_index + 1) % len(jets)
            if not self.droppable(depth, floor):
                break
            depth -= 1
            
            # print(self.rock, curr_jet, jet_index, depth)
        floor = add_floor(depth, floor, self)
        # floor = cut_floor(floor)
        return floor, jet_index


def add_floor(depth, floor, rock):
    added_height = 0
    for _ in range(rock.height + depth):
        new_floor = [False] * 7
        added_height += 1
        floor.append(new_floor)
    for r in rock.rock:
        r_level = r // 7
        floor_level = (3 - r_level) - added_height + depth
        floor[floor_level][r % 7] = True
    # render_floor(floor)
    return floor


def cut_floor(floor):
    full_floor = [False] * 7
    count = 0
    for i in range(len(floor) - 1, -1, -1):
        for t, tile in enumerate(floor[i]):
            if tile and not full_floor[t]:
                full_floor[t] == tile
                count += 1
        if count >= 7:
            break
    print(i)
    floor = floor[i:]
    return floor


def render_floor(floor):
    for i in range(len(floor)-1, -1, -1):
        for tile in floor[i]:
            print(f"{'#' if tile else '.'}", end= ' ')
        print('\n')
    print('======================================')


def solution_part1(inputs):
    jets = inputs[0]
    width = 7
    floor = [[True] * width]
    jet_index = 0
    for r in range(2022):
        rock = Rock(r % 5)
        floor, jet_index = rock.drop_rock(jets, jet_index, floor)
    # render_floor(floor)
    return len(floor) - 1


def solution_part2(inputs):
    jets = inputs[0]
    width = 7
    floor = [[True] * width]
    jet_index = 0
    for r in range(2022):
        rock = Rock(r % 5)
        floor, jet_index = rock.drop_rock(jets, jet_index, floor)
    # render_floor(floor)
    return len(floor) - 1


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=0
    )
    print(f"Solution for {day} part 1 = {solution_part1(inputs)}")
    # print(f"Solution for {day} part 2 = {solution_part2(inputs)}")