import re
import string

def get_regex():
    regex = ''
    for index, char in enumerate(string.ascii_uppercase):
        if index != 0:
            regex += '|'
        regex += f'{char}{char.lower()}|{char.lower()}{char}'
    return regex

def get_pattern_matches(polymer):
    return re.findall(r'([a-z])(\1)', polymer, re.IGNORECASE)

with open('05.txt', 'r') as file:
    original_polymer = file.read().rstrip('\n')
    polymer_lengths = []
    for char in string.ascii_uppercase:
        polymer = original_polymer.replace(char, '').replace(char.lower(), '')
        regex = get_regex()
        while re.search(regex, polymer):
            polymer = re.sub(regex, '', polymer)
        polymer_lengths.append(len(polymer))
    print(polymer_lengths)
    print(min(polymer_lengths))

    
