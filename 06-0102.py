from collections import Counter
import sys

def manhattan_distance(loc1, loc2):
    return abs(loc2[1]-loc1[1]) + abs(loc2[0]-loc1[0])


with open('06.txt', 'r') as file:
    locations = [(int(line[:line.index(",")]), int(line[line.index(",")+2:])) for line in file.readlines()]
    ys = [loc[1] for loc in locations]
    xs = [loc[0] for loc in locations]
    max_y = max(ys)
    max_x = max(xs)
    min_y = min(ys)
    min_x = min(xs)
    closest = Counter()
    distances = {}
    finite_locations = locations.copy()
    for i in range(0, max_x+1):
        for j in range(0, max_y+1):
            distance = sys.maxsize
            closest_loc = None
            distances[(i,j)] = 0
            for loc in locations:
                temp_distance = manhattan_distance((i,j), loc)
                distances[(i,j)] += temp_distance
                if temp_distance < distance:
                    closest_loc = loc
                    distance = temp_distance
                elif temp_distance == distance:
                    closest_loc = None
            if closest_loc in finite_locations:
                if i == 0 or i == max_x or j == 0 or j == max_y:
                    finite_locations.remove(closest_loc)
                    closest[closest_loc] = -1
                else:                
                    closest[closest_loc] += 1
    
    print(closest)
    print(len(list(key for key in distances.keys() if distances[key] < 10_000)))

