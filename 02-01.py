from collections import Counter

with open('02.txt') as file:
    lines = file.readlines()
    twice = [line for line in lines if 2 in Counter(line).values()]
    three_times = [line for line in lines if 3 in Counter(line).values()]
    print(len(twice))
    print(len(three_times))
    print(len(twice)*len(three_times))

