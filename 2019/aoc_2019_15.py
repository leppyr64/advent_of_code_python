from collections import deque
import itertools

f = open("./2019/2019_15.txt")
inp = f.read().splitlines()[0].split(",")
inp = [int(a) for a in inp]
f.close()

class IntcodeComputer:
    
    def __init__(self, program):
        self.mem = dict()
        for i in range(len(program)):
            self.mem[i] = program[i]

        self.ptr = 0
        self.inputs = deque()
        self.outputs = deque()

        self.opcode = ""
        self.memmmode = ""
        self.relative_offset = 0

        self.next_opcode()


    def next_opcode(self):
        x = "0000000000" + str(self.mem[self.ptr])
        self.opcode = x[-2:]
        self.memmode = x[:-2][::-1]

    def replace_mem(self, idx, val):
        self.mem[idx] = val

    def status(self):
        if self.opcode == "99":
            return "Complete"
        elif self.opcode == "03" and len(self.inputs) > 0:
            return "Ready for Input"
        elif self.opcode == "03" and len(self.inputs) == 0:
            return "Waiting for Input"
        else:
            return "Ready"

    def add_input(self, val):
        self.inputs.append(val)

    def get_output(self):
        if len(self.outputs) == 0:
            return None
        return self.outputs.popleft()

    def has_outputs(self):
            return len(self.outputs) > 0
    # parameter mode
    # - 0 = position mode - mem refers to an address
    # - 1 = immediate mode - mem is a value
    # - 2 = relative mode - mem refers to an address + relative offset
    # Parameters that an instruction writes to will never be in immediate mode.

    def get_mem_address(self, mode, local_ptr):
        if mode == "1":
            return local_ptr
        elif mode == "0":
            if self.mem[local_ptr] not in self.mem.keys():
                self.mem[self.mem[local_ptr]] = 0
            return self.mem[local_ptr]
        elif mode == "2":
            if self.mem[local_ptr] + self.relative_offset not in self.mem.keys():
               self.mem[self.mem[local_ptr] + self.relative_offset] = 0 
            return self.mem[local_ptr] + self.relative_offset
        else:
            assert False
        
    def op1_add(self):
        mem1 = self.get_mem_address(self.memmode[0], self.ptr + 1)
        mem2 = self.get_mem_address(self.memmode[1], self.ptr + 2)
        mem3 = self.get_mem_address(self.memmode[2], self.ptr + 3)
        self.mem[mem3] = self.mem[mem1] + self.mem[mem2]
        self.ptr += 4

    def op2_mult(self):
        mem1 = self.get_mem_address(self.memmode[0], self.ptr + 1)
        mem2 = self.get_mem_address(self.memmode[1], self.ptr + 2)
        mem3 = self.get_mem_address(self.memmode[2], self.ptr + 3)
        self.mem[mem3] = self.mem[mem1] * self.mem[mem2]
        self.ptr += 4

    def op3_take_input(self):
        if len(self.inputs) == 0:
            return False
        mem1 = self.get_mem_address(self.memmode[0], self.ptr + 1)
        self.mem[mem1] = self.inputs.popleft()
        self.ptr += 2
        return True

    def op4_give_output(self):
        mem1 = self.get_mem_address(self.memmode[0], self.ptr + 1)
        self.outputs.append(self.mem[mem1])
        self.ptr += 2

    def op5_jump_if_true(self):
        mem1 = self.get_mem_address(self.memmode[0], self.ptr + 1)
        mem2 = self.get_mem_address(self.memmode[1], self.ptr + 2)
        if self.mem[mem1] != 0:
            self.ptr = self.mem[mem2]
        else:
            self.ptr += 3
    
    def op6_jump_if_false(self):
        mem1 = self.get_mem_address(self.memmode[0], self.ptr + 1)
        mem2 = self.get_mem_address(self.memmode[1], self.ptr + 2)
        if self.mem[mem1] == 0:
            self.ptr = self.mem[mem2]
        else:
            self.ptr += 3
        
    def op7_less_than(self):
        mem1 = self.get_mem_address(self.memmode[0], self.ptr + 1)
        mem2 = self.get_mem_address(self.memmode[1], self.ptr + 2)
        mem3 = self.get_mem_address(self.memmode[2], self.ptr + 3)
        if self.mem[mem1] < self.mem[mem2]:
            self.mem[mem3] = 1
        else:
            self.mem[mem3] = 0
        self.ptr += 4

    def op8_equals(self):
        mem1 = self.get_mem_address(self.memmode[0], self.ptr + 1)
        mem2 = self.get_mem_address(self.memmode[1], self.ptr + 2)
        mem3 = self.get_mem_address(self.memmode[2], self.ptr + 3)
        if self.mem[mem1] == self.mem[mem2]:
            self.mem[mem3] = 1
        else:
            self.mem[mem3] = 0
        self.ptr += 4

    def op9_adjust_relative_base(self):
        mem1 = self.get_mem_address(self.memmode[0], self.ptr + 1)
        self.relative_offset += self.mem[mem1]
        self.ptr += 2

    def execute(self):
        while(self.opcode != "99"):
            if self.opcode == "01":
                self.op1_add()
            elif self.opcode == "02":
                self.op2_mult()
            elif self.opcode == "03":
                if self.op3_take_input() == False:
                    break
            elif self.opcode == "04":
                self.op4_give_output()
            elif self.opcode == "05":
                self.op5_jump_if_true()
            elif self.opcode == "06":
                self.op6_jump_if_false()
            elif self.opcode == "07":
                self.op7_less_than()
            elif self.opcode == "08":
                self.op8_equals()
            elif self.opcode == "09":
                self.op9_adjust_relative_base()
            else:
                assert False
            self.next_opcode()


NR = 2000
NC = 2000
minr = 1000000
minc = 1000000
maxr = 0
maxc = 0
G = [['*' for c in range(NC)] for r in range(NR)]
D = [[5000 for c in range(NC)] for r in range(NR)]
D[1000][1000] = 0

ic = IntcodeComputer(inp)
ic.execute()
print(ic.status())


dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
rp = [0, 2, 1, 4, 3]

def DFS(r, c, returnpath):
    global minr
    global maxr
    global minc
    global maxc
    minr = min(minr, r)
    minc = min(minc, c)
    maxr = max(maxr, r)
    maxc = max(maxc, c)
    for i in range(1, 5):
        if G[r + dr[i]][c + dc[i]] == '*':
            ic.add_input(i)
            ic.execute()
            x = ic.get_output()
            # print (r, c, returnpath, i, x)
            if x == 0:
                G[r + dr[i]][c + dc[i]] = '#'
            else:
                G[r + dr[i]][c + dc[i]] = str(x)
                D[r + dr[i]][c + dc[i]] = D[r][c] + 1
                DFS(r + dr[i], c + dc[i], rp[i])
        elif G[r + dr[i]][c + dc[i]] != '#':
            D[r + dr[i]][c + dc[i]] = min(D[r + dr[i]][c + dc[i]], D[r][c] + 1)
    if returnpath != 0:
        ic.add_input(returnpath)
        ic.execute()
        x = ic.get_output()
                
DFS(1000, 1000, 0)
print (minr, maxr, minc, maxc)

minc -= 1
maxc += 1
minr -= 1
maxr += 1
for r in range(minr, maxr + 1):
    s = ''
    for c in range(minc, maxc + 1):
        if G[r][c] == '1':
            s += ' '
        else:
            s += G[r][c]
    print (s)

oxr = 0
oxc = 0

for r in range(2000):
    for c in range(2000):
        if G[r][c] == '2':
            print (r, c, D[r][c])
            oxr = r
            oxc = c

maxd = 0
q = deque()
q.append([oxr, oxc, 0])
D = [[5000 for c in range(NC)] for r in range(NR)]
D[oxr][oxc] = 0
while len(q) != 0:
    r,c,d = q.popleft()
    maxd = d
    for i in range(1,5):
        newr = r + dr[i]
        newc = c + dc[i]
        if G[newr][newc] != '#' and D[newr][newc] == 5000:
            D[newr][newc] = D[r][c] + 1
            q.append([newr, newc, D[r][c] + 1])
print (maxd)



