import pygame

from base_object import BaseObject
from bullet_class import Bullet


class MyShip(BaseObject):
    def __init__(self, x, y, velocity, width, height, img_path, controller):
        super().__init__(x, y, velocity, width, height, controller)
        self.img_path = img_path
        self.sprite = pygame.transform.scale(pygame.image.load(self.img_path), (self.width, self.height))
        self.facing_direction = pygame.Vector2(0, 1)

    def update_coords(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_d] and self.is_inbound(self.x + self.velocity, self.y):
            self.x += self.velocity
            self.pos_vector.x += self.velocity
        if keys_pressed[pygame.K_a] and self.is_inbound(self.x - self.velocity, self.y):
            self.x -= self.velocity
            self.pos_vector.x -= self.velocity
        if keys_pressed[pygame.K_s] and self.is_inbound(self.x, self.y + self.velocity):
            self.y += self.velocity
            self.pos_vector.y += self.velocity
        if keys_pressed[pygame.K_w] and self.is_inbound(self.x, self.y - self.velocity):
            self.y -= self.velocity
            self.pos_vector.y -= self.velocity

    def calculate_bullet_vector(self):
        m_x, m_y = pygame.mouse.get_pos()
        mouse_pos_vector = pygame.Vector2(m_x, m_y)
        bullet_movement_vector = (mouse_pos_vector - self.pos_vector).normalize()
        return bullet_movement_vector

    def get_sprite_rotation_angle(self, bullet_movement_vector):
        rotation_angle = self.facing_direction.angle_to(bullet_movement_vector)
        self.facing_direction = bullet_movement_vector
        return rotation_angle

    def is_inbound(self, new_x, new_y):
        check_x = (new_x + self.width <= self.controller.WIN_WIDTH) and (new_x >= 0)
        check_y = (new_y + self.height <= self.controller.WINDOW_HEIGHT) and (new_y >= 0)
        return check_x and check_y

    def fire_bullet(self):
        bl_x, bl_y = self.get_coords_for_new_bullet()
        bullet_movement_vector = self.calculate_bullet_vector()

        bullet = Bullet(bl_x, bl_y, self.controller.BULLET_VELOCITY,
                        self.controller.BL_WIDTH, self.controller.BL_HEIGHT, self.controller, bullet_movement_vector)
        self.controller.game_objects.append(bullet)

    def on_collide(self, other):
        pass

    def destroy(self):
        self.controller.game_objects.remove(self)

    def get_coords_for_new_bullet(self):
        x = self.x + self.width // 2 - self.controller.BL_WIDTH // 2
        y = self.y + self.height
        return x, y

    def draw(self):
        self.controller.window_manager.blit(self.sprite, (self.x, self.y))
