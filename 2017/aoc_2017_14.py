from collections import deque

def DenseHash(sparsehash):
    op = ''
    for i in range(16):
        x = 0
        for j in range(16):
            x ^= sparsehash[i*16+j]
        s = hex(x)
        s = '0' + s[2:]
        op += s[-2:]
    return op

def KnotHash(inp):
    memlen = 256
    lengths = [ord(x) for x in inp] + [17,31,73,47,23]
    mem = [x for x in range(memlen)]
    skip = 0
    pos = 0
    for i in range(64):
        mem, pos, skip = KnotHashRound(mem, pos, skip, memlen, lengths)
    return DenseHash(mem)

def KnotHashRound(mem, pos, skip, memlen, lengths):
    for l in lengths:
        mem = mem + mem
        seg = mem[pos:pos + l]
        seg.reverse()
        mem =  mem[:pos] + seg + mem[pos + l:]
        mem = mem[pos:pos + memlen]
        mem = mem[-pos:] + mem[:-pos]
        pos = (pos + skip + l) % memlen
        skip = (skip + 1) % memlen
        #print (pos, skip, mem)
    return mem, pos, skip

def hextobin(h):
    op = ''
    for c in h:
        x = 0
        if c >= 'a':
            x = ord(c) - ord('a') + 10
        else:
            x = int(c)
        s = bin(x)
        s = '0000' + s[2:]
        op += s[-4:]
    return op

def usedsquares(G):
    result = 0
    for r in G:
        result += sum(r)
    return result

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
def countregions(G):
    regions = 1
    q = deque()
    for i in range(128):
        for j in range(128):
            if G[i][j] == 1:
                regions += 1
                G[i][j] = regions
                q.append((i,j))
                while q:
                    (r,c) = q.popleft()
                    for x in range(4):
                        nr = r + dr[x]
                        nc = c + dc[x]
                        if nr < 128 and nc < 128 and nr >= 0 and nc >= 0 and  G[nr][nc] == 1:
                            q.append((nr,nc))
                            G[nr][nc] = regions

    for r in G[:8]:
        print(r[:8])
    return regions - 1

f = open("./2017/Input/2017_14.txt")
inp = f.read().splitlines()
for k in inp:
    krs = [KnotHash(k + '-' + str(r)) for r in range(128)]
    G = [[0 for j in range(128) ] for i in range(128)]
    for r in range(128):
        h = hextobin(krs[r])
        for c in range(128):
            G[r][c] = int(h[c])

    print(usedsquares(G))
    print(countregions(G))

