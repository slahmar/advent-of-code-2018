from itertools import product


def get_power(cell, serial_number):
    rack_id = cell[0] + 10
    power = rack_id * cell[1]
    power += serial_number
    power *= rack_id
    power = power // 100 % 10
    power -= 5
    return power


serial_number = 6303
max_fuel = 0
for i in range(0, 297):
    for j in range(0, 297):
        square = list(product([i, i+1, i+2], [j, j+1, j+2]))
        total_fuel = sum(get_power(cell, serial_number) for cell in square)
        if total_fuel > max_fuel:
            max_fuel = total_fuel
            max_square_left_cell = [i,j]
print(f'Max fuel {max_fuel} at square with top left {max_square_left_cell}')
