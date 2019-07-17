########################
# This file contains the Game class
# Written by Koen den Hertog

from Board import BoardClass
import pygame
from settings import screenwidth, screenheight

class Game:

    def __init__(self, boardtype):          
        self.Board = BoardClass(boardtype)
        self.screen = pygame.display.set_mode((screenwidth, screenheight))
        pygame.display.set_caption("The Game of Life")
        self.Board.draw(self.screen)

    def run(self):
        run = True

        while run:

            self.Board.update()
            self.Board.draw(self.screen)
            
            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False