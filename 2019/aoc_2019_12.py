import math

f = open("./2019/2019_12.txt")
inp = f.read().splitlines()
f.close()

inp = [a[1:-1] for a in inp]
inp = [a.split(",") for a in inp]

P = [[ int(a.strip()[2:]) for a in b ] for b in inp]

def hash(p, v):
    hash = 0
    for i in range(4):
        assert abs(p[i] < 10000)
        assert abs(v[i] < 10000)
        
        hash *= 10
        if p[i] < 0:
            hash += 1
        hash *= 100000
        hash += abs(p[i])
        hash *= 10
        if v[i] < 0:
            hash += 1
        hash *= 100000
        hash += abs(v[i])
    return hash

def find_cycle(d):
    mem = dict()

    v = [0, 0, 0, 0]
    p = [a[d] for a in P]
    
    maxn = 1000000
    for n in range(maxn):
        h = hash(p, v)
        if h in mem.keys():
            print (p, v)
            return n
        mem[h] = n
        #print(n, p, v)
        for i in range(4):
            for j in range(4):
                if(p[i] < p[j]):
                    v[i] += 1
                elif(p[i] > p[j]):
                    v[i] -= 1
        for i in range(4):
            p[i] += v[i]
     
    return -1       
    #print(maxn, p, v)

a = find_cycle(0)
b = find_cycle(1)
c = find_cycle(2)

g = int(math.gcd(a, b))
x = a * b // g
g = int(math.gcd(x, c))
x = x * c // g

print (a, b, c, x)

pos = [[a for a in b] for b in P]
vel = [[0 for a in b] for b in P]
for n in range(1000):
    steps = n + 1
    for i in range(4):
        for j in range(4):
            for d in range(3):
                if pos[i][d] > pos[j][d]:
                    vel[i][d] -= 1
                elif pos[i][d] < pos[j][d]:
                    vel[i][d] += 1
    for i in range(4):
        for d in range(3):
            pos[i][d] += vel[i][d]
    #print_system()

total = 0
for i in range(4):
    pot = 0
    kin = 0
    for d in range(3):
        pot += abs(pos[i][d])
        kin += abs(vel[i][d])
    total += pot * kin
print(total)