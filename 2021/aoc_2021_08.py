# Advent of Code 2021 - Day 8
# https://adventofcode.com/2021/day/8

f = open('./2021/input/08.txt')
#f = open('./2021/input/08_sample.txt')
lines = f.read().splitlines() 
f.close()

#length: digits
#2: 1
#3: 7
#4: 4
#7: 8

# |_|  ->   |_  = four_vs_one
#   |   

#5: 2, 3, 5
#   3 - contains 1
#   5 - contains four_vs_one
#   2 - only one left

#6: 0, 6, 9
#   9 - contains 4
#   6 - contains four_vs_one
#   0 - only one left

def contains(whole, sub):
    for c in sub:
        if c not in whole:
            return False
    return True

def get_code(digits, sevseg):
    result = 0
    for s in sevseg:
        s = ''.join(sorted(s))
        for i, d in enumerate(digits):
            if s == d:
                result = result * 10 + i
    return result

def find_digits(sevseg):
    digits = ['' for _ in range(10)]
    for i,s in enumerate(sevseg):
        s = ''.join(sorted(s))
        if len(s) == 2:
            digits[1] = s
        elif len(s) == 3:
            digits[7] = s
        elif len(s) == 4:
            digits[4] = s
        elif len(s) == 7:
            digits[8] = s

    four_vs_one = digits[4]
    for c in digits[1]:
        four_vs_one = four_vs_one.replace(str(c), '')

    five = [''.join(sorted(s)) for s in sevseg if len(s) == 5]
    for s in five:
        if contains(s, digits[1]):
            digits[3] = s
        elif contains(s, four_vs_one):
            digits[5] = s
        else:
            digits[2] = s

    six = [''.join(sorted(s)) for s in sevseg if len(s) == 6]
    for s in six:
        if contains(s, digits[4]):
            digits[9] = s
        elif contains(s, four_vs_one):
            digits[6] = s
        else:
            digits[0] = s

    return digits


part1 = 0
for l in lines:
    l = l.split(' ')[11:]
    for x in l:
        if len(x) in [2,3,4,7]:
            part1 += 1

part2 = 0
for l in lines:
    a,b = l.split(' | ')
    digits = find_digits(a.split())
    digit_readout = get_code(digits, a.split())
    code = get_code(digits, b.split())
    part2 += code
    #print(digits, digit_readout, code)


print('Part 1', part1)
print('Part 2', part2)
