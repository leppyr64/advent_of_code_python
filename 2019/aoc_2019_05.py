
f = open("./2019_05.txt")
inp = f.read().splitlines()[0].split(",")
inp = [int(a) for a in inp]
inp.append(0)
inp.append(0)
inp.append(0)
f.close()

mem = []
    #p1 = mem[idx + 1] if pmode[2] == "1" else mem[mem[idx + 1]]
    #p2 = mem[idx + 2] if pmode[1] == "1" else mem[mem[idx + 2]]
    #p3 = mem[idx + 2] if pmode[1] == "1" else mem[mem[idx + 2]]

def opcode1(mem, pmode, idx):
    assert pmode[0] == "0"
    p1 = mem[idx + 1] if pmode[2] == "1" else mem[mem[idx + 1]]
    p2 = mem[idx + 2] if pmode[1] == "1" else mem[mem[idx + 2]]
    mem[mem[idx + 3]] = p1 + p2

def opcode2(mem, pmode, idx):
    assert pmode[0] == "0"
    p1 = mem[idx + 1] if pmode[2] == "1" else mem[mem[idx + 1]]
    p2 = mem[idx + 2] if pmode[1] == "1" else mem[mem[idx + 2]]
    mem[mem[idx + 3]] = p1 * p2

def opcode3(mem, pmode, idx, x):
    assert pmode == "000"
    mem[mem[idx + 1]] = x # the input is 1 for part a, 5 for part b

def opcode4(mem, pmode, idx):
    p1 = mem[idx + 1] if pmode[2] == "1" else mem[mem[idx + 1]]
    print("OUTPUT:", p1)

def opcode5(mem, pmode, idx):
    p1 = mem[idx + 1] if pmode[2] == "1" else mem[mem[idx + 1]]
    p2 = mem[idx + 2] if pmode[1] == "1" else mem[mem[idx + 2]]
    if p1 != 0:
        return p2 
    else:
        return idx + 3

def opcode6(mem, pmode, idx):
    p1 = mem[idx + 1] if pmode[2] == "1" else mem[mem[idx + 1]]
    p2 = mem[idx + 2] if pmode[1] == "1" else mem[mem[idx + 2]]
    if p1 == 0:
        return p2 
    else:
        return idx + 3

def opcode7(mem, pmode, idx):
    assert pmode[0] == "0"
    p1 = mem[idx + 1] if pmode[2] == "1" else mem[mem[idx + 1]]
    p2 = mem[idx + 2] if pmode[1] == "1" else mem[mem[idx + 2]]
    mem[mem[idx + 3]] = 1 if p1 < p2 else 0

def opcode8(mem, pmode, idx):
    assert pmode[0] == "0"
    p1 = mem[idx + 1] if pmode[2] == "1" else mem[mem[idx + 1]]
    p2 = mem[idx + 2] if pmode[1] == "1" else mem[mem[idx + 2]]
    mem[mem[idx + 3]] = 1 if p1 == p2 else 0



def intcode_computer(id):
    mem = inp.copy()
    idx = 0
    p1 = 0
    p2 = 0
    while idx < len(mem):
        pmode_op = ("00000" + str(mem[idx]))[-5:]
        pmode, op = pmode_op[:3], pmode_op[3:]
        #print(mem[idx], pmode, op)

        if op == "01":
            opcode1(mem, pmode, idx)
            idx += 4
        elif op == "02":
            opcode2(mem, pmode, idx)
            idx += 4
        elif op == "03":
            opcode3(mem, pmode, idx, id)
            idx += 2
        elif op == "04":
            opcode4(mem, pmode, idx)
            idx += 2
        elif op == "05":
            idx = opcode5(mem, pmode, idx)
        elif op == "06":
            idx = opcode6(mem, pmode, idx)
        elif op == "07":
            opcode7(mem, pmode, idx)
            idx += 4 
        elif op == "08":
            opcode8(mem, pmode, idx)
            idx += 4 
        else:
            assert op == "99"
            #print (mem)
            idx = len(mem)
        #print (mem)
            
#for i in range(15):
#    print (i)
#    intcode_computer(i)

print (1)
intcode_computer(1)

print(5)
intcode_computer(5)