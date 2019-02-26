import random
import pygame
from pygame.locals import *
from class_Coordinates import *


def random_coordinates():
    """Method to get random coordinates.
    Returns a Coordinates type object."""
    return Coordinates(random.randint(0, 14), random.randint(0, 14))


def put_item_in_laby(laby, item, player, exit):
    """Method to put the items in the laby,
    at random position"""
    for square in laby:
        if (
            square.get_coord().get_x() ==
            item.get_coord().get_x() and
            square.get_coord().get_y() ==
            item.get_coord().get_y()
                ):
            if (
                item.get_coord().get_x() !=
                exit.get_coord().get_x() and
                item.get_coord().get_y() !=
                exit.get_coord().get_y()
                ) and (
                item.get_coord().get_x() !=
                player.get_coord().get_x() and
                item.get_coord().get_y() !=
                player.get_coord().get_y()
                    ):
                if square.get_has_item() is True:
                    item.set_coord(random_coordinates())
                    put_item_in_laby(laby, item, player, exit)
                    break
                if square.get_is_wall() is True:
                    item.set_coord(random_coordinates())
                    put_item_in_laby(laby, item, player, exit)
                    break
                if (
                    square.get_is_wall()
                    is False and square.get_has_item() is False
                        ):
                    square.set_has_item(True)
                    square.set_item(item)
                    break
            else:
                item.set_coord(random_coordinates())
                put_item_in_laby(laby, item, player, exit)
                break

    return laby
