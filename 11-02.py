from itertools import product
import numpy as np


def get_power(cell, serial_number):
    rack_id = cell[0] + 10
    power = rack_id * cell[1]
    power += serial_number
    power *= rack_id
    power = power // 100 % 10
    power -= 5
    return power


serial_number = 6303
cells = np.ndarray((300,300))
for i in range(0, 300):
    for j in range(0, 300):
        cells[i,j] = get_power((i,j), serial_number)

cell_sum = np.ndarray((300,300))
cell_sum[0][0] = cells[0][0]
for j in range(1,300):
    cell_sum[0][j] = cells[0][j] + cell_sum[0][j-1]
for j in range(1,300):
    cell_sum[i][0] = cells[i][0] + cell_sum[i-1][0]
for i in range(1, 300):
    for j in range(1, 300):
        cell_sum[i,j] = cell_sum[i][j-1] + cell_sum[i-1][j] + cells[i,j] - cell_sum[i-1][j-1]

max_fuel = 0
for k in range(0,300):
    for i in range(k-1,300):
        for j in range(k-1,300):
            total = cell_sum[i][j]
            if i-k >= 0:
                total -= cell_sum[i-k][j]
            if j-k >= 0:
                total -= cell_sum[i][j-k]
            if i-k >= 0 and j-k >= 0:
                total += cell_sum[i-k][j-k]
            if total > max_fuel:
                max_fuel = total
                max_cell = (i-k+1,j-k+1,k)

print(f'Max fuel {max_fuel} obtained for cell {max_cell}')
