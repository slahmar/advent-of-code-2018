from dataclasses import dataclass
import re


@dataclass
class Group:
    nb_units: int
    hit_points: int
    weaknesses: list
    immunities: list
    attack_damage: int
    attack_type: str
    initiative: int
    infectious: bool
    target_index: int = None
    targeted: bool = False

    @property
    def effective_power(self):
        return self.nb_units * self.attack_damage

    def damage_to(self, other_group):
        damage = self.effective_power
        if self.attack_type in other_group.weaknesses:
            damage *= 2
        elif self.attack_type in other_group.immunities:
            damage = 0
        return damage

    def receive_damage(self, damage):
        print(f'{self.hit_points} receives {damage} and loses {min(self.nb_units, damage // self.hit_points)} units')
        self.nb_units -= min(self.nb_units, damage // self.hit_points)  

    def reset_targets(self):
        self.target_index = None
        self.targeted = False    


def parse_group(description, infectious):
    match = re.search('([0-9]+) units each with ([0-9]+) hit points ?(?:\(([ ,;\w]*)\))? with an attack that does ([0-9]+) (\w+) damage at initiative ([0-9]+)', description)
    immunities = []
    weaknesses = []
    if match[3] is not None:
        immunities_and_weaknesses = match[3].split(';')

        for element in immunities_and_weaknesses:
            if element.find('immune to') != -1:
                immunities = element[element.index('to')+3:].split(', ')
            elif element.find('weak to') != -1:
                weaknesses = element[element.index('to')+3:].split(', ')

    return Group(int(match[1]), int(match[2]), weaknesses, immunities, int(match[4]), match[5], int(match[6]), infectious)
    

with open("24.txt", 'r') as file:
    content = file.read()
    parts = content.split(':\n')
    immune_system = parts[1][:parts[1].index("Infection")-1].splitlines()
    infection = parts[2].splitlines()
    groups = [parse_group(desc, False) for desc in immune_system]
    groups.extend([parse_group(desc, True) for desc in infection])
    
    while not all(group.infectious == groups[0].infectious for group in groups):
        for group in sorted(groups, key=lambda g: (-g.effective_power, -g.initiative)):
            max_damage = 0
            possible_targets = []
            for other in groups:
                if other.infectious != group.infectious and not other.targeted:
                    damage = group.damage_to(other)
                    print(f'group {group.hit_points} would deal {damage} to {other.hit_points}')
                    if damage > max_damage:
                       max_damage = damage
                       possible_targets = [other]
                    elif damage == max_damage:
                       possible_targets.append(other)
            if max_damage > 0:
                target = max(possible_targets, key=lambda t: (t.effective_power, t.initiative))
                group.target_index = groups.index(target)
                target.targeted = True

        print('\n\n')

        for group in sorted(groups, key=lambda g: -g.initiative):
            if group.nb_units > 0 and group.target_index is not None:
                target = groups[group.target_index]
                print(f'group {group.hit_points} attacks {target.hit_points} and deals {group.damage_to(target)}')
                target.receive_damage(group.damage_to(target))
            group.reset_targets()

        groups = [group for group in groups if group.nb_units > 0]
         
    print(f'Winning army has {sum([group.nb_units for group in groups])} units')
                    
