# Tools for AoC 2022
import math
import bisect

def clean_line(line, convert_to_int = True):
    l = line.strip()
    if convert_to_int:
        l = int(l)
    return l

def get_inputs(input_file, convert_to_int = False):
    inputs = []
    with open(input_file, encoding = 'utf-8') as f:
        for line in f:
            inputs.append(clean_line(line, convert_to_int))
    return inputs