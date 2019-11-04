# -*- coding: utf-8 -*-

__author__ = 'Martin Sanderøy'
__email__ = 'martsand@nmbu.no'


class LCGRand:
    def __init__(self, input_seed):
        self.random_number = input_seed
        self.a = 7 ** 5
        self.m = 2 ** 31 - 1

    def rand(self):
        self.random_number = self.a * self.random_number % self.m
        return self.random_number

    def random_sequence(self, length):
        return RandIter(self, length)


class RandIter:
    def __init__(self, random_number_generator, length):
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
        self.length = int(length)
        self.num_generated_numbers = None

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
        self.num_generated_numbers += 1
        return self.generator
