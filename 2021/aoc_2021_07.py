# Advent of Code 2021 - Day 7
# https://adventofcode.com/2021/day/7

import math

f = open('./2021/input/07.txt')
lines = f.read().splitlines() 
f.close()

init = lines[0].split(',')
init = [int(x) for x in init]

# simple to understand method
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

# big brain method
init.sort()

median = init[len(init)//2]
part1 = sum([abs(median - x) for x in init])

mean_low = int(math.floor(sum(init) / len(init)))
part2_1 = sum([(abs(x - mean_low))*(abs(x - mean_low)+1)//2 for x in init])
mean_high = int(math.ceil(sum(init) / len(init)))
part2_2 = sum([(abs(x - mean_high))*(abs(x - mean_high)+1)//2 for x in init])

print('Part 1', part1)
print('Part 2', min(part2_1, part2_2))