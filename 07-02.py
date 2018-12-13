from collections import deque
import string

class Worker:
    def __init__(self,time_idle=0):
        self.time_idle = time_idle
    
    def is_idle(self, time):
        return time >= self.time_idle


with open('07.txt', 'r') as file:
    lines = file.readlines()
    couples = [(line[line.index('Step')+5],line[line.index('step')+5]) for line in lines]
    prerequisites = {}
    order = {}
    time = 0
    for couple in couples:
        if couple[0] not in prerequisites:
            prerequisites[couple[0]] = []
        if couple[1] not in prerequisites:
            prerequisites[couple[1]] = []
        prerequisites[couple[1]].append(couple[0])

    workers = [Worker() for _ in range(5)]
    while prerequisites:
        print(prerequisites)
        leading_steps = sorted({key for key in prerequisites if not prerequisites[key]})
        print(f'Leading steps {leading_steps} at time = {time}')
        idle_workers = [worker for worker in workers if worker.is_idle(time)]
        for i in range(min(len(leading_steps), len(idle_workers))):
            worker = idle_workers[i]
            leading_step = leading_steps[i]
            print(f'Worker {workers.index(worker)} is idle, taking up {leading_step}')
            worker.time_idle = time + string.ascii_uppercase.index(leading_step) + 61
            print(f'Worker {workers.index(worker)} will be busy until {worker.time_idle}')
            order[worker.time_idle] = leading_step
            del prerequisites[leading_step]
        time = min([key for key in order.keys() if key > time])
        for step in prerequisites:
            if order[time] in prerequisites[step]:
                prerequisites[step].remove(order[time])
        print(f'Time {time} after {order[time]} ended')
    print(f'Final order {"".join([order[k] for k in sorted(order.keys())])}')

