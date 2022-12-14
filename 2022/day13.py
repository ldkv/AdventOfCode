import os
import aoc_tools
import json

# Bad manual parsing - not working => using JSON
def parse_packet(pack_str):
    packet = []
    stack = []
    for i in pack_str:
        match(i):
            case '[':
                stack.append([])
            case ']':
                last_stack = stack.pop()
                if len(last_stack) + len(stack) > 0:
                    packet.append(last_stack)
            case ',':
                continue
            case _:
                stack[-1].append(int(i))
    return packet


def compare_packet(packet1, packet2):
    """
    There are 3 possible return values:
        1 => packet1 < packet2 => valid pair
        0 => packet1 == packet2 => continue to check
       -1 => packet1 > packet2 => invalid pair
    """
    for idx, ele1 in enumerate(packet1):
        if idx >= len(packet2):
            return -1
        ele2 = packet2[idx]
        if type(ele1) == type(ele2) == int:
            if ele1 > ele2:
                return -1
            if ele1 < ele2:
                return 1
            continue
        if type(ele1) == int:
            ele1 = [ele1]
        if type(ele2) == int:
            ele2 = [ele2]
        res = compare_packet(ele1, ele2)
        if res != 0:
            return res
    if len(packet1) < len(packet2):
        return 1
    return 0


def solution_both_parts(inputs):
    sum_pair = 0
    all_packets = []
    for i in range(0, len(inputs), 3):
        packet1 = json.loads(inputs[i])
        packet2 = json.loads(inputs[i+1])
        all_packets.append(packet1)
        all_packets.append(packet2)
        res = compare_packet(packet1, packet2)
        if res > 0:
            sum_pair += (i // 3) + 1
    
    pos_2 = 1
    pos_6 = 2
    pack_2 = [[2]]
    pack_6 = [[6]]
    for packet in all_packets:
        if compare_packet(packet, pack_2):
            pos_2 += 1
        if compare_packet(packet, pack_6):
            pos_6 += 1
    return sum_pair, pos_2 * pos_6


if __name__ == '__main__':
    day = os.path.basename(__file__).split('.')[0]
    inputs = aoc_tools.generate_input_filename_and_get_inputs(
        day,
        raw_input=False,
        test_file=False
    )
    print(f"Solution for {day} part 1 & 2 = {solution_both_parts(inputs)}")