# Advent of Code 2021 - Day 3
# https://adventofcode.com/2021/day/3

from itertools import combinations



f = open('./2021/input/03.txt')
#f = open('./2021/input/03_sample.txt')
lines = f.read().splitlines() 
f.close()

count = [[0,0] for i in range(10000)]
for l in lines:
    idx = 1
    for c in l:
        x = int(c)
        count[idx][x] += 1
        idx = idx * 2 + x

idx = 1
result = ''
while sum(count[idx]) > 0:
    x = 0
    if sum(count[idx]) == 1:
        if count[idx][1] == 1:
            x = 1
    elif count[idx][0] <= count[idx][1]:
        x = 1
    result += str(x)
    idx = idx * 2 + x
a = int(result,2)

idx = 1
result = ''
while sum(count[idx]) > 0:
    x = 1
    if sum(count[idx]) == 1:
        if count[idx][0] == 1:
            x = 0
    elif count[idx][1] >= count[idx][0]:
        x = 0
    result += str(x)
    idx = idx * 2 + x
b = int(result,2)

print(b*a)