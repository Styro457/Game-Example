from pygame import Vector2

import constants, data, pygame, random
import visual.particles as particles
import visual.effects as effects
from objects.base import Object, Point


class Enemy(Object):

    def __init__(self, position, speed, target=None, color=(150, 0, 0)):
        super(Enemy, self).__init__(position, color=color, layer=constants.layers["enemies"])
        self.speed = speed
        self.target = target

    def update(self):
        if self.target:
            direction = (self.target.position - self.position)
            if direction != constants.zero:
                direction = direction.normalize()
                self.set_position(self.position + direction * self.speed * data.delta_time)

        if self.rect.colliderect(self.target.rect):
            self.target.kill()

    def kill(self):
        super(Enemy, self).kill()
        particles.spawn_particle(self.position, 4, size=Vector2(10, 10), color=(150, 40, 40), speed=0.01,
                                 shrinking_speed=0.005)
        particles.spawn_particle(self.position, 12, size=Vector2(6, 6), color=(255, 0, 0), speed=0.1,
                                 shrinking_speed=0.001)
        effects.camera_shake(10, 200)
        data.score += 1
        data.score_display.text = "Score: " + str(data.score)


def get_random_location_outside():
    x = 0
    y = 0
    if random.randint(0, 1):
        x = random.choice([0, data.width])
        y = random.randint(0, data.height)
    else:
        x = random.randint(0, data.width)
        y =random.choice([0, data.height])
    return Vector2(x, y)


class EnemySpawner(Point):

    enemy_spawn_counter = 1500
    delay = 2000

    def __init__(self, enemy_color=(150, 0, 0)):
        Point.__init__(self)
        self.enemy_color = enemy_color


    def draw(self):
        pass

    def update(self):
        self.enemy_spawn_counter += data.delta_time
        if self.enemy_spawn_counter > self.delay:
            self.enemy_spawn_counter = 0
            self.delay -= 60
            if self.delay < 500:
                self.delay = 500
            Enemy(get_random_location_outside(), 0.1, data.player, color=self.enemy_color)
