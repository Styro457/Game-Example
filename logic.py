import pygame
from pygame import Vector2
from pygame.locals import *
import random

pygame.init()
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

surface = pygame.Surface((40, 40))

pygame.display.set_caption('window')

class Base():
    def __init__(self, x, y, velocity, size):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.size = size

    def draw(self):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.size, self.size))

    
class Player(Base):
    def __init__(self, x, y, velocity, size):
        super().__init__(x, y, velocity, size)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.velocity
            print("a press")
        if keys[pygame.K_d]:
            self.x += self.velocity
        if keys[pygame.K_s]:
            self.y += self.velocity
        if keys[pygame.K_w]:
            self.y -= self.velocity
    
class Enemy(Base):
    def __init__(self, x, y, velocity, size):
        super().__init__(x, y, velocity, size)
        self.position = pygame.Rect((self.x, self.y, self.size, self.size))
    
    def spawn(self):
        self.x = random.randint(random.randint(WINDOWWIDTH), WINDOWHEIGHT)
        self.y = random.randint(random.randint(WINDOWWIDTH), WINDOWHEIGHT)
        self.position = pygame.Rect((self.x, self.y, self.size, self.size))


player = Player(400, 300, 5, 40)

gamerun = True
while gamerun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False
    
    player.move()
    player.draw()
    pygame.display.update()

    window.fill((0, 0, 0))

pygame.quit()