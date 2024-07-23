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
pygame.display.set_caption("Chess")

# Initialize pieces
pieces = {
    "wR": Piece("wR", "pieces/wR.png"),
    "wN": Piece("wN", "pieces/wN.png"),
    "wB": Piece("wB", "pieces/wB.png"),
    "wQ": Piece("wQ", "pieces/wQ.png"),
    "wK": Piece("wK", "pieces/wK.png"),
    "wP": Piece("wP", "pieces/wP.png"),
    "bR": Piece("bR", "pieces/bR.png"),
    "bN": Piece("bN", "pieces/bN.png"),
    "bB": Piece("bB", "pieces/bB.png"),
    "bQ": Piece("bQ", "pieces/bQ.png"),
    "bK": Piece("bK", "pieces/bK.png"),
    "bP": Piece("bP", "pieces/bP.png"),
}

# Initial board setup
initial_board = [
    [Piece("bR", "pieces/bR.png"), Piece("bN", "pieces/bN.png"), Piece("bB", "pieces/bB.png"), Piece("bQ", "pieces/bQ.png"), Piece("bK", "pieces/bK.png"), Piece("bB", "pieces/bB.png"), Piece("bN", "pieces/bN.png"), Piece("bR", "pieces/bR.png")],
    [Piece("bP", "pieces/bP.png"), Piece("bP", "pieces/bP.png"), Piece("bP", "pieces/bP.png"), Piece("bP", "pieces/bP.png"), Piece("bP", "pieces/bP.png"), Piece("bP", "pieces/bP.png"), Piece("bP", "pieces/bP.png"), Piece("bP", "pieces/bP.png")],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Piece("wP", "pieces/wP.png"), Piece("wP", "pieces/wP.png"), Piece("wP", "pieces/wP.png"), Piece("wP", "pieces/wP.png"), Piece("wP", "pieces/wP.png"), Piece("wP", "pieces/wP.png"), Piece("wP", "pieces/wP.png"), Piece("wP", "pieces/wP.png")],
    [Piece("wR", "pieces/wR.png"), Piece("wN", "pieces/wN.png"), Piece("wB", "pieces/wB.png"), Piece("wQ", "pieces/wQ.png"), Piece("wK", "pieces/wK.png"), Piece("wB", "pieces/wB.png"), Piece("wN", "pieces/wN.png"), Piece("wR", "pieces/wR.png")]
]

# Copy of the initial board for game state
board = [[piece for piece in row] for row in initial_board]

# Colors for the board and highlights
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
VALID_MOVE = (0, 255, 0, 100)  # RGBA for valid move highlights
HIGHLIGHT = (173, 216, 230, 100)  # RGBA for selected square highlights

# Font for displaying text
font = pygame.font.SysFont(None, 36)

# Game state variables
move_history = []
fifty_move_counter = 0
en_passant_target = []

# Variables for piece dragging
dragging_piece = None
dragging_start_pos = None

# Function to draw the chessboard and pieces
def draw_board(selected_square=None, valid_moves=[], player_color='w', dragging_piece=None, mouse_pos=None):
    for row in range(ROWS):
        for col in range(COLS):
            # Adjust row and column based on player color
            if player_color == 'w':
                board_row, board_col = row, col
            else:
                board_row, board_col = ROWS - 1 - row, COLS - 1 - col
            
            # Determine the color of the square
            if (board_row + board_col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(WIN, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))  # Draw the square
            piece = board[board_row][board_col]  # Get the piece at the current position
            if piece and piece != dragging_piece:  # Draw the piece if it's not the dragged piece
                WIN.blit(piece.image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    # Draw valid move highlights
    overlay = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
    for row, col in valid_moves:
        if player_color == 'w':
            board_row, board_col = row, col
        else:
            board_row, board_col = ROWS - 1 - row, COLS - 1 - col
        overlay.fill(VALID_MOVE)
        WIN.blit(overlay, (board_col * SQUARE_SIZE, board_row * SQUARE_SIZE))
    
    # Draw selected square highlight
    if selected_square:
        selected_row, selected_col = selected_square
        if player_color != 'w':
            selected_row, selected_col = ROWS - 1 - selected_row, COLS - 1 - selected_col
        overlay.fill(HIGHLIGHT)
        WIN.blit(overlay, (selected_col * SQUARE_SIZE, selected_row * SQUARE_SIZE))
    
    # Draw the dragging piece last to ensure it is on top
    if dragging_piece and mouse_pos:
        WIN.blit(dragging_piece.image, (mouse_pos[0] - SQUARE_SIZE // 2, mouse_pos[1] - SQUARE_SIZE // 2))

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)  # Render the text
    textrect = textobj.get_rect()  # Get the text rectangle
    textrect.topleft = (x, y)  # Set the position of the text
    surface.blit(textobj, textrect)  # Draw the text on the surface

# Function to draw a button on the screen
def draw_button(text, font, color, surface, x, y, width, height):
    rect = pygame.Rect(x, y, width, height)  # Create a rectangle for the button
    pygame.draw.rect(surface, color, rect)  # Draw the button rectangle
    draw_text(text, font, (0, 0, 0), surface, x + 10, y + 10)  # Draw the button text
    return rect  # Return the button rectangle for collision detection

# Function to validate basic moves (excluding checks)
def basic_valid_move(piece, start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos

    # Check if the target position contains a piece of the same color
    if board[end_row][end_col] and board[end_row][end_col].name[0] == piece.name[0]:
        return False

    if piece.name[1] == 'P':  # Pawn movement
        direction = -1 if piece.name[0] == 'w' else 1  # Determine the direction based on piece color
        start_row_valid = (start_row == 6 and piece.name[0] == 'w') or (start_row == 1 and piece.name[0] == 'b')
        if start_col == end_col: 
            if board[end_row][end_col] is None:
                if end_row - start_row == direction:
                    return True
                elif end_row - start_row == 2 * direction and start_row_valid and board[start_row + direction][start_col] is None:
                    return True
        elif abs(start_col - end_col) == 1 and end_row - start_row == direction:
            if board[end_row][end_col] is not None and board[end_row][end_col].name[0] != piece.name[0]:
                return True
            if board[end_row][end_col] is None and (start_row, end_col) in en_passant_target:
                return True

    elif piece.name[1] == 'R':  # Rook movement
        if start_row == end_row or start_col == end_col:
            if not any_piece_between(start_pos, end_pos):
                return True

    elif piece.name[1] == 'N':  # Knight movement
        if (abs(start_row - end_row), abs(start_col - end_col)) in [(2, 1), (1, 2)]:
            return True

    elif piece.name[1] == 'B':  # Bishop movement
        if abs(start_row - end_row) == abs(start_col - end_col):
            if not any_piece_between(start_pos, end_pos):
                return True

    elif piece.name[1] == 'Q':  # Queen movement
        if (start_row == end_row or start_col == end_col) or (abs(start_row - end_row) == abs(start_col - end_col)):
            if not any_piece_between(start_pos, end_pos):
                return True

    elif piece.name[1] == 'K':  # King movement
        if max(abs(start_row - end_row), abs(start_col - end_col)) == 1:
            return True
        # Castling
        if start_row == end_row and abs(start_col - end_col) == 2:
            if piece.name[0] == 'w' and start_row == 7:
                if end_col == 6 and not any_piece_between(start_pos, (start_row, 7)) and board[start_row][7] and board[start_row][7].name == 'wR':
                    return True  # White kingside
                if end_col == 2 and not any_piece_between(start_pos, (start_row, 0)) and board[start_row][0] and board[start_row][0].name == 'wR':
                    return True  # White queenside
            elif piece.name[0] == 'b' and start_row == 0:
                if end_col == 6 and not any_piece_between(start_pos, (start_row, 7)) and board[start_row][7] and board[start_row][7].name == 'bR':
                    return True  # Black kingside
                if end_col == 2 and not any_piece_between(start_pos, (start_row, 0)) and board[start_row][0] and board[start_row][0].name == 'bR':
                    return True  # Black queenside

    return False

# Function to check if a king is in check
def is_in_check(board, color):
    king_pos = None
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece and piece.name == f'{color}K':
                king_pos = (row, col)
                break
        if king_pos:
            break
    
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece and piece.name[0] != color:
                if basic_valid_move(piece, (row, col), king_pos):
                    return True
    return False

# Function to check if a move is valid considering checks
def is_valid_move(piece, start_pos, end_pos):
    if not basic_valid_move(piece, start_pos, end_pos):
        return False

    # Make a temporary move
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    temp_piece = board[end_row][end_col]
    board[end_row][end_col] = piece
    board[start_row][start_col] = None
    if is_in_check(board, piece.name[0]):
        # Undo the temporary move
        board[start_row][start_col] = piece
        board[end_row][end_col] = temp_piece
        return False
    # Undo the temporary move
    board[start_row][start_col] = piece
    board[end_row][end_col] = temp_piece

    return True

# Function to check if there are any pieces between two positions
def any_piece_between(start_pos, end_pos):
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

# Function to move a piece from start position to end position
def move_piece(start_pos, end_pos):
    global en_passant_target, move_history, fifty_move_counter

    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = board[start_row][start_col]
    board[start_row][start_col] = None
    
    # Handle en passant
    if piece.name[1] == 'P' and (end_row, end_col) in en_passant_target:
        board[start_row][end_col] = None  # Remove the captured pawn
    
    # Handle castling
    if piece.name[1] == 'K' and abs(start_col - end_col) == 2:
        # Kingside castling
        if end_col == 6:
            board[end_row][5] = board[end_row][7]
            board[end_row][7] = None
        # Queenside castling
        elif end_col == 2:
            board[end_row][3] = board[end_row][0]
            board[end_row][0] = None
    
    board[end_row][end_col] = piece
    
    # Handle pawn promotion
    promote_pawn(end_row, end_col)
    
    # Update en_passant_target
    en_passant_target = []
    if piece.name[1] == 'P' and abs(end_row - start_row) == 2:
        en_passant_target = [(start_row + end_row) // 2, start_col]
    
    # Update move history and fifty-move counter
    move_history.append([[piece for piece in row] for row in board])
    if piece.name[1] == 'P' or board[end_row][end_col] is not None:
        fifty_move_counter = 0
    else:
        fifty_move_counter += 1

# Function to promote a pawn
def promote_pawn(row, col):
    global board
    piece = board[row][col]
    if piece.name[1] == 'P':
        if (piece.name[0] == 'w' and row == 0) or (piece.name[0] == 'b' and row == 7):
            # Replace pawn with a queen (default promotion)
            board[row][col] = Piece(f"{piece.name[0]}Q", f"pieces/{piece.name[0]}Q.png")

# Function to check if a player is in checkmate
def is_checkmate(board, color):
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece and piece.name[0] == color:
                for r in range(ROWS):
                    for c in range(COLS):
                        if is_valid_move(piece, (row, col), (r, c)):
                            return False
    return True

# Function to check if the game is in stalemate
def is_stalemate(board, color):
    if not is_in_check(board, color):
        for row in range(ROWS):
            for col in range(COLS):
                piece = board[row][col]
                if piece and piece.name[0] == color:
                    for r in range(ROWS):
                        for c in range(COLS):
                            if is_valid_move(piece, (row, col), (r, c)):
                                return False
        return True
    return False

# Function to check for insufficient material
def insufficient_material(board):
    pieces = [piece for row in board for piece in row if piece]
    if len(pieces) == 2:
        return True  # Only two kings left
    if len(pieces) == 3:
        names = [piece.name[1] for piece in pieces]
        if 'K' in names and ('B' in names or 'N' in names):
            return True  # King and Bishop or Knight vs King
    return False

# Function to check for threefold repetition
def is_threefold_repetition():
    state_count = {}
    for state in move_history:
        state_str = str(state)
        if state_str in state_count:
            state_count[state_str] += 1
        else:
            state_count[state_str] = 1
        if state_count[state_str] >= 3:
            return True
    return False

# Function to check for fifty-move rule
def is_fifty_move_rule():
    return fifty_move_counter >= 50

# Function to reset the board to the initial state
def reset_board():
    global board, turn, selected_piece, valid_moves, checkmate, stalemate, draw
    board = [[piece for piece in row] for row in initial_board]
    turn = 'w'
    selected_piece = None
    valid_moves = []
    checkmate = False
    stalemate = False
    draw = False

# Main menu function
def main_menu():
    run = True
    while run:
        WIN.fill(WHITE)  # Fill the window with white color
        draw_text('Chess', font, BLACK, WIN, WIDTH//2 - 50, HEIGHT//4)  # Draw the title text
        draw_text('Choose Your Color', font, BLACK, WIN, WIDTH//2 - 100, HEIGHT//2 - 50)  # Draw the prompt text
        
        # Draw the buttons for choosing the color
        white_button = draw_button('White', font, GREEN, WIN, WIDTH//4, HEIGHT//2, 150, 50)
        black_button = draw_button('Black', font, GREEN, WIN, 3 * WIDTH//4 - 150, HEIGHT//2, 150, 50)
        
        # Event loop to handle user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the window
                pygame.quit()  # Quit Pygame
                return
            if event.type == pygame.MOUSEBUTTONDOWN:  # If the user clicks the mouse
                if white_button.collidepoint(event.pos):  # If the white button is clicked
                    game_loop('w')  # Start the game with white color
                if black_button.collidepoint(event.pos):  # If the black button is clicked
                    game_loop('b')  # Start the game with black color
        
        pygame.display.update()  # Update the display

# Main game loop
def game_loop(player_color):
    global turn, selected_piece, valid_moves, checkmate, stalemate, draw, dragging_piece, dragging_start_pos
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    selected_piece = None  # Initially, no piece is selected
    valid_moves = []  # Initially, no valid moves are available
    turn = 'w'  # White starts the game
    run = True  # Variable to control the game loop
    while run:
        clock.tick(60)  # Limit the frame rate to 60 FPS
        mouse_pos = pygame.mouse.get_pos()  # Get the current position of the mouse
        for event in pygame.event.get():  # Event loop to handle user inputs
            if event.type == pygame.QUIT:  # If the user closes the window
                pygame.quit()  # Quit Pygame
                return
            if event.type == pygame.MOUSEBUTTONDOWN:  # If the user clicks the mouse
                col, row = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE  # Calculate the column and row of the click
                if player_color == 'b':  # Adjust for black player
                    row, col = ROWS - 1 - row, COLS - 1 - col
                if board[row][col] is not None and board[row][col].name[0] == turn:  # If a piece of the current player is clicked
                    selected_piece = (row, col)  # Mark the piece as selected
                    dragging_piece = board[row][col]  # Set the dragging piece
                    dragging_start_pos = (row, col)  # Set the starting position of the drag
                    valid_moves = []  # Reset valid moves
                    for r in range(ROWS):
                        for c in range(COLS):
                            if is_valid_move(dragging_piece, selected_piece, (r, c)):  # Check for valid moves
                                valid_moves.append((r, c))  # Add valid move
            if event.type == pygame.MOUSEBUTTONUP:  # If the user releases the mouse button
                if dragging_piece:  # If a piece is being dragged
                    col, row = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE  # Calculate the column and row of the release
                    if player_color == 'b':  # Adjust for black player
                        row, col = ROWS - 1 - row, COLS - 1 - col
                    if is_valid_move(dragging_piece, dragging_start_pos, (row, col)):  # If the move is valid
                        move_piece(dragging_start_pos, (row, col))  # Move the piece
                        if is_in_check(board, 'b' if turn == 'w' else 'w'):  # Check if the opponent is in check
                            if is_checkmate(board, 'b' if turn == 'w' else 'w'):  # Check if it's checkmate
                                checkmate = True
                        if is_stalemate(board, 'b' if turn == 'w' else 'w'):  # Check if it's stalemate
                            stalemate = True
                        if insufficient_material(board):  # Check if there is insufficient material for checkmate
                            draw = True
                        if is_threefold_repetition():  # Check if there is a threefold repetition
                            draw = True
                        if is_fifty_move_rule():  # Check if the fifty-move rule applies
                            draw = True
                        turn = 'b' if turn == 'w' else 'w'  # Switch turns
                    dragging_piece = None  # Reset dragging piece
                    dragging_start_pos = None  # Reset dragging start position
                    selected_piece = None  # Reset selected piece
                    valid_moves = []  # Reset valid moves
            if event.type == pygame.MOUSEMOTION:  # If the user moves the mouse
                if dragging_piece:  # If a piece is being dragged
                    mouse_pos = event.pos  # Update the mouse position
        
        draw_board(selected_piece, valid_moves, player_color, dragging_piece, mouse_pos)  # Draw the board
        
        # Display checkmate, stalemate, or draw messages
        if checkmate:
            draw_text(f"Checkmate! {'White' if turn == 'b' else 'Black'} wins!", font, RED, WIN, WIDTH // 2 - 150, HEIGHT // 2 - 100)
            restart_button = draw_button('Restart', font, GREEN, WIN, WIDTH // 2 - 75, HEIGHT // 2, 150, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        reset_board()
                        main_menu()
        elif stalemate:
            draw_text("Stalemate! It's a draw!", font, RED, WIN, WIDTH // 2 - 150, HEIGHT // 2 - 100)
            restart_button = draw_button('Restart', font, GREEN, WIN, WIDTH // 2 - 75, HEIGHT // 2, 150, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        reset_board()
                        main_menu()
        elif draw:
            draw_text("Draw!", font, RED, WIN, WIDTH // 2 - 150, HEIGHT // 2 - 100)
            restart_button = draw_button('Restart', font, GREEN, WIN, WIDTH // 2 - 75, HEIGHT // 2, 150, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        reset_board()
                        main_menu()
        
        pygame.display.update()  # Update the display

# Run the game
if __name__ == "__main__":
    reset_board()  # Reset the board to the initial state
    main_menu()  # Display the main menu
