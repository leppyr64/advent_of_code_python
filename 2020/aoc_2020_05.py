
f = open("./2020/input/2020_05.txt")
inp = f.read().splitlines()
f.close()

def seat(bp):
    rlo, rhi = 0, 127
    clo, chi = 0, 7
    for c in bp:
        if c == 'L':
            chi = (clo + chi) // 2
        elif c == 'R':
            clo = (clo + chi + 1) // 2
        elif c == 'F':
            rhi = (rlo + rhi) // 2
        elif c == 'B':
            rlo = (rlo + rhi + 1) // 2
    return (rlo, clo, rlo * 8 + clo)

allids = [seat(b)[2] for b in inp]

part1 = max(allids)
print('part1', part1)

allids.sort()
for i in range(1, len(allids)):
    if allids[i] - allids[i-1] > 1:
        print('part2', allids[i] - 1)