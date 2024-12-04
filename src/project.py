import pygame
import math
import sys
import random


ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# PLAYER1_PIECE = "🔵"
# PLAYER2_PIECE = "🔴"

falling_pieces = []

class FallingPiece:
    def __init__(self, screen, col, piece_type, squaresize, final_y):
        self.screen = screen
        self.col = col
        self.piece_type = piece_type
        self.squaresize = squaresize

        
        if self.piece_type == 1:
            self.color = RED
        elif self.piece_type == 2:
            self.color = YELLOW  # Fixed this line

        self.width = screen.get_width()
        self.height = screen.get_height()
        self.x = int(col * squaresize + squaresize / 2)
        self.y = squaresize / 2
        
       
        self.final_y = final_y[1] if isinstance(final_y, tuple) else final_y

        self.falling_speed = random.uniform(0, 0.01)
        self.acceleration = 0.001

        self.is_complete = False

    def update(self):

        if self.is_complete == False:
            self.falling_speed += self.acceleration
            self.y += self.falling_speed

        if self.final_y is not None:
            self.is_complete = self.y >= self.final_y
        else: 
            self.is_complete = self.y > self.height

        return self.is_complete
    
    def draw(self):

        # surf = pygame.Surface((SQUARESIZE, SQUARESIZE))
        pygame.draw.circle(self.screen, self.color, (self.x, int(self.y)), int(self.squaresize/2-5))
        # surf.blit
        pygame.display.update()

def create_board():
 

    board = [[0 for i in range(COLUMN_COUNT)] for j in range(ROW_COUNT)]
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

    # Calculate the target position for the piece
    targetPosition = (int(col*SQUARESIZE + SQUARESIZE/2), height-int(row*SQUARESIZE+SQUARESIZE/2))

    # Create a new falling piece and add it to the list
    new_piece = FallingPiece(screen, col, piece, SQUARESIZE, targetPosition)
    falling_pieces.append(new_piece)

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

   

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)

screen = pygame.display.set_mode(size)

def main():

    board = create_board()
    print_board(board)

    game_over = False
    turn = 0

    pygame.init()

    # SQUARESIZE = 100

    # width = COLUMN_COUNT * SQUARESIZE
    # height = (ROW_COUNT+1) * SQUARESIZE
    # size = (width, height)


    draw_board(screen, SQUARESIZE, board)
    pygame.display.update()

    current_player = 1
    posx = 0
    
    while not game_over:

        
        
        
        draw_board(screen, SQUARESIZE, board)

        for piece in falling_pieces:
            piece.update()
            piece.draw()

        

        # Update falling pieces
        falling_pieces[:] = [piece for piece in falling_pieces if not piece.is_complete]
        
        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

        if current_player == 1:
            pygame.draw.circle(screen, RED, (int(posx), int(SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
        else:
            pygame.draw.circle(screen, YELLOW, (int(posx), int(SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
         
        
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEMOTION: 
                posx = event.pos[0]
                # pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE)) 

                
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                

                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, current_player)
                    
                    if winning_move(board, current_player):
                        print(f"Congratulations Player {current_player}!")
                        game_over = True
                    
                    turn += 1
                    current_player = turn % 2 + 1
                    print_board(board)
                    draw_board(screen, SQUARESIZE, board)

def draw_board(screen, SQUARESIZE, board):
    # Background
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))  
    
    # # Player Pieces
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE + SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE + SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
    
    # Holes
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))

                

    pygame.display.update()


if __name__ == "__main__":
    main()