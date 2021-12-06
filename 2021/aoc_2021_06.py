# Advent of Code 2021 - Day 6
# https://adventofcode.com/2021/day/6

f = open('./2021/input/06.txt')
lines = f.read().splitlines() 
f.close()

init = lines[0].split(',')
init = [int(x) for x in init]

def run_it(days):
    current = [0 for x in range(10)]
    for x in init:
        current[x] += 1
    for i in range(1, days + 1):
        x = current[0]
        for j in range(9):
            current[j] = current[j + 1]
        current[8] = x
        current[6] += x
    return sum(current)

print('Part 1', run_it(80))
print('Part 2', run_it(256))

