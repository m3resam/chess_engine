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

#about to add the pieces

board = [
    [Wr, Wn, Wb, Wq, Wk, Wb, Wn, Wr],
    [Wp, Wp, Wp, Wp, Wp, Wp, Wp, Wp],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Bp, Bp, Bp, Bp, Bp, Bp, Bp, Bp],
    [Br, Bn, Bb, Bq, Bk, Bb, Bn, Br]
]

def draw_board():
    for i in range(ROWS):
        for j in range(COLS):
            pygame.draw.rect(WIN, colors[(i+j)%2], (j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
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
