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
                      87: 70, }

    pos_player = [0] * num_players
    num_moves = [0] * num_players

    while max(pos_player) < 90:

        for player in range(len(pos_player)):

            pos_player[player] = pos_player[player] + randint(1, 6)
            num_moves[player] = num_moves[player] + 1

            for key in snakes_ladders.keys():

                if pos_player[player] == key:
                    pos_player[player] = snakes_ladders[key]

    return num_moves

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