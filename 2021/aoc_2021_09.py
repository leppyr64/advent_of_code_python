# Advent of Code 2021 - Day 9
# https://adventofcode.com/2021/day/9

f = open('./2021/input/09.txt')
#f = open('./2021/input/09_sample.txt')
lines = f.read().splitlines() 
f.close()

ROWS = len(lines)
COLS = len(lines[0])
DELTA = [(-1, 0), (0,-1), (1, 0), (0, 1)]

g = []
for l in lines:
    r = [int(c) for c in l]
    r.insert(0, 10)
    r.append(10)
    g.append(r)
g.insert(0, [10 for _ in range(len(lines[0]) + 2)])
g.append([10 for _ in range(len(lines[0]) + 2)])

basin_map = [[0 for c in r] for r in g]
basin_size = [0 for _ in range(100000)]
basins = 0

part1 = 0
for h in range(9):
    for r in range(1, ROWS + 1):
        for c in range(1, COLS + 1):
            if g[r][c] == h:
                for dr, dc in DELTA:
                    if g[r + dr][c + dc] < g[r][c]:
                        basin_map[r][c] = basin_map[r + dr][c +dc]
                        basin_size[basin_map[r][c]] += 1
                        break
                if basin_map[r][c] == 0:
                    part1 += g[r][c] + 1
                    basins += 1
                    basin_map[r][c] = basins
                    basin_size[basins] = 1
                    

basin_size = basin_size[1:basins+1]
basin_size.sort(reverse=True)

print('Part 1', part1)
print('Part 2', basin_size[0] * basin_size[1] * basin_size[2])
