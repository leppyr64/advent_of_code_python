# Advent of Code 2020 - Day 20
# https://adventofcode.com/2020/day/20

import copy
import math
'                  # '
'#    ##    ##    ###'
' #  #  #  #  #  #   '

def is_sea_serpent(row, col):
    global ocean
    #row1
    key = ['                  # ', '#    ##    ##    ###',' #  #  #  #  #  #   ']
    chk = [ocean[row*96+col:row*96+col+20], ocean[(row+1)*96+col:(row+1)*96+col+20], ocean[(row+2)*96+col:(row+2)*96+col+20]]
    for r in range(3):
        for c in range(20):
            if key[r][c] == '#':
                if not (chk[r][c] == '#' or chk[r][c] == 'O'):
                    return False

    for r in range(3):
        for c in range(20):
            if key[r][c] == '#':
                ocean = ocean[:(row + r)*96+col + c] + 'O' + ocean[(row + r)*96+col + c + 1:] 

    
    return True

def find_sea_serpents():
    found = False
    for r in range(93):
        for c in range(76):
            if is_sea_serpent(r, c):
                found = True
    return found


def find_tiling(r, c):
    print(r,c)
    global tiles
    global used
    global grid
    global gridid

    if c > 12:
        c = 1
        r = r + 1

    if r == 13:
        return 1

    for tid in tiles:
        if used[tid] == False:
            used[tid] = True
            t = tiles[tid]
            for flp in range(2):
                t = flip_tile(t)
                for rot in range(4):
                    t = rotate_tile(t)
                    if (r == 1 or get_bot_key(grid[(r - 1, c)]) == get_top_key(t)) and (c == 1 or get_right_key(grid[(r,c-1)]) == get_left_key(t)):
                        grid[(r,c)] = t
                        gridid[(r,c)] = tid
                        result = find_tiling(r, c + 1)
                        if result == 1:
                            return 1
            used[tid] = False
    return -1
                
def flip_tile(t1):
    t2 = ''
    n = int(math.sqrt(len(t1)))
    for r in range(n):
        for c in range(n):
            t2 += t1[r*n + (n-c-1)]
    return t2

def rotate_tile(t1):
    t2 = ''
    n = int(math.sqrt(len(t1)))
    for c in range(n):
        for r in range(n):
            t2 += t1[r*n + (n - c - 1)]
    return t2

def print_tile(t1):
    n = int(math.sqrt(len(t1)))
    for r in range(n):
        for c in range(n):
            print(t1[r*n+c],end='')
        print('')
    print('')

def get_bot_key(t1):
    return flip_tile(rotate_tile(rotate_tile(t1)))[:10]

def get_top_key(t1):
    return t1[:10]

def get_left_key(t1):
    return flip_tile(rotate_tile(rotate_tile(rotate_tile(t1))))[:10]

def get_right_key(t1):
    return rotate_tile(t1)[:10]
            
def init_tiles(inp):
    newtile = True
    tiles = {}
    for l in inp:
        if l == '':
            newtile = True
        elif newtile == True:
            newtile = False
            t = int(l[l.find(' '):-1])
            tiles[t] = ''
        else:
            tiles[t] += l
    return tiles

f = open('./2020/input/2020_20_ocean.txt')
lines = f.read().splitlines()
f.close()

ocean = lines[0]
for f in range(2):
    ocean = flip_tile(ocean)
    for r in range(4):
        ocean = rotate_tile(ocean)
        temp = ocean
        if find_sea_serpents() == False:
            ocean = temp
        else:
            n = int(math.sqrt(len(ocean)))
            result = 0
            for r in range(n):
                for c in range(n):
                    if ocean[r*n+c] == '#':
                        result += 1
            print(result)

if False:

    f = open('./2020/input/2020_20.txt')
    lines = f.read().splitlines()
    f.close()

    tiles = init_tiles(lines)
    used = {}
    grid = {}
    gridid = {}
    for tid in tiles:
        used[tid] = False
    #print(len(tiles))

    find_tiling(1,1)
    #for k in gridid:
    #    print(k, gridid[k])

    print(gridid[(1,1)] * gridid[(1,12)] * gridid[(12,1)] * gridid[(12,12)])


    ocean = ''
    for R in range(1,13):
        for r in range(1,9):
            for C in range(1,13):
                for c in range(1, 9):
                    ocean += grid[(R,C)][r*10+c]

    print(len(ocean))
    print (ocean)
