with open('01.txt', 'r') as file:
    lines = file.readlines()
    resulting_frequency = sum([int(line) for line in lines])
    print(resulting_frequency)
