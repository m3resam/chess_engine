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

Wr = Piece("Wr", "pieces/Wr.png")
Wn = Piece("Wn", "pieces/Wn.png")
Wb = Piece("Wb", "pieces/Wb.png")
Wq = Piece("Wq", "pieces/Wq.png")
Wk = Piece("Wk", "pieces/Wk.png")
Wp = Piece("Wp", "pieces/Wp.png")
Br = Piece("Br", "pieces/Br.png")
Bn = Piece("Bn", "pieces/Bn.png")
Bb = Piece("Bb", "pieces/Bb.png")
Bq = Piece("Bq", "pieces/Bq.png")
Bk = Piece("Bk", "pieces/Bk.png")
Bp = Piece("Bp", "pieces/Bp.png")


board = [
    [Br, Bn, Bb, Bq, Bk, Bb, Bn, Br],
    [Bp, Bp, Bp, Bp, Bp, Bp, Bp, Bp],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Wp, Wp, Wp, Wp, Wp, Wp, Wp, Wp],
    [Wr, Wn, Wb, Wq, Wk, Wb, Wn, Wr]
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
