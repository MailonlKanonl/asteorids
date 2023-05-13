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
SCROLL_DELAY = 100
SPAWN_DIFFERENCE = 500
SPAWN_PROBABILITY = 50

asteroids = []

# Class
class Asteroid():
    def __init__(self):
        self.ast_x = random.randint(0,4)
        self.ast_y = 0
        self.ast_speed = random.randint(100,2000)
        self.time_last_update = time.ticks_ms()
        self.last_spawn = time.ticks_ms()
        self.is_active = True

    def update(self):
        current_time = time.ticks_ms()
        if current_time - self.time_last_update > self.ast_speed:
            self.time_last_update = time.ticks_ms()
            self.ast_y += 1
            if self.ast_y > EDGE_Y_DOWN:
                self.is_active = False

while True:

    game_over = False

    #variables
    ship_x = 2
    score = 0 #gets higher after every asteroid you pass
    spawn_probability = random.randint(1,100)

    display.scroll("Press button", SCROLL_DELAY)
    time.sleep(2)
    if button_a.get_presses() > 0 or button_b.get_presses() > 0:
       display.scroll("Let's goo", SCROLL_DELAY)
    else:
        game_over = True

    ast = Asteroid()

    while game_over != True:

        #Spawn
        spawn_time = time.ticks_ms()
        if spawn_time - ast.last_spawn > SPAWN_DIFFERENCE and spawn_probability <= SPAWN_PROBABILITY:
            asteroids.append(ast)

        for a in asteroids:
            ast.update()
            if not ast.is_active:
                score += 1
                asteroids.pop(a)

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
        if ship_x == ast.ast_x and ast.ast_y == SHIP_Y:
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
        display.set_pixel(ast.ast_x, ast.ast_y, AST_BRIGHTNESS)
        #short sleep
        time.sleep(0.001)
