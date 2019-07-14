# GameOfLife
An implementation of Conway's Game of Life

# Explanation
- The 'game' exists of a large board, in which each fiels has two states: dead (empty) or alive (filled)
- To calculate the next state (generation), of the board for each field, sum the number of cells in the neighbouring eight cells
- Standard rules for determining the next state:
    - Sum 0 or 1: death
    - Sum 2: same as current state
    - Sum 3: birth
    - Sum >4: death

# Implementation in python


# To-do
- Fancify loading screen
- Add options 'load board' and 'create new board' to main menu
- Fancify main menu
- Add option to resize the screen