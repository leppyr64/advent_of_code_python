# Advent of Code 2020 - Day 15
# https://adventofcode.com/2020/day/15

def process_case(inp, depth):
    mem = {}
    digits = [int(x) for x in inp.split(',')]
    
    idx = 1
    for d in digits[:-1]:
        mem[d] = idx
        idx += 1
    last = digits[-1]
    while idx < depth:
        if last not in mem:
            nxt = 0
        else:
            nxt = idx - mem[last]
        mem[last] = idx
        idx += 1
        last = nxt
    return last

print('part 1', process_case('12,20,0,6,1,17,7', 2020))
print('part 2', process_case('12,20,0,6,1,17,7', 30000000))
#print(process_case('0,3,6', 10)) #0
#print(process_case('0,3,6', 2020)) #436
#print(process_case('1,3,2', 2020)) #1
#print(process_case('2,1,3', 2020)) #10
#print(process_case('1,2,3', 2020)) #27
#print(process_case('2,3,1', 2020)) #78
#print(process_case('3,2,1', 2020)) #438
#print(process_case('3,1,2', 2020)) #1836
#print(process_case('0,3,6', 30000000)) #175594
#print(process_case('1,3,2', 30000000)) #2578
#print(process_case('2,1,3', 30000000)) #3544142
#print(process_case('1,2,3', 30000000)) #261214
#print(process_case('2,3,1', 30000000)) #6895259
#print(process_case('3,2,1', 30000000)) #18
#print(process_case('3,1,2', 30000000)) #362

