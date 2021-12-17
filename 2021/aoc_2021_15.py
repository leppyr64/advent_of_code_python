# Advent of Code 2021 - Day 15
# https://adventofcode.com/2021/day/15

import queue

f = open('./2021/input/15.txt')
#f = open('./2021/input/15_sample.txt')
lines = f.read().splitlines() 
f.close()

g = [[int(x) for x in l] for l in lines]
ROWS = len(g)
COLS = len(g[0])
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def shortest_path():
    Q = queue.PriorityQueue()
    best = {(0,0): 0}
    Q.put((0, 0, 0))
    while not Q.empty():
        dist, r, c = Q.get()
        #print(dist, r, c)
        if best.get((r,c)) == dist:
            for dr, dc in DELTA:
                rr = r + dr
                cc = c + dc
                if rr < 0 or rr >= ROWS or c < 0 or cc >= COLS:
                    continue
                dd = dist + g[rr][cc]
                if best.get((rr, cc)) == None or best.get((rr, cc)) > dd:
                    best[(rr, cc)] = dd
                    Q.put((dd, rr, cc))
    return (best.get((ROWS-1,COLS-1)))

print('Part 1', shortest_path())
    
ROWS = ROWS * 5
COLS = COLS * 5
g = [[0 for a in range(ROWS)] for b in range(COLS)]
for rmult in range(5):
    for cmult in range(5):
        for r in range(len(lines)):
            for c in range(len(lines[0])):
                g[rmult*len(lines) + r][cmult*len(lines[0]) + c] = (int(lines[r][c]) - 1 + rmult + cmult) % 9 + 1

print('Part 2', shortest_path())