################################
# Main menu of the Game of Life

import pygame
from PygameUtil import Button, draw_text
from Game import Game
from settings import screenwidth, screenheight

class MainMenu:
    # Main menu class
    # Atributes: width of the display, height of the display, the display itself, and a dictionary of the buttons found in the main menu
    # Functions: run (runs the main menu), draw (draws the elements in the main menu, called once every loop in run)

    def __init__(self, screen):
        # Input: screen, python display object
        # Creates the buttons needed in the main menu

        self.screen = screen 

        # Create buttons: dictionary of button objects (from PygameUtils)
        self.buttons = {"Example": Button("Example", screenwidth/2-150/2, 450, 150, 50, (0, 200, 0), (0, 255, 0)),
                        "Random": Button("Random", 200, 450, 120, 50, (0, 200, 0), (0, 255, 0)),
                        "Load": Button("Load", 350, 450, 120, 50, (0, 200, 0), (0, 255, 0)),
                        "Create": Button("Create", screenwidth-350-120, 450, 120, 50, (0, 200, 0), (0, 255, 0)),
                        "Quit": Button("Quit", screenwidth-200-120, 450, 120, 50, (200, 0, 0,), (255, 0, 0,))}
    
    
    def run(self):
        # Function which actually runs the main menu
        run = True

        while run:
            
            # Draw the elements of the main menu
            self.draw()
            
            # Load the events
            for event in pygame.event.get():

                # Check if the game has to be quit
                if event.type == pygame.QUIT:
                    run = False

                # Determine if the event is a button click, and if so, so something
                if event.type == pygame.MOUSEBUTTONUP:
                    
                    # Which button has been clicked?
                    if self.buttons["Random"].is_over(): 
                        print("Random")
                
                    elif self.buttons["Load"].is_over(): 
                        game = Game("Load","lwssgun")
                        game.run()
                        del game
                        run = False

                    elif self.buttons["Create"].is_over(): 
                        print("Create")

                    elif self.buttons["Quit"].is_over(): 
                        # Set run to false in order to quit the main menu, and thus the game
                        run = False 

                    elif self.buttons["Example"].is_over(): 
                        game = Game("Standard")
                        game.run()
                        del game
                        run = False
        
        # After the main menu we want to quit the game
        pygame.quit()
        quit()

    
    def draw(self):
        # Function to draw the elements found in the main menu ---  TO-DO: add the elements to the init function, instead of introducing them here
        
        # Draw background
        self.screen.fill((255,255,255))

        # Draw text
        draw_text(self.screen,"Conway's Game of Life", screenwidth/2, screenheight/2, "freesansbold.ttf",72,(0, 0, 0))

        # Draw buttons
        for _name, button in self.buttons.items():
            button.draw(self.screen)

        # Update display
        pygame.display.update() 
