# Advent of Code 2021 - Day 11
# https://adventofcode.com/2021/day/11

from typing import Deque

f = open('./2021/input/11.txt')
#f = open('./2021/input/11_sample.txt')
lines = f.read().splitlines() 
f.close()

g = [[int(x) for x in l] for l in lines]


ROWS = len(g)
COLS = len(g[0])
DELTA = [(-1,-1),(-1, 0), (-1, 1), (0,-1),(0,1),(1,-1),(1,0),(1,1)]

part1 = 0
part2 = 0
for n in range(1000):
    q = Deque()
    for r in range(ROWS):
        for c in range(COLS):
            g[r][c] += 1
            if g[r][c] == 10:
                q.append((r,c))
    
    while q:
        r,c = q.popleft()
        for dr,dc in DELTA:
            rr = r + dr
            cc = c + dc
            if rr < 0 or rr >= ROWS or cc < 0 or cc >= COLS:
                continue
            g[rr][cc] += 1
            if g[rr][cc] == 10:
                q.append((rr,cc))
    
    flashes = 0
    for r in range(ROWS):
        for c in range(COLS):
            if g[r][c] >= 10:
                flashes += 1
                g[r][c] = 0
    
    if n < 100:
        part1 += flashes
    if flashes == 100:
        part2 = n + 1
        break


print('Part 1', part1)
print('Part 2', part2)

