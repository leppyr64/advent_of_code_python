# Advent of Code 2023 - Day 2
# https://adventofcode.com/2023/day/3

f = open('./2023/input/03.txt')
lines = f.read().splitlines() 
f.close()

def handle_symbol(r, c):
    adj = set()
    for r1 in range(r-1, r+2):
        for c1 in range(c-1, c+2):
            if lines[r1][c1] in ['0','1','2','3','4','5','6','7','8','9']:
                adj.add(get_part_num(r1, c1))
    result = 1
    if lines[r][c] == '*' and len(adj) == 2:
        for x in adj:
            result *= int(lines[x[0]][x[1]: x[2] + 1])
    else:
        result = -1
    return adj, result

def is_symbol(c):
    if c in ['0','1','2','3','4','5','6','7','8','9']:
        return False
    if c == '.':
        return False
    return True

def get_part_num(r, c):
    lt = c
    rt = c
    while lines[r][lt - 1] in ['0','1','2','3','4','5','6','7','8','9']:
        lt -= 1
    while lines[r][rt + 1] in ['0','1','2','3','4','5','6','7','8','9']:
        rt += 1
    
    return (r, lt, rt)
    

# set guardians
for r in range(len(lines)):
    lines[r] = '.' + lines[r] + '.'

s = ''
for c in range(len(lines[0])):
    s += '.'
lines.insert(0, s)
lines.append(s)


part1 = 0
part2 = 0
all_adj = set()
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if is_symbol(lines[r][c]):
            adj, x = handle_symbol(r, c)
            for a in adj:
                all_adj.add(a)
            if x != -1:
                part2 += x

for a in all_adj:
    part1 += int(lines[a[0]][a[1]:a[2]+1])

print('Part 1', part1)
print('Part 2', part2)

