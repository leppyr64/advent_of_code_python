# Advent of Code 2023 - Day 7
# https://adventofcode.com/2023/day/7

f = open('./2023/input/07.txt')
lines = f.read().splitlines() 
f.close()

CARDRANK = {'A':14,'K':13,'Q':12,'J':11,'T': 10, '9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
def card_rank(c, j_wild):
    if j_wild and c == 'J':
        return 0
    return CARDRANK[c]


class Hand(object):
    def __init__(self, cards, wager, j_wild):
        self.cards = cards
        self.wager = wager
        self.j_wild = j_wild

    def __lt__(self, other):
        a = self.hand_type()
        b = other.hand_type()
        if a != b:
            return a < b
        for i in range(len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return card_rank(self.cards[i], self.j_wild) < card_rank(other.cards[i], other.j_wild)
        return False

    def hand_type(self):
        cards_in_hand = [0 for x in range(15)]
        for c in self.cards:
            cards_in_hand[CARDRANK[c]] += 1
        js = cards_in_hand[11]
        if self.j_wild:
            cards_in_hand[11] = 0
        cards_in_hand.sort(reverse=True)    
        if self.j_wild:
            cards_in_hand[0] += js
        if cards_in_hand[0] == 5:
            return 7
        if cards_in_hand[0] == 4:
            return 6
        if cards_in_hand[0] == 3:
            if cards_in_hand[1] == 2:
                return 5
            return 4
        if cards_in_hand[0] == 2:
            if cards_in_hand[1] == 2:
                return 3
            return 2
        return 1
        
        
part1 = 0
deck = [Hand(x.split(' ')[0], int(x.split(' ')[1]), False) for x in lines]
deck.sort()
for i in range(len(deck)):
    h = deck[i]
    part1 += (i+1) * h.wager
    #print(h.cards, h.hand_type(), h.wager)
print('Part 1', part1)

part2 = 0
deck = [Hand(x.split(' ')[0], int(x.split(' ')[1]), True) for x in lines]
deck.sort()
for i in range(len(deck)):
    h = deck[i]
    part2 += (i+1) * h.wager
    #print(h.cards, h.hand_type(), h.wager)
print('Part 2', part2)