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
    #print(register_pointed)
    instrs = lines[1:]
    registers = [4, 0, 10551338, 4, 5, 10551339]
    instr_pointer = 6
    to_execute = []
    for instr in instrs:
        args = instr.split(" ")
        code = args[0]
        A, B, C = args[1:]
        to_execute.append((code, int(A), int(B), int(C)))
        
    i = 0
    while instr_pointer < len(to_execute):
        print(f'Instr pointer {instr_pointer}')
        instr = to_execute[instr_pointer]
        #print(f'Executing {code} with args {A,B,C}')
        registers[register_pointed] = instr_pointer
        registers = instructions[instr[0]].execute(instr[1], instr[2], instr[3], registers)
        instr_pointer = registers[register_pointed] + 1
        print(f'Registers {registers}')
        i += 1
        if i == 20:
            break

    print('end')
    
# Write-up :
# Checking the flow of instructions, I realized that
# at the beginning of the program, R5 received the value of 10551339
# Besides, there were two loops:
# One over the value of R2 : R2 oscillated between 0 and R5
# One over the value of R3
# Each time R2*R3 = R5, R0 += R3
# Each time R2 > R5, R3 += 1
# I understood that the program computed the sum of the dividers of R5 !
