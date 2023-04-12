import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk
from tictactoe.game import *


class TicTacToeGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Load the saved model
        self.model = tf.keras.models.load_model("./models/tictactoe")

        # Create the game environment
        self.game = TicTacToe()

        # Create the GUI elements
        self.board_frame = tk.Frame(self)
        self.board_buttons = []
        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = tk.Button(self.board_frame, text="", font=("Helvetica", 30), width=2, height=1, command=lambda x=row, y=col: self.play_move(x, y))
                button.grid(row=row, column=col, padx=5, pady=5)
                row_buttons.append(button)
            self.board_buttons.append(row_buttons)
        self.board_frame.pack(side = "bottom")

        self.message_label = tk.Label(self, text="TicTacToe AI", font=("Helvetica", 16))
        self.message_label.pack(side = "top")

        self.reset_button = tk.Button(self, text="Reset Game", font=("Helvetica", 16), command=self.reset_game)
        self.reset_button.pack(side = "bottom")


        # Create a frame for the bar graph
        self.graph_frame = tk.Frame(self,padx = 5, pady = 5, borderwidth= 5)
        self.graph_frame.pack(side="right")

        # Create a figure for the bar graph
        self.fig = plt.figure(figsize=(4, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Create a canvas to display the bar graph
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(side="right", fill="both", expand=1)

        
        # Start the game
        self.player_turn = 1

    def update_graph(self):
        # Get the probability values
        probs = self.get_prob()

        # Clear the previous bar graph
        self.ax.clear()

        # Create a new bar graph with the probability values
        x_labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.ax.bar(x_labels, probs, align='center')

        # Set the axis labels and title
        self.ax.set_title('Probability distribution of Agent\'s last move')

        # Redraw the canvas
        self.canvas.draw()


    def play_move(self, x, y):
        if self.game.in_progress and self.player_turn:
            # Play the player's move and update the game state
            self.game.play_move(1, x, y)
            self.game.check_for_winner()
            self.update_board()

            if self.game.in_progress:
                # Get the model's move
                # Before the AI moves, we update the graph with its output for the current board state
                self.update_graph()
                
                state = np.array(self.game.board)
                available_moves = 3*np.where(state == 0)[0] + np.where(state == 0)[1]
                probabilities = self.model.predict(np.array([state]), verbose = 1)[0]
                valid_probabilities = probabilities[available_moves]
                move = available_moves[np.argmax(valid_probabilities)]

                x, y = move // 3, move % 3

                # Play the model's move and update the game state
                self.game.play_move(-1, x, y)
                self.game.check_for_winner()
                self.update_board()
                
                
        # Print the final game state and winner
        if not self.game.in_progress:
            self.message_label.config(text="")
            if self.game.winner == 1:
                self.message_label.config(text = "You won!")
            elif self.game.winner == -1:
                self.message_label.config(text = "Model won!")
            else:
                self.message_label.config(text = "Tie!")


    def update_board(self):
        # Update the board buttons with the current game state
        print("Board Updated")
        for row in range(3):
            for col in range(3):
                value = self.game.board[row][col]
                if value == 1:
                    self.board_buttons[row][col].config(text="X", state="disabled")
                elif value == -1:
                    self.board_buttons[row][col].config(text="O", state="disabled")
                else:
                    self.board_buttons[row][col].config(text="")

        # Update the message label
        if self.game.in_progress:
            if self.player_turn:
                self.message_label.config(text="Your turn")
                
            self.player_turn = not self.player_turn

    def reset_game(self):
        # Clear the game board
        self.game.clear_board()

        # Enable all the board buttons
        for row in range(3):
            for col in range(3):
                self.board_buttons[row][col].config(text="", state="normal")

        # Reset the message label
        self.message_label.config(text="TicTacToe AI")
        
        # Reset the probability graph
        probs = [0,0,0,0,0,0,0,0,0]
        
        # Clear the previous bar graph
        self.ax.clear()
        
        # Create a new bar graph with the probability values
        x_labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.ax.bar(x_labels, probs, align='center')
        
        # Set the axis labels and title
        self.ax.set_title('Probability distribution of Agent\'s last move')

        # Redraw the canvas
        self.canvas.draw()
        
        # Start the game
        self.player_turn = True
        
        
        
    def get_prob(self):
        state = np.array(self.game.board)
        unavailable_moves = 3*np.where(state != 0)[0] + np.where(state != 0)[1]
        probabilities = self.model.predict(np.array([state]), verbose = 1)[0]
        #Filtering out probabilities which cannot be selected
        for move in unavailable_moves:
            probabilities[move] = 0
        #Returning the probabilities the network can select from
        return probabilities