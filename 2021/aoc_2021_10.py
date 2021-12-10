# Advent of Code 2021 - Day 10
# https://adventofcode.com/2021/day/10

f = open('./2021/input/10.txt')
#f = open('./2021/input/10_sample.txt')
lines = f.read().splitlines() 
f.close()

def is_invalid(s):
    symbols = {')':'(', '}':'{', ']':'[', '>':'<'}
    symbolscore = {')': 3, '}':1197, ']':57, '>':25137}
    store = ''
    for c in s:
        if c in symbols.keys():
            if store[-1] != symbols[c]:
                return (symbolscore[c], '')
            else:
                store = store[:-1]
        else:
            store += c
    return (0, store)

def score_incomplete(s):
    symbolvalue = {'(':1, '[':2, '{':3,'<': 4}
    s = s[::-1]
    score = 0 
    for c in s:
        score = score * 5 + symbolvalue[c]
    return score

part1 = 0
part2 = 0
scores = []
for l in lines:
    value, store = is_invalid(l)
    part1 += value
    if store != '':
        scores.append(score_incomplete(store))

scores.sort()
part2 = scores[len(scores)//2]

print('Part 1', part1)
print('Part 2', part2)


