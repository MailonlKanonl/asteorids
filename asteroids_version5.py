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

asteroids = []

# Class
class Asteroid():
    def __init__(self, ast_x, ast_y, ast_speed, time_last_update):
        self.ast_x = ast_x
        self.ast_y = ast_y
        self.ast_speed = ast_speed
        self.time_last_update = time_last_update

    def update(self):
        current_time = time.ticks_ms()
        if current_time - self.time_last_update > self.ast_speed:
            self.time_last_update = time.ticks_ms()
            self.ast_y += 1
            if self.ast_y > EDGE_Y_DOWN:
                asteroids.pop[a]

while True:

    game_over = False

    #variables
    ship_x = 2
    score = 0 #gets higher after every asteroid you pass

    display.scroll("Press button", SCROLL_DELAY)
    time.sleep(2)
    if button_a.get_presses() > 0 or button_b.get_presses() > 0:
       display.scroll("Let's goo", SCROLL_DELAY)
    else:
        game_over = True

    for i in range(random.randint(0,5)):
        asteroids.append(Asteroid(random.randint(0,4), 0, random.randint(100,500), time.ticks_ms()))

    while game_over != True:

        for a in asteroids:
            a.update()

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
        for a in asteroids:
            if ship_x == a.ast_x and a.ast_y == SHIP_Y:
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
        for a in asteroids:
            display.set_pixel(a.ast_x, a.ast_y, AST_BRIGHTNESS)
        #short sleep
        time.sleep(0.001)
