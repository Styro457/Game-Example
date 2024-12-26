import pygame
from pygame import Vector2

import data

# Define our generic object class
# give it all the properties and methods of pygame.sprite.Sprite
class Object(pygame.sprite.Sprite):

    def __init__(self, position, size = Vector2(25, 25), rotation = 0,
                 layer = 0, color = (0, 200, 255)):
        super(Object, self).__init__()
        data.add_object(self)

        self.position = position
        self.size = size
        self.rotation = rotation
        self.layer = layer
        self.color = color

        self.surf, self.rect = None, None
        self.update_graphics()

    def update(self):
        pass

    def draw(self):
        data.screen.blit(self.surf, self.rect.topleft)

    def kill(self):
        data.remove_object(self)

    def update_graphics(self):
        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center=self.position)

    def set_position(self, position):
        self.position = position
        self.update_graphics()

    def set_rotation(self, rotation):
        self.rotation = rotation
        self.update_graphics()

    def set_size(self, size):
        self.size = size
        self.update_graphics()

class Bullet(Object):

    direction = Vector2(0, 0)

    def __init__(self, position, direction):
        super(Bullet, self).__init__(position)
        self.direction = direction

    def update(self):
        self.position += self.direction