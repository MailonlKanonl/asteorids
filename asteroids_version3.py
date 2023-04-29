#Asteroids Game
from microbit import *
import time
import random

#CONSTANTS
EDGE_X_RIGHT = 4
EDGE_X_LEFT = 0
EDGE_Y_DOWN = 4
SHIP_Y = 4
SHIP_BRIGHTNESS = 9
AST_BRIGHTNESS = 3
AST_DELAY = 400

#variables
ship_x = 2
ast_x = random.randint(0,4)
ast_y = 0

time_ast_last_update = time.ticks_ms()

while True:
    #get current time
    current_time = time.ticks_ms()

    #update asteroid position
    if current_time - time_ast_last_update > AST_DELAY:
        ast_y += 1
        time_ast_last_update = time.ticks_ms()
        if ast_y > EDGE_Y_DOWN:
            ast_y = 0
            ast_x = random.randint(0,4)

    #update player (button a)
    if button_a.get_presses() > 0:
        ship_x -= 1
        if ship_x < EDGE_X_LEFT:
            ship_x = EDGE_X_LEFT

    #update player (button b)
    if button_b.get_presses() > 0:
        ship_x += 1
        if ship_x > EDGE_X_RIGHT:
            ship_x = EDGE_X_RIGHT

    #collision check
    if ship_x == ast_x and ast_y == SHIP_Y:
        display.show(Image.SKULL)
        time.sleep(5)
        ship_x = 2

    #Update display
    display.clear()
    display.set_pixel(ship_x, SHIP_Y, SHIP_BRIGHTNESS) #update player position
    display.set_pixel(ast_x, ast_y, AST_BRIGHTNESS) #update asteroid position

    #short sleep
    time.sleep(0.01)
