import pygame, math
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

# Bullet class
# When it hits an enemy, it kills itself and the enemy
class Bullet(Object):

    direction = Vector2(0, 0)

    def __init__(self, position, direction, speed = 0.1):
        size = Vector2(10, 10)

        super(Bullet, self).__init__(position, size, color=(25, 25, 25))

        self.direction = (direction-position).normalize() * speed

    def update(self):
        self.set_position(self.position + self.direction * data.delta_time)

        if not data.screen.get_rect().colliderect(self.rect):
            self.kill()

        for obj in data.objects:
            if obj.layer == data.layers["enemies"] and self.rect.colliderect(obj.rect):
                self.kill()
                obj.kill()
                break

class Particle(Object) :

    def __init__(self, position, size, color, direction, speed, shrinking_speed) :
        super(Particle, self).__init__(position, size, color=color)
        self.direction = direction
        self.speed = speed
        self.shrinking_speed = shrinking_speed

    def update(self) :
        self.position += self.direction * self.speed * data.delta_time
        self.size -= Vector2(1, 1) * self.shrinking_speed * data.delta_time
        self.update_graphics()
        if self.size.x < 0 or self.size.y < 0 :
            self.kill()

def spawn_particle(position, amount):
    for i in range(amount):
        angle = 2 * math.pi * i / amount  # Angle in radians
        Particle(position, Vector2(20, 20), (255, 0, 0), Vector2(math.cos(angle), math.sin(angle)), 0.2, 0.05)

