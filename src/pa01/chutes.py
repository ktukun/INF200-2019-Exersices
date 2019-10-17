from random import randint


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """


snakes_ladders = {1: 40,
                  8: 10,
                  36: 52,
                  43: 62,
                  49: 79,
                  65: 82,
                  68: 85,
                  24: 5,
                  33: 3,
                  42: 30,
                  56: 37,
                  64: 27,
                  74: 12,
                  87: 70,
                  }

number_of_players = 4

position_players = [0] * number_of_players
number_of_rolls = [0] * number_of_players

while max(position_players) < 90:

    for player in range(len(position_players)):

        position_players[player] = position_players[player] + randint(1, 6)
        number_of_rolls[player] = number_of_rolls[player] + 1

        for key in snakes_ladders.keys():

            if position_players[player] == key:
                position_players[player] = snakes_ladders[key]

print('You have won!')


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.