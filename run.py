##################################
# Main file used to run the Game of Life

import pygame
from MainMenu import MainMenu

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption("The Game of Life")
    mainMenu = MainMenu(screen)
    mainMenu.run()