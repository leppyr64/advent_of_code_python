# Advent of Code 2021 - Day 7
# https://adventofcode.com/2021/day/7

f = open('./2021/input/07.txt')
lines = f.read().splitlines() 
f.close()

init = lines[0].split(',')
init = [int(x) for x in init]
init.sort()

bestp1 = 1000000000
bestp2 = 1000000000
for i in range(2000):
    sum1 = 0
    sum2 = 0
    for x in init:
        d = abs(i - x)
        sum1 += d
        sum2 += d * (d + 1) // 2
    bestp1 = min(bestp1, sum1)
    bestp2 = min(bestp2, sum2)
print('Part 1', bestp1)
print('Part 2', bestp2)

