# Advent of Code 2023 - Day 12
# https://adventofcode.com/2023/day/12

f = open('./2023/input/12.txt')
lines = f.read().splitlines() 
f.close()

memo = []

def place_tile(s, p, i, j):
    if i + p[j] > len(s):
        return 0

    if i + p[j] == len(s):
        for k in range(p[j]):
            if s[i + k] == '.':
                return 0
        return num_tilings(s, p, i + p[j], j + 1)
    
    for k in range(p[j]):
        if s[i + k] == '.':
            return 0
    if s[i + p[j]] == '#':
        return 0
    return num_tilings(s, p, i + p[j] + 1, j + 1)

def num_tilings(s, p, i, j):
    if i >= len(s):
        if j == len(p):
            return 1
        return 0
    
    if j == len(p):
        for x in range(i, len(s)):
            if s[x] == '#':
                return 0
        return 1
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    if s[i] == '.':
        memo[i][j] = num_tilings(s, p, i + 1, j)
    
    if s[i] == '#':
        memo[i][j] = place_tile(s, p, i, j)
    
    if s[i] == '?':
        memo[i][j] = num_tilings(s, p, i + 1, j) + place_tile(s, p, i, j)

    return memo[i][j]

def get_result(s, p):
    p = [int(x) for x in p.split(',')]
    global memo
    memo = [[-1 for y in range(len(p))] for x in range(len(s))]
    return num_tilings(s, p, 0, 0)

part1 = 0
part2 = 0
for l in lines:
    s, p = l.split(' ')
    s2 = s
    p2 = p
    for z in range(4):
        s2 = s2 + '?' + s
        p2 = p2 + ',' + p
    
    part1 += get_result(s, p)
    part2 += get_result(s2, p2)

print('Part 1', part1)
print('Part 2', part2)