# Advent of Code 2020 - Day 4
# https://adventofcode.com/2020/day/10


def count_arrangements(chain):
    memo = [0 for x in range(max(chain) + 1)]
    memo[0] = 1
    for x in chain:
        for i in range(max(0, x - 3), x):
            memo[x] += memo[i]
    return memo[max(chain)]

def count_steps(chain, diff):
    result = 0
    for i in range(1, len(chain)):
        if chain[i] - chain[i-1] == diff:
            result += 1
    return result

def build_chain(adaptors):
    chain = adaptors.copy()
    chain.append(0)
    chain.sort()
    chain.append(max(chain) + 3)
    return chain


f = open('./2020/input/10_small.txt')
lines = f.read().splitlines()
f.close()
a = [int(x) for x in lines]
x = count_steps(build_chain(a), 3)
y = count_steps(build_chain(a), 1)
z = count_arrangements(build_chain(a))

print('Part1', x, y, x*y)
print('Part2', z)

f = open('./2020/input/10.txt')
lines = f.read().splitlines()
f.close()
a = [int(x) for x in lines]
x = count_steps(build_chain(a), 3)
y = count_steps(build_chain(a), 1)
z = count_arrangements(build_chain(a))

print('Part1', x, y, x*y)
print('Part2', z)