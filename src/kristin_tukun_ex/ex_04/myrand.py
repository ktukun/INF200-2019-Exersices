class LCGRand:

    def __init__(self, number_seed):

        self.random_number = number_seed

    def rand(self):
        a = 7 ** 5
        m = 2 ** 31 - 1
        self.random_number = a * self.random_number % m
        return self.random_number


class ListRand:

    def __init__(self, list_numbers):
        self.list_numbers = list_numbers
        self.idx = 0

    def rand(self):
        if self.idx == len(self.list_numbers):
            return RuntimeError
        number = self.list_numbers[self.idx]
        self.idx += 1
        return number
