# Advent of Code 2023 - Day 2
# https://adventofcode.com/2023/day/2

f = open('./2023/input/02.txt')
lines = f.read().splitlines() 
f.close()


#only 12 red cubes, 13 green cubes, and 14 blue cubes

part1 = 0
part2 = 0

for l in lines:
    x, y = l.split(': ')
    gamenum = int(x.split(' ')[1])
    rounds = y.split('; ')
    rgb = {'red':0,'green':0,'blue':0}
    for r in rounds:
        c = r.split(', ')
        for x in c:
            a,b = x.split(' ')
            rgb[b] = max(rgb[b], int(a))
    part2 += rgb['red'] * rgb['green'] * rgb['blue']
    if rgb['red'] > 12 or rgb['green'] > 13 or rgb['blue'] > 14:
        print('Impossible', gamenum)
    else:
        part1 += gamenum
        

print('Part 1', part1)
print('Part 2', part2)