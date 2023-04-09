import tensorflow as tf
import numpy as np
from tictactoe.tictactoe import *
from tqdm import tqdm

def train_model(epochs):
# Create the game environment
    game = TicTacToe()

    # Define the model using TensorFlow
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(3, 3)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(9, activation='softmax')
    ])

    # Define the optimizer and loss function
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()
    model.compile(optimizer,loss_fn)
    # Set the number of episodes to play
    num_episodes = epochs
    print("Training the tic-tac-toe neural network...")
    # Train the model by playing against itself
    for episode in tqdm(range(num_episodes)):
        # Reset the game environment
        game.__init__()
        
        # Initialize the game state and reward
        state = np.array(game.board)
        reward = 0

        # Loop through the game until it ends
        while game.in_progress:
            # Choose a move based on the current state
            available_moves = 3*np.where(state == 0)[0] + np.where(state == 0)[1]
            probabilities = model.predict(np.array([state]), verbose = 0)[0]
            valid_probabilities = probabilities[available_moves]
            move = np.random.choice(available_moves, p=valid_probabilities/np.sum(valid_probabilities))
            x, y = move // 3, move % 3

            # Play the move and update the game state
            player = -1 if len(np.where(state == 0)[0]) % 2 == 0 else 1
            # print("Player {} played move ({},{})".format(player,x,y))
            game.play_move(player, x, y)
            state = np.array(game.board)
            
            # Check if the game has ended and calculate the reward
            game.check_winner()
            if game.in_progress:
                reward = 0
            elif game.winner == player:
                reward = 1
            else:
                reward = -1
                
            # Update the model using the reward and new state
            with tf.GradientTape() as tape:
                probabilities = model(np.array([state]))
                loss = loss_fn(np.array([move]), probabilities)
            gradients = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        
        # Evaluate the model after every 100 episodes
        if episode % 100 == 0:
            model.evaluate(np.array([state]), np.array([move]), verbose=0)

    print("Saving the model as 'tic_tac_toe' to ./models")
    model.save("./models",save_format='tf')