# Advent of Code 2020 - Day 1
# https://adventofcode.com/2020/day/1

from itertools import combinations

f = open('./2020/input/01.txt')
lines = f.read().splitlines() 
f.close()
e = [int(x) for x in lines]
e.sort()

for a in e:
    if 2020 - a in [x for x in e if x < a]:
        print('Part1', a * (2020 - a), (a, 2020 - a))
    for b in [x for x in e if x < a]:
        if 2020 - a - b in [x for x in e if x < b]:
            print('Part2',a * b * (2020 - a - b), (a, b, 2020 - a - b))


def prod(x):
    r = 1
    for a in x:
        r *= a
    return r

a = [x for x in combinations(e, 2) if sum(x) == 2020][0]
print(a, prod(a))

a = [x for x in combinations(e, 3) if sum(x) == 2020][0]
print(a, prod(a))