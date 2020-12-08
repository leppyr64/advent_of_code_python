f = open("./2019/2018_16.txt")
inp = f.read().splitlines()
f.close()

inp = [a.strip() for a in inp]

ins = []
for i in range(len(inp)):
    if inp[i][:6] == "Before":
        #print(inp[i], inp[i+1], inp[i+2])
        ins.append(inp[i].split("[")[1][:-1].split(","))
        ins.append(inp[i + 1].split())
        ins.append(inp[i + 2].split("[")[1][:-1].split(","))


ins = [[int(a) for a in b] for b in ins]
print(len(ins) // 3 * 4)

print (inp[3230])
M = []
for i in range(3230, len(inp)):
    for j in inp[i].split():
        M.append(int(j))
print(M)

class Device(object):
    
    def __init__(self, mem):
        self.M = mem.copy()
        self.F = mem.copy()

    def flashreset(self):
        self.M = self.F.copy()


# Addition:

# addr (add register) stores into register C the result of adding register A and register B.
# addi (add immediate) stores into register C the result of adding register A and value B.
    def addr(self, a, b, c):
        self.M[c] = self.M[a] + self.M[b]
        #print ("addr", self.M)
        return self.M

    def addi(self, a, b, c):
        self.M[c] = self.M[a] + b
        #print ("addi", self.M)
        

# Multiplication:

# mulr (multiply register) stores into register C the result of multiplying register A and register B.
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
    def mulr(self, a, b, c):
        self.M[c] = self.M[a] * self.M[b]
        #print ("mulr", self.M)
        
    
    def muli(self, a, b, c):
        self.M[c] = self.M[a] * b
        #print ("muli", self.M)
        

# Bitwise AND:

# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
    def banr(self, a, b, c):
        self.M[c] = self.M[a] & self.M[b]
        #print ("banr", self.M)
        

    def bani(self, a, b, c):
        self.M[c] = self.M[a] & b
        #print ("bani", self.M)
        

# Bitwise OR:

# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
    def borr(self, a, b, c):
        
        self.M[c] = self.M[a] | self.M[b]
        #print ("borr", self.M)
        

    def bori(self, a, b, c):
        
        self.M[c] = self.M[a] | b
        #print ("bori", self.M)
        

# Assignment:

# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
# seti (set immediate) stores value A into register C. (Input B is ignored.)
    def setr(self, a, b, c):
        
        self.M[c] = self.M[a]
        #print ("setr", self.M)
        

    def seti(self, a, b, c):
        
        self.M[c] = a
        #print ("seti", self.M)
        

# Greater-than testing:

# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.

    def gtir(self, a, b, c):
        
        if a > self.M[b]:
            self.M[c] = 1
        else:
            self.M[c] = 0
        
    
    def gtri(self, a, b, c):
        
        if self.M[a] > b:
            self.M[c] = 1
        else:
            self.M[c] = 0
        

    def gtrr(self, a, b, c):
        
        if self.M[a] > self.M[b]:
            self.M[c] = 1
        else:
            self.M[c] = 0
        

# Equality testing:

# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.

    def eqir(self, a, b, c):
        
        if a == self.M[b]:
            self.M[c] = 1
        else:
            self.M[c] = 0
        
    
    def eqri(self, a, b, c):
        
        if self.M[a] == b:
            self.M[c] = 1
        else:
            self.M[c] = 0
        

    def eqrr(self, a, b, c):
        
        if self.M[a] == self.M[b]:
            self.M[c] = 1
        else:
            self.M[c] = 0
        
    def execute(self):
        for i in range(0, len(self.M), 4):
            x = self.M[i]
            a = self.M[i + 1]
            b = self.M[i + 2]
            c = self.M[i + 3]
            
            if x == 6:
                self.addi(a, b, c)
            if x == 9:
                self.addr(a, b, c)
            if x == 0: 
                self.muli(a, b, c)
            if x == 8:
                self.mulr(a, b, c)
            if x == 11:
                self.bani(a, b, c)
            if x == 14:
                self.banr(a, b, c)
            if x == 10: 
                self.bori(a, b, c)
            if x == 1:
                self.borr(a, b, c)
            if x == 12:
                self.seti(a, b, c)
            if x == 7:
                self.setr(a, b, c)
            if x == 15:
                self.gtir(a, b, c)
            if x == 2:
                self.gtri(a, b, c)
            if x == 4:
                self.gtrr(a, b, c)
            if x == 5:
                self.eqir(a, b, c)
            if x == 3:
                self.eqri(a, b, c)
            if x == 13:
                self.eqrr(a, b, c)

# count = 0
# for i in range(0, len(ins), 3):
#     d = Device(ins[i])
#     n = d.test(ins[i + 1], ins[i + 2])
#     if n >= 3:
#         count += 1
#     a = d.test2(ins[i + 1], ins[i + 2])
#     if len(a) == 1:
#         if ins[i + 1][0] not in [9, 0, 8, 1, 10, 6, 12, 2, 4,3 , 5, 13, 15, 7, 14, 11]:
#             print (ins[i], ins[i + 1], ins[i + 2], a[0])
# print (count)

d = Device(M)
d.execute()
print(d.M[0])
