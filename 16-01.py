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
    samples = lines.split("\n\n\n")[0]
    samples = samples.split('\n')
    samples = [samples[i:i+3] for i in range(0, len(samples), 4)]

    nb_samples = 0 
    for sample in samples:
        registers_before = json.loads(sample[0][sample[0].index(':')+2:])
        instruction = [int(nb) for nb in sample[1].split(' ')]
        A, B, C = instruction[1:]
        registers_after = json.loads(sample[2][sample[2].index(':')+2:])
        matching = 0
        for instr in instructions:
            if instr.execute(A, B, C, registers_before) == registers_after:
                matching += 1
            if matching >= 3:
                nb_samples += 1
                break
    print(f'Number of samples {nb_samples}')

        
