import pygame


class BaseObject(pygame.Rect):
    def __init__(self, x, y, velocity, width, height, controller):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.velocity = velocity
        self.controller = controller
        self.pos_vector = pygame.Vector2(x + width // 2, y + height // 2)

    def on_collide(self, other):
        pass

    def destroy(self):
        self.controller.game_objects.remove(self)

    def update_coords(self):
        pass