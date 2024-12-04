import pygame
import math
import sys



ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# PLAYER1_PIECE = "🔵"
# PLAYER2_PIECE = "🔴"

def create_board():
 

    board = [[0 for i in range(COLUMN_COUNT)] for j in range(ROW_COUNT)]
    return board

def drop_piece(board, row, col, piece):

    board[row][col] = piece

def is_valid_location(board, col):

    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):

    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
    return None  

def print_board(board):
 
    for row in board[::-1]:
        print(row)

def winning_move(board, piece):
        # Horizontal
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True
                
        # Vertical
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r+1][c] == piece and board [r+2][c] == piece and board[r+3][c] == piece:
                    return True
                
        # Diagonal (Bottom Left to Top Right)
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board [r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Diagonal (Top Left to Bottom Right)
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board [r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

   



def main():

    board = create_board()
    print_board(board)

    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE
    size = (width, height)

    screen = pygame.display.set_mode(size)
    draw_board(screen, SQUARESIZE, board)
    pygame.display.update()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Determine current player based on turn
                current_player = turn % 2 + 1
                
                # Get the column clicked
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                
                # Only allow the current player to place a piece
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, current_player)
                    
                    # Check for winning move
                    if winning_move(board, current_player):
                        print(f"Congratulations Player {current_player}!")
                        game_over = True
                    
                    # Increment turn AFTER placing the piece
                    turn += 1
                    
                    # Print the board after each move
                    print_board(board)
                    draw_board(screen, SQUARESIZE, board)

def draw_board(screen, SQUARESIZE, board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))  
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
            elif board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))


if __name__ == "__main__":
    main()