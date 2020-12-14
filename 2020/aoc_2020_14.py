# Advent of Code 2020 - Day 14
# https://adventofcode.com/2020/day/14

import copy

def maskint(x, mask):
    result = x
    for i in range(len(mask)):
        c = mask[len(mask) - i - 1]
        if c == '0':
            y = (1<<i) & result
            result -= y
        elif c == '1':
            y = (1 << i) | result
            result = y
    return result


def maskmem(x, mask):
    result = x
    floaters = []
    for i in range(len(mask)):
        c = mask[len(mask) - i - 1]
        if c == '1':
            y = ((1 << i) & result) ^ (1 << i)
            result += y
        elif c == 'X':
            y = ((1 << i) & result) & (1 << i)
            result -= y
            floaters.append(i)
    floatmems = []
    for i in range((1<<len(floaters))):
        z = result
        for j in range(len(floaters)):
            if ((1 << j) & i) >= 1:
                z += (1 << floaters[j])
        floatmems.append(z)
    return result, floatmems

def process_inst(lines):
    allmem = {}
    mask = ''
    for l in lines:
        l = l.split(' ')
        if l[0] == 'mask':
            mask = l[2]
        else:
            mem = int(l[0].split('[')[1].split(']')[0])
            num = int(l[2])
            allmem[mem] = maskint(num, mask)
    sum = 0
    for k in allmem:
        sum += allmem[k]
    return sum

def process_inst_part2(lines):
    allmem = {}
    mask = ''
    for l in lines:
        l = l.split(' ')
        if l[0] == 'mask':
            mask = l[2]
        else:
            mem = int(l[0].split('[')[1].split(']')[0])
            num = int(l[2])
            x, mems = maskmem(mem, mask)
            for m in mems:
                allmem[m] = num
    sum = 0
    for k in allmem:
        #print(k, allmem[k])
        sum += allmem[k]
    return sum

#f = open('./2020/input/14_small.txt')
#lines = f.read().splitlines()
#f.close()
#print(process_inst(lines))
#print(process_inst_part2(lines))

f = open('./2020/input/2020_14.txt')
lines = f.read().splitlines()
f.close()
print(process_inst(lines))
print(process_inst_part2(lines))