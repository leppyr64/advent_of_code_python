# Advent of Code 2021 - Day 21
# https://adventofcode.com/2021/day/21

#filename = './2021/input/21.txt'
filename = './2021/input/21_sample.txt'
f = open(filename)
lines = f.read().splitlines()
f.close()

wins = dict()
losses = dict()

def rolldice(dice):
    roll = 3*dice + 3
    if dice == 98:
        roll = 3*dice + 3
        dice = 1
    elif dice == 99:
        roll = 99 + 100 + 1
        dice = 2
    elif dice == 100:
        roll = 100 + 1 + 2
        dice = 3
    else:
        roll = 3*dice + 3
        dice = dice + 3
    return dice, roll

def part1(posa, posb):
    posa -= 1
    posb -= 1
    scorea = 0
    scoreb = 0
    dice = 1
    totalrolls = 0
    while scorea < 1000 and scoreb < 1000:
        dice, roll = rolldice(dice)
        posa = (posa + roll) % 10
        scorea += posa + 1
        totalrolls += 3
        if scorea < 1000:
            dice, roll = rolldice(dice)
            posb = (posb + roll) % 10
            scoreb += posb + 1
            totalrolls += 3
    result = min(scorea, scoreb) * totalrolls
    return result

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


print('Part 1', part1(4, 5)) 

totwins = calculate_wins(0, 0, 4, 8)
totlosses = losses[(0, 0, 4, 8)]
print('Part 2 Sample', totwins, totlosses)

totwins = calculate_wins(0, 0, 4, 5)
totlosses = losses[(0, 0, 4, 5)]
print('Part 2', totwins, totlosses)

