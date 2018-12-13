from collections import deque


with open('07.txt', 'r') as file:
    lines = file.readlines()
    couples = [(line[line.index('Step')+5],line[line.index('step')+5]) for line in lines]
    prerequisites = {}
    order = ''
    for couple in couples:
        if couple[0] not in prerequisites:
            prerequisites[couple[0]] = []
        if couple[1] not in prerequisites:
            prerequisites[couple[1]] = []
        prerequisites[couple[1]].append(couple[0])

    while prerequisites:
        leading_step = sorted({key for key in prerequisites if not prerequisites[key]})[0]
        order += leading_step
        del prerequisites[leading_step]
        print(f'Leading step {leading_step}')
        for step in prerequisites:
            if leading_step in prerequisites[step]:
                prerequisites[step].remove(leading_step)
        print(f'Prereq {prerequisites}')
    print(f'Final order {order}')

