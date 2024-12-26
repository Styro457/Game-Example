import pygame
from base_object import BaseObject


class Target(BaseObject):
    def __init__(self, x, y, velocity, width, height, controller, ship_obj):
        super().__init__(x, y, velocity, width, height, controller)
        self.color = (255, 255, 255)
        self.ship_obj = ship_obj
        self.update_movement_vector()

    def draw(self):
        pygame.draw.rect(self.controller.window_manager, self.color, self)

    def on_collide(self, other):
        self.destroy()
        self.controller.create_random_target()

    def update_coords(self):
        self.update_movement_vector()
        self.pos_vector += self.movement_vector * self.velocity
        self.x = self.pos_vector.x
        self.y = self.pos_vector.y

    def destroy(self):
        self.controller.game_objects.remove(self)

    def update_movement_vector(self):
        self.movement_vector = (self.ship_obj.pos_vector - self.pos_vector).normalize()
