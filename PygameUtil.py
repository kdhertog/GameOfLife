########################
# File with help functions for pygame
# Written by Koen den Hertog

import pygame as pg
from settings import fonts, colors

def button(scr, message, xpos, ypos, width, height, color, act_color, *actionargs):
    # Function that creates a button
    # Inputs: text on the button, xpos of the left top corner, ypos of the left top corner
    #          button width, button height, color when inactive, color when active (hovering)
    #          action when the button is pressed
    # Outputs: none

    # Get the current mouse position
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    # Determine if hovering over the button
    if xpos + width > mouse[0] > xpos and ypos+height > mouse[1] > ypos:
        pg.draw.rect(scr, act_color, (xpos, ypos, width, height))

        # Detect if the button is clicked and an action has to be performed
        if click[0] == 1:

            # Run actions    
            for action in actionargs:
                action()

    else:
        pg.draw.rect(scr, color, (xpos, ypos, width, height))

    draw_text(scr, message, xpos+(width/2), ypos+(height/2), fonts["button_font"], 20, colors["black"])

    return

def draw_text(scr, message, xpos, ypos, fonttype, size, color):
    
    # Set font
    textfont = pg.font.Font(fonttype, size)

    # Create the text surface and blit it to the display
    textSurface = textfont.render(message, True, color)
    textRect = textSurface.get_rect()
    textRect.center = (xpos,ypos)
    scr.blit(textSurface, textRect)

    return

def quit_game(): # Function that determines if the game has to end, and ends the game.
    
    # Determine if the escape key is pressed. 'keys[pg.K_ESCAPE]' equals true if that is the case
    keys = pg.key.get_pressed()
    escape = keys[pg.K_ESCAPE]

    # Determine if a quit event has taken place within pygame
    pg.event.pump() # pump the event queue
    for event in pg.event.get():
        if event.type==pg.QUIT:
            escape = True   # Set escape to true if a quit event has taken place

    # If escape is true, so either the escape key is pressed, or a quit event has taken place, quit pygame
    if escape:
        pg.quit()
        quit()

    return