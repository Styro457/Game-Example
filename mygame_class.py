from random import randint

import pygame

from ship_class import MyShip
from target_class import Target


class MyGame():
    WIN_WIDTH, WINDOW_HEIGHT = 700, 700
    WINDOW_TITLE = 'Top-Down Respectfully'
    WINDOW_BG_COLOR = (59, 59, 59)
    FPS = 120
    pygame.display.set_caption(WINDOW_TITLE)

    SP_WIDTH, SP_HEIGHT = 55, 40
    BL_WIDTH, BL_HEIGHT = 5, 5
    TG_WIDTH, TG_HEIGHT = 20, 20

    SHIP_VELOCITY = 5
    BULLET_VELOCITY = 10
    TARGET_VELOCITY = 1

    def __init__(self):
        self.window_manager = pygame.display.set_mode((self.WIN_WIDTH, self.WINDOW_HEIGHT))
        self.game_objects = []
        self.game_running = True
        self.my_ship = MyShip(100, 300, self.SHIP_VELOCITY, self.SP_WIDTH, self.SP_HEIGHT,
                              './Assets/spaceship_yellow.png', self)

    def draw_window(self):
        self.window_manager.fill(self.WINDOW_BG_COLOR)
        for obj in self.game_objects:
            obj.draw()

        pygame.display.update()

    def generate_random_target_coords(self):
        x = randint(100, self.WIN_WIDTH - self.TG_WIDTH - 100)
        y = randint(100, self.WINDOW_HEIGHT - self.TG_HEIGHT - 100)
        return x, y

    def create_random_target(self):
        x, y = self.generate_random_target_coords()
        target = Target(x, y, self.TARGET_VELOCITY, self.TG_WIDTH, self.TG_HEIGHT, self, self.my_ship)
        self.game_objects.append(target)

    def start_game_loop(self):
        self.game_objects.append(self.my_ship)

        in_game_clock = pygame.time.Clock()

        self.create_random_target()

        while self.game_running:
            in_game_clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.my_ship.fire_bullet()

            for obj in self.game_objects:
                obj.update_coords()

            self.check_collisions()

            self.draw_window()

    def check_collisions(self):
        for obj1 in self.game_objects:
            for obj2 in self.game_objects:
                if obj1 != obj2:
                    if obj1.colliderect(obj2):
                        obj1.on_collide(obj1)
                        obj2.on_collide(obj2)
