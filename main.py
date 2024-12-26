import pygame

# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *
from pygame.math import Vector2

from objects import Object, Bullet
import data

data.init()

# instantiate all square objects
player = Object(Vector2(800/2, 600/2))
player.layer = data.layers["player"]

Object(Vector2(50, 70), color=(255, 0, 0), layer=data.layers["enemies"])
Object(Vector2(500, 550), color=(255, 0, 0), layer=data.layers["enemies"])
Object(Vector2(600, 400), color=(255, 0, 0), layer=data.layers["enemies"])
Object(Vector2(60, 400), color=(255, 0, 0), layer=data.layers["enemies"])
Object(Vector2(700, 200), color=(255, 0, 0), layer=data.layers["enemies"])

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

        elif event.type == MOUSEBUTTONDOWN:
            Bullet(player.position.copy(), pygame.mouse.get_pos(), 1)

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