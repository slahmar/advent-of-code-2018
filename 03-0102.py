from itertools import product
from collections import Counter

with open('03.txt') as file:
    lines = [(line[:line.index('@')+2], line.rstrip('\n')[line.index('@')+2:]) for line in file]
    coords_by_claim = {}
    coords = Counter()
    for line_id, line in lines:
        first_x = int(line[0:line.index(',')])
        first_y = int(line[line.index(',')+1:line.index(':')])
        width = int(line[line.index(':')+2:line.index('x')])
        height = int(line[line.index('x')+1:])
        xs = range(first_x+1, first_x+width+1)
        ys = range(first_y+1, first_y+height+1)
        coordinates = list(product(xs, ys))
        coords_by_claim[line_id] = coordinates
        coords.update(coordinates)
    overlapping = [coord for coord in coords if coords[coord] >= 2]
    print(len(overlapping))
    for claim in coords_by_claim:
        if any([coords[(x,y)] > 1 for x, y in coords_by_claim[claim]]):
            continue
        else:
            break
    print(claim)
        

