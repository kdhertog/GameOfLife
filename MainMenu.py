################################
# Main menu of the Game of Life

import pygame

class MainMenu:

    def __init__(self, screen):
        self.width, self.height = pygame.display.get_surface().get_size()
        self.screen = screen

    def run(self):
        run = True

        while run:
            
            # Load the events
            for event in pygame.event.get():

                # Check if the game has to be quit
                if event.type == pygame.QUIT:
                    run = False

                # Determine if the event is a button click, and if so, so something

            self.draw()
        
        pygame.quit()


    def draw(self):
        
        # Draw background
        self.screen.fill((255,255,255))

        # Update display
        pygame.display.update()