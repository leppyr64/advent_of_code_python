# Advent of Code 2020 - Day 4
# https://adventofcode.com/2020/day/4

import string

f = open('./2020/input/04.txt')
lines = f.read().splitlines()
f.close()

def is_valid_passport(passport):
    result = True
    if 'byr' in passport:
        if len(passport['byr']) != 4 or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            result = False
    else:
        result = False

    if 'iyr' in passport:
        if len(passport['iyr']) != 4 or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            result = False
    else:
        result = False

    if 'eyr' in passport:
        if len(passport['eyr']) != 4 or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            result = False
    else:
        result = False

    if 'hcl' in passport:
        if len(passport['hcl']) != 7 or not all(c in string.hexdigits for c in passport['hcl'][1:]):
            result = False
    else:
        result = False

    eyc = ['amb','blu','brn','gry','grn','hzl','oth']
    if 'ecl' in passport:
        if passport['ecl'] not in eyc:
            result = False
    else:
        result = False

    if 'pid' in passport:
        if len(passport['pid']) != 9 or not all(c in string.digits for c in passport['pid']):
            result = False
    else:
        result = False

    if 'hgt' in passport:
        if len(passport['hgt']) < 4:
            result = False
        elif passport['hgt'][-2:] == 'cm':
            h = int(passport['hgt'][:-2])
            if h < 150 or h > 193:
                result = False
        elif passport['hgt'][-2:] == 'in':
            h = int(passport['hgt'][:-2])
            if h < 59 or h > 76:
                result = False
        else:
            result = False

    else:
        result = False



    return result
idx = 0
categories = {'byr':0,'iyr':0,'eyr':0,'hgt':0,'hcl':0,'ecl':0,'pid':0,'cid':1}
passports = {}

for l in lines:
    if idx not in passports:
        passports[idx] = {}
    if len(l) == 0:
        idx += 1
    else:
        for tags in l.split(' '):
            tag,val = tags.split(':')
            passports[idx][tag] = val

part1 = 0
part2 = 0
for idx in passports:
    is_valid = True
    for tag in categories:
        if categories[tag] == 0 and tag not in passports[idx]:
            is_valid = False
    if is_valid:
        part1 += 1
    if is_valid_passport(passports[idx]):
        part2 += 1

print('Part1',part1)
print('Part2',part2)

