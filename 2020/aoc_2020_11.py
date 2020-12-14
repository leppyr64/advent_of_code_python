# Advent of Code 2020 - Day 11
# https://adventofcode.com/2020/day/11

from datetime import datetime
import time
import copy

CURR_MS = lambda:time.time()*1000

def count_occ(occ):
    result = 0
    for k in occ:
        if occ[k]:
            result += 1
    return result

def print_grid(g, occ):
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == '.':
                print(g[r][c],end='')
            elif occ[(r,c)]:
                print('#',end='')
            else:
                print('L',end='')
        print('')
    print('')

def build_adj(g, adjsteps):
    delta = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    adj = {}
    occ = {}
    for r in range(len(g)):
        for c in range(len(g[r])):
            if not g[r][c] =='.':
                adj[(r,c)] = []
                if g[r][c] == 'L':
                    occ[(r,c)] = False
                else:
                    occ[(r,c)] = True
                for d in range(8):
                    dr,dc = delta[d]
                    for step in range(1, adjsteps + 1):
                        nr,nc = r+dr*step,c+dc*step
                        if nr < 0 or nc < 0 or nr == len(g) or nc == len(g[0]):
                            break
                        if not g[nr][nc] == '.':
                            adj[(r,c)].append((nr,nc))
                            break
            
    return adj, occ

def get_occ(r1, c1, adj, occ):
    result = 0
    for r2,c2 in adj[r1,c1]:
        if occ[(r2,c2)]:
            result += 1
    return result

def stabilize(g, emptyrule, adjsteps):
    adj, occ = build_adj(g, adjsteps)
    changed = True
    idx = 0
    while changed:
        idx += 1
        changed = False
        occ2 = {}
        for r1,c1 in adj:
#            print(r1, c1, occ[r1,c1], get_occ(r1,c1,adj,occ))
            if occ[(r1,c1)] == True and get_occ(r1, c1, adj, occ) >= emptyrule:
                occ2[(r1,c1)] = False
                changed = True
            elif occ[(r1,c1)] == False and get_occ(r1, c1, adj, occ) == 0:
                occ2[(r1,c1)] = True
                changed = True
            else:
                occ2[(r1,c1)] = occ[(r1,c1)]

        occ = copy.deepcopy(occ2)

        #print_grid(g, occ)
    return count_occ(occ), idx

t1 = datetime.now()
ms1 = CURR_MS()
f = open('./2020/input/11.txt')
g = f.read().splitlines()
f.close()
g = [[c for c in r] for r in g]
print('Part1',stabilize(g, 4, 1))
t2 = datetime.now()
ms2 = CURR_MS()
print('Time', t2 - t1)
print('TIME TAKEN... %.6fms\n' % (ms2 - ms1))
f = open('./2020/input/11.txt')
g = f.read().splitlines()
f.close()
g = [[c for c in r] for r in g]
print('Part2',stabilize(g, 5, 1000000))
t3 = datetime.now()
ms3 = CURR_MS()
print('Time', t3 - t2)
print('TIME TAKEN... %.6fms\n' % (ms3 - ms2))

