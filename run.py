##################################
# Main file used to run the Game of Life

import pygame
from MainMenu import MainMenu
from settings import screenwidth, screenheight, fullscreen
from PygameUtil import create_window

if __name__ == "__main__":
    pygame.init()
    screen = create_window(screenwidth,screenheight,fullscreen)
    mainMenu = MainMenu(screen)
    mainMenu.run()