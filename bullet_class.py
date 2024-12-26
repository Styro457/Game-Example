from base_object import BaseObject
import pygame

class Bullet(BaseObject):
    def __init__(self, x, y, velocity, width, height, controller, movement_vector):
        super().__init__(x, y, velocity, width, height, controller)
        self.color = (255, 255, 255)
        self.movement_vector = movement_vector

    def draw(self):
        pygame.draw.rect(self.controller.window_manager, self.color, self)

    def update_coords(self):
        self.pos_vector += self.movement_vector * self.velocity
        self.x = self.pos_vector.x
        self.y = self.pos_vector.y

    def on_collide(self, other):
        pass

    def destroy(self):
        self.controller.game_objects.remove(self)
