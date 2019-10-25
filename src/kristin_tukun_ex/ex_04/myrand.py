class LCGRand(self):

    def __init__(self, number_seed):

        self.random_number = number_seed

    def rand(self):
        a = 7 ** 5
        m = 2 ** 31 - 1
        self.random_number = a * self.random_number % m
        return self.random_number


class ListRand(self):

    def __init__(self, list_numbers):

        self. = seed
