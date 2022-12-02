import os
import aoc_tools

def count_bits(inputs):
    zeros = [0] * (len(inputs[0]))
    ones = [0] * (len(inputs[0]))
    for line in inputs:
        for idx, bit in enumerate(line.strip()):
            if bit == '0':
                zeros[idx] += 1
            else:
                ones[idx] += 1
    return(zeros, ones)


def solution_part1(inputs):
    (zeros, ones) = count_bits(inputs)
    eps = ''
    gamma = ''
    for i in range(len(zeros)):
        if zeros[i] > ones[i]:
            gamma += '0'
            eps += '1'
        else:
            gamma += '1'
            eps += '0'

    print(int(gamma, 2) * int(eps, 2))


def generate_most_least(inputs, pos):
    nb_zeros = 0
    nb_ones = 0
    zeros = []
    ones = []
    for line in inputs:
        line = line.strip()
        if line[pos] == '0':
            nb_zeros += 1
            zeros.append(line)
        else:
            nb_ones += 1
            ones.append(line)
    
    if nb_ones >= nb_zeros:
        return (ones, zeros)
    return (zeros, ones)


def solution_part2(inputs):
    curr_most, curr_least = generate_most_least(inputs, 0)
    ln = len(inputs[0])    
    pos = 1
    while len(curr_most) > 1 and pos < ln:
        curr_most, _ = generate_most_least(curr_most, pos)
        pos += 1
    # print(curr_most, pos)
    
    pos = 1
    while len(curr_least) > 1 and pos < ln:
        _, curr_least = generate_most_least(curr_least, pos)
        print(len(curr_least))
        pos += 1
    # print(curr_least, pos)
    print(int(curr_most[0], 2) * int(curr_least[0], 2))


if __name__ == '__main__':
    day = 3
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    input_file = f"./inputs/input_day{day}.txt"
    inputs = aoc_tools.get_inputs(input_file)
    solution_part1(inputs)
    solution_part2(inputs)