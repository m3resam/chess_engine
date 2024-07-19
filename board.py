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

def draw_board():
    for i in range(ROWS):
        for j in range(COLS):
            if (i+j)%2 == 0:
                pygame.draw.rect(WIN, 'white', (j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(WIN, 'black', (j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[i][j]
            if piece:
                WIN.blit(piece.image, (j*SQUARE_SIZE, i*SQUARE_SIZE))

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
