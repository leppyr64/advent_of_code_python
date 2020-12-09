
#f = open("./2020/input/2020_08_small.txt")
f = open("./2020/input/2020_08.txt")
inp = f.read().splitlines()
f.close()

def has_loop(inst):
    accumulator = 0
    idx = 0
    used = {}
    while idx not in used and idx < len(inst):
        used[idx] = 1
        if inst[idx][0] == 'nop':
            idx += 1
        elif inst[idx][0] == 'jmp':
            idx += inst[idx][1]
        elif inst[idx][0] == 'acc':
            accumulator += inst[idx][1]
            idx += 1
        else:
            assert False
    return idx < len(inst), accumulator


inp = [x.split(' ') for x in inp]
inp = [[x[0], int(x[1])] for x in inp]
print('part1', has_loop(inp)[1])

for i in range(len(inp)):
    if inp[i][0] == 'jmp':
        inp[i][0] = 'nop'
    elif inp[i][0] == 'nop':
        inp[i][0] = 'jmp'

    result = has_loop(inp)
    if result[0] == False:
        print('part2', result[1])
            
    if inp[i][0] == 'jmp':
        inp[i][0] = 'nop'
    elif inp[i][0] == 'nop':
        inp[i][0] = 'jmp'


