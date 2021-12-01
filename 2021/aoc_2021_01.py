# Advent of Code 2021 - Day 1
# https://adventofcode.com/2021/day/1

from itertools import combinations

f = open('./2021/input/01.txt')
lines = f.read().splitlines() 
f.close()


depths = [int(x) for x in lines]
sums = [0 for x in depths]
sums.append(0)

inc1 = 0
inc3 = 0
n = len(depths)
for i in range(1,n+1):
    sums[i] = sums[i-1] + depths[i-1]
    
for (part, step) in [(1,1),(2,3)]:
    inc = 0
    for i in range(step+1, n+1):
        if sums[i] - sums[i-step] > sums[i-1] - sums[i-1-step]:
            inc += 1
    print('Part', part, step, inc)
