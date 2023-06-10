from asteroids_model import Game
import os
import sys
#Illustrations
EDGE_X = "|"
EDGE_Y = "I"
PLAYER = "Δ"
ASTEROID = "*"
PARAGRAPH = "\n"
EMPTY_FIELD = " "

def show(g):
    #clear display
    #clear_screen()

    display = ""

    #show field
    for field_Y in range(g.n_x_field):
        display += EDGE_Y
    for i in range (g.n_y_field):
        display += PARAGRAPH
        display += EDGE_X
        for field_X in range(g.n_x_field - 2):
            display += EMPTY_FIELD
        display += EDGE_X
    display += PARAGRAPH
    for field_Y in range(g.n_x_field):
        display += EDGE_Y

    #show Player
    player_pos = g.player.ship_x + 1 + (g.player.ship_y + 1) * (g.n_x_field + 2)
    display = display[:player_pos] + PLAYER + display[player_pos + 1:]
    print(display)

g = Game(20,5) # create Game object

show(g)