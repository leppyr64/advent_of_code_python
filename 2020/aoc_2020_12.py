# Advent of Code 2020 - Day 12
# https://adventofcode.com/2020/day/12


def process_path1(inst):
    inst = [[z[:1],int(z[1:])] for z in inst]
    x = 0
    y = 0
    didx = int(0)
    delta = [(1,0),(0,-1),(-1,0), (0,1)]
    for a, n in inst:
        if a == 'N':
            y += n
        elif a == 'S':
            y -= n
        elif a == 'E':
            x += n
        elif a == 'W':
            x -= n
        elif a == 'F':
            dx,dy = delta[didx]
            x += dx * n
            y += dy * n
        else:
            n //= 90
            if a == 'L':
                didx = (didx + 16 - n) % 4
            else:
                didx = (didx + n) % 4
    return (x, y, abs(x) + abs(y))

def get_delta(x1, y1, x2, y2):
    return (x2 - x1, y2 - y1)
        
def process_path2(inst):
    inst = [[z[:1],int(z[1:])] for z in inst]
    sx = 0
    sy = 0
    wpx = 10
    wpy = 1
    for a, n in inst:
        if a == 'N':
            wpy += n
        elif a == 'S':
            wpy -= n
        elif a == 'E':
            wpx += n
        elif a == 'W':
            wpx -= n
        elif a == 'F':
            for i in range(0, n):
                sx += wpx
                sy += wpy
        else:
            while n > 0:
                tx, ty = wpx, wpy
                if a == 'L':
                    wpy = tx
                    wpx = -ty
                else:
                    wpx = ty
                    wpy = -tx
                n -= 90
    return (sx, sy, abs(sx) + abs(sy))


f = open('./2020/input/2020_12_small.txt')
lines = f.read().splitlines()
f.close()
print(process_path1(lines))
print(process_path2(lines))

f = open('./2020/input/2020_12.txt')
lines = f.read().splitlines()
f.close()
print(process_path1(lines))
print(process_path2(lines))
