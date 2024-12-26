from pygame.math import Vector2
from pygame.locals import *

layers = {
    "background": 0,
    "objects": 1,
    "player": 3,
    "enemies": 4,
    "ui": 6
}

directions = {
    "up": Vector2(0, -0.1),
    "down": Vector2(0, 0.1),
    "left": Vector2(-0.1, 0),
    "right": Vector2(0.1, 0),
}

key_controls = {
    K_w: "up",
    K_s: "down",
    K_a: "left",
    K_d: "right",
}

zero = Vector2(0, 0)

color_schemes = [
    {
        "background": (255, 255, 255),
        "player": (0, 200, 255),
        "gun": (0, 0, 0),
        "bullet": (25, 25, 25),
        "enemies": (150, 0, 0),
        "ui": (0, 0, 0)
    },
    {
        "background": (50, 50, 50),
        "player": (0, 120, 255),
        "gun": (10, 10, 10),
        "bullet": (20, 20, 20),
        "enemies": (255, 80, 0),
        "ui": (200, 200, 200)
    },
    {
        "background": (240, 248, 255),
        "player": (0, 150, 200),
        "gun": (30, 30, 30),
        "bullet": (50, 50, 50),
        "enemies": (200, 50, 0),
        "ui": (20, 20, 20)
    },
    {
        "background": (0, 0, 0),
        "player": (0, 170, 255),
        "gun": (15, 15, 15),
        "bullet": (50, 50, 50),
        "enemies": (255, 60, 20),
        "ui": (180, 180, 180)
    },
    {
        "background": (255, 239, 213),
        "player": (0, 130, 230),
        "gun": (10, 10, 10),
        "bullet": (40, 40, 40),
        "enemies": (255, 69, 0),
        "ui": (20, 20, 20)
    },
    {
        "background": (240, 240, 240),
        "player": (0, 100, 255),
        "gun": (20, 20, 20),
        "bullet": (40, 40, 40),
        "enemies": (220, 0, 0),
        "ui": (0, 0, 0)
    },
    {
        "background": (50, 50, 100),
        "player": (0, 200, 255),
        "gun": (0, 0, 0),
        "bullet": (30, 30, 30),
        "enemies": (255, 100, 0),
        "ui": (220, 220, 220)
    },
    {
        "background": (255, 250, 240),
        "player": (0, 150, 240),
        "gun": (5, 5, 5),
        "bullet": (15, 15, 15),
        "enemies": (255, 80, 30),
        "ui": (20, 20, 20)
    }
]