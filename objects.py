import pygame, math
from pygame import Vector2

import data
import effects

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
        data.screen.blit(self.surf, self.rect.topleft - data.camera)

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

        self.speed = speed
        self.direction = (direction-position).normalize()

        spawn_particle(position+self.direction.normalize()*15, 4, math.pi/4, self.direction,
                       (255, 158, 68), Vector2(20, 20), 0.1, 0.015)
        effects.camera_shake(5,  100)

    def update(self):
        self.set_position(self.position + self.direction * self.speed * data.delta_time)

        if not data.screen.get_rect().colliderect(self.rect):
            self.kill()

        for obj in data.objects:
            if obj.layer == data.layers["enemies"] and self.rect.colliderect(obj.rect):
                spawn_particle(obj.position, 4, size=Vector2(10, 10), color=(150, 40, 40), speed=0.01, shrinking_speed=0.005)
                spawn_particle(obj.position, 12, size=Vector2(6, 6), color=(255, 0, 0), speed=0.1, shrinking_speed=0.001)

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

def spawn_particle(position, amount,
                   angle = math.pi*2 ,direction=Vector2(1, 0),
                   color=(255, 0, 0), size = Vector2(5, 5), speed = 0.1, shrinking_speed = 0.01) :
    direction = direction.copy().normalize()
    for i in range(amount):
        current_angle = angle * i / amount - angle / 2  # Center the arc around 0 angle

        rotation_matrix = [
            [math.cos(current_angle), -math.sin(current_angle)],
            [math.sin(current_angle), math.cos(current_angle)]
        ]
        final_direction = Vector2(
            rotation_matrix[0][0] * direction.x + rotation_matrix[0][1] * direction.y,
            rotation_matrix[1][0] * direction.x + rotation_matrix[1][1] * direction.y
        )
        Particle(position.copy(), size, color, final_direction, speed, shrinking_speed)

class Gun(Object):

    center = Vector2(400, 300)

    def update(self):
        self.position = self.center + (pygame.mouse.get_pos()-self.position).normalize()*15
        self.update_graphics()