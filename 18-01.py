from itertools import product


GROUND = '.'
TREES = '|'
LUMBERYARD = '#'


def get_adjacent_acres(acre, area):
    i = acre[0]
    j = acre[1]
    i_range = range(max(0,i-1), min(i+2, len(area[0])))
    j_range = range(max(0,j-1), min(j+2, len(area)))
    acres = list(product(i_range, j_range))
    if acre in acres:
        acres.remove(acre)
    return acres


with open('18.txt', 'r') as file:
    lines = file.readlines()
    area = [list(line[:-1]) for line in lines]
    print('\n'.join([''.join(line) for line in area]))
    minutes = 10
    minute = 0
    while minute < minutes:
        new_area = [[char for char in line] for line in area]
        for i in range(len(area)):
            for j in range(len(area[i])):
                adjacent_acres = get_adjacent_acres((i,j), area)
                print(f'Ajacent acres to {(i,j)} area {adjacent_acres}')
                adjacent_lumberyards = [(i,j) for (i,j) in adjacent_acres if area[i][j] == LUMBERYARD]
                adjacent_trees = [(i,j) for (i,j) in adjacent_acres if area[i][j] == TREES]
                if area[i][j] == GROUND and len(adjacent_trees) >= 3:
                    new_area[i][j] = TREES
                elif area[i][j] == TREES and len(adjacent_lumberyards) >= 3:
                    new_area[i][j] = LUMBERYARD
                elif area[i][j] == LUMBERYARD:
                    if len(adjacent_lumberyards) < 1 or len(adjacent_trees) < 1:
                        new_area[i][j] = GROUND
        area = new_area                
        minute += 1
        print(f'After {minute} minutes')
        print('\n'.join([''.join(line) for line in area]))
                
        
    lumberyards = sum([len([acre for acre in line if acre == LUMBERYARD]) for line in area])
    wooded = sum([len([acre for acre in line if acre == TREES]) for line in area])
    print(f'Lumberyards {lumberyards} x Wooded {wooded} = {lumberyards * wooded}')
