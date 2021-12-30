# Advent of Code 2021 - Day 19
# https://adventofcode.com/2021/day/19

from itertools import permutations
import copy
from collections import defaultdict, deque

filename = './2021/input/19.txt'
#filename = './2021/input/19_sample.txt'
f = open(filename)
scanners = [x[1:] for x in [s.splitlines() for s in f.read().split('\n\n')]]
f.close()


# Points can be all six permutations of (x,y,z) -> (x, y, z), (x, z, y), (y, x, z), (y, z, x), (z, x, y), (z, y, x), 3! = 6 options
# All points can be + or - as well.  2^3 = 8 options
# 6 * 8 = 48 options
def adjust_point_orientation(pt, adj):
    assert(0 <= adj < 48)
    p = [pt[0], pt[1], pt[2]]
    if adj % 2 == 1:
        p[0] *= -1 
    adj //= 2
    if adj % 2 == 1:
        p[1] *= -1 
    adj //= 2
    if adj % 2 == 1:
        p[2] *= -1 
    adj //= 2
    assert(adj < 6)

    for i, perm in enumerate(permutations([0, 1, 2])):
        if i == adj:
            return (p[perm[0]], p[perm[1]], p[perm[2]])

def check_match(pta, ptb_orig):
    for i in range(48):
        ptb = [adjust_point_orientation(p, i) for p in ptb_orig]
        deltas = defaultdict(int)
        for a in pta:
            for b in ptb:
                dx = a[0] - b[0]
                dy = a[1] - b[1]
                dz = a[2] - b[2]
                deltas[(dx, dy, dz)] += 1
        for (dx, dy, dz), v in deltas.items():
            if v >= 12:
                retb = [(x + dx, y + dy, z + dz) for (x, y, z) in ptb]
                # return the good adjusted beacon here
                return retb, (dx, dy, dz)
    return None, None



pts = [[] for s in scanners]
for i, s in enumerate(scanners):
    for c in s:
        p = c.split(',')
        p = [int(x) for x in p]
        p = (p[0], p[1], p[2])
        pts[i].append(p)

done = set()
scanner_locs = [(0,0,0) for b in pts]
Q = deque()
Q.append(0)
done.add(0)
while Q:
    nxt = Q.popleft()
    for i in range(len(pts)):
        if i in done:
            continue
        p, bloc = check_match(pts[nxt], pts[i])
        if p is None:
            continue
        scanner_locs[i] = bloc
        pts[i] = p
        done.add(i)
        Q.append(i)

all_beacons = set()
for b in pts:
    for p in b:
        all_beacons.add(p)
print('Part 1', len(all_beacons))

part2 = 0
for a in scanner_locs:
    for b in scanner_locs:
        manhat = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        part2 = max(part2, manhat)

print('Part 2', part2)
