from dataclasses import dataclass


@dataclass
class Nanobot:
    position: tuple
    radius: int

    def distance(self, other):
        return sum([abs(a-b) for (a,b) in zip(self.position, other.position)])
    
    def in_range(self, other):
        return self.distance(other) <= self.radius


with open('23.txt', 'r') as file:
    lines = file.read().splitlines()
    nanobots = [Nanobot(tuple(map(int, line[line.index("<")+1:line.index(">")].split(","))), int(line[line.index("r")+2:])) for line in lines]
    strongest = max(nanobots, key=lambda nanobot: nanobot.radius)
    in_range = 0
    for bot in nanobots:
        if strongest.in_range(bot):
            in_range += 1
    print(f'{in_range} nanobots are in range of the strongest nanobot {strongest}')

        
