# Advent of Code 2021 - Day 13
# https://adventofcode.com/2021/day/13

f = open('./2021/input/13.txt')
#f = open('./2021/input/13_sample.txt')
lines = f.read().splitlines() 
f.close()

points = [[int(x) for x in l.split(',')] for l in lines if ',' in l]
folds = [x for x in lines if 'fold' in x]

def remdupes(points):
    list

part1 = -1
for f in folds:
    c, n = (f.split()[2]).split('=')
    n = int(n)
    points2 = []
    for p in points:
        p2 = p 
        if c == 'y' and p[1] > n:
            p2 = [p[0], n - (p[1] - n)]
        elif c == 'x' and p[0] > n:
            p2 = [n - (p[0] - n), p[1]]
        if p2 not in points2:
            points2.append(p2)    
    points = points2
    if part1 == -1:
        part1 = len(points)

print('Part 1', part1)

f = open('./2021/output.txt','w')
for y in range(7):
    for x in range(45):
        if [x,y] in points:
            f.write('*')
        else:
            f.write('.')
    f.write('\n')
f.close()


