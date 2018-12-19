import re

def fill_state(index_start, state):
    index_start = (index_start + state.index('#')) - 3
    state = '...' + state[state.index('#'):len(state)-state[::-1].index('#')+1] + '...'
    return index_start, state


def apply_notes(state, notes):
    new_state = ['.', '.']
    for i in range(2, len(state)-2):
        nearby = state[i-2:i+3]
        if nearby in notes:
            new_state.append('#')
        else:
            new_state.append('.')
    return ''.join(new_state)

with open('12.txt', 'r') as file:
    lines = file.read().splitlines()
    state = ''.join(lines[0][lines[0].index(':')+2:])
    notes = lines[2:]
    notes_for_plants = [note[:note.index('=>')-1] for note in notes if note[note.index('=>')+3:] == '#']
    generation = 0
    index_start = 0
    while generation < 20:
        index_start, state = fill_state(index_start, state)
        state = apply_notes(state, notes_for_plants)
        generation += 1
    remaining_plants = [index+index_start for index in range(len(state)) if state[index] == '#']
    print(f'Answer is {sum(remaining_plants)} after {generation} generations')
