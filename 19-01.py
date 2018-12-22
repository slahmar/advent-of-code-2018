import json
from collections import Counter

class Instruction:
    def __init__(self, reg_a, reg_b, operation):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.operation = operation
    
    def execute(self, A, B, C, registers):
        a = registers[A] if self.reg_a else A
        b = registers[B] if self.reg_b else B
        result = self.operation(a, b)
        registers_after = registers.copy()
        registers_after[C] = result
        return registers_after

instructions = {}
instructions["addr"] = Instruction(True, True, lambda a,b:a+b)
instructions["addi"] = Instruction(True, False, lambda a,b:a+b)
instructions["mulr"] = Instruction(True, True, lambda a,b:a*b)
instructions["muli"] = Instruction(True, False, lambda a,b:a*b)
instructions["banr"] = Instruction(True, True, lambda a,b:a&b)
instructions["bani"] = Instruction(True, False, lambda a,b:a&b)
instructions["borr"] = Instruction(True, True, lambda a,b:a|b)
instructions["bori"] = Instruction(True, False, lambda a,b:a|b)
instructions["setr"] = Instruction(True, False, lambda a,b:a)
instructions["seti"] = Instruction(False, False, lambda a,b:a)
instructions["gtir"] = Instruction(False, True, lambda a,b:1 if a>b else 0)
instructions["gtri"] = Instruction(True, False, lambda a,b:1 if a>b else 0)
instructions["gtrr"] = Instruction(True, True, lambda a,b:1 if a>b else 0)
instructions["eqir"] = Instruction(False, True, lambda a,b:1 if a==b else 0)
instructions["eqri"] = Instruction(True, False, lambda a,b:1 if a==b else 0)
instructions["eqrr"] = Instruction(True, True, lambda a,b:1 if a==b else 0)

with open('19.txt', 'r') as file:
    lines = file.read().splitlines()
    register_pointed = int(lines[0][-1])
    print(register_pointed)
    instrs = lines[1:]
    registers = [0] * 6
    instr_pointer = 0
    while instr_pointer < len(instrs):
        #print(f'Instr pointer {instr_pointer}')
        instr = instrs[instr_pointer]
        args = instr.split(" ")
        code = args[0]
        A, B, C = args[1:]
        #print(f'Executing {code} with args {A,B,C}')
        registers[register_pointed] = instr_pointer
        registers = instructions[code].execute(int(A), int(B), int(C), registers)
        if registers[register_pointed] != instr_pointer:
            #print(f'Jump to {registers[register_pointed]}')
            instr_pointer = registers[register_pointed]
        instr_pointer += 1
    print(f'Registers {registers}')
        
