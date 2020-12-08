f = open("./2019/2018_18.txt")
inp = f.read().splitlines()
f.close()

R = len(inp)
C = len(inp[0])

s = ''
for i in range(C):
    s += '.'
inp.append(s)
inp.insert(0, s)
inp = ['.' + a + '.' for a in inp]

G = [[c for c in b] for b in inp]

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def transition(G):
    X = [[c for c in r] for r in G]
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if G[r][c] == '.':
                count = 0
                for i in range(8):
                    if G[r + dr[i]][c + dc[i]] == '|':
                        count += 1
                if count >= 3:
                    X[r][c] = '|'
            elif G[r][c] == '|':
                count = 0
                for i in range(8):
                    if G[r + dr[i]][c + dc[i]] == '#':
                        count += 1
                if count >= 3:
                    X[r][c] = '#'
            elif G[r][c] == '#':
                counta = 0
                countb = 0
                s = ''
                for i in range(8):
                    s += G[r + dr[i]][c + dc[i]]
                    if G[r + dr[i]][c + dc[i]] == '#':
                        counta += 1
                    elif G[r + dr[i]][c + dc[i]] == '|':
                        countb += 1
                #print(r, c, counta, countb, s)
                if counta == 0 or countb == 0:
                    X[r][c] = '.'
    return X


# An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
# An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.
# An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.

def printx(G):
    for r in range(1, R + 1):
        s = ''
        for c in range(1, C + 1):
            s += G[r][c]
        print (s)
    print('')

#printx(G)
for i in range(1000):
    G = transition(G)
    #printx(G)

    counta = 0
    countb = 0
    for r in G:
        for c in r:
            if c == '|':
                counta += 1
            elif c == '#':
                countb += 1
    print(i, counta, countb, counta * countb)
printx(G)

