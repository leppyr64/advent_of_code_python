# Advent of Code 2020 - Day 16
# https://adventofcode.com/2020/day/16

import copy



def process_case(inp):
    rules = {}
    yourticket = ''
    othertickets = []
    invalid = []

    for z in inp:
        if z == '':
            break
        r, ranges = z.split(': ')
        r1, r2 = ranges.split(' or ')
        r1 = r1.split('-')
        r2 = r2.split('-')
        rules[r] = []
        for x in range(int(r1[0]), int(r1[1]) + 1):
            rules[r].append(x)
        for x in range(int(r2[0]), int(r2[1]) + 1):
            rules[r].append(x)
    
    idx = inp.index('nearby tickets:')
    othertickets = [x.split(',') for x in inp[idx+1:]]
    for i in range(len(othertickets)):
        othertickets[i] = [int(x) for x in othertickets[i]]
    yourticket = inp[inp.index('your ticket:')+1]
    yourticket = [int(x) for x in yourticket.split(',')]

    part1 = 0
    for t in othertickets:
        valid = True
        for v in t:
            found = False
            for r in  rules:
                if v in rules[r]:
                    found = True
            if found == False:
                part1 += v
                valid = False
        if valid == False:
            invalid.append(t)

    for t in invalid:
        othertickets.remove(t)

       
    totalpossiblities = [list(rules.keys())  for k in rules]
    for t in othertickets:
        possible = [[] for k in rules]
        for i in range(len(t)):
            for k in rules:
                if t[i] in rules[k]:
                    possible[i].append(k)
        for i in range(len(totalpossiblities)):
            totalpossiblities[i] = [value for value in totalpossiblities[i] if value in possible[i]] 
        
    print(totalpossiblities)
    for i in range(len(totalpossiblities)):
        for j in range(len(totalpossiblities)):
            if len(totalpossiblities[j]) == 1:
                for k in range(len(totalpossiblities)):
                    if not k == j:
                        if totalpossiblities[j][0] in totalpossiblities[k]:
                            totalpossiblities[k].remove(totalpossiblities[j][0])
    
    fields = [k[0] for k in totalpossiblities]
    
    ticket = {}
    for i in range(len(fields)):
        ticket[fields[i]] = yourticket[i]

    part2 = 1
    for k in ticket:
        print(k, ticket[k])
        if k.find('departure') > -1:
            part2 *= ticket[k]


    return part1, part2




f = open('./2020/input/2020_16.txt')
lines = f.read().splitlines()
f.close()

print(process_case(lines))

f = open('./2020/input/2020_16.txt')
lines = f.read().splitlines()
f.close()

#print(process_case(lines))