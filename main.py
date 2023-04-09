import argparse
import os
import tictactoe.tictactoeAI as tictactoeAI
#import connect4AI
#import battleshipAI
import tictactoe.playtictactoe as playtictactoe
#import playconnect4
#import playbattleship


parser = argparse.ArgumentParser()
parser.add_argument('--game', choices=['tictactoe', 'connect4', 'battleship'], help='Select the game')
parser.add_argument('--train', action='store_true', help='Train the game-specific AI')
parser.add_argument('--play', action='store_true', help='Play against the AI of the chosen game')
parser.add_argument('--epochs', type=int, default=10, help='Number of epochs to train over')
args = parser.parse_args()

if args.game == 'tictactoe':
    if args.train:
        if not os.path.exists('models'):
            os.makedirs('models')
        tictactoeAI.train_model(epochs=args.epochs)
    elif args.play:
        if not os.path.exists('models'):
            print('Error: AI model folder not found. Please train the AI first using the --train option.')
        else:
            playtictactoe.play_game()
    else:
        parser.print_help()


# Placeholder code for future expansion of the project:

# elif args.game == 'connect4':
#     if args.train:
#         if not os.path.exists('models'):
#             os.makedirs('models')
#         connect4AI.train_model('models')
#     elif args.play:
#         if not os.path.exists('models'):
#             print('Error: AI model folder not found. Please train the AI first using the --train option.')
#         else:
#             playconnect4.play_game('models')
#     else:
#         parser.print_help()

# elif args.game == 'battleship':
#     if args.train:
#         if not os.path.exists('models'):
#             os.makedirs('models')
#         battleshipAI.train_model('models')
#     elif args.play:
#         if not os.path.exists('models'):
#             print('Error: AI model folder not found. Please train the AI first using the --train option.')
#         else:
#             playbattleship.play_game('models')
#     else:
#         parser.print_help()

else:
    parser.print_help()