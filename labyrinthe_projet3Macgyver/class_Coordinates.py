import pygame
from pygame.locals import *


class Coordinates:
    """
    Description.

    Class to create an object to stock the coordinates of the various elements.
    """

    def __init__(self, x, y):
        """Constructor. Takes two values to set the coordinates : x and y."""
        self.x = x
        self.y = y

    def get_x(self):
        """Return the x value of the coordinates."""
        return self.x

    def get_y(self):
        """Return the y value of the coordinates."""
        return self.y
