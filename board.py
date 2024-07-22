#it doesnt work, i do not understand, im taking a brake

import pygame
import os

class Piece:
    def __init__(self, name, image_path):
        self.name = name
        self.image = pygame.image.load(os.path.join(image_path))

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

wR = Piece("wR", "pieces/wR.png")
wN = Piece("wN", "pieces/wN.png")
wB = Piece("wB", "pieces/wB.png")
wQ = Piece("wQ", "pieces/wQ.png")
wK = Piece("wK", "pieces/wK.png")
wP = Piece("wP", "pieces/wP.png")
bR = Piece("bR", "pieces/bR.png")
bN = Piece("bN", "pieces/bN.png")
bB = Piece("bB", "pieces/bB.png")
bQ = Piece("bQ", "pieces/bQ.png")
bK = Piece("bQ", "pieces/bK.png")
bP = Piece("bP", "pieces/bP.png")

board = [
    [bR, bN, bB, bQ, bK, bB, bN, bR],
    [bP, bP, bP, bP, bP, bP, bP, bP],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [wP, wP, wP, wP, wP, wP, wP, wP],
    [wR, wN, wB, wQ, wK, wB, wN, wR]
]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
HIGHLIGHT = (173, 216, 230)

def draw_board(selected_square = None):
    for row in range(ROWS):
        for col in range(COLS):
            if selected_square == (row, col):
                color = HIGHLIGHT
            elif (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(WIN, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece:
                WIN.blit(piece.image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def valid_move(piece, start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos

    if piece.name[1] == 'P': #pawn
        if piece.name[0] == 'w':
            direction = -1
        else:
            direction = 1
        start_row_valid = (start_row == 6 and piece.name[0] == 'w') or (start_row == 1 and piece.name[0] == 'b')
        if start_col == end_col: 
            if board[end_row][end_col] == None:
                if end_row - start_row == direction:
                    return True
                elif end_row - start_row == 2 * direction and start_row_valid and board[start_row + direction][start_col] == None:
                    return True
        elif abs(start_col - end_col) == 1 and end_row - start_row == direction:
            if board[end_row][end_col] != None and board[end_row][end_col].name[0] != piece.name[0]:
                return True
            
    elif piece.name[1] == 'R': #rook
        if start_row == end_row or start_col == end_col:
            if not piece_in_between(start_pos, end_pos):
                return True
            
    elif piece.name[1] == 'N': #knight
        pass
    elif piece.name[1] == 'B': #bishop
        pass
    elif piece.name[1] == 'Q': #queen
        pass
    elif piece.name[1] == 'K': #king
        pass
        
    return False

def piece_in_between(start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    
    if end_row > start_row: row_step = 1
    elif end_row < start_row: row_step = -1
    else: row_step = 0

    if end_col > start_col: col_step = 1
    elif end_col < start_col: col_step = -1
    else: col_step = 0

    current_row, current_col = start_row + row_step, start_col + col_step
    while (current_row, current_col) != (end_row, end_col):
        if board[current_row][current_col] is not None:
            return True
        current_row += row_step
        current_col += col_step

    return False

def move_piece(start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = board[start_row][start_col]
    board[start_row][start_col] = None
    board[end_row][end_col] = piece

def main():
    clock = pygame.time.Clock()
    selected_piece = None
    turn = 'w'
    run = True
    while run:
        clock.tick(60)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                col, row = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
                if selected_piece: 
                    if valid_move(board[selected_piece[0]][selected_piece[1]], selected_piece, (row, col)):
                        move_piece(selected_piece, (row, col))
                        turn = 'b' if turn == 'w' else 'w'
                    selected_piece = None
                else:
                    if board[row][col] != None:
                        selected_piece = (row, col)
            
        draw_board(selected_piece)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
