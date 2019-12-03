


f = open("./2019/02/2019_02.txt")
inp = f.readline()
f.close()
mem = inp.split(",")
mem = [int(x) for x in mem]

def simulate(repl_a, repl_b):
    m = mem.copy()
    i = 0
    m[1] = repl_a
    m[2] = repl_b
    while(m[i] != 99):
        if m[i] == 1:
            m[m[i+3]] = m[m[i+1]] + m[m[i+2]]
        elif m[i] == 2:
            m[m[i+3]] = m[m[i+1]] * m[m[i+2]]
        i += 4
    return m[0]

print(simulate(12,2))

for a in range(100):
    for b in range(100):
        if(simulate(a,b) == 19690720):
            print(a * 100 + b)


