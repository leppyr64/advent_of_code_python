


f = open("./2016/2016_02.txt")
inp = f.read().splitlines()
f.close()

def area(l, w, h):
    a = l * w
    b = l * h
    c = h * w
    d = min(a, min(b, c))
    return 2 * a + 2 * b + 2 * c + d

def volume(l, w, h):
    return l * w * h

def smallp(l, w, h):
    x = sorted([l, w, h])
    return 2 * (x[0] + x[1])

part1 = 0
part2 = 0
for a in inp:
    l, w, h = [int(x) for x in a.split('x')]
    # print(l, w, h, area(l, w, h))
    part1 += area(l, w, h)
    part2 += volume(l, w, h) + smallp(l, w, h)
print(part1, part2)