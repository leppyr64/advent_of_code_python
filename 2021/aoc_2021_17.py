# Advent of Code 2021 - Day 17
# https://adventofcode.com/2021/day/17

filename = './2021/input/17.txt'
#filename = './2021/input/17_sample.txt'
f = open(filename)
lines = f.read().splitlines()
f.close()

lines = lines[0][13:]
lines = lines.split(', ')
lines[0] = lines[0][2:].split('..')
lines[1] = lines[1][2:].split('..')

xmin = int(lines[0][0])
xmax = int(lines[0][1])
ymin = int(lines[1][0])
ymax = int(lines[1][1])

def time_to_target(initx, inity, xmin, xmax, ymin, ymax):
    xpos, ypos = 0, 0
    xvel, yvel = initx, inity
    for i in range(-2 * ymin + 1):
        xpos += xvel
        ypos += yvel
        xvel = max(0, xvel - 1)
        yvel = yvel - 1
        if xpos >= xmin and xpos <= xmax and ypos >= ymin and ypos <= ymax:
            return i + 1
    return -1

part1 = (-1 * ymin) * (-1 * ymin - 1) // 2
print('Part 1', part1)

part2 = 0 
maxchk = 0
for initx in range(0, xmax + 5):
    for inity in range(ymin, -1 * ymin + 5):
        chk = time_to_target(initx, inity, xmin, xmax, ymin, ymax)
        if chk > -1:
            maxchk = max(chk, maxchk)
            part2 += 1
print('Part 2', part2)