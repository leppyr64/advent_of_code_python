
def DenseHash(sparsehash):
    op = ''
    for i in range(16):
        x = 0
        for j in range(16):
            x ^= sparsehash[i*16+j]
        s = hex(x)
        s = '0' + s[2:]
        op += s[-2:]
    return op

def KnotHash(inp):
    memlen = 256
    lengths = [ord(x) for x in inp] + [17,31,73,47,23]
    mem = [x for x in range(memlen)]
    skip = 0
    pos = 0
    for i in range(64):
        mem, pos, skip = KnotHashRound(mem, pos, skip, memlen, lengths)
    return DenseHash(mem)

def KnotHashRound(mem, pos, skip, memlen, lengths):
    for l in lengths:
        mem = mem + mem
        seg = mem[pos:pos + l]
        seg.reverse()
        mem =  mem[:pos] + seg + mem[pos + l:]
        mem = mem[pos:pos + memlen]
        mem = mem[-pos:] + mem[:-pos]
        pos = (pos + skip + l) % memlen
        skip = (skip + 1) % memlen
        #print (pos, skip, mem)
    return mem, pos, skip

def KnotHashPart1(inp, memlen):
    lengths = [int(x) for x in  inp.split(',')]
    mem = [x for x in range(memlen)]
    skip = 0
    pos = 0
    mem, pos, skip = KnotHashRound(mem, pos, skip, memlen, lengths)
    return mem[0]*mem[1]

print(KnotHashPart1('3,4,1,5', 5))
print(KnotHashPart1('225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110', 256))

print(KnotHash(''))
print(KnotHash('AoC 2017'))
print(KnotHash('1,2,3'))
print(KnotHash('1,2,4'))

print(KnotHash('225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110'))


#f = open("./2017/Input/2017_10.txt")
#inp = f.read().splitlines()
#for x in inp:
#    KnotHash(x)

