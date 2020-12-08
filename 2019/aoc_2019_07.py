
from collections import deque

f = open("./2019/2019_07.txt")
inp = f.readline().splitlines()[0].split(",")
inp = [int(a) for a in inp]
f.close()

class IntcodeComputer:
    def __init__(self, flash):
        self.mem_flash = flash.copy()
        self.mem_flash.append(0)
        self.mem_flash.append(0)
        self.mem_flash.append(0)
        self.mem = self.mem_flash.copy()
        self.ptr = 0
        self.inputs = deque()
        self.outputs = deque()
        self.pmode = ""
        self.opcode = ""
        self.parameters = [0,0,0]
        self.set_parameters()

    def reset(self):
        self.mem = self.mem_flash.copy()
        self.ptr = 0
        self.set_parameters()

    def add_input(self, newinput):
        if isinstance(newinput, list):
            for a in newinput:
                self.inputs.append(a)
        else:
            self.inputs.append(newinput)

    def has_output(self):
        return len(self.outputs) > 0

    def get_output(self):
        if self.has_output() == False:
            return None
        return self.outputs.popleft()

    def set_parameters(self):
        pmode_op = ("00000" + str(self.mem[self.ptr]))[-5:]
        self.pmode, self.op = pmode_op[:3], pmode_op[3:]

        if self.pmode[2] == "0":
            self.parameters[0] = self.mem[self.mem[self.ptr + 1]] if self.mem[self.ptr + 1] < len(self.mem) else None
        else:
            self.parameters[0] = self.mem[self.ptr + 1]

        if self.pmode[1] == "0":
            self.parameters[1] = self.mem[self.mem[self.ptr + 2]] if self.mem[self.ptr + 2] < len(self.mem) else None
        else:
            self.parameters[1] = self.mem[self.ptr + 2]        

        if self.pmode[0] == "0":
            self.parameters[2] = self.mem[self.mem[self.ptr + 3]] if self.mem[self.ptr + 3] < len(self.mem) else None
        else:
            self.parameters[2] = self.mem[self.ptr + 3]        

    def replace_memory(self, idx, val):
        self.mem[idx] = val
        self.set_parameters()
    
    def get_memory(self, idx):
        return self.mem[idx]

    def get_state(self):
        if self.op == "99":
            return "Complete"
        elif self.op == "03" and len(self.inputs) == 0:
            return "Awaiting Input"
        elif self.op == "03":
            return "Input Ready"
        else:
            return "WTF?"

    
    def opcode1(self):
        assert self.pmode[0] == "0"
        self.mem[self.mem[self.ptr + 3]] = self.parameters[0] + self.parameters[1]
        self.ptr += 4

    def opcode2(self):
        assert self.pmode[0] == "0"
        self.mem[self.mem[self.ptr + 3]] = self.parameters[0] * self.parameters[1]
        self.ptr += 4


    def opcode3(self):
        assert self.pmode == "000"
        if len(self.inputs) == 0:
            return False
        self.mem[self.mem[self.ptr + 1]] = self.inputs.popleft()
        self.ptr += 2
        return True


    def opcode4(self):
        self.outputs.append(self.parameters[0])
        self.ptr += 2


    def opcode5(self):
        if self.parameters[0] != 0:
            self.ptr = self.parameters[1]
        else:
            self.ptr += 3

    def opcode6(self):
        if self.parameters[0] == 0:
            self.ptr = self.parameters[1]
        else:
            self.ptr += 3

    def opcode7(self):
        assert self.pmode[0] == "0"
        self.mem[self.mem[self.ptr + 3]] = 1 if self.parameters[0] < self.parameters[1] else 0
        self.ptr += 4

    def opcode8(self):
        assert self.pmode[0] == "0"
        self.mem[self.mem[self.ptr + 3]] = 1 if self.parameters[0] == self.parameters[1] else 0
        self.ptr += 4

    def execute(self):
        while self.op != "99":
            if self.op == "01":
                self.opcode1()
            elif self.op == "02":
                self.opcode2()
            elif self.op == "03":
                if self.opcode3() == False:
                    break
            elif self.op == "04":
                self.opcode4()
            elif self.op == "05":
                self.opcode5()
            elif self.op == "06":
                self.opcode6()
            elif self.op == "07":
                self.opcode7()
            elif self.op == "08":
                self.opcode8()

            self.set_parameters()



best = None
for a in range(5,10):
    for b in range(5,10):
        if b == a:
            continue
        for c in range(5,10):
            if c == a or c == b:
                continue
            for d in range(5,10):
                if d == c or d == b or d == a:
                    continue
                for e in range(5,10):
                    if e != d and e != c and e != b and e != a:
                        
                        
                        ic_a = IntcodeComputer(inp)
                        ic_b = IntcodeComputer(inp)
                        ic_c = IntcodeComputer(inp)
                        ic_d = IntcodeComputer(inp)
                        ic_e = IntcodeComputer(inp)
                        ic_a.add_input(a)
                        ic_b.add_input(b)
                        ic_c.add_input(c)
                        ic_d.add_input(d)
                        ic_e.add_input(e)

                        x = 0
                        while ic_a.get_state() != "Complete":
                            ic_a.add_input(x)
                            ic_a.execute()
                            ic_b.add_input(ic_a.get_output())
                            ic_b.execute()
                            ic_c.add_input(ic_b.get_output())
                            ic_c.execute()
                            ic_d.add_input(ic_c.get_output())
                            ic_d.execute()
                            ic_e.add_input(ic_d.get_output())
                            ic_e.execute()
                            x = ic_e.get_output()
                            
                        
                        if best == None:
                            best = x
                        else:
                            best = max(best, x)
                        print(a, b, c, d, e, x)
print (best)