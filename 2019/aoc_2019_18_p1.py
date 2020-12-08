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
            start = r,c
    # print('')
print (R, C)

def hashit(pos, keys):
    return (keys * 100 + r) * 100 + c

q = deque()
q.append((start[0], start[1], 0))
D = {}
D[(start[0], start[1], 0)]  = 0

dr =[0, 1, 0, -1]
dc = [-1, 0, 1, 0]

maxk = 0
mind = 0
while len(q) != 0:
    r, c, k = q.popleft()
    if k > maxk:
        mind = D[(r, c, k)]
        maxk = k
    # print(r, c, k)
    for i in range(4):
        rr,cc, kk = r + dr[i], c + dc[i], k
        ok = True
        
        if G[rr][cc] >= 'a' and G[rr][cc] <= 'z':
            kk = k | (1 << (ord(G[rr][cc]) - ord('a')))
        
        if G[rr][cc] >= 'A' and G[rr][cc] <= 'Z':
            if k & (1 << (ord(G[rr][cc]) - ord('A'))) == 0:
                ok = False
        
        if G[rr][cc] == '#':
            ok = False

        if ok and (rr, cc, kk) not in D.keys():
            D[(rr, cc, kk)] = D[(r, c, k)] + 1
            q.append((rr, cc, kk))

print(mind)           





    

