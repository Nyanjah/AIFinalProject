#import tensorflow as tf 
#from tensorflow import keras
#from keras import layers
from tictactoe import *

def main():
    # Create an instance of the tic-tac-toe game
    print("Start of the Tic-Tac-Toe game!")
    game = TicTacToe()
    # Player ID's are represented as 1 and -1
    current_player = 1
    while game.in_progress == True:
        # Take in the player's move
        move = input("Enter tic-tac-toe move as x,y: ")
        x, y = move.split(",")
        x,y  = int(x), int(y)
        game.play_move(current_player,x,y)
        game.print_board()
        game.check_winner()
        # Swap players
        current_player = current_player * - 1
    print(" The winner is {}!".format(game.winner))        

main()