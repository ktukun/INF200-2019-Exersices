# -*- coding: utf-8 -*-

__author__ = 'Martin Sanderøy'
__email__ = 'martsand@nmbu.no'
import math


class LCGRand:
    slope = 7 ** 5
    congruence_class = 2 ** 31 - 1

    def __init__(self, seed):
        """
        Initialise a linear congruence random number generator

        Arguments
        ---------
        seed : int
            The initial seed for the generator
        """
        self._hidden_state = seed

    def rand(self):
        """
        Generate a single random number.

        Returns
        -------
        int
            A random integer
        """
        self._hidden_state *= self.slope
        self._hidden_state %= self.congruence_class

        return self._hidden_state

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.
        Yields
        ------
        int
            A random number.
        """
        return RandIter(self, math.inf)


class RandIter:
    def __init__(self, random_number_generator, length, stop=True,
                 max_iter=10**9):
        """
        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None
        self.stop = stop
        self.max_iter = max_iter

    def __iter__(self):
        """
        Initialise the iterator.
        Returns
        -------
        self : RandIter
        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError('can only be initialised once')
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.
        Returns
        -------
        int
        A random number.
        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError(f'{type(self)} is not initialised')
        if self.num_generated_numbers >= self.length:
            raise StopIteration
        if self.stop and self.num_generated_numbers > self.max_iter:
            raise RuntimeError(f'reached maximum iterations = {10**9} '
                               f'change it or set stop=False for true '
                               f'infinite')
        self.num_generated_numbers += 1
        return self.generator.rand()


if __name__ == '__main__':
    generator = LCGRand(1)
    for i, rand in enumerate(generator.random_sequence(10)):
        print(f'The {i}th random_sequence number is {rand}')

    for i, rand in enumerate(
            generator.infinite_random_sequence()):
        print(f'The {i}-th random number is {rand}')

        if i > 100:
            break
