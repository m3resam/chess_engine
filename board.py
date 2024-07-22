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

YELLOW = (255, 238, 110, 1)
DARK = (129, 142, 112)
LIGHT = (189, 196, 180)
def draw_board(selected_square = None):
    for row in range(ROWS):
        for col in range(COLS):
            #color selection
            if selected_square == (row, col):
                color = YELLOW
            elif (row + col) % 2 == 0:
                color = LIGHT
            else:
                color = DARK
            #draw squares with colors
            pygame.draw.rect(WIN, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece:
                WIN.blit(piece.image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
                
def move_piece(start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    #gets the selected piece
    piece = board[start_row][start_col]
    #removes the piece from the start pos
    board[start_row][start_col] = None
    #moves the piece the end pos
    board[end_row][end_col] = piece    
    
def main():
    clock = pygame.time.Clock()
    selected_piece = None
    run = True
    while run:
        clock.tick(60)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                col, row = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE #event.po[0] = col, event.pos[1] = row
                #already selected piece wait for move_piece
                if selected_piece:    
                    #selected_piece is the initial position, (row, col) is the returned end position
                    move_piece(selected_piece, (row, col))
                    selected_piece = None
                #piece not yet selected
                else:
                    if board[row][col] != None:
                        selected_piece = (row, col)

        draw_board(selected_piece)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
