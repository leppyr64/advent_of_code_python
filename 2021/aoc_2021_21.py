# Advent of Code 2021 - Day 21
# https://adventofcode.com/2021/day/21

#filename = './2021/input/21.txt'
filename = './2021/input/21_sample.txt'
f = open(filename)
lines = f.read().splitlines()
f.close()

wins = dict()
losses = dict()

def calculate_wins(scorea, scoreb, posa, posb):
    
    if (scorea, scoreb, posa, posb) in wins:
        return wins[(scorea, scoreb, posa, posb)]
    
    if scorea >= 21:
        wins[(scorea, scoreb, posa, posb)] = 1
        losses[(scorea, scoreb, posa, posb)] = 0
        return 1
    
    if scoreb >= 21:
        wins[(scorea, scoreb, posa, posb)] = 0
        losses[(scorea, scoreb, posa, posb)] = 1
        return 0
    
    result = 0
    nlosses = 0
    for a in [1,2,3]:
        for b in [1,2,3]:
            for c in [1,2,3]:
                nposa = posa + a + b + c
                if nposa > 10:
                    nposa -= 10
                nscorea = scorea + nposa
                if nscorea >= 21:
                    result += 1
                else:
                    nlosses += calculate_wins(scoreb, nscorea, posb, nposa)
                    for d in [1,2,3]:
                        for e in [1,2,3]:
                            for f in [1,2,3]:
                                nposb = posb + d + e + f
                                if nposb > 10:
                                    nposb -= 10
                                nscoreb = scoreb + nposb
                                result += calculate_wins(nscorea, nscoreb, nposa, nposb)
    wins[(scorea, scoreb, posa, posb)] = result
    losses[(scorea, scoreb, posa, posb)] = nlosses
    return result

totwins = calculate_wins(0, 0, 4, 8)
totlosses = losses[(0, 0, 4, 8)]
print('Part 1', totwins, totlosses)

totwins = calculate_wins(0, 0, 4, 5)
totlosses = losses[(0, 0, 4, 5)]
print('Part 2', totwins, totlosses)
