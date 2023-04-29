# Game AI 
This is a command line tool to play games against AI or train AI to play games.
This is a (WIP) final project as part of the spring 2023 CMPSC 442 course at Pennsylvania State University,
belonging to the second group given the topic of "AI & PLAY".
Currently tic-tac-toe is the only supported game.
This project will eventually also support connect 4 and battleship.

The directory for the project is organized so that each game has a single folder corresponding to it, which contains
the necessary .py files to play against it, train it, its game logic, and its (optional) GUI. There is also a folder
which is used to store the model after training. This folder is what is accessed by the play file to fetch the model
and laod it into memory for the player to challenge. Further implementation details can be found in the comments of the 
individual files.

## Usage
To use the tool, navigate to the root directory of the project and run the `gameAI.py` file with the following options:

- `--game`: Choose the game to play/train. Available options are 'tictactoe', 'connect4', and 'battleship'.
- `--train`: Train the game-specific AI model. 
- `--play`: Play against the AI of the chosen game.
- `--epochs`: (Optional) Number of epochs to train over. Default is 10.



## Example
To play Tic Tac Toe against the trained AI, run the following command:

```
py gameAI.py --game tictactoe --play
```

To train a Tic Tac Toe AI model for 50 epochs:
```
py gameAI.py --game tictactoe --train --epoch 50
```
## Future Expansion

Placeholder code has been included in the main.py script to support Connect 4 and Battleship games. Although not fully implemented, the skeleton code which make them up is visible in this repository in various locations in the directory.
