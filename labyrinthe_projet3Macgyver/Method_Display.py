import pygame
from pygame.locals import *


def display_laby(laby, window, wall, background, exit, player):
    """Method to display the laby."""
    window.blit(background, (0, 0))
    window.blit(
        player.get_sprite(),
        (player.get_coord().get_x() * 30, player.get_coord().get_y() * 30)
        )
    window.blit(
        exit.get_sprite(),
        (exit.get_coord().get_x() * 30, exit.get_coord().get_y() * 30)
        )

    for square in laby:
        if square.get_is_wall() is True:
            window.blit(
                wall, (
                    square.get_coord().get_x() * 30,
                    square.get_coord().get_y() * 30
                    )
                )

        else:
            if square.get_has_item() is True:
                window.blit(
                    square.get_item().get_sprite(),
                    (
                        square.get_coord().get_x() * 30,
                        square.get_coord().get_y() * 30
                        )
                    )
    pygame.display.flip()
