# Advent of Code 2020 - Day 19
# https://adventofcode.com/2020/day/19

import copy
from textwrap import wrap

rules = {}

allstrings = []
invalid = []

rules42 = []
rules31 = []

def build_all_strings(rule):
    global rules
    
    allrules = rules[rule]
    allresults = []
    for r in allrules:
        results = ['']
        for k in r:
            if k == 'a' or k == 'b':
                results = [k]
            else:
                temp = build_all_strings(k)
                temp2 = results.copy()
                results = []
                for  x in temp2:
                    for y in temp:
                        results.append(x + y)
        for k in results:
            allresults.append(k)
            
    return allresults


def checkvalid_42_31(s):
    global rules42
    global rules31
     
    s = wrap(s, 8)   
    for i in range(len(s) - 1):
        if s[i] not in rules42:
            return False
        if not (len(s) - i - 1) % 2 == 0:
            continue
        ok = True
        for j in range(i + 1, len(s)):
            k = len(s) - (j - (i + 1) + 1)
            if j > k:
                break
            if s[j] not in rules42 or s[k] not in rules31:
                ok = False
        if ok:
            return True
    return False


def checkmsgs(inp):
    global invalid
    global rules42
    global rules31

    start = False
    result = 0
    for m in inp:
        if m == '':
            start = True
        elif start == True:
            if m in allstrings:
                result += 1
            else:
                invalid.append(m)


    rules42 = build_all_strings('42')
    rules31 = build_all_strings('31')

#    0: 8 11
#    8: 42 | 42 8
#    11: 42 31 | 42 11 31

    part2 = 0
    for x in invalid:
        if checkvalid_42_31(x) == True:
            part2 += 1


    
    return result, result + part2
        

def init_rules(inp):
    global rules
    for s in inp:
        if s == '':
            break
        n,s = s[:s.find(':')], s[s.find(":") + 2:]
        if s == '"a"':
            rules[n] = 'a'
        elif s == '"b"':
            rules[n] = 'b'
        else:
            s = s.split(' | ')
            for i in range(len(s)):
                s[i] = s[i].split(' ')
            rules[n] = s  

f = open('./2020/input/2020_19.txt')
lines = f.read().splitlines()
f.close()

init_rules(lines)
allstrings = set(build_all_strings('0'))
print(checkmsgs(lines))


# 300 too low
# 362 too high

#print(checkmsgs(lines))