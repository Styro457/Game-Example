import pygame
from pygame.locals import *
from pygame.math import Vector2

import data, constants
from objects.enemy import EnemySpawner
from objects.player import Player, Gun
from objects.base import Text
import visual.effects as effects

data.init()

data.player = Player(Vector2(data.width/2, data.height/2), color=data.color_scheme["player"])
data.player.layer = constants.layers["player"]
gun = Gun(Vector2(0, 0), Vector2(15, 15), color=data.color_scheme["gun"])
gun.parent = data.player
gun.distance = 15

EnemySpawner(data.color_scheme["enemies"])

data.score_display = Text(Vector2(data.width/2, 20), "Score: 0", size=20, color=data.color_scheme["ui"])

background = data.color_scheme["background"]

while data.gameOn:
    data.delta_time = pygame.time.get_ticks() - data.time
    data.time = pygame.time.get_ticks()

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE:
                data.gameOn = False

        # Check for QUIT event
        elif event.type == QUIT:
            data.gameOn = False

    # Draw background
    data.screen.fill(background)

    effects.update()

    # Update all objects
    for obj in data.objects:
        obj.update()

    # Draw all objects
    for obj in data.objects:
        obj.draw()

    # Update the display using flip
    pygame.display.flip()
print("Game Over! Score: " + str(data.score))
