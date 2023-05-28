import time
import random
import sys


def get_time_in_ms():
    """
    Time is handled differently on microbit than on regular computers.
    Call this function to get current (system) time.
    """
    if sys.platform == 'microbit':
        return time.ticks_ms()
    return time.time()*1000

class Player:
    def __init__(self, ship_x, ship_y):
        self.ship_x = ship_x
        self.ship_y = ship_y 

    def move(self,move):
        self.ship_x += move

class Asteroid:
    def __init__(self, ast_x, ast_y):
        self.ast_x = ast_x
        self.ast_y = ast_y
        self.ast_speed = random.randint(50,1000)
        self.last_update = get_time_in_ms()
        self.is_active = True
 
    def update(self, n_y_field):
        """
        if enough time has passed, asteroid's y position increases by 1
        """
        if  get_time_in_ms() - self.last_update > self.ast_speed:
            self.last_update = time.ticks_ms()
            self.ast_y += 1
            if self.ast_y > n_y_field:
                self.is_active = False

class Game:
    def __init__(self, n_x_field, n_y_field): # pass game settings as parameters
        self.n_x_field = n_x_field
        self.n_y_field = n_y_field
        self.spawn_time = 500
        self.last_spawn = get_time_in_ms()
        self.spawn_probability = 40
        self.player = Player(n_x_field//2, n_y_field) # create player and attache to Game-class as attribute
        self.asteroids = [] # also create empty list for asteroids
 
    def spawn_asteroids(self):
        """
        Checks if enough time has passed s.t. new asteroid is allowed to spawn.
        If it is, new asteroid spawns with given probability
        """
        if  get_time_in_ms() - self.last_spawn > self.spawn_time:
            self.last_spawn = get_time_in_ms()
            if len(self.asteroids) < self.n_x_field and random.randint(0, 100) <= self.spawn_probability:
                self.asteroids.append(Asteroid(random.randint(0, self.n_x_field), 0))
 
    def update_asteroids(self):
        """
        updates position of all asteroids
        """
        for asteroid in self.asteroids:
            asteroid.update(4)
            if not asteroid.is_active:
                self.asteroids.pop(self.asteroids.index(asteroid))
 
    def player_is_colliding(self):
        """
        checks if player is colliding with an asteroid
        returns False or True
        """
        for asteroid in self.asteroids:
            if self.player.ship_x == asteroid.ast_x and self.player.ship_y == asteroid.ast_y:
                return True
