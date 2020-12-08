


f = open("./2015/2015_03.txt")
inp = f.read().splitlines()[0]
f.close()

dr = {'^':-1,'v':1, '<':0, '>':0}
dc = {'^':0,'v':0, '<':-1, '>':1}

vis = {}
vis2 = {}
r = 0
c = 0
r1 = 0
c1 = 0
r2 = 0
c2 = 0
vis[(r, c)] = 1
for i in range(len(inp)):
    x = inp[i]
    r += dr[x]
    c += dc[x]
    vis[(r, c)] = 1

    if i % 2 == 0:
        r1 += dr[x]
        c1 += dc[x]
        vis2[(r1, c1)] = 1
    else:
        r2 += dr[x]
        c2 += dc[x]
        vis2[(r2, c2)] = 1
print(len(vis.keys()), len(vis2.keys()))
    
