import pygame
from pygame.locals import *
from class_Coordinates import *


class Item:
    """
    Description.

    A class to define the items of the laby.
    """

    def __init__(self, name, sprite):
        """Constructor. Name and sprite (file name) as arguments."""
        self.name = name
        self.got_item = False
        self.coord = Coordinates(None, None)
        self.sprite = pygame.image.load(sprite).convert_alpha()

    def get_coord(self):
        """Return the item's position as a Coordinate type object."""
        return self.coord

    def set_coord(self, coord):
        """Set the item's coordinates.
        Use a Coordinate type object as argument."""
        self.coord = coord

    def get_sprite(self):
        """Return the item"""
        return self.sprite
