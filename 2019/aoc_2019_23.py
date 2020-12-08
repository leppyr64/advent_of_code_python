from collections import deque
import itertools

f = open("./2019/2019_23.txt")
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
        self.next_opcode()

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


ics = [IntcodeComputer(inp) for a in range(500)]

for i in range(50):
    ics[i].add_input(i)
    ics[i].execute()

part1 = False
done = False
idle = 0
idleused = {}
while done != True:
    idle += 1
    for i in range(50):
        while ics[i].has_outputs() == True:
            idle = 0
            address = ics[i].get_output()
            x = ics[i].get_output()
            y = ics[i].get_output()
            ics[address].add_input(x)
            ics[address].add_input(y)
            if address == 255 and part1 == False:
                print ("PART 1", y)
                part1 = True

    for i in range(50):
        if len(ics[i].inputs) == 0:
            ics[i].add_input(-1)
        else:
            idle = 0
        ics[i].execute()
        
    if idle == 10:
        while len(ics[255].inputs) > 2:
            ics[255].inputs.popleft()
        x = ics[255].inputs.popleft()
        y = ics[255].inputs.popleft()
        ics[0].add_input(x)
        ics[0].add_input(y)
        if y in idleused.keys():
            print ("PART2", y)
            done = True
        else:
            idleused[y] = 1
