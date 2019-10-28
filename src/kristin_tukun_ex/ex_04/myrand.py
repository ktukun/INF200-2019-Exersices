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
        if len(self.list_numbers) == 0:
            return RuntimeError
        return self.list_numbers.pop(0)
