import pygame
from pygame.locals import *
from class_Coordinates import *
from class_Item import *


class Square:
    """
    Description.

    A class that will define the squares of the laby.
    """

    def __init__(self, coord, is_wall):
        """Use Coordinates and is_Wall boolean as arguments.
        Starts with no item on it."""
        self.is_wall = is_wall
        self.coord = coord
        self.has_item = False
        self.item = Item(None, 'ressource/empty.png')

    def get_is_wall(self):
        """Return a boolean to know if the square is a wall."""
        return self.is_wall

    def get_has_item(self):
        """Return a boolean to know if there's an item on the square."""
        return self.has_item

    def set_has_item(self, state):
        """Set the state of the has_item boolean."""
        self.has_item = state

    def get_coord(self):
        """Return the square's position as a Coordinate type object."""
        return self.coord

    def set_item(self, item):
        """Change the Item attribute of the square.
        Uses an Item type object."""
        self.item = item

    def get_item(self):
        """Return the item on the square."""
        return self.item
