import tensorflow as tf
import numpy as np
from tictactoe.game import *


def play_game():
    # Load the saved model
    model = tf.keras.models.load_model("./models/tictactoe")

    # Create the game environment
    game = TicTacToe()

    # Play against the model in the terminal
    print("Playing against the tic-tac-toe neural network...")
    while game.in_progress:
        # Print the current game state
        game.print_board()
        
        # Get the player's move
        player_move = input("Enter your move as row,column (e.g. 1,2): ")
        y, x = [int(i) for i in player_move.split(",")]
        
        # Play the player's move and update the game state
        game.play_move(1, x, y)
        game.check_for_winner()
        game.print_board()
        if not game.in_progress:
            break
        
        if game.in_progress:
            # Get the model's move
            state = np.array(game.board)
            available_moves = 3*np.where(state == 0)[0] + np.where(state == 0)[1]
            probabilities = model.predict(np.array([state]), verbose = 1)[0]
            valid_probabilities = probabilities[available_moves]
            move = available_moves[np.argmax(valid_probabilities)]
            
            x, y = move // 3, move % 3
            print("Model played move ({},{})".format(x,y))

            # Play the model's move and update the game state
            game.play_move(-1, x, y)
            game.check_for_winner()

    game.print_board()
    # Print the final game state and winner
    if game.winner == 1:
        print("You win!")
    elif game.winner == -1:
        print("Model wins!")
    else:
        print("Tie game!")
