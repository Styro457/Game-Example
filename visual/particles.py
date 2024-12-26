from objects.base import Object
from pygame.math import Vector2
import math, data

class Particle(Object) :

    def __init__(self, position, size, color, direction, speed, shrinking_speed, parent) :
        super(Particle, self).__init__(position, size, color=color, parent=parent)
        self.direction = direction
        self.speed = speed
        self.shrinking_speed = shrinking_speed

    def update(self) :
        self.position += self.direction * self.speed * data.delta_time
        self.size -= Vector2(1, 1) * self.shrinking_speed * data.delta_time
        if self.size.x < 0 or self.size.y < 0 :
            self.kill()
            return
        self.update_graphics()

def spawn_particle(position, amount,
                   angle = math.pi*2 ,direction=Vector2(1, 0),
                   color=(255, 0, 0), size = Vector2(5, 5), speed = 0.1, shrinking_speed = 0.01,
                   parent = None) :
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
        Particle(position.copy(), size, color, final_direction, speed, shrinking_speed, parent)