
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

# Main Starts Here
f = open("./2020/input/2020_08.txt")
inp = f.read().splitlines()
f.close()

inp = [x.split(' ') for x in inp]
inp = [[x[0], int(x[1])] for x in inp]


visited = [False for x in inp]
is_sink = [False for x in inp]

print('part1', has_loop(inp))
label_sinks()
find_replacement(0)
print('part2 O(n)', has_loop(inp))
