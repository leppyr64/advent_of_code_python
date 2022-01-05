# Advent of Code 2021 - Day 22
# https://adventofcode.com/2021/day/22

import re

filename = './2021/input/22.txt'
#filename = './2021/input/22_sample.txt'
f = open(filename)
lines = f.read().splitlines()
f.close()


### PART 1 - Naive - Will be too slow for Part 2
def reboot(is_part1):
    G = set()
    for l in lines:
        op, coords = l.split()
        (x1, x2, y1, y2, z1, z2) = [int(x) for x in re.findall('-?\d+', coords)]
        if is_part1 and (x1 < -50 or x2 > 50 or y1 < -50 or y2 > 50 or z1 < -50 or z2 > 50):
            continue
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    if op == 'on':
                        G.add((x,y,z))
                    else:
                        G.discard((x,y,z))
    return len(G)

print('Part 1', reboot(True))


# Part 2 - There are small things I can do better, but this takes too long.  It's right though.
X = set()
Y = set()
Z = set()

for l in lines:
    op, coords = l.split()
    (x1, x2, y1, y2, z1, z2) = [int(x) for x in re.findall('-?\d+', coords)]
    X.add(x1)
    X.add(x2 + 1)
    Y.add(y1)
    Y.add(y2 + 1)
    Z.add(z1)
    Z.add(z2 + 1)

X = sorted(X) 
Y = sorted(Y) 
Z = sorted(Z) 

mx = 0

G = set()
for l in lines:
    op, coords = l.split()
    (x1, x2, y1, y2, z1, z2) = [int(x) for x in re.findall('-?\d+', coords)]
    idx_x2 = X.index(x2 + 1)
    idx_x1 = X.index(x1)
    idx_y2 = Y.index(y2 + 1)
    idx_y1 = Y.index(y1)
    idx_z2 = Z.index(z2 + 1)
    idx_z1 = Z.index(z1)

    for x in range(idx_x1, idx_x2):
        for y in range(idx_y1, idx_y2):
            for z in range(idx_z1, idx_z2):
                if op == 'on':
                    G.add((x,y,z))
                else:
                    G.discard((x,y,z))
result = 0            
for (x,y,z) in G:
    result += (X[x+1] - X[x]) * (Y[y+1] - Y[y]) * (Z[z+1] - Z[z])
    

print('Part 2', result)