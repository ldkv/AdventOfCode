import os
import aoc_tools

class Node:
    def __init__(self, name, type='D', size=0, parent=None):
        self.name = name
        self.parent = parent
        self.type = type
        self.children = {}
        self.size = size
        if type == 'F':
            self.children = None
 
    def add_child(self, child_node):
        if child_node.name not in self.children: 
            self.children[child_node.name] = child_node

    def update_size(self):
        if self.type == 'F':
            return self.size
        self.size = 0
        for child in self.children:
            self.size += self.children[child].update_size()
        return self.size

    def find_nodes(self, limit=100000):
        if self.type == 'F':
            return 0
        add = 0
        for child in self.children:
            if self.children[child].type == 'D' and self.children[child].size <= limit:
                add += self.children[child].size
            add += self.children[child].find_nodes()
        return add


def generate_root_folder(inputs):
    root = Node('/')
    curr = root
    for line in inputs[2:]:
        read = line.split(' ')
        if read[0] == '$' and read[1] == 'cd':
            if read[2] == '..':
                curr = curr.parent
            elif read[2] == '/':
                curr = root
            else:
                curr = curr.children[read[2]]
            continue
        if read[0] == '$' and read[1] == 'ls':
            continue

        if read[0] == 'dir':
            child = Node(read[1], 'D', 0, curr)
        else:
            child = Node(read[1], 'F', int(read[0]), curr)
        curr.add_child(child)
    root.update_size()    
    return root


def solution_part1(root):
    res1 = root.find_nodes(100000)
    return res1


def solution_part2(root):
    min_limit = 30000000 - 70000000 + root.size
    curr_min = root
    stack = [root]
    while stack:
        curr_node = stack.pop()
        if curr_node.type == 'F':
            continue
        if curr_node.size >= min_limit and curr_node.size < curr_min.size:
            curr_min = curr_node
        for child in curr_node.children:
            stack.append(curr_node.children[child])
    return curr_min.size
 

if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    root = generate_root_folder(inputs)
    print(f"Solution for {day} part 1 = {solution_part1(root)}")
    print(f"Solution for {day} part 2 = {solution_part2(root)}")