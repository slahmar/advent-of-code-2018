from collections import deque


with open('09.txt', 'r') as file:
    parameters = file.read()
    players = int(parameters[:parameters.index('players')-1])
    last_marble = int(parameters[parameters.index('worth')+6:parameters.index('points')-1])*100
    print(f'{players} players, last marble: {last_marble}')

    player = 0
    marble_index = 0
    marble = 0
    marbles = deque([marble])  
    score = {}      
    while marble < last_marble:
        marble += 1
        player = player%(players)+1
        if marble % 23 == 0:
            #print(f'Marble {marble} is a multiple of 23')
            if player not in score:
                score[player] = 0
            score[player] += marble
            marbles.rotate(7)
            score[player] += marbles.pop()
            marbles.rotate(-1)
            #print(f'Player {player} has now {score[player]} points')
        else:
            marbles.rotate(-1)
            marbles.append(marble)
    print(f'High score {sorted(score.values())[-1]}')

