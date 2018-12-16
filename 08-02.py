from collections import deque


def read_node(numbers):
    if len(numbers) == 0:
        return 0
    metadata_sum = 0
    value = 0
    children_count = numbers.popleft()
    metadata_count = numbers.popleft()
    print(f'{children_count} children, {metadata_count} metadata')
    children_value = []    
    for i in range(children_count):
        child_value, numbers = read_node(numbers)
        children_value.append(child_value)
    for _ in range(metadata_count):
        index = numbers.popleft()
        metadata_sum += index
        if 1 <= index <= children_count:
            value += children_value[index-1]
    if children_count == 0:
        value = metadata_sum
    return value, numbers 


with open('08.txt', 'r') as file:
    numbers = deque(map(int, file.read().split(' ')))
    value, numbers = read_node(numbers)
    print(f'Value {value}')
