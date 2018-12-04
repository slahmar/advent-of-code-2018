from collections import Counter

with open('02.txt', 'r') as file:
    for line in file.readlines():
        differences = {other: sum(1 for a, b in zip(line, other) if a != b) for other in lines}
        if 1 in differences.values():
           print(line)
           other_id = list(differences.keys())[list(differences.values()).index(1)]
           print(other_id)
           print(''.join([char for char in line if char in other_id]))
           break
   
