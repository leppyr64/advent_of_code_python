# Advent of Code 2021 - Day 2
# https://adventofcode.com/2021/day/2

from itertools import combinations

f = open('./2021/input/02.txt')
lines = f.read().splitlines() 
f.close()

depthp1 = 0
pos = 0
aim = 0
depthp2 = 0
lines = [s.split(' ') for s in lines]

for step, d in lines:
    d = int(d)
    if step == 'forward':
        pos += d
        depthp2 += aim * d
    elif step == 'up':
        depthp1 -= d
        aim -= d
    else:
        depthp1 += d
        aim += d
    
print('Part 1', depthp1, pos, depthp1*pos)
print('Part 2', depthp2, pos, depthp2*pos)
 
