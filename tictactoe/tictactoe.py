# Tic-Tac-Toe Game Environment
class TicTacToe:
    def __init__(self):
        # --- Gamestate ---
        self.in_progress = True
        # [3x3] grid of entries which take on the following values:
        #  Player 1   -> -1
        #  Empty Spot ->  0
        #  Player 2   -> +1
        self.mapping = {"-1":"X", '1': "O", "0" :" "}
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.winner = None
        
    def play_move(self,player,x,y):
        # If the chosen spot is open, place the mark.
        if self.board[x][y] == 0:
            self.board[x][y] = player
        # Otherwise, do not modify the game state
        return
    
    def print_board(self):
        # Print the contents of the board
        print("{},{},{}".format(self.mapping[str(self.board[0][0])], self.mapping[str(self.board[1][0])], self.mapping[str(self.board[2][0])]))
        print("{},{},{}".format(self.mapping[str(self.board[0][1])], self.mapping[str(self.board[1][1])], self.mapping[str(self.board[2][1])]))
        print("{},{},{}".format(self.mapping[str(self.board[0][2])], self.mapping[str(self.board[1][2])], self.mapping[str(self.board[2][2])]))

    
    def check_winner(self):
        # If we find a winner, we set that player as the winner and stop the game
        for player in [-1, 1]:
            # Check rows for a win
            for i in range(3):
                if all([self.board[i][j] == player for j in range(3)]):
                    self.winner = player
                    self.in_progress = False
                    return
                
            # Check columns for a win
            for j in range(3):
                if all([self.board[i][j] == player for i in range(3)]):
                    self.winner = player
                    self.in_progress = False
                    return
                
            # Check diagonals for a win
            if all([self.board[i][i] == player for i in range(3)]):
                self.winner = player
                self.in_progress = False
                return
            
            if all([self.board[i][2-i] == player for i in range(3)]):
                self.winner = player
                self.in_progress = False
                return
            
             # Check if all cells on the board are filled (i.e., a draw)
            if all([self.board[i][j] != 0 for i in range(3) for j in range(3)]):
                self.winner = None
                self.in_progress = False
                return 
        # If no winner was found, do nothing
        return