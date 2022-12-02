import bisect

def solution(f):
    strat1 = {
        'X' : {
            'point': 1,
            'A': 3,
            'B': 0,
            'C': 6
        },
        'Y' : {
            'point': 2,
            'A': 6,
            'B': 3,
            'C': 0
        },
        'Z' : {
            'point': 3,
            'A': 0,
            'B': 6,
            'C': 3
        }
    }

    strat2 = {
        'X' : {
            'point': 0,
            'A': 3,
            'B': 1,
            'C': 2
        },
        'Y' : {
            'point': 3,
            'A': 1,
            'B': 2,
            'C': 3
        },
        'Z' : {
            'point': 6,
            'A': 2,
            'B': 3,
            'C': 1
        }
    }

    add1 = 0
    add2 = 0

    for line in f:
        a = line.strip().split(' ')
        left = a[0]
        right = a[1]
        add1 += strat1[right]['point'] + strat1[right][left]
        add2 += strat2[right]['point'] + strat2[right][left]
    f.close()

    print(add1, add2)

day = 2
input_file = f"input_day{day}.txt"
with open(input_file, encoding = 'utf-8') as f:
   solution(f)