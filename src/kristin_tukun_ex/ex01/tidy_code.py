from random import randint

__author__ = ''
__email__ = '@nmbu.no'

""" A guessing game where you have three tries to guess a number between 2 and 12.
    The right answer is generated randomly.
"""


def guess_a_number():
    """
    A function with a number as input. It will make you guess until you have guessed a number between 2 and 12.
    :return: Returns an integer number of your guess that meets the requirements for number interval.
    """
    number = 0
    while number < 2 or number > 12:
        number = int(input('Your guess: '))
    return number


def random_number():
    """
    This is a function returns a number between 2 and 12.
    :return: a number between 2 and 12
    """
    return randint(1, 6) + randint(1,6)


def is_equal(arg1, arg2):
    """
    A function that checks if two arguments are true
    :param arg1: An arbitrary argument.
    :param arg2: Another arbitrary argument.
    :return: True or False depending on if the arguments are equal.
    """
    return arg1 == arg2


if __name__ == '__main__':

    is_guess_correct = False
    remaining_tries = 3
    answer = random_number()
    """ This while loop continues as long as the guess is not the same as the answer, and the number of remaining tries
        are larger than zero. It will run the guess_a_number function an check if that is equal to the answer. If it is 
        not equal it will print 'Wrong* and update number of remaining tries.
    """
    while not is_guess_correct and remaining_tries > 0:
        guess = guess_a_number()
        is_guess_correct = is_equal(answer, guess)
        if not is_guess_correct:
            print('Wrong, try again!')
            remaining_tries -= 1

    if remaining_tries > 0:
        print('You won {} points.'.format(remaining_tries))
    else:
        print('You lost. Correct answer: {}.'.format(answer))
