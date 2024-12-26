import pygame, random
from pygame.math import Vector2
import constants

objects = []
screen = None
width, height = 800, 600
time, delta_time = 0, 0
gameOn = True

player = None
score = 0
score_display = None
camera = Vector2(0, 0)

color_scheme = constants.color_schemes[0]

def init(w=800, h=600):
    pygame.init()

    global gameOn, screen, time, width, height, color_scheme
    width, height = w, h
    gameOn = True
    screen = pygame.display.set_mode((width, height))
    time = pygame.time.get_ticks()

    color_scheme = constants.color_schemes[0] if check_if_its_first_time_playing() else random.choice(constants.color_schemes)

def check_if_its_first_time_playing():
    file_name = "data.txt"
    try:
        with open(file_name, "r"):
            return False
    except FileNotFoundError:
        with open(file_name, "w") as file:
            file.write("T")
        return True

def add_object(new_object):
    global objects
    objects.append(new_object)
    return new_object

def remove_object(object_to_remove):
    global objects
    objects.remove(object_to_remove)