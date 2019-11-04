# -*- coding: utf-8 -*-

__author__ = 'Kristin Tukun'
__email__ = 'ktukun@nmbu.no'


class LCGRand:
    slope = 7 ** 5
    congruence_class = 2 ** 31 - 1

    def __init__(self, number_seed):

        self.random_number = number_seed

    def rand(self):
        self.random_number *= self.slope
        self.random_number %= self.congruence_class
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
        self.length = length
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

        #self.num__generated_numbers = 0
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
        if self.num__generated_numbers is None:
            raise RuntimeError(f'{type(self)} is not initialised as an iterator.')
        if self.num__generated_numbers >= self.length:
            raise StopIteration
        self.num__generated_numbers += 1
        return self.generator


if __name__ == "__main__":
    random_number_generator = LCGRand(1)
    for rand in generator.random_sequence(10):
        print(rand)