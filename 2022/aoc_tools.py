# Tools for AoC 2022
import os

def clean_line(line, convert_to_int=True):
    l = line.strip()
    if convert_to_int:
        l = int(l)
    return l


def generate_input_filename(day, test_file=False):
    test = ""
    if test_file:
        test = "test_"
    return f"./inputs/{test}input_{day}.txt"


def get_inputs(input_file, raw_input=False, convert_to_int=False):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    inputs = []
    with open(input_file, encoding = 'utf-8') as f:
        if raw_input:
            return f.readlines()
        for line in f:
            inputs.append(clean_line(line, convert_to_int))
    return inputs


def generate_input_filename_and_get_inputs(day, raw_input=False, convert_to_int=False, test_file=False):
    input_filename = generate_input_filename(day, test_file)
    return get_inputs(input_filename, raw_input, convert_to_int)