# Advent of Code 2020 - Day 2
# https://adventofcode.com/2020/day/2

f = open('./2020/input/02.txt')
lines = f.read().splitlines() 
f.close()

def is_valid_p1(pw_policy):
    counts, letter, pw = pw_policy.split(' ')
    letter = letter[:-1]
    actual = pw.count(letter)
    lwr, upr = (int(x) for x in counts.split('-'))
    return actual >= lwr and actual <= upr

def is_valid_p2(pw_policy):
    counts, letter, pw = pw_policy.split(' ')
    letter = letter[:-1]
    a, b = (int(x) - 1 for x in counts.split('-'))
    assert b < len(pw)

    return (pw[a] == letter) != (pw[b] == letter) 

def count_valid_p1(pws):
    count = 0
    for pw in pws:
        if is_valid_p1(pw):
            count += 1
    return count

def count_valid_p2(pws):
    count = 0
    for pw in pws:
        if is_valid_p2(pw):
            count += 1
    return count

print('Part1', count_valid_p1(lines))
print('Part2', count_valid_p2(lines))