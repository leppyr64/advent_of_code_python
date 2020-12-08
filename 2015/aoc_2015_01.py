


f = open("./2016/2016_01.txt")
inp = f.read().splitlines()[0]
f.close()

floor = 0
x = 0
part2 = -1
for c in inp:
    x += 1
    if c == ')':
        floor -= 1
    else:
        floor += 1
    if floor == -1 and part2 == -1:
        part2 = x
print(floor, part2)
