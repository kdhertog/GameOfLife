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
