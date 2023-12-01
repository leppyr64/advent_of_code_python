# Advent of Code 2023 - Day 1
# https://adventofcode.com/2023/day/1

f = open('./2023/input/01.txt')
lines = f.read().splitlines() 
f.close()

def getamt_p1(s):
    lo = len(l)
    hi = -1
    lodig = 0
    hidig = 0
    for c in '0123456789':
        x = l.find(c)
        y = l.rfind(c)
        if x != -1 and x < lo:
            lo = x
            lodig = int(c)
        if y != -1 and y > hi:
            hi = y
            hidig = int(c)
    return lodig*10 + hidig

def getamt_p2(s):
    lo = len(l)
    hi = -1
    lodig = ''
    hidig = ''
    words = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    for c in words.keys():
        x = l.find(c)
        y = l.rfind(c)
        if x != -1 and x < lo:
            lo = x
            lodig = c
        if y != -1 and y > hi:
            hi = y
            hidig = c
    
    return words[lodig]*10 + words[hidig]

part1 = 0
part2 = 0

for l in lines:
    part1 += getamt_p1(l)
    part2 += getamt_p2(l)

print('Part 1:', part1)
print('Part 2:', part2)