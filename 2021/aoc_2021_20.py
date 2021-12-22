# Advent of Code 2021 - Day 20
# https://adventofcode.com/2021/day/20

from copy import copy

filename = './2021/input/20.txt'
#filename = './2021/input/20_sample.txt'
f = open(filename)
lines = f.read().splitlines()
f.close()

def getbin(s):
    result = 0
    for c in s:
        result *= 2
        if c == '#':
            result += 1
    return result


def enhance_pic(a, algo, cycle):
    result = 0

    border = '.'
    if cycle % 2 == 0:
        border = '#'

    R = len(a)
    C = len(a[0])

    b = copy(a)
    for r in range(R):
        rout = ''
        for c in range(C):
            s = ''
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    rr = r + dr
                    cc = c + dc
                    if rr < 0 or rr >= R or cc < 0 or cc >= C:
                        s += border
                    else:
                        s += a[rr][cc]
            rout += algo[getbin(s)]
            if rout[len(rout)-1] == '#':
                result += 1
        b[r] = rout
    return b, result

algo = lines[0]
picture = lines[2:]

g = [''.join(['.' for r in range(1000)]) for c in range(1000)]


lc = 500 - len(picture[0]) //  2
lr = 500 - len(picture) // 2

print(lr, lc)
for r in range(len(picture)):
    g[lr + r] = g[lr + r][:lc] + picture[r] + g[lr + r][lc + len(picture):]

lit = 0
for i in range(25):
    g, lit = enhance_pic(g, algo, 1)
    g, lit = enhance_pic(g, algo, 0)
    print(i, lit)
