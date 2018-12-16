
with open('09.txt', 'r') as file:
    parameters = file.read()
    players = int(parameters[:parameters.index('players')-1])
    last_marble = int(parameters[parameters.index('worth')+6:parameters.index('points')-1])*100
    print(f'{players} players, last marble: {last_marble}')

    player = 0
    marble_index = 0
    marble = 0
    marbles = [marble]  
    score = {}      
    while marble < last_marble:
        marble += 1
        player = player%(players)+1
        if marble % 23 == 0:
            #print(f'Marble {marble} is a multiple of 23')
            if player not in score:
                score[player] = 0
            score[player] += marble
            new_index = (marble_index-7)%len(marbles)
            #print(f'Removing {marbles[new_index]} from game')
            score[player] += marbles[new_index]
            marbles.pop(new_index)
            marble_index = new_index
            #print(f'Player {player} has now {score[player]} points')
        else:
            new_index = (marble_index+1)%len(marbles) +1
            marbles.insert(new_index, marble)
            marble_index = new_index
    print(f'High score {sorted(score.values())[-1]}')

# 52,429
