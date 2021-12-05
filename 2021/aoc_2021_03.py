# Advent of Code 2021 - Day 3
# https://adventofcode.com/2021/day/3

from itertools import combinations

f = open('./2021/input/03.txt')
#f = open('./2021/input/03_sample.txt')
lines = f.read().splitlines() 
f.close()

def part1():
    mostcommon = ''
    leastcommon = ''

    for i in range(len(lines[0])):
        count = [0,0]
        for l in lines:
            x = int(l[i])
            count[x] += 1
        print(i, count)
        if count[0] > count[1]:
            mostcommon += '0'
            leastcommon += '1'
        elif count[0] < count[1]:
            mostcommon += '1'
            leastcommon += '0'
        else:
            assert False
    print(mostcommon, leastcommon)
    print(int(mostcommon,2), int(leastcommon,2))
    print(int(mostcommon, 2) * int(leastcommon, 2))

def part2():
    mostcommon = ''
    leastcommon = ''

    for i in range(len(lines[0])):
        count = [0,0]
        for l in lines:
            x = int(l[i])
            count[x] += 1
        if count[0] > count[1]:
            mostcommon += '0'
            leastcommon += '1'
        elif count[0] < count[1]:
            mostcommon += '1'
            leastcommon += '0'
        else:
            assert False
    print(mostcommon, leastcommon)
    
    print(int(mostcommon, 2) * int(leastcommon, 2))

def getmostlestcommon(lst, most):
    for i in range(len(lst[0])):
        count = [0,0]
        for l in lst:
            x = int(l[i])
            count[x] += 1
        match = '1'
        if most == True and count[0] > count[1]:
            match = '0'
        elif most == True:
            match = '1'
        elif count[1] < count[0]:
            match = '1'
        else:
            match = '0'

        lst2 = []
        for l in lst:
            if l[i] == match:
                lst2.append(l)
        lst = lst2
        if len(lst) == 1:
            return lst[0]
    return lst[0]

# mostcommon = getmostlestcommon(lines, True)
# leastcommon = getmostlestcommon(lines, False)
# print(mostcommon, leastcommon)
# print(int(mostcommon,2), int(leastcommon,2))
# print(int(mostcommon, 2) * int(leastcommon, 2))

part1()

