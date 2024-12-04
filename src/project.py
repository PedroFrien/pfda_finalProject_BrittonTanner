import pygame
import math
import sys
import random
import pygame.font



ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

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
            self.color = YELLOW

        self.width = screen.get_width()
        self.height = screen.get_height()
        self.x = int(col * squaresize + squaresize / 2)
        self.y = squaresize / 2

        self.final_y = final_y[1] if isinstance(final_y, tuple) else final_y
        self.falling_speed = random.uniform(0, 0.01)
        self.acceleration = 0.005

        self.is_complete = False

        self.surface = pygame.Surface((squaresize, squaresize), pygame.SRCALPHA)

    def update(self):
        if not self.is_complete:
            self.falling_speed += self.acceleration
            self.y += self.falling_speed

            if self.y >= self.final_y:
                self.y = self.final_y
                self.is_complete = True
                check_for_win(board, self.piece_type)
                
                

    def draw(self):
        self.surface.fill((0, 0, 0, 0))
        pygame.draw.circle(self.surface, self.color, (self.squaresize // 2, self.squaresize // 2), int(self.squaresize / 2 - 5))
    # Blit the surface onto the screen at the correct position
        self.screen.blit(self.surface, (self.x - self.squaresize // 2, self.y - self.squaresize // 2))
        # pygame.display.update()

    def fall(self):
        self.surface.fill((0,0,0,0))
        self.y += 0.5
        

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


    

def check_for_win(board, current_player):
    if winning_move(board, current_player):
        print(f"Congratulations Player {current_player}!")
        ending_anim(current_player)


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

game_over = False
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)

screen = pygame.display.set_mode(size)
board = create_board()
def main():
    
    

    current_player = 1
    posx = 1
    print_board(board)

    
    turn = 0

    pygame.init()

    # SQUARESIZE = 100

    # width = COLUMN_COUNT * SQUARESIZE
    # height = (ROW_COUNT+1) * SQUARESIZE
    # size = (width, height)


    draw_board(screen, SQUARESIZE, board, posx, current_player)
    pygame.display.update()

    
    
    
    while not game_over:

        
        
        
        draw_board(screen, SQUARESIZE, board, posx, current_player)

        for piece in falling_pieces:
            piece.update()
            piece.draw()

        

        # Update falling pieces
        falling_pieces[:] = [piece for piece in falling_pieces]

        
       
        
        
         
        
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEMOTION: 
                posx = event.pos[0]
                 

                
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                

                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, current_player)
                    
                    
                    
                    turn += 1
                    current_player = turn % 2 + 1
                    print_board(board)
                    draw_board(screen, SQUARESIZE, board, posx, current_player)


def draw_board(screen, SQUARESIZE, board, posx, current_player):

    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
    if current_player == 1:
        pygame.draw.circle(screen, RED, (int(posx), int(SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
    else:
        pygame.draw.circle(screen, YELLOW, (int(posx), int(SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
    # Background
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))  
    
    # # Player Pieces
    # for c in range(COLUMN_COUNT):
    #     for r in range(ROW_COUNT):
    #         if board[r][c] == 1:
    #             pygame.draw.circle(screen, RED, (int(c*SQUARESIZE + SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
    #         elif board[r][c] == 2:
    #             pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE + SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))
    

    
    # Holes
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # if board[r][c] == 0:
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))

    for piece in falling_pieces:
            piece.draw()

    
    pygame.display.update()
    
def ending_anim(current_player):

    game_over = True

    pygame.time.wait(1000)

    for piece in falling_pieces:
        piece.color = GREEN
        piece.draw()  # Redraw just this piece
        pygame.display.update()  # Update the display for this specific piece
        pygame.time.wait(200)

    pygame.time.wait(1500)

    for i in range(1000):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE)) 

        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),int(SQUARESIZE/2 - 5))

        
        for piece in falling_pieces:

            piece.fall()
            piece.draw()
            pygame.display.update()
    
    pygame.time.wait(1000)

    for alpha in range(0, 256, 10):
        screen.fill(BLACK)
        s = pygame.Surface((width, height))  
        s.set_alpha(alpha)                   
        s.fill((0,0,0))                      
        screen.blit(s, (0,0))                
        pygame.display.update()
        pygame.time.delay(50)

    if current_player == 1:
        text_color = RED
    else:
        text_color = YELLOW

    pygame.font.init()
    font = pygame.font.Font(None, 100)
    for idx, piece in enumerate(falling_pieces):
            del falling_pieces[idx]
    text = font.render(f"Player {current_player} Wins!", True, text_color)

    text_rect = text.get_rect(center=(width/2, height/2))

    screen.blit(text, text_rect)
    pygame.display.update()

    pygame.time.wait(3000)
    

    

    sys.exit()



if __name__ == "__main__":
    main()