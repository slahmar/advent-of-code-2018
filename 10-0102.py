import re
from dataclasses import dataclass
import matplotlib.pyplot as plt


@dataclass
class MovingPoint:
    x: int
    y: int
    v_x: int
    v_y : int
    
    def move(self):
        self.x += self.v_x
        self.y += self.v_y

    def reverse(self):
        self.x -= self.v_x
        self.y -= self.v_y


def draw(points):
    plt.scatter(*zip(*[(point.x, point.y) for point in points]))
    plt.show()
    

with open('10.txt', 'r') as file:
    lines = file.readlines()
    matches = [re.match(r'position=<[ ]*(-*[0-9]+),[ ]*(-*[0-9]+)> velocity=<[ ]*(-*[0-9]+),[ ]*(-*[0-9]+)>', line) for line in lines]
    points = [MovingPoint(int(match.group(1)), -int(match.group(2)), int(match.group(3)), -int(match.group(4))) for match in matches]
    second = 0
    max_y = max([point.y for point in points])
    min_y = min([point.y for point in points])
    previous_max_y = max_y+1
    previous_min_y = min_y-1
    while max_y < previous_max_y and min_y > previous_min_y:
        previous_max_y = max_y
        previous_min_y = min_y
        for point in points:
            point.move()
        max_y = max([point.y for point in points])
        min_y = min([point.y for point in points])
        second += 1
    for point in points:
        point.reverse()
    draw(points)
    print(f'Second {second-1}')

    

    
