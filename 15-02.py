from dataclasses import dataclass

SYMBOLS = ['E', 'G', '#']

def shortest_path(start_point, end_point, cavern):
    queue = []
    visited = set()
    queue.append([start_point])
    paths = []
    while queue:
        path = queue.pop(0)
        current_point = path[-1]
        if current_point == end_point:
            return path[1:-1]
        x = current_point[0]
        y = current_point[1]
        adjacent_points = [(x-1,y), (x,y-1), (x,y+1), (x+1,y)]
        adjacent_points = [(a,b) for (a,b) in adjacent_points if (a,b) == end_point or cavern[a][b] not in SYMBOLS]
        for adjacent_point in adjacent_points:
            if adjacent_point not in visited:
                if adjacent_point != end_point:
                    visited.add(adjacent_point)
                new_path = list(path)
                new_path.append(adjacent_point)
                queue.append(new_path)
    return None


@dataclass
class Unit:
    x: int
    y: int
    symbol: str
    hit_points: int = 200
    attack_power: int = 3
    alive : bool = True

    def path_to_target(self, target, cavern):
        under = 1 if (target.y-self.y) > 0 else -1
        right = 1 if (target.x-self.x) > 0 else -1
        path = shortest_path((self.x, self.y), (target.x, target.y), cavern)
        #print(f'{path} from {self} to {target}')
        return path

    def find_nearest_target(self, targets, cavern):
        distance = 10000
        nearest_targets = []
        for target in targets:
            path = self.path_to_target(target, cavern)
            if path is None:
                #print(f'No path from {self} to {target}')
                continue
            elif len(path) < distance:
                distance = len(path)
                nearest_targets = [(path, target)]
            elif len(path) == distance:
                nearest_targets.append((path, target))

        if len(nearest_targets) >= 1:
            path_target = min(nearest_targets, key=lambda path_target: (path_target[1].x, path_target[1].y))
        else:
            path_target = None, None
        #print(f'Nearest target to {self} is {path_target[1]} with distance {distance+1} and path {path_target[0]}')
        return path_target

    def move_to_next_square(self, path, cavern):
        cavern[self.x][self.y] = '.'
        self.x = path[0][0]
        self.y = path[0][1]
        cavern[self.x][self.y] = self.symbol
        return cavern

    def attack(self, targets, cavern):
        target = None
        available_targets = [target for target in targets if self.path_to_target(target, cavern) == []]
        if len(available_targets) > 0:
            #print(f'Available targets {available_targets}')
            target = min(available_targets, key=lambda target: (target.hit_points, target.x, target.y))
            target.hit_points -= self.attack_power
            #print(f'{self} attacks {target} which has now {target.hit_points} hit points')
            if(target.hit_points <= 0):
                #print(f'Removing dead {target}')
                cavern[target.x][target.y] = '.'
                target.alive = False
        return cavern



@dataclass
class Goblin(Unit):
    symbol: str = 'G'


@dataclass
class Elf(Unit):
    symbol: str = 'E'


with open('15.txt', 'r') as file:
    lines = file.read().splitlines()
    initial_cavern = [list(line) for line in lines]

    cavern = [list(line) for line in lines.copy()]
    units = []
    for i in range(len(cavern)):
        for j in range(len(cavern[i])):
            if cavern[i][j] == 'G':
                units.append(Goblin(i,j))
            elif cavern[i][j] == 'E':
                units.append(Elf(i,j))

    elves_win = False
    power = 3
    elves_number = len([unit for unit in units if isinstance(unit, Elf)])
    while not elves_win:
        power += 1
        cavern = [list(line) for line in lines.copy()]
        units = []
        for i in range(len(cavern)):
            for j in range(len(cavern[i])):
                if cavern[i][j] == 'G':
                    units.append(Goblin(i,j))
                elif cavern[i][j] == 'E':
                    units.append(Elf(i,j, attack_power=power))

        target_found = True
        rounds = -1
        while target_found:
            dead = []
            for unit in sorted(units, key=lambda unit: (unit.x, unit.y)):
                if unit.alive:
                    other_units = [other_unit for other_unit in units if type(other_unit) != type(unit) and other_unit.alive]
                    if len(other_units) == 0:
                        target_found = False
                        break
                    path, target = unit.find_nearest_target(other_units, cavern)
                    if path is not None and len(path) > 0:
                        cavern = unit.move_to_next_square(path, cavern)
                    cavern = unit.attack(other_units, cavern)
            rounds += 1
        elves_win = len([unit for unit in units if isinstance(unit, Elf) and unit.alive]) == elves_number and len([unit for unit in units if isinstance(unit, Goblin) and unit.alive]) == 0

    print(f'Elves must have an attack power of {power}')
    sum_of_hit_points = sum([unit.hit_points for unit in units if unit.alive])
    print(f'Number of full rounds {rounds}, sum of hit points {sum_of_hit_points}')
    print(f'Answer {rounds*sum_of_hit_points}')
