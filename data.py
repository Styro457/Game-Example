import pygame

objects = []
screen = None

time, delta_time = 0, 0

layers = {
    "background": 0,
    "objects": 1,
    "player": 3,
    "enemies": 4,
}

def init():
    pygame.init()

    # Define the dimensions of screen object
    global screen
    screen = pygame.display.set_mode((800, 600))

    global time
    time = pygame.time.get_ticks()

def add_object(new_object):
    global objects
    objects.append(new_object)
    return new_object

def remove_object(object_to_remove):
    global objects
    objects.remove(object_to_remove)