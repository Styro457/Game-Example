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
        "background": (255, 255, 255),  # Bright white
        "player": (0, 200, 255),       # Bright cyan
        "gun": (0, 0, 0),              # Black
        "bullet": (25, 25, 25),        # Dark gray
        "enemies": (150, 0, 0),        # Deep red
        "ui": (0, 0, 0)                # Black
    },
    {
        "background": (30, 30, 30),    # Dark gray
        "player": (0, 120, 255),       # Medium blue
        "gun": (10, 10, 10),           # Near black
        "bullet": (50, 50, 50),        # Medium gray
        "enemies": (255, 80, 0),       # Vivid orange
        "ui": (200, 200, 200)          # Light gray
    },
    {
        "background": (250, 240, 230), # Light cream
        "player": (0, 180, 230),       # Light blue
        "gun": (20, 20, 20),           # Very dark gray
        "bullet": (40, 40, 40),        # Dark gray
        "enemies": (200, 30, 0),       # Bright red
        "ui": (10, 10, 10)             # Blackish
    },
    {
        "background": (0, 50, 100),    # Dark navy blue
        "player": (0, 230, 255),       # Bright cyan
        "gun": (15, 15, 15),           # Very dark gray
        "bullet": (35, 35, 35),        # Darker gray
        "enemies": (255, 100, 0),      # Strong orange
        "ui": (220, 220, 220)          # Light gray
    },
    {
        "background": (255, 250, 220), # Pale yellow
        "player": (50, 150, 250),      # Soft blue
        "gun": (5, 5, 5),              # Blackish
        "bullet": (25, 25, 25),        # Dark gray
        "enemies": (255, 60, 10),      # Fiery orange
        "ui": (30, 30, 30)             # Dark gray
    },
    {
        "background": (50, 20, 50),    # Dark purple
        "player": (0, 200, 255),       # Bright cyan
        "gun": (10, 10, 10),           # Almost black
        "bullet": (40, 40, 40),        # Dark gray
        "enemies": (255, 70, 0),       # Warm orange-red
        "ui": (220, 220, 220)          # Light gray
    },
    {
        "background": (20, 40, 60),    # Deep slate blue
        "player": (0, 150, 255),       # Sky blue
        "gun": (15, 15, 15),           # Near black
        "bullet": (35, 35, 35),        # Dark gray
        "enemies": (255, 100, 50),     # Salmon orange
        "ui": (200, 200, 200)          # Light gray
    },
    {
        "background": (220, 230, 240), # Light cool gray
        "player": (0, 140, 230),       # Bright blue
        "gun": (10, 10, 10),           # Blackish
        "bullet": (30, 30, 30),        # Very dark gray
        "enemies": (255, 60, 30),      # Deep orange
        "ui": (20, 20, 20)             # Blackish gray
    }
]