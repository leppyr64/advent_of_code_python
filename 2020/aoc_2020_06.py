
f = open("./2020/input/2020_06.txt")
inp = f.read().splitlines()
f.close()

inp.append('')

def getscore(group):
    seen = {}
    for a in group:
        for c in a:
            if c not in seen:
                seen[c] = 0
            seen[c] += 1
    part2 = 0
    for k in seen:
        if seen[k] == len(group):
            part2 += 1
    
    return len(seen), part2



group = []
part1 = 0
part2 = 0
for s in inp:
    if s == '':
        print(group)
        a,b = getscore(group)
        part1 += a
        part2 += b
        group = []
    else:
        group.append(s)

print('part1', part1)
print('part2', part2)