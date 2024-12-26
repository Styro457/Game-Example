import pygame, math
from pygame import Vector2

import data, constants

class Point:

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    def abs_position(self):
        if self.parent:
            return self.position + self.parent.abs_position()
        return self.position

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    def __init__(self, position = Vector2(0, 0), rotation = 0, parent = None, layer = 0):
        self._position = position
        self._rotation = rotation
        self._parent = parent
        self.layer = layer
        data.add_object(self)


    def update(self):
        pass

    def draw(self):
        pass

    def update_graphics(self):
        pass

    def set_position(self, position):
        self.position = position
        self.update_graphics()

    def set_rotation(self, rotation):
        self.rotation = rotation
        self.update_graphics()

    def kill(self):
        data.remove_object(self)

    def get_camera_offset(self):
        return data.camera if self.layer != constants.layers["ui"] else constants.zero

# Define our generic object class
# give it all the properties and methods of pygame.sprite.Sprite
class Object(pygame.sprite.Sprite, Point):

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    def __init__(self, position = Vector2(0, 0), size = Vector2(25, 25), rotation = 0,
                 parent = None,
                 layer = 0, color = (0, 200, 255)):
        super(Object, self).__init__()
        Point.__init__(self, position, rotation, parent, layer)

        self._size = size
        self.color = color

        self.surf, self.rect = None, None
        self.update_graphics()

    def draw(self):
        data.screen.blit(self.surf, self.rect.topleft - self.get_camera_offset())

    def update_graphics(self):
        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center=self.abs_position())

    def set_size(self, size):
        self.size = size
        self.update_graphics()

    def kill(self):
         data.remove_object(self)

class Text(Point):

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.update_graphics()

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value
        self.update_graphics()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.update

    @property
    def align(self):
        return self._align

    @align.setter
    def align(self, value):
        self._align = value
        self.update_graphics()

    def __init__(self, position = Vector2(0, 0),
                 text = "", font = None, size = 36, color = (0, 0, 0), align = "center",
                 parent = None, layer = constants.layers["ui"]):
        Point.__init__(self, position, parent=parent, layer=layer)
        self._text = text
        self._font = pygame.font.Font(font, size)
        self._color = color
        self.surf, self.rect = None, None
        self._align = align
        self.update_graphics()

    def update_graphics(self):
        self.surf = self.font.render(self.text, True, self.color)
        if self.align == "center":
            self.rect = self.surf.get_rect(center=self.abs_position())
        elif self.align == "left":
            self.rect = self.surf.get_rect(topleft=self.abs_position())
        elif self.align == "right":
            self.rect = self.surf.get_rect(topright=self.abs_position())

    def draw(self):
        data.screen.blit(self.surf, self.rect.topleft - self.get_camera_offset())
