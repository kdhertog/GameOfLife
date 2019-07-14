##################
# This is the main file for the Conway's Game of Life implementation
# Written by Koen den Hertog

from settings import *
from LifeGraphics import loadscreen, show, closescr

def main():
    # Loading screen
    screen = loadscreen()

    # Main menu
        # Add function for the main menu here

    # Run the game of life, until the closescr functions returns that the program has to end
    escape = False
    while not escape:
        #show(screen,board)
        #board = engine(board)
        escape = closescr()


if __name__ == "__main__":
    main()



'''
OLD OLD OLD OLD OLD OLD OLD 

##########################
# Game of Life
# Code written by Koen den Hertog

import numpy as np
import pygame as pg
import os
import time

from LifeGraphics import initscr,closescr,show,main_menu
from functions import engine,load_board

os.system('cls' if os.name == 'nt' else 'clear')

# Main menu
filename = main_menu("acorn")

# Load board
board = load_board(filename)
time.sleep(.5)

# Set up display
screen = initscr()

# Run the game of life
escape = False
while not escape:
    show(screen,board)
    board = engine(board)
    escape = closescr()
''' 