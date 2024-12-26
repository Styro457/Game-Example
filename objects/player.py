from objects.base import Object

from pygame.math import Vector2

import math, data, pygame, constants
import visual.particles as particles
import visual.effects as effects

class Player(Object):

    shot = False
    speed = 2

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        for key, direction in constants.key_controls.items():
            if pressed_keys[key]:
                old_position = self.position
                self.set_position(self.position + constants.directions[direction] * data.delta_time * self.speed)
                if not data.screen.get_rect().colliderect(self.rect):
                    self.set_position(old_position)
                else:
                    for obj in data.objects:
                        if obj.layer == constants.layers["objects"] and self.rect.colliderect(obj.rect):
                            self.set_position(old_position)
                            break

        if pygame.mouse.get_pressed()[0]:
            if not self.shot:
                self.shoot((Vector2(pygame.mouse.get_pos())-self.position).normalize())
                self.shot = True
        elif self.shot:
            self.shot = False

    def shoot(self, direction):
        Bullet(self.position.copy(), direction, 1)
        particles.spawn_particle(direction*15, 4, math.pi/4, direction,
                       (255, 158, 68), Vector2(20, 20), 0.1, 0.015, parent=self)
        effects.camera_shake(5,  100)

    def kill(self):
        data.gameOn = False

# Bullet class
# When it hits an enemy, it kills itself and the enemy
class Bullet(Object):

    direction = Vector2(0, 0)

    def __init__(self, position, direction, speed = 0.1):
        size = Vector2(10, 10)

        super(Bullet, self).__init__(position, size, color=data.color_scheme["bullet"])

        self.speed = speed
        self.direction = direction

    def update(self):
        self.set_position(self.position + self.direction * self.speed * data.delta_time)

        if not data.screen.get_rect().colliderect(self.rect):
            self.kill()

        for obj in data.objects:
            if obj.layer == constants.layers["enemies"]:
                if self.rect.colliderect(obj.rect):
                    self.kill()
                    obj.kill()
                    break
            elif obj.layer == constants.layers["objects"] and self.rect.colliderect(obj.rect):
                self.kill()
                break

class Gun(Object):

    distance = 15

    def update(self):
        self.position = (pygame.mouse.get_pos()-self.abs_position()).normalize()*self.distance
        self.update_graphics()