from microbit import *
import time
import random

#CONSTANTS
AST_BRIGHTNESS = 3
EDGE_X_RIGHT = 4
EDGE_X_LEFT = 0
EDGE_Y_DOWN = 4
MAX_ASTEROIDS = 6
SCROLL_DELAY = 100
SHIP_BRIGHTNESS = 9
SHIP_Y = 4
SPAWN_DIFFERENCE = 500
SPAWN_PROBABILITY = 40

asteroids = []

# Class Asteroid
class Asteroid():
    def __init__(self):
        self.ast_x = random.randint(0,4)
        self.ast_y = 0
        self.ast_brightness = AST_BRIGHTNESS
        self.ast_speed = random.randint(50,2000)
        self.last_update = time.ticks_ms()
        self.spawn_probability = random.randint(1,100)
        self.is_active = True

    def update(self):
        current_time = time.ticks_ms()
        if current_time - self.last_update > self.ast_speed:
            self.last_update = time.ticks_ms()
            self.ast_y += 1
            if self.ast_y > EDGE_Y_DOWN:
                self.is_active = False

    def display(self):
        display.set_pixel(self.ast_x, self.ast_y, AST_BRIGHTNESS)

class Player():
    def __init__(self):
        self.ship_x = 2
        self.ship_y = SHIP_Y
        self.ship_brightness = SHIP_BRIGHTNESS

    def update_a(self):
        self.ship_x -= 1
        if self.ship_x < EDGE_X_LEFT:
            self.ship_x = EDGE_X_LEFT

    def update_b(self):
        self.ship_x += 1
        if self.ship_x > EDGE_X_RIGHT:
            self.ship_x = EDGE_X_RIGHT


    def display(self):
        display.set_pixel(self.ship_x, self.ship_y, SHIP_BRIGHTNESS)

#Game Loop
def game_loop():

    score = 0

    player = Player()

    display.scroll("Press button", SCROLL_DELAY)
    time.sleep(2)
    if button_a.get_presses() > 0 or button_b.get_presses() > 0:
       pass

    while True:
        #asteroid movement
        asteroid = Asteroid()
        if len(asteroids) < MAX_ASTEROIDS and asteroid.spawn_probability <= SPAWN_PROBABILITY:
            asteroids.append(asteroid)
        for asteroid in asteroids:
            asteroid.update()
            if not asteroid.is_active:
                asteroids.pop(asteroids.index(asteroid))
                score += 1


        #update player (button a)
        if button_a.get_presses() > 0:
            player.update_a()

        #update player (button b)
        if button_b.get_presses() > 0:
            player.update_b()

        #collision check and game over
        for asteroid in asteroids:
            if player.ship_x == asteroid.ast_x and player.ship_y == asteroid.ast_y:
                game_over(score)

        #Update display
        display.clear()
        for asteroid in asteroids:
            asteroid.display()
        player.display()
        time.sleep(0.001)

#Game Over
def game_over(score):
    display.show(Image.SAD)
    time.sleep(2)
    display.scroll("Game over", SCROLL_DELAY)
    display.scroll("Your score: {0}".format(score), SCROLL_DELAY)
    time.sleep(2)
    game_loop()

game_loop()
