import os
import aoc_tools

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.folders = {}
        self.files = {}     # Not necessary for this puzzle
        self.size = 0

    def add_folder(self, child_node):
        self.folders[child_node.name] = child_node

    def add_file(self, file_name, file_size):
        self.files[file_name] = file_size
        self.update_size(file_size)

    # Update total size of all parent folders until root
    def update_size(self, file_size):
        curr = self
        while curr:
            curr.size += file_size
            curr = curr.parent


def parse_and_generate_root_folder(inputs):
    root = Node('/')
    curr = root
    for line in inputs:
        line_split = line.split(' ')
        if line_split[0] == '$' and line_split[1] == 'ls':
            continue
        if line_split[0] == '$' and line_split[1] == 'cd':
            if line_split[2] == '..':
                curr = curr.parent
            elif line_split[2] == '/':
                curr = root
            else:
                curr = curr.folders[line_split[2]]
            continue
        
        if line_split[0] == 'dir':
            child = Node(line_split[1], curr)
            curr.add_folder(child)
        else:
            curr.add_file(line_split[1], int(line_split[0]))
    
    return root


def solution_both_parts(root):
    limit_part1 = 100000
    min_limit_part2 = 30000000 - 70000000 + root.size
    total_size = 0
    curr_min = root.size
    stack = [root]
    while stack:
        curr_node = stack.pop()
        # Solution for part1
        if curr_node.size <= limit_part1:
            total_size += curr_node.size
        # Solution for part2
        if min_limit_part2 <= curr_node.size < curr_min:
            curr_min = curr_node.size
        for child in curr_node.folders:
            stack.append(curr_node.folders[child])
    
    return total_size, curr_min
 

if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    root = parse_and_generate_root_folder(inputs)
    sol1, sol2 = solution_both_parts(root)
    print(f"Solution for {day} part 1 = {sol1}")
    print(f"Solution for {day} part 2 = {sol2}")