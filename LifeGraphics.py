#####################
# Module to provide graphics to the game of life
# Written by Koen den Hertog

import pygame as pg

def loadscreen(): # Function that sets up the pygame display, and acts as an initial loading screen. Returns the display object
    
    # Initialize pygame
    pg.init()

    # Set up display
    scr = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    pg.display.set_caption("Game of Life")

    # Returning display for further usage
    return scr

def closescr(): # Function that determines if the game has to end, and ends the game. Returns the bolean 'escape', which allows the main program to quit
    
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

    return escape

def show(scr,board): #OLD OLD OLD OLD OLD
    nx = len(board[0,:])
    ny = len(board[:,0])
    xmax,ymax = pg.display.get_surface().get_size()
    scr.fill((0,0,0))
    square_size = (xmax/nx*0.95,ymax/ny*0.95)
    for i in range(len(board[:,0])):
        for j in range(len(board[0,:])):
            if board[i,j] == 1:
                square_rect = pg.Rect((i*(xmax/nx),j*(ymax/ny)),square_size)
                pg.draw.rect(scr,(255,255,255),square_rect)
    pg.display.flip()

'''
OLD OLD OLD OLD OLD OLD

#####################
# Module to provide graphics to the game of life
# Written by Koen den Hertog

import pygame as pg

def initscr():
    pg.init()
    scr = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    #scr = pg.display.set_mode((1360,850))
    pg.display.set_caption("Game of Life")
    print("Start Game of Life")
    return scr

def closescr():
    keys = pg.key.get_pressed()
    escape = keys[pg.K_ESCAPE]
    pg.event.pump()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            escape = True
    if escape:
        pg.quit()
        print ("Ready.")
    return escape

def show(scr,board):
    nx = len(board[0,:])
    ny = len(board[:,0])
    xmax,ymax = pg.display.get_surface().get_size()
    scr.fill((0,0,0))
    square_size = (xmax/nx*0.95,ymax/ny*0.95)
    for i in range(len(board[:,0])):
        for j in range(len(board[0,:])):
            if board[i,j] == 1:
                square_rect = pg.Rect((i*(xmax/nx),j*(ymax/ny)),square_size)
                pg.draw.rect(scr,(255,255,255),square_rect)
    pg.display.flip()

def main_menu(filename1):
    pg.init()
    scr = pg.display.set_mode((640,480))
    pg.display.set_caption("Game of Life")
    scr.fill((0,0,0))
    pg.display.flip()
    filename = filename1
    return filename
'''