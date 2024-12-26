import pygame

# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *
from pygame.math import Vector2

from objects import Object, Bullet
import data

data.init()

# instantiate all square objects

gameOn = True
# Our game loop
while gameOn:
    data.delta_time = pygame.time.get_ticks() - data.time
    data.time = pygame.time.get_ticks()

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE:
                gameOn = False

        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False

    # Draw background
    data.screen.fill((255, 255, 255))

    # Update all objects
    for obj in data.objects:
        obj.update()

    # Draw all objects
    for obj in data.objects:
        obj.draw()


    # Update the display using flip
    pygame.display.flip()