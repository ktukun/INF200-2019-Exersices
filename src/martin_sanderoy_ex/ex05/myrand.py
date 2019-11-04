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


class ListRand:
    def __init__(self, number_list):
        self.random_numbers = number_list.copy()

    def rand(self):
        if len(self.random_numbers) == 0:
            raise RuntimeError

        return self.random_numbers.pop(0)


if __name__ == '__main__':
    lcg = LCGRand(1)
    print('two numbers from LCGRand: {0} and {1}'.format(lcg.rand(),
                                                         lcg.rand()))
    lr = ListRand([4, 5, 29, 11])
    print('two numbers from ListRand: {0} and {1}'.format(lr.rand(),
                                                          lr.rand()))
