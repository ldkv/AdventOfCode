import bisect

f = open("input_day1.txt", "r")
count = 0

max = []
add = 0
for x in f:
    if x == '\n':
        bisect.insort(max, add)
        add = 0
        continue
    add += int(x)

print(sum(max[-3:]))