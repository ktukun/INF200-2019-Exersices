# -*- coding: utf-8 -*-

__author__ = 'Martin Sanderøy'
__email__ = 'martsand@nmbu.no'


class LCGRand:
    def __init__(self, input_seed):
        self.random_number = input_seed

    def rand(self):
        a = 7 ** 5 # =16807
        m = 2 ** 31 - 1
        self.random_number = a * self.random_number % m
        return self.random_number


class ListRand(self, number_list):
    def __init__(self):
        a = 7 ** 5 = 16807
        m = 2 ** 31 - 1
        r[n + 1] = a * r[n] % m

    def __rand__(self, other):(self):
        return self.width * self.height






