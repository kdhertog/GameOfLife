########################
# File with help functions for pygame
# Written by Koen den Hertog

import pygame
import numpy

def create_window(w, h, fullscreen):
    if fullscreen:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((w, h))
    
    pygame.display.set_caption("The Game of Life")
    
    return screen

class Button():
    # Class for creating buttons
    # Atributes: text on the button, x-coordinate of the left side of the button, y coordinate of the top of the button,
    #             width, height, color when inactive, color when active (hovering over it)
    # Functions: is_over (returns true if the mouse is hovering over the button), draw (draws the button in the correct color)


    def __init__(self, text, left, top, width, height, color, act_color):
        self.text = text
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.act_color = act_color

    def is_over(self):
        mouse = pygame.mouse.get_pos()

        if self.left + self.width > mouse[0] > self.left and self.top + self.height > mouse[1] > self.top:
            return True
        else:
            return False 
    
    def draw(self, screen):
        
        # Determine if hovering over the button, if so draw in the active color, else in the inactive color
        if self.is_over():
            pygame.draw.rect(screen, self.act_color, (self.left, self.top, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.left, self.top, self.width, self.height))

        draw_text(screen, self.text, self.left+(self.width/2), self.top+(self.height/2), "freesansbold.ttf", 20, (0, 0, 0))

def draw_text(scr, message, xpos, ypos, fonttype, size, color):
    # Function for drawing text. Requires a python display object, a text (str), 
    # the x and y position of the text, a fonttype (str), a textsize (int)m, and a text color

    # Set font
    textfont = pygame.font.Font(fonttype, size)

    # Create the text surface and blit it to the display
    textSurface = textfont.render(message, True, color)
    textRect = textSurface.get_rect()
    textRect.center = (xpos,ypos)
    scr.blit(textSurface, textRect)

    return

def strip_array(arr): 
    # Function that strips an array of all leading or trailing rows or columns
    
    # Leading rows
    for i in range(int(len(arr[0,:]/2))+1):
        if sum(arr[:,0]) == 0:
            arr = arr[:,1:]
        else:
            break
    
    # Leading columns
    for i in range(int(len(arr[:,0]/2))+1):
        if sum(arr[0,:]) == 0:
            arr = arr[1:,:]
        else:
            break

    # Trailing columns
    
    # Trailing rows

    return arr