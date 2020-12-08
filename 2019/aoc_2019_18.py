from collections import deque

f = open("./2019/2019_18.txt")
inp = f.read().splitlines()
f.close()

G = [[c for c in r] for r in inp]

R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        #print(G[r][c],end='')
        if G[r][c] == '@':
            G[r][c] = '.'
            sr, sc = r,c
    # print('')
print (R, C)



dr =[0, 1, 0, -1]
dc = [-1, 0, 1, 0]

for i in range(4):
    r,c  = sr + dr[i], sc + dc[i]
    G[r][c] = '#'


q = deque()
q.append((sr-1,sc-1,sr-1,sc+1,sr+1,sc-1,sr+1,sc+1,0))
D = {}
D[(sr-1,sc-1,sr-1,sc+1,sr+1,sc-1,sr+1,sc+1,0)]  = 0


maxk = 0
mind = 0
while len(q) != 0:
    r1, c1, r2, c2, r3, c3, r4, c4,  k = q.popleft()
    if k > maxk:
        mind = D[(r1, c1, r2, c2, r3, c3, r4, c4, k)]
        maxk = k
    # print(r, c, k)
    for i in range(4):
        # Robot 1
        rr,cc, kk = r1 + dr[i], c1 + dc[i], k
        ok = True
        
        if G[rr][cc] >= 'a' and G[rr][cc] <= 'z':
            kk = k | (1 << (ord(G[rr][cc]) - ord('a')))
        
        if G[rr][cc] >= 'A' and G[rr][cc] <= 'Z':
            if k & (1 << (ord(G[rr][cc]) - ord('A'))) == 0:
                ok = False
        
        if G[rr][cc] == '#':
            ok = False

        if ok and (rr, cc, r2, c2, r3, c3, r4, c4, kk) not in D.keys():
            D[(rr, cc, r2, c2, r3, c3, r4, c4, kk)] = D[(r1, c1, r2, c2, r3, c3, r4, c4, k)] + 1
            q.append((rr, cc, r2, c2, r3, c3, r4, c4, kk))

        # Robot 2
        rr,cc, kk = r2 + dr[i], c2 + dc[i], k
        ok = True
        
        if G[rr][cc] >= 'a' and G[rr][cc] <= 'z':
            kk = k | (1 << (ord(G[rr][cc]) - ord('a')))
        
        if G[rr][cc] >= 'A' and G[rr][cc] <= 'Z':
            if k & (1 << (ord(G[rr][cc]) - ord('A'))) == 0:
                ok = False
        
        if G[rr][cc] == '#':
            ok = False

        if ok and (r1, c1, rr, cc, r3, c3, r4, c4, kk) not in D.keys():
            D[(r1, c1, rr, cc, r3, c3, r4, c4, kk)] = D[(r1, c1, r2, c2, r3, c3, r4, c4, k)] + 1
            q.append((r1, c1, rr, cc, r3, c3, r4, c4, kk))


        # Robot 3
        rr,cc, kk = r3 + dr[i], c3 + dc[i], k
        ok = True
        
        if G[rr][cc] >= 'a' and G[rr][cc] <= 'z':
            kk = k | (1 << (ord(G[rr][cc]) - ord('a')))
        
        if G[rr][cc] >= 'A' and G[rr][cc] <= 'Z':
            if k & (1 << (ord(G[rr][cc]) - ord('A'))) == 0:
                ok = False
        
        if G[rr][cc] == '#':
            ok = False

        if ok and (r1, c1, r2, c2, rr, cc, r4, c4, kk) not in D.keys():
            D[(r1, c1, r2, c2, rr, cc, r4, c4, kk)] = D[(r1, c1, r2, c2, r3, c3, r4, c4, k)] + 1
            q.append((r1, c1, r2, c2, rr, cc, r4, c4, kk))

        # Robot 4
        rr,cc, kk = r4 + dr[i], c4 + dc[i], k
        ok = True
        
        if G[rr][cc] >= 'a' and G[rr][cc] <= 'z':
            kk = k | (1 << (ord(G[rr][cc]) - ord('a')))
        
        if G[rr][cc] >= 'A' and G[rr][cc] <= 'Z':
            if k & (1 << (ord(G[rr][cc]) - ord('A'))) == 0:
                ok = False
        
        if G[rr][cc] == '#':
            ok = False

        if ok and (r1, c1, r2, c2, r3, c3, rr, cc, kk) not in D.keys():
            D[(r1, c1, r2, c2, r3, c3, rr, cc, kk)] = D[(r1, c1, r2, c2, r3, c3, r4, c4, k)] + 1
            q.append((r1, c1, r2, c2, r3, c3, rr, cc, kk))
print(mind)           





    

