from operator import itemgetter, attrgetter
from collections import deque

f = open("./2019/2018_15.txt")
inp = f.read().splitlines()
f.close()

M = [[c for c in a] for a in inp]
P = []

class Player(object):

    def __init__(self, row, col, team):
        self.hp = 200
        self.r = row
        self.c = col
        self.t = team
        self.target = None

    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]

    def __str__(self):
        return str(self.t) + ' (' + str(self.r) + ', ' + str(self.c) + ') ' + str(self.hp)

    def other_team(self):
        if self.t == 'G':
            return 'E'
        return 'G'

    def can_attack(self):
        self.target = None
        for i in range(4):
            for x in P:
                if self.c + self.dc[i] == x.c and self.r + self.dr[i] == x.r and self.t != x.t:
                    if self.target == None:
                        self.target = x
                    elif self.target.hp > x.hp:
                        self.target = x
        if self.target == None:
            return False
        return True

    def can_move(self):
        D = [[100000 for a in b] for b in M]
        PREV = [[[10000, 10000] for a in b] for b in M]
        q = deque()
        q.append([0, self.r, self.c])
        D[self.r][self.c] = 0
        while len(q) != 0:
            x = q.pop()
            r = x[1]
            c = x[2]
            d = x[0]
            for i in range(4):
                newr = r + self.dr[i]
                newc = c + self.dc[i]
                if M[newr][newc] == '.' and D[newr][newc] > d + 1:
                    D[newr][newc] = d + 1
                    PREV[newr][newc] = [r,c]
                    q.append([d + 1, newr, newc])
                elif M[newr][newc] == '.' and D[newr][newc] == d + 1 and (r < PREV[newr][newc][0] or (r == PREV[newr][newc] and c < PREV[newr][newc][1])):
                    PREV[newr][newc] = [r,c]
        bestd = 100000
        bestr = 0
        bestc = 0
        for p in P:
            if p.t != self.t:
                for i in range(4):
                    newr = p.r + self.dr[i]
                    newc = p.c + self.dc[i]
                    if D[newr][newc] < bestd or (D[newr][newc] == bestd and (newr < bestr or (newr == bestr and newc < bestc))):
                        bestd = D[newr][newc]
                        bestr = newr
                        bestc = newc

        if bestd == 100000:
            return False   
        print(self.r, self.c, bestr, bestc)     
        while PREV[bestr][bestc] != [self.r, self.c]:
            nextr = PREV[bestr][bestc][0]
            nextc = PREV[bestr][bestc][1]
            bestr = nextr
            bestc = nextc
            print (bestr, bestc)
        M[self.r][self.c] = '.'
        self.r = bestr
        self.c = bestc
        M[self.r][self.c] = self.t
        return True
        
        

    def take_turn(self):
        if self.can_attack() == True:
            self.target.hp -= 3
            if self.target.hp < 0:
                M[self.target.r][self.target.c] = '.'
        else:
            if self.can_move() == True:
                pass
            if self.can_attack() == True:
                self.target.hp -= 3
                if self.target.hp < 0:
                    G[self.target.r][self.target.c] = '.'
        
        
            
            

def print_system():
    for r in range(len(M)):
        s = ''
        for c in range(len(M[0])):
            s += M[r][c]
        print (s)
    for x in P:
        print (x)
    print(' ')


for r in range(len(M)):
    for c in range(len(M[r])):
        if M[r][c] == 'G':
            P.append(Player(r, c, 'G'))
        elif M[r][c] == 'E':
            P.append(Player(r, c, 'E'))

G = [x for x in P if x.t == 'G']
E = [x for x in P if x.t == 'E']
rounds = 0
P = sorted(P, key=attrgetter('r', 'c'))
print_system()
while len(G) > 0 and len(E) > 0:
    rounds += 1
    for x in P:
        if x.hp > 0:
            x.take_turn()
    P = [x for x in P if x.hp > 0]
    P = sorted(P, key=attrgetter('r', 'c'))
    G = [x for x in P if x.t == 'G']
    E = [x for x in P if x.t == 'E']
    print_system()

sum = 0
for p in P:
    sum += p.hp
print (rounds, sum, rounds * sum)