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
AST_SPEED_INCREASE = 50
AST_SPEED_LIMIT = 100
SCROLL_DELAY = 100

while True:

    game_over = False

    #variables
    ship_x = 2
    ast_x = random.randint(0,4)
    ast_y = 0
    ast_delay = 500
    time_till_speeding = 15000 #gets higher after every level
    time_till_speeding_increase = 2000
    score = 0 #gets higher after every asteroid you pass
    level = 1

    display.scroll("Press any button to play", SCROLL_DELAY)
    time.sleep(5)
    if button_a.get_presses() > 0 or button_b.get_presses() > 0:
        display.scroll("Level {0}".format(level), SCROLL_DELAY)

        time_ast_last_update = time.ticks_ms()
        time_ast_speed_update = time.ticks_ms()

        while game_over != True:
            #get current time
            current_time = time.ticks_ms()

            #asteroids speed update
            if current_time - time_ast_speed_update > time_till_speeding:
                level += 1
                time_till_speeding += time_till_speeding_increase
                display.scroll("Level {0}".format(level), SCROLL_DELAY)
                time_ast_speed_update = time.ticks_ms()
                ast_delay -= AST_SPEED_INCREASE
                if ast_delay < AST_SPEED_LIMIT:
                    ast_delay = AST_SPEED_LIMIT

            #update asteroid position
            if current_time - time_ast_last_update > ast_delay:
                ast_y += 1
                time_ast_last_update = time.ticks_ms()
                if ast_y > EDGE_Y_DOWN:
                    ast_y = 0
                    ast_x = random.randint(0,4)
                    score += 1

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

            #collision check and game over
            if ship_x == ast_x and ast_y == SHIP_Y:
                display.show(Image.SAD)
                time.sleep(2)
                display.scroll("Game over", SCROLL_DELAY)
                display.scroll("Your score:", SCROLL_DELAY)
                display.show(score)
                time.sleep(2)
                game_over = True

            #Update display
            display.clear()
            display.set_pixel(ship_x, SHIP_Y, SHIP_BRIGHTNESS) #update player position
            display.set_pixel(ast_x, ast_y, AST_BRIGHTNESS) #update asteroid position

            #short sleep
            time.sleep(0.001)
