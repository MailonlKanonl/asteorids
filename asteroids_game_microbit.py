from microbit import *
from asteroids_model import Game

AST_BRIGHTNESS = 4
SHIP_BRIGHTNESS = 9
SCROLL_DELAY = 100

def show(g):
    """
    Takes game object (instance of Game class) and visualizes it on microbit's led-matrix.
    """
    display.clear()
    for asteroid in g.asteroids:
        display.set_pixel(asteroid.ast_x, asteroid.ast_y, AST_BRIGHTNESS)
    display.set_pixel(g.player.ship_x, g.player.ship_y, SHIP_BRIGHTNESS)
 
g = Game(4,4) # create Game object

#Game Loop
def game_loop():
    
    while True:
        # call methods of Game object
        g.spawn_asteroids()
        g.update_asteroids()
        if button_a.get_presses() > 0:
            g.player.move(-1)
        if button_b.get_presses() > 0:
            g.player.move(1)
        if g.player_is_colliding() == True:
            #game over
            pass
        show(g)
        time.sleep(0.001)
def game_over():
    display.show(Image.SAD)
    time.sleep(2)
    display.scroll("Game over", SCROLL_DELAY)
    time.sleep(2)
    if button_a.get_presses() > 0 or button_b.get_presses() > 0:
        game_loop()

game_loop()