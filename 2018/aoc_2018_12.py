
#input
state = ""
transitions = dict()
added = 0

f = open("./2019/2018_12.txt")
inp = f.readline().strip().split()
state = inp[2]

inp = f.readline()
inp = f.read().splitlines()
f.close()

for a in inp:
    print(a, len(a))
    transitions[a[:5]] = a[9]

print(len(transitions))

added = 0



def calcsum(s, added):
    sum = 0
    for i in range(len(s)):
        if s[i] == "#":
            sum += i - added
    return sum

print(0, calcsum(state, added))
for gen in range(1, 500):
    if state[:3] != "...":
        state = "..." + state
        added += 3
    if state[-3:] != "...":
        state = state + "..."
    newstate = ".."
    for i in range(2, len(state) - 2):
        s = state[i-2:i+3]
        if s in transitions.keys():
            newstate += transitions[s]
        else:
            newstate += "."
    newstate += ".."
    state = newstate
    print(gen, calcsum(state, added))

print((50000000000 - 127)*36+4030)