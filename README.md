# Game AI
This is a command line tool to play games against AI or train AI to play games.
This is a (WIP) final project as part of the spring 2023 CMPSC 442 course at Pennsylvania State University,
belonging to the second group given the topic of "AI & PLAY".
Currently tic-tac-toe is the only supported game.
This project will eventually also support connect 4 and battleship.

## Usage
To use the tool, navigate to the root directory of the project and run the `gameAI.py` file with the following options:

- `--game`: Choose the game to play/train. Available options are 'tictactoe', 'connect4', and 'battleship'.
- `--train`: Train the game-specific AI model. 
- `--play`: Play against the AI of the chosen game.
- `--epochs`: (Optional) Number of epochs to train over. Default is 10.



## Example
To play Tic Tac Toe against the trained AI, run the following command:

`py gameAI.py --game tictactoe --play`

To train a Tic Tac Toe AI model for 50 epochs:

`py gameAI.py --game tictactoe --train 50`

## Future Expansion
Placeholder code has been included in the main.py script to support Connect 4 and Battleship games. To use these games, uncomment the necessary import statements and code blocks.
