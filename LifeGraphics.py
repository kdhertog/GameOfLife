#####################
# Module to provide graphics to the game of life
# Written by Koen den Hertog

import pygame as pg

from settings import colors, fonts, dim
from PygameUtil import quit_game, button, draw_text


def loadscreen():  # Function that sets up the pygame display, and acts as an initial loading screen. Returns the display object 

    # Initialize pygame
    pg.init()

    # Set up display
    scr = pg.display.set_mode((dim[0], dim[1]))
    pg.display.set_caption("Game of Life")

    # Loop for the loading screen
    loading = True
    while loading:

        # Determine if we have to quit the game
        quit_game()

        # Fill background
        scr.fill(colors["white"])

        # Draw text
        draw_text(scr,"Conway's Game of Life",dim[0] / 2,dim[1] / 2, fonts["main_font"],72,colors["black"])

        # Update the display
        pg.display.update()

        # Set loading to false (since there is nothing to load)
        loading = False

    # Returning display for further usage
    return scr


def main_menu(scr):  # Functions that creates the main menu. It contains two options: 'load random board', and 'quit'

    # Main_menu loop
    in_menu = True
    while in_menu:

        # Determine if the game has to be quit
        quit_game()

        # Fill background with white
        scr.fill(colors["white"])

        # Draw text
        draw_text(scr, "Conway's Game of Life", dim[0]/2, dim[1]/2, fonts["main_font"], 72, colors["black"]) 

        # Create the random button
        board = button(scr,"Random", 200,450,120,50,colors["green"],colors["bright_green"],"random")

        # Create the quit button
        button(scr, "Quit",dim[0] - 200 - 120,450,120,50,colors["red"], colors["bright_red"],pg.quit,quit)

        # Update the display
        pg.display.update()

    return board


def show(scr, board):  # OLD OLD OLD OLD OLD
    nx = len(board[0, :])
    ny = len(board[:, 0])
    xmax, _ymax = pg.display.get_surface().get_size()
    scr.fill((0, 0, 0))
    square_size = (xmax / nx * 0.95, dim[1] / ny * 0.95)
    for i in range(len(board[:, 0])):
        for j in range(len(board[0, :])):
            if board[i, j] == 1:
                square_rect = pg.Rect((i * (xmax / nx), j * (dim[1] / ny)), square_size)  
                pg.draw.rect(scr, (255, 255, 255), square_rect)
    pg.display.flip()


"""
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
    dim[0],dim[1] = pg.display.get_surface().get_size()
    scr.fill((0,0,0))
    square_size = (dim[0]/nx*0.95,dim[1]/ny*0.95)
    for i in range(len(board[:,0])):
        for j in range(len(board[0,:])):
            if board[i,j] == 1:
                square_rect = pg.Rect((i*(dim[0]/nx),j*(dim[1]/ny)),square_size) 
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
"""
