from collections import deque


def read_node(numbers):
    metadata_sum = 0
    if len(numbers) == 0:
        return 0
    children_count = numbers.popleft()
    metadata_count = numbers.popleft()
    print(f'{children_count} children, {metadata_count} metadata')
    for _ in range(children_count):
        children_metadata_sum, numbers = read_node(numbers)
        metadata_sum += children_metadata_sum
    for _ in range(metadata_count):
        metadata_sum += numbers.popleft()
    print(f'Metadata sum {metadata_sum}')
    return metadata_sum, numbers 


with open('08.txt', 'r') as file:
    numbers = deque(map(int, file.read().split(' ')))
    metadata_sum, numbers = read_node(numbers)
    print(f'Metadata sum {metadata_sum}')
