# Advent of Code 2021 - Day 12
# https://adventofcode.com/2021/day/12

from collections import deque

f = open('./2021/input/12.txt')
#f = open('./2021/input/12_sample.txt')
lines = f.read().splitlines() 
f.close()

adj = {}
for l in lines:
    a,b = l.split('-')
    if a not in adj:
        adj[a] = []
    if b not in adj:
        adj[b] = []
    adj[a].append(b)
    adj[b].append(a)

def find_paths(allow_duplicate):
    result = 0
    Q = deque()
    if allow_duplicate:
        Q.append(('start', 'start ', False))
    else:
        Q.append(('start', 'start ', True))
    while Q:
        cur, path, used_duplicate = Q.popleft()
        if cur == 'end':
            #print(path)
            result += 1
            continue
        for nxt in adj[cur]:
            if nxt == 'start':
                continue
            if nxt == nxt.lower() and nxt in path:
                if used_duplicate:
                    continue
                else:
                    Q.append((nxt, path + nxt + ' ', True))
            else:
                Q.append((nxt, path + nxt + ' ', used_duplicate))
    return result

print('Part 1', find_paths(False))
print('Part 2', find_paths(True))