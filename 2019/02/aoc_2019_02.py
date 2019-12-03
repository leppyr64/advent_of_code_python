# Advent of Code 2019 - Day 2
# https://adventofcode.com/2019/day/2
# --- Day 2: 1202 Program Alarm ---

# Simulation is O(number of commands) - O(n)
# There is an O(1) solution from analyzing input
# Part b is O(a * b * O(simulate)) - O(n^2)

# Read the input
f = open("./2019/02/2019_02.txt")
inp = f.readline()
f.close()
mem = inp.split(",")
mem = [int(x) for x in mem]

# Simulate the OpCodes using the suggested replacements
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

# Output for Part A
print(simulate(12,2))

# Loop through all possible options for memory[1] and memory[2]
# Compare output to required output and print result
for a in range(100):
    for b in range(100):
        if(simulate(a,b) == 19690720):
            print(a * 100 + b)


