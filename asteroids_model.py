import time
import random
import sys


def get_time_in_ms():
    if sys.platform == 'microbit':
        try:
            return time.ticks_ms()
        except Exception as e:
            print("An error occurred on microbit:", str(e))
    else:
        try:
            return time.time()*1000
        except Exception as e:
            print("An error occurred on Windows/Mac/Linux/... (not microbit):", str(e))
            
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
        if  get_time_in_ms() - self.last_update > self.ast_speed:
            self.last_update = get_time_in_ms()
            self.ast_y += 1
            if self.ast_y > n_y_field:
                self.is_active = False

class Game:
    def __init__(self, n_x_field, n_y_field): # pass game settings as parameters
        self.n_x_field = n_x_field
        self.n_y_field = n_y_field
        self.run = True
        self.spawn_time = 500
        self.last_spawn = get_time_in_ms()
        self.spawn_probability = 40
        self.player = Player(n_x_field//2, n_y_field-1) # create player and attache to Game-class as attribute
        self.asteroids = [] # also create empty list for asteroids
 
    def spawn_asteroids(self):
        if  get_time_in_ms() - self.last_spawn > self.spawn_time:
            self.last_spawn = get_time_in_ms()
            if len(self.asteroids) < self.n_x_field and random.randint(0, 100) <= self.spawn_probability:
                self.asteroids.append(Asteroid(random.randint(0, self.n_x_field-1), 0))
 
    def update_asteroids(self):
        for asteroid in self.asteroids:
            asteroid.update(4)
            if not asteroid.is_active:
                self.asteroids.pop(self.asteroids.index(asteroid))
 
    def player_is_colliding(self):
        for asteroid in self.asteroids:
            if self.player.ship_x == asteroid.ast_x and self.player.ship_y == asteroid.ast_y:
                self.run = False
                return True
        return False
            
    def move_player(self, move):
        if self.player.ship_x > 0 and move == -1:
            self.player.move(move)
        
        elif self.player.ship_x < self.n_x_field-1 and move == 1:
            self.player.move(move)
