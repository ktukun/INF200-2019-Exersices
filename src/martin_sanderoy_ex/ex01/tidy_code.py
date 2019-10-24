from random import randint

__author__ = 'Martin Sanderoy'
__email__ = 'martsand@nmbu.no'
"""
Script for a guessing game where you are asked to guess a number higher than zero and the correct answer is between
2 and 12.
"""


def your_guess():
    guess = 0
    while 2 > guess or guess > 12:
        guess = int(input('Please guess a number between 2 and 12: '))
    return guess


def random_number():
    return randint(1, 6) + randint(1, 6)


def is_equal(n_1, n_2):
    return n_1 == n_2


if __name__ == '__main__':

    correct_guess = False
    remaining_tries = 3
    correct_number = random_number()
    while not correct_guess and remaining_tries > 0:

        correct_guess = is_equal(correct_number, your_guess())
        if not correct_guess:
            print('Wrong, try again!')
            remaining_tries -= 1

    if remaining_tries > 0:
        print('You won {} points.'.format(remaining_tries))
    else:
        print('You lost. Correct answer: {}.'.format(correct_number))
