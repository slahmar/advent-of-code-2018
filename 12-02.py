import re


def apply_notes(state, notes):
    new_state = set()
    for i in range(min(state)-2, max(state)+2):
        nearby = {j-i+2 for j in {j for j in range(i-2,i+3)}.intersection(state)}
        if nearby in notes:
            new_state.add(i)
    return new_state

with open('12.txt', 'r') as file:
    lines = file.read().splitlines()
    state = lines[0][lines[0].index(':')+2:]
    initial_state = {index for index, char in enumerate(state) if char == "#"}
    state = initial_state.copy()    

    notes = lines[2:]
    notes_for_plants = {note[:note.index('=>')-1] for note in notes if note[note.index('=>')+3:] == '#'}
    notes_for_plants = [{index for index in range(len(note)) if note[index] == '#'} for note in notes_for_plants]

    generation = 0
    previous_sum = sum(state)
    while generation < 200:
        state = apply_notes(state, notes_for_plants)
        generation += 1
        print(f'At generation {generation}, delta is {sum(state)-previous_sum}, sum is {sum(state)}')
        previous_sum = sum(state)
    print(f'Answer is {8717+63*(50_000_000_000-124)} after {50_000_000_000} generations')
