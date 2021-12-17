# Advent of Code 2021 - Day 14
# https://adventofcode.com/2021/day/14

from copy import copy, deepcopy

f = open('./2021/input/14.txt')
#f = open('./2021/input/14_sample.txt')
lines = f.read().splitlines() 
f.close()

init = lines[0]
memo = {}
pairs = {}

def addarray(a, b):
    result = copy(a)
    for i, x in enumerate(b):
        result[i] += x
    return result

def a0z25(c):
    return ord(c) - 65

for l in lines[2:]:
    x, c = l.split(' -> ')
    a = a0z25(x[0])
    b = a0z25(x[1])
    c = a0z25(c)

    pairs[(a, b)] = c
    memo[(a, b, 1)] = [0 for _ in range(26)]
    memo[(a, b, 1)][c] = 1
        
def dfs(l, r, n):
    if memo.get((l, r, n)) == None:
        m = pairs[(l, r)]
        a = dfs(l, m, n - 1)
        b = dfs(m, r, n - 1)
        a = addarray(a, b)
        a[m] += 1
        memo[(l, r, n)] = copy(a)
    return copy(memo.get((l, r, n)))

def get_result(init, depth):
    result = [0 for i in range(26)]
    a = a0z25(init[0])
    result[a] = 1
    for i in range(1, len(init)):
        a = a0z25(init[i - 1])
        b = a0z25(init[i])
        result[b] += 1
        step = dfs(a, b, depth)
        for x in range(26):
            result[x] += step[x]
    
    result = [x for x in result if x > 0]
    result.sort()
    return result[-1] - result[0] 

print('Part 1', get_result(init, 10))
print('Part 2', get_result(init, 40))