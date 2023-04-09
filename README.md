# Game AI
This is a command line tool to play games against AI or train AI to play games.
Currently supported games are Tic Tac Toe, Connect 4, and Battleship.

## Usage
To use the tool, navigate to the root directory of the project and run the `gameAI.py` file with the following options:

- `--game`: Choose the game to play/train. Available options are 'tictactoe', 'connect4', and 'battleship'.
- `--train`: Train the game-specific AI model. 
- `--play`: Play against the AI of the chosen game.
- `--epochs`: (Optional) Number of epochs to train over. Default is 10.

For example, to train a Tic Tac Toe AI model for 50 epochs, run the following command:

## Example
To play Tic Tac Toe against the trained AI, run the following command:

- 'python gameAI.py --game tictactoe --play'


## Future Expansion
Placeholder code has been included in the main.py script to support Connect 4 and Battleship games. To use these games, uncomment the necessary import statements and code blocks.
