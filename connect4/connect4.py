import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

class Connect4():
    
    def __init__(self):
        self.in_progress = True
        self.winner = None
        self.board = np.zeros(ROW_COUNT,COLUMN_COUNT)

    def play_move(self,piece,col):
        # If the column has an empty spot still
        if self.is_valid_location(col):
            # We can play the move
            row = self.get_next_open_row(col)
            self.place_piece(row,col,piece)
            return
        # If the column is already full, do nothing
        # This effectively wastes a turn
        else:
            return
            

    def _place_piece(self,row,col,piece):
        self.board[row][col] = piece

    def _is_valid_location(self,col):
        return self.board[ROW_COUNT-1][col] == 0

    def _get_next_open_row(self,col):
        for r in range(ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def print_board(self):
        #Flipping the board since numpy arrays are indexed by top-left
        print(np.flip(self.board, 0))

    def check_for_winner(self, piece):
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    # If we detect the piece is a winner, we are done.
                    self.in_progress = False
                    self.winner = piece
                    return

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    # If we detect the piece is a winner, we are done.
                    self.in_progress = False
                    self.winner = piece
                    return

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    # If we detect the piece is a winner, we are done.
                    self.in_progress = False
                    self.winner = piece
                    return

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    # If we detect the piece is a winner, we are done.
                    self.in_progress = False
                    self.winner = piece
                    return
