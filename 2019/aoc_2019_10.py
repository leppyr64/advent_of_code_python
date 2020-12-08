import math

f = open("./2019/2019_10.txt")
inp = f.read().splitlines()
f.close()

visible = [[0 for i in range(33)] for i in range(33)]

ast = []

nr = len(inp)
nc = len(inp[0])

for r in range(nr):
    for c in range(nc):
        if inp[r][c] == "#":
            ast.append([r,c])

for a in ast:
    print (a[0], a[1])

def hash(r, c):
    if r < 0 and c >= 0:
        return 1*10000 + abs(r)*100 + abs(c)
    elif c > 0 and r >= 0:
        return 2*10000 + abs(r)*100 + abs(c)
    elif c <= 0 and r > 0:
        return 3*10000 + abs(r)*100 + abs(c)
    else:
        return 4*10000 + abs(r)*100 + abs(c)

best = -1
bestloc = [0,0]
for a1 in ast:
    r1, c1 = a1
    slopes = dict()
    for a2 in ast:
        if a2 != a1:

            r2, c2 = a2
            dr = r2 - r1
            dc = c2 - c1

            g = int(math.gcd(abs(dr), abs(dc)))
            dr //= g
            dc //= g
            #if a1 == [3,4]:
            #    print (a2, dr, dc)
            if hash(dr,dc) not in slopes.keys():
                slopes[hash(dr, dc)] = []    
            slopes[hash(dr, dc)].append([r2,c2])
    if len(slopes.keys()) > best:
        best = max(best, len(slopes.keys()))
        bestloc = [r1, c1]
    #print(r1, c1, len(slopes.keys()))
print (best, bestloc)


slopes = dict()
r1, c1 = bestloc
for a in ast:
    if a != [r1, c1]:
        r2, c2 = a
        dr = r2 - r1
        dc = c2 - c1
        g = int(math.gcd(abs(dr), abs(dc)))
        dr //= g
        dc //= g
        print (r2, c2, dr, dc, g) 
        if hash(dr, dc) not in slopes.keys():
            slopes[hash(dr, dc)] = []
        slopes[hash(dr, dc)].append([r2, c2])


for k in sorted(slopes.keys()):
    print (k, slopes[k])

    

