"""Pygame importation."""
import pygame
from pygame.locals import *
from class_Coordinates import *


class MacGyver:
    """
    Description.

    A class to define the attributes of Macgyver.
    """

    def __init__(self):
        """Constructor. Sets blank coordinates and 'player.png' as sprite."""
        self.coord = Coordinates(None, None)
        self.sprite = pygame.image.load(
            'ressource/MacGyver.png'
            ).convert_alpha()

    def get_coord(self):
        """Return Macgyver's position as a Coordinate type object."""
        return self.coord

    def set_coord(self, coord):
        """Set Macgyver's coordinates.
        Uses a Coordinate type object as argument."""
        self.coord = coord

    def get_sprite(self):
        """Return macgyver's sprite."""
        return self.sprite


class Guardian():
    """
    Description.

    A class for the Guardian.
    Same as Macgyver, but wanted to create one because it
    will be easier for future customization.
    """

    def __init__(self):
        """Constructor. Sets blank coordinates and 'exit.png' as sprite."""
        self.coord = Coordinates(None, None)
        self.sprite = pygame.image.load('ressource/exit.png').convert_alpha()

    # Getsetters
    def get_coord(self):
        """Return the exit's position as a Coordinate type object."""
        return self.coord

    def set_coord(self, coord):
        """Set the exit's coordniates.
        Uses a Coordinate type object as argument."""
        self.coord = coord

    def get_sprite(self):
        """Return exit's sprite."""
        return self.sprite


