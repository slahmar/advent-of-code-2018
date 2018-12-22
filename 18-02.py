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


def get_resource_value(area):
    lumberyards = sum([len([acre for acre in line if acre == LUMBERYARD]) for line in area])
    wooded = sum([len([acre for acre in line if acre == TREES]) for line in area])
    resource_value = lumberyards * wooded
    #print(f'{minute}: Lumberyards {lumberyards} x Wooded {wooded} = {resource_value}') 
    return lumberyards, wooded, resource_value     

with open('18.txt', 'r') as file:
    lines = file.readlines()
    area = [list(line[:-1]) for line in lines]
    #print('\n'.join([''.join(line) for line in area]))
    minutes = 10
    minute = 0
    previous_l, previous_w, previous_r = get_resource_value(area)
    while minute < minutes:
        new_area = [[char for char in line] for line in area]
        for i in range(len(area)):
            for j in range(len(area[i])):
                adjacent_acres = get_adjacent_acres((i,j), area)
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
        l, w, r = get_resource_value(area)
        print(f'At minute {minute}, R {r}')
        #print('\n'.join([''.join(line) for line in area]))
        previous_l = l
        previous_w = w
        previous_r = r
        
    # Write-up :
    # I realized that starting from a certain minute,
    # there was a loop on the result value (with a length of 35)
    # So I just compute the result with a modulo !
    loop = [95550, 94656, 93612, 92649, 92115, 90816, 89180, 88400, 86445, 84500,
        83328,82992,83239,83415,82992,83824, 84750,87032, 87897,92160,95526,98580,
        102850, 105000, 107068, 108864,109152, 110208,110396, 109347, 107912,106477,
        106134, 103076, 97578]
    print(loop[(1_000_000_000-970)%35])



