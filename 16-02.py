import json
from collections import Counter
import random

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

instructions = []
operations = [lambda a,b:a+b, lambda a,b:a*b, lambda a,b:a&b, lambda a,b:a|b]
for op in operations:
    instructions.append(Instruction(True, True, op))
    instructions.append(Instruction(True, False, op))
instructions.append(Instruction(True, True, lambda a,b:a))
instructions.append(Instruction(False, True, lambda a,b:a))

instructions.append(Instruction(False, True, lambda a,b:1 if a>b else 0))
instructions.append(Instruction(True, False, lambda a,b:1 if a>b else 0))
instructions.append(Instruction(True, True, lambda a,b:1 if a>b else 0))

instructions.append(Instruction(False, True, lambda a,b:1 if a==b else 0))
instructions.append(Instruction(True, False, lambda a,b:1 if a==b else 0))
instructions.append(Instruction(True, True, lambda a,b:1 if a==b else 0))

with open('16.txt', 'r') as file:
    lines = file.read()
    parts = lines.split("\n\n\n")
    samples = parts[0]
    samples = samples.split('\n')
    samples = [samples[i:i+3] for i in range(0, len(samples), 4)]

    nb_samples = 0
    possible = {opcode: set(instructions) for opcode in range(0,16)}
    for sample in samples:
        registers_before = json.loads(sample[0][sample[0].index(':')+2:])
        instruction = [int(nb) for nb in sample[1].split(' ')]
        opcode = instruction[0]
        A, B, C = instruction[1:]
        registers_after = json.loads(sample[2][sample[2].index(':')+2:])
        for instr in instructions:
            result = instr.execute(A, B, C, registers_before)
            if result != registers_after and instr in possible[opcode]:
                possible[opcode].remove(instr)
    
    while not all([len(possible[opcode]) == 1 for opcode in possible]):
        for opcode in possible: 
            if len(possible[opcode]) == 1:
                instr = possible[opcode]
                for other in possible:
                    if len(possible[other]) != 1:
                        possible[other] -= instr
         
    possible = {opcode: possible[opcode].pop() for opcode in possible}

    test_program = parts[1]
    registers = [0 for i in range(0,4)]
    for line in test_program.split('\n')[1:]:
        if len(line) > 0:
            numbers = list(map(int, line.split(" ")))
            registers = possible[numbers[0]].execute(numbers[1], numbers[2], numbers[3], registers)
    print(registers[0])
