########################
# This file contains the Board class
# Written by Koen den Hertog

import numpy as np
import pygame
import os

from settings import screenwidth, screenheight

class BoardClass:
    # Board class
    # Attributes: the boardtype, to determine how the board is created
    #             board, which contains the numpy matrix that represents the board
    # Functions: update, standard (to load a standard board), random (to load a random board)
    #             load (to load a board from saves), create (to create a new board)

    def __init__(self, boardtype, filename=None):
        self.boardtype = boardtype
        self.filename = filename
        if self.boardtype == "Standard":
            self.board = self.standard()
        elif self.boardtype == "Random":
            self.board = self.random()
        elif self.boardtype == "Create":
            self.board = self.create()
        elif self.boardtype == "Load":
            self.board = self.load(filename)
        self.nx = len(self.board[0,:])
        self.ny = len(self.board[:,0])

    def update(self):
        # Function that updates the board, based on the rules

        # Create new board for calculations
        calc_board = np.zeros((self.nx + 2, self.ny + 2))
        calc_board[1:self.nx+1, 1:self.ny+1] = self.board

        # Shift the board in each of the eight directions, and sum them
        sum_board = (
            calc_board[0:self.nx+0, 0:self.ny+0] + 
            calc_board[0:self.nx+0, 1:self.ny+1] + 
            calc_board[0:self.nx+0, 2:self.ny+2] + 
            calc_board[1:self.nx+1, 0:self.ny+0] + 
            calc_board[1:self.nx+1, 2:self.ny+2] + 
            calc_board[2:self.nx+2, 0:self.ny+0] + 
            calc_board[2:self.nx+2, 1:self.ny+1] + 
            calc_board[2:self.nx+2, 2:self.ny+2]) 

        # Return the new board. If a cell has a value of 2 in the sum_board, it will stay the same as in the old board
        # Else, if the sum = 3, the cell will become alive, else it will die. 
        new_board = np.where(sum_board == 2, self.board, (np.where(sum_board == 3, 1, 0)))
        
        self.board = new_board

    def draw(self, screen):
        # Function to draw the board to the screen
        # Attribute: a pygame display object

        # Fill the background with black
        screen.fill((0, 0, 0))

        # Determine the size of the cells
        cell_size = (screenwidth/self.nx*0.95, screenheight/self.ny*0.95)
        
        # Draw every alive cell
        for i in range(self.nx):
            for j in range(self.ny):
                if self.board[j,i] == 1:
                    square_rect = pygame.Rect((i * (screenwidth / self.nx), j * (screenheight / self.ny)), cell_size)
                    pygame.draw.rect(screen, (255, 255, 255), square_rect)
                    
        pygame.display.update()

    def standard(self):
        # Function to create the standard board
        board = np.zeros((100, 100))
        initial = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
        xpos_initial = 1
        ypos_initial = 1
        board[xpos_initial:xpos_initial + len(initial[:, 0]),
              ypos_initial:ypos_initial + len(initial[0, :]),] = initial  # Load initial into the board

        return board


    def load(self, filename):  # OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD
        # Loads an existing board from a .lif file. Only works for the 'Life 1.05' format
        folder = os.path.dirname(__file__)
        check_file = folder + "/Saves/LIF105/" + filename + ".lif"
        if os.path.exists(check_file):
            f = open(check_file, "r")
            lines = f.readlines()
            f.close()
            
            # Append the file in order to be able to read it
            if lines[0][0:10] == "#Life 1.05":  # Check if the file is "Life 1.05"
                cell_lines = []  # Create empty list for storing just the cell lines
                for i in range(
                    1, len(lines)
                ):  # remove lines that are not for cells, ignoring the rules
                    if not (
                        lines[i][1] == "D" or lines[i][1] == "R" or lines[i][1] == "N"
                    ):
                        cell_lines.append(lines[i])

                # Split cell_lines into individual cells
                cells = []
                current_cell = []
                i = 0
                while i <= len(cell_lines) - 1:
                    if cell_lines[i][1] == "P":  # Start of a new cell
                        cells.append(current_cell)  # Append old cell to list of cells
                        current_cell = [cell_lines[i]]  # Start new cell
                    else:
                        cell_lines[i] = cell_lines[i].strip("\n")
                        current_cell.append(cell_lines[i])  # Append line to cell
                    i = i + 1
                cells.append(current_cell)
                cells = cells[1:]  # Cells

                # Create an empty board of a 10000 by 10000 size, if the board that has to be loaded is bigger there will be errors
                board = np.zeros((10000, 10000))

                # Fill the board with the cells
                xlocs = (
                    []
                )  # Lists for rembering locations of the cells, and for the longest dimension of the cells
                ylocs = []
                long_dim = []
                for cell in cells:

                    # Determine location of the cell, remember locations
                    start = cell[0].split()
                    try:
                        xpos_initial = int(start[1]) + int(len(board[:, 0]) / 2)
                        ypos_initial = int(start[2]) + int(len(board[0, :]) / 2)
                    except:
                        xpos_initial = 0
                        ypos_initial = 0
                    xlocs.append(xpos_initial)
                    ylocs.append(ypos_initial)

                    # Create new cell for appending format
                    new_cell = []  # new_cell will be a list of numpy arrays
                    longest = 0
                    for i in range(1, len(cell)):
                        # Create single line as array, and determine the longest line
                        line_array = np.array(list(cell[i]))
                        line = np.where(line_array == "*", 1, 0)
                        if len(line) > longest:
                            longest = len(line)
                        new_cell.append(line)

                    # Create appending board
                    initial = np.zeros((len(new_cell), longest))
                    for i in range(len(new_cell)):
                        initial[i, 0 : len(new_cell[i])] = new_cell[i]

                    long_dim.append(max(len(initial[:, 0]), len(initial[0, :])))

                    # Load initial into the board after creating an empty board
                    board[
                        xpos_initial : xpos_initial + len(initial[:, 0]),
                        ypos_initial : ypos_initial + len(initial[0, :]),
                    ] = initial

                # Resize board to remove lot of empty space on the edges, we want to keep the board square
                x_min = min(xlocs) - 5
                x_max = max(xlocs) + max(long_dim)
                y_min = min(ylocs) - 5
                y_max = max(ylocs) + max(long_dim)
                min_dim = min(x_min, y_min)
                max_dim = max(x_max, y_max)  # We want a minimum board size of 200
                board = board[min_dim:max_dim, min_dim:max_dim]

            else:
                print("Only Life 1.05 files will work")
                board = np.zeros((100, 100))
                initial = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
                xpos_initial = 1
                ypos_initial = 1
                board[
                    xpos_initial : xpos_initial + len(initial[:, 0]),
                    ypos_initial : ypos_initial + len(initial[0, :]),
                ] = initial  # Load initial into the board
            
        else:
            print(
                "Please choose an existing file next time. For now, we'll go with a standard board"
            )
            board = np.zeros((100, 100))
            initial = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
            xpos_initial = 1
            ypos_initial = 1
            board[
                xpos_initial : xpos_initial + len(initial[:, 0]),
                ypos_initial : ypos_initial + len(initial[0, :]),
            ] = initial  # Load initial into the board

        return board