# Advent of Code 2020 - Day 17
# https://adventofcode.com/2020/day/17

def print_active(active):
    #for k in active:
    #    print(k)
    #print('')
    print(len(active))

def next_cycle(active):
    neighbours = {}
    
    for a in active:
        if a not in neighbours:
            neighbours[a] = 0
        r,c,z = a
        for dr in range(-1,2):
            for dc in range(-1,2):
                for dz in range(-1,2):
                    b = (r + dr, c + dc, z + dz)
                    if not b == a:
                        if b not in neighbours:
                            neighbours[b] = 0
                        neighbours[b] += 1
    #print(neighbours)
    
    new_active = {}
    for b in neighbours:
        if b in active and neighbours[b] in [2,3]:
            new_active[b] = 1
        elif b not in active and neighbours[b] == 3:
            new_active[b] = 1

    return new_active

def init_active(inp):
    active = {}
    for r in range(len(inp)):
        for c in range(len(inp[r])):
            if inp[r][c] == '#':
                active[(r,c,0)] = 1
    return active

def next_cycle_p2(active):
    neighbours = {}
    
    for a in active:
        if a not in neighbours:
            neighbours[a] = 0
        r,c,z,w = a
        for dr in range(-1,2):
            for dc in range(-1,2):
                for dz in range(-1,2):
                    for dw in range(-1,2):
                        b = (r + dr, c + dc, z + dz, w + dw)
                        if not b == a:
                            if b not in neighbours:
                                neighbours[b] = 0
                            neighbours[b] += 1
    #print(neighbours)
    
    new_active = {}
    for b in neighbours:
        if b in active and neighbours[b] in [2,3]:
            new_active[b] = 1
        elif b not in active and neighbours[b] == 3:
            new_active[b] = 1

    return new_active

def init_active_p2(inp):
    active = {}
    for r in range(len(inp)):
        for c in range(len(inp[r])):
            if inp[r][c] == '#':
                active[(r,c,0,0)] = 1
    return active


f = open('./2020/input/17.txt')
lines = f.read().splitlines()
f.close()

active = init_active(lines)
for i in range(6):
    active = next_cycle(active)
print_active(active)

active = init_active_p2(lines)
for i in range(6):
    active = next_cycle_p2(active)
print_active(active)