import bisect

day = 1

def solution(f):
    sorted = []
    add = 0
    for line in f:
        if line == '\n':
            bisect.insort(sorted, add)
            add = 0
            continue
        add += int(line)
    
    print(sorted[-1])
    print(sum(sorted[-3:]))

if __name__ == '__main__':
    input_file = f"./inputs/input_day{day}.txt"
    with open(input_file, encoding = 'utf-8') as f:
        solution(f)