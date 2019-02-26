import pygame
from pygame.locals import *
from class_Square import *
from class_Coordinates import *


def generate_laby(player, exit):
    """
    Method to generate the laby.

    Transforms the .txt file into a list of lines,
    then each line into a list of characters.
    For each character it will generate a square,
    or set Macgyver/exit's position.
    """
    with open('macgyverlaby.txt') as laby:
        str_laby = ''.join(str(line) for line in laby)
        list_str = list(str_laby)
        laby = []
        x = 0
        y = 0

        for entry in list_str:
            # Sets square as a wall if the character is 'm'
            if entry == 'm':
                laby.append(Square(Coordinates(x, y), True))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

            elif entry == 'x':
                # Sets square as empty if the character is 'x'
                laby.append(Square(Coordinates(x, y), False))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

            elif entry == 'd':
                # Sets the inital position of the
                # player if the character is a 'd'
                laby.append(Square(Coordinates(x, y), False))
                player.set_coord(Coordinates(x, y))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

            elif entry == 'a':
                # Sets the position of the exit if the character is a 'a'
                laby.append(Square(Coordinates(x, y), False))
                exit.set_coord(Coordinates(x, y))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

    return laby
