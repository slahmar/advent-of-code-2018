from dataclasses import dataclass
import numpy as np


TURNS = [lambda x,y: (-y,x), lambda x,y: (x,y), lambda x,y: (y,-x)]
CARTS = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
LAST_SYMBOL = {'>':'-', '<':'-', 'v':'|', '^':'|'}

@dataclass
class Cart:
    x: int
    y: int
    symbol: str
    last_turn: int
    last_symbol: str

    def move(self, tracks):
        crash = False
        tracks[self.x][self.y] = self.last_symbol
        facing = CARTS[self.symbol]
        self.last_symbol = tracks[self.x+facing[0]][self.y+facing[1]]
        self.x += facing[0]
        self.y += facing[1]
        next_symbol = tracks[self.x][self.y]
        if next_symbol == '+':
            self.last_turn = (self.last_turn+1)%len(TURNS)
            facing = TURNS[self.last_turn](*facing)
            self.symbol = list(CARTS.keys())[list(CARTS.values()).index(facing)]
        elif next_symbol == '/':
            facing = (-facing[1], -facing[0])
            self.symbol = list(CARTS.keys())[list(CARTS.values()).index(facing)]
        elif next_symbol == '\\':
            facing = (facing[1], facing[0])
            self.symbol = list(CARTS.keys())[list(CARTS.values()).index(facing)]
        elif next_symbol in CARTS:
            crash = True
        tracks[self.x][self.y] = self.symbol
        return crash, tracks



with open('13.txt', 'r') as file:
    tracks = file.read().splitlines()
    tracks = [list(track) for track in tracks]
    carts = []
    for i in range(len(tracks)):
        for j in range(len(tracks[i])):
            if tracks[i][j] in CARTS.keys():
                carts.append(Cart(i,j,tracks[i][j],-1,LAST_SYMBOL[tracks[i][j]]))
    crash = False
    while not crash:
        for cart in sorted(carts, key=lambda cart: cart.x):
            crash, tracks = cart.move(tracks)
            if crash:
                print(f'Crash at {cart.y, cart.x}')
                break
