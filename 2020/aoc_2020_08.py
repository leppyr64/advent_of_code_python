
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


visited = [False for x in inp]
is_sink = [False for x in inp]

def rec_fill(idx):
    global visited, is_sink, inp
    nxt = 0
    visited[idx] = True
    if inp[idx][0] == 'jmp':
        nxt = idx + inp[idx][1]
    else:
        nxt = idx + 1
    if nxt >= len(inp):
        is_sink[idx] = True
    elif visited[nxt] == True:
        is_sink[idx] = is_sink[nxt]
    else:
        rec_fill(nxt)
        is_sink[idx] = is_sink[nxt]

def label_sinks():
    global visited, is_sink, inp
    for i in range(len(inp)):
        if visited[i] == False:
            rec_fill(i)
        

def find_replacement(idx):
    global visited, is_sink, inp
    while is_sink[idx] == False:
        if inp[idx][0] == 'jmp' and is_sink[idx + 1] == True:
            #print(idx)
            inp[idx][0] = 'nop'
            idx += 1
        elif inp[idx][0] == 'nop' and is_sink[idx + inp[idx][1]]:
            #print(idx)
            inp[idx][0] = 'jmp'
            idx += inp[idx][1]
        elif inp[idx][0] == 'jmp':
            idx += inp[idx][1]
        else:
            idx += 1

def calc_accumulator(idx):
    global visited, is_sink, inp
    if idx >= len(inp):
        return 0
    if inp[idx][0] == 'acc':
        return inp[idx][1] + calc_accumulator(idx + 1)
    elif inp[idx][0] == 'nop':
        return calc_accumulator(idx + 1)
    else:
        return calc_accumulator(idx + inp[idx][1])

label_sinks()
find_replacement(0)
visited = [False for x in inp]
print('part2 O(n)', calc_accumulator(0))
