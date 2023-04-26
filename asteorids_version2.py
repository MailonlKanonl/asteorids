#Asteroids Game
from microbit import *
import time
import random

ship_x = 2
ast_x = random.randint(0,4)
ast_y = 0
last_movement = time.ticks_ms()

while True:
    #My Ship
    display.set_pixel(ship_x, 4, 9)

    #Moves My Ship to the left
    if button_a.get_presses() > 0:
        display.set_pixel(ship_x, 4, 0)
        ship_x -= 1
        if ship_x < 0:
            ship_x = 0

    #Moves My Ship to the right
    if button_b.get_presses() > 0:
        display.set_pixel(ship_x, 4, 0)
        ship_x += 1
        if ship_x > 4:
            ship_x = 4
    time.sleep(0.1)

    #Asteroid
    display.set_pixel(ast_x, ast_y, 3)
    current_time = time.ticks_ms()
    if current_time - last_movement > 500:
        ast_y += 1
        last_movement = current_time
        display.set_pixel(ast_x, ast_y - 1, 0)
        if ast_y >= 5:
            ast_y = 0
            ast_x = random.randint(0,4)

    #My ship collides with Asteroid
    if ship_x == ast_x and ast_y == 4:
        display.show(Image.SKULL)
        time.sleep(5)
        display.clear()
        ship_x = 2
        ast_x = random.randint(0,4)
        ast_y = 0
        last_movement = time.ticks_ms()
