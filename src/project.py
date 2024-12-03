import pygame
import math



ROW_COUNT = 6
COLUMN_COUNT = 7

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
                if board[r][c] == piece and board[r-1][c] == piece and board [r-2][c] == piece and board[r-3][c] == piece:
                    return True

                


def main():

    board = create_board()
    print_board(board)
    
    game_over = False
    turn = 0

    while not game_over:

        current_player = turn % 2 + 1
        
        while True:
            try:
                col = (int(input(f"Player {current_player} Selection (1-7): ")) - 1)
                if 0 <= col <= 6:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 7.")
            
        
        if 0 <= col < COLUMN_COUNT and is_valid_location(board, col):
            row = get_next_open_row(board, col)
            if current_player == 1:
                drop_piece(board, row, col, current_player)
            if current_player == 2:
                drop_piece(board, row, col, current_player)
            
            print_board(board)

            if winning_move(board, current_player):
                print(f"Congratulations to Player {current_player}!")
                game_over = True

            turn += 1
            
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()