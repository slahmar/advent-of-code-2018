from collections import Counter

with open('01.txt', 'r') as file:
    freqs = Counter()
    freq = 0
    while not freqs or freqs.most_common(1)[0][1] < 2:
        for line in file.readlines():
            freq += int(line)
            freqs[freq] += 1
            if freqs[freq] == 2:
                break
    print("First frequency which appeared twice {}".format(freqs.most_common(1)))


