import tkinter as tk
from tictactoe.gui import TicTacToeGUI

def play_game():
    # Create the GUI
    gui = TicTacToeGUI()
    # Run the GUI's main event loop which contains the tic-tac-toe game
    gui.mainloop()

