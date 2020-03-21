########################
# This file contains the Game class
# Written by Koen den Hertog

from Board import BoardClass
import pygame
import time
from settings import screenwidth, screenheight, fullscreen
from PygameUtil import create_window

class Game:

    def __init__(self, boardtype, filename=None, filetype=None):          
        self.Board = BoardClass(boardtype, filename, filetype)
        self.screen = create_window(screenwidth, screenheight, fullscreen)
        self.Board.draw(self.screen)

    def run(self):
        run = True

        while run:

            self.Board.update()
            self.Board.draw(self.screen)
            
            # Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            # Determine if the escape key has been pressed for quitting the game
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
            
            #time.sleep(.25)