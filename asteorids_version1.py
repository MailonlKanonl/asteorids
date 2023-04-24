from microbit import *
import time
import random

x = 2
xr = random.randint(0,4)
y = 0
i = 0

while True:
    #Mein Schiff
    display.set_pixel(x, 4, 9)

    #Bewegung von Mein Schiff nach linggs
    if button_a.is_pressed() == True:
        display.set_pixel(x, 4, 0)
        x -= 1
        if x < 0:
            x = 0

    #Bewegung von Mein Schiff nach rechts
    if button_b.is_pressed() == True:
        display.set_pixel(x, 4, 0)
        x += 1
        if x > 4:
            x = 4
    time.sleep(0.1)

    #Flüügende Brocke
    display.set_pixel(xr, y, 3)
    i += 1
    if i == 15:
        y += 1
        i = 0
        display.set_pixel(xr, y-1, 0)
        if y >= 5:
            y = 0
            xr = random.randint(0,4)

    #If Mein Schiff trifft auf Flüügende Brocke
    if x == xr and y == 4:
        display.show(Image.SKULL)
        time.sleep(5)
        display.clear()
        x = 2
        xr = random.randint(0,4)
        y = 0
        i = 0

