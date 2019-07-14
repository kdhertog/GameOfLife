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