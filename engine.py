# Contains the old engine
# OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD

def engine(board):
    # Create new board for calculations
    nx = len(board[0,:])
    ny = len(board[:,0])
    calc_board = np.zeros((nx+2,ny+2)) 
    calc_board[1:nx+1,1:ny+1] = board
    
    # Shift the board in each of the eight directions, and sum them
    sum_board = calc_board[0:nx+0,0:ny+0]+ \
                calc_board[0:nx+0,1:ny+1]+ \
                calc_board[0:nx+0,2:ny+2]+ \
                calc_board[1:nx+1,0:ny+0]+ \
                calc_board[1:nx+1,2:ny+2]+ \
                calc_board[2:nx+2,0:ny+0]+ \
                calc_board[2:nx+2,1:ny+1]+ \
                calc_board[2:nx+2,2:ny+2]

    # Return the new board
    new_board = np.where(sum_board == 2,board,(np.where(sum_board == 3,1,0)))
    return new_board