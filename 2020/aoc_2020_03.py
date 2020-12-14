# Advent of Code 2020 - Day 3
# https://adventofcode.com/2020/day/3

#f = open('./2020/input/03_small.txt')
f = open('./2020/input/03.txt')
lines = f.read().splitlines()
f.close()

def CountTrees(g, dr, dc):
    c = 0
    numtrees = 0
    for r in range(0, len(g), dr):
        if g[r][c] == '#':
            numtrees += 1
        c = (c + dc) % len(g[r])
    print(dr, dc, numtrees)
    return numtrees

x = 1
x *= CountTrees(lines, 1, 1)
x *= CountTrees(lines, 1, 3)
x *= CountTrees(lines, 1, 5)
x *= CountTrees(lines, 1, 7)
x *= CountTrees(lines, 2, 1)

print('Part1', CountTrees(lines, 1, 3))
print('Part2', x)




