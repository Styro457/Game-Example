import random
from pygame import Vector2
import data

amount_left = 0
intensity = 0

def camera_shake(shake_intensity, duration):
    global amount_left, intensity
    intensity = shake_intensity
    amount_left = duration

def camera_shake_update(amount):
        data.camera = Vector2(0, 0) + Vector2(random.uniform(-amount, amount), random.uniform(-amount, amount))

def update():

    global amount_left, intensity

    if amount_left > 0:

        camera_shake_update(intensity)
        amount_left -= data.delta_time
        return True
    else:
        data.camera = Vector2(0, 0)
    return False