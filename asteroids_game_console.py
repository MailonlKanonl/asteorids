from asteroids_model import Game
import time
import os   
import keyboard

#Illustrations
EDGE_X = "|"
EDGE_Y = "-"
PLAYER = "Δ"
ASTEROID = "*"
PARAGRAPH = "\n"
EMPTY_FIELD = " "

N_X_FIELD = 20
N_Y_FIELD = 5

g = Game(N_X_FIELD,N_Y_FIELD) # create Game object

def button_presses(g):
    if keyboard.is_pressed('left'):
        g.move_player(-1)
    elif keyboard.is_pressed('right'):
        g.move_player(1)
    elif keyboard.is_pressed('enter') and g.run == False:
        g.__init__(N_X_FIELD,N_Y_FIELD)  # init new game

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def coord_to_index(x, y):
    return (y + 1)*(N_X_FIELD + 3) + x + 1

def game_over(g):
    clear_screen()
    print("Game over")
    print("Press <Enter> to play again")
    

def show(g):
    clear_screen()
    #show field
    display_list = []
    for y in range(g.n_y_field+2):
        display_list.append(EDGE_X)
        if y == 0 or y == g.n_y_field + 1:
            for x in range(g.n_x_field):
                display_list.append(EDGE_Y)
        else:
            for x in range(g.n_x_field):
                display_list.append(EMPTY_FIELD)
        display_list.append(EDGE_X)
        display_list.append(PARAGRAPH)

    for asteroid in g.asteroids:
        ast_index = coord_to_index(asteroid.ast_x, asteroid.ast_y)
        display_list[ast_index] = ASTEROID
    
    player_index = coord_to_index(g.player.ship_x, g.player.ship_y)
    display_list[player_index] = PLAYER

    display_string = "".join(display_list)
    print(display_string)

#Game Loop
def game_loop(g):
    while True:
        # call methods of Game object
        button_presses(g)
        if g.run:
            g.spawn_asteroids()
            g.update_asteroids()
            show(g)

            if g.player_is_colliding():
                game_over(g) 

        time.sleep(0.01)
game_loop(g)