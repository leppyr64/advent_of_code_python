# Advent of Code 2021 - Day 5
# https://adventofcode.com/2021/day/5

#f = open('./2021/input/05_sample.txt')
f = open('./2021/input/05.txt')
lines = f.read().splitlines() 
f.close()

def run_it(part):
    #grid = [[0 for r in range(10)] for c in range(10)]
    grid = [[0 for r in range(1000)] for c in range(1000)]
    
    for l in lines:
        a,b = l.split(' -> ')
        c1,r1 = a.split(',')
        c2,r2 = b.split(',')

        c1 = int(c1)
        c2 = int(c2)
        r1 = int(r1)
        r2 = int(r2)

        if c1 == c2:
            if r1 > r2:
                x = r1
                r1 = r2
                r2 = x
            for r in range(r1, r2 + 1):
                grid[r][c1] += 1
        elif r1 == r2:
            if c1 > c2:
                x = c1
                c1 = c2
                c2 = x
            for c in range(c1, c2 + 1):
                grid[r1][c] += 1
        elif part == 2:
            n = abs(r2 - r1) + 1
            stepr = 1
            if r1 > r2:
                stepr = -1
            stepc = 1
            if c1 > c2:
                stepc = -1
            for i in range(n):
                grid[r1 + i * stepr][c1 + i * stepc] += 1
            
    count = 0
    for r in grid:
        for c in r:
            # if c==0:
            #     print('.', end='')
            # else:
            #     print(c, end='')
            if c > 1:
                count += 1
        #print('')

    print('Part', part, count)

run_it(1)
run_it(2)