import os
import aoc_tools

def parse_monkeys(inputs):
    monkeys = {}
    i = 0
    while i < len(inputs):
        # Parse items
        i += 1
        items = inputs[i].split(':')[1].strip()
        items = [int(x) for x in items.split(', ')]
        # Parse operation
        i += 1
        op = inputs[i].split('new = old ')[1].split(' ')
        op_nb = None if op[1] == 'old' else int(op[1])
        # Parse mod
        i += 1
        mod = int(inputs[i].split('by ')[1])
        # Parse next monkey
        i += 1
        true = int(inputs[i].split('monkey ')[1])
        i += 1
        false = int(inputs[i].split('monkey ')[1])
        i += 2
        monkeys[i//7-1] = {
            'items' : items,
            'ope'   : op[0],
            'op_nb' : op_nb,
            'mod'   : mod,
            'true'  : true,
            'false' : false,
            'active': 0
        }

    return monkeys


def calc_operation(x, op, op_nb, divider=3):
    if op_nb == None:
        op_nb = x
    new_item = x
    match(op):
        case '*':
            new_item = x * op_nb
        case '+':
            new_item = x + op_nb
        case '-':
            new_item = x - op_nb
        case '/':
            new_item = x // op_nb
    new_item = new_item // divider if divider==3 else new_item % divider
    return new_item


def monkey_business_rounds(monkeys, nb_rounds, divider=3):
    for _ in range(nb_rounds):
        for i in range(len(monkeys)):
            for item in monkeys[i]['items']:
                monkeys[i]['active'] += 1
                new_item = calc_operation(item, monkeys[i]['ope'], monkeys[i]['op_nb'], divider)
                next_monkey = monkeys[i]['false']
                if new_item % monkeys[i]['mod'] == 0:
                    next_monkey = monkeys[i]['true']
                monkeys[next_monkey]['items'].append(new_item)
            monkeys[i]['items'] = []
    return monkeys


# Calculate result from number of inspections
def calc_inspections(monkeys):
    list_active = [monkeys[i]['active'] for i in range(len(monkeys))]
    list_active.sort()
    res = list_active[-1] * list_active[-2]
    return res


# Part 1
def solution_part1(inputs):
    monkeys = parse_monkeys(inputs)
    monkeys = monkey_business_rounds(monkeys, 20)
    res = calc_inspections(monkeys)
    return res


# Modulo number for part2
# Since all modulos in inputs are prime numbers, we can just multiply them together
def calc_modulo(monkeys):
    modulo = 1
    set_modulo = {1}
    for i in range(len(monkeys)):
        if monkeys[i]['mod'] not in set_modulo:
            modulo *= monkeys[i]['mod']
        set_modulo.add(monkeys[i]['mod'])
    return modulo


# Part 2
def solution_part2(inputs):
    monkeys = parse_monkeys(inputs)
    modulo = calc_modulo(monkeys)
    monkeys = monkey_business_rounds(monkeys, 10000, modulo)
    res = calc_inspections(monkeys)
    return res


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    print(f"Solution for {day} part 1 = {solution_part1(inputs)}")
    print(f"Solution for {day} part 2 = {solution_part2(inputs)}")