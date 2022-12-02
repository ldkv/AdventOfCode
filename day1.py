day = 1

def solution(f):
    elves = []
    add = 0
    for line in f:
        if line == '\n':
            elves.append(add)
            add = 0
            continue
        add += int(line)
    
    elves.sort() # NlogN
    print(elves[-1])
    print(sum(elves[-3:]))

if __name__ == '__main__':
    input_file = f"./inputs/input_day{day}.txt"
    with open(input_file, encoding = 'utf-8') as f:
        solution(f)