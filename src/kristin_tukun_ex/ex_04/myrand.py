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
        self.numbers = list_numbers.copy()
        self.idx = 0

    def rand(self):
        if len(self.numbers) == 0:
            raise RuntimeError
        return self.numbers.pop(0)


if __name__ == "__main__":

    test_seeds = [1, 5, 10, 100]

    for seed in test_seeds:
        print('Seed: {0} gives a random number {1}'
              .format(seed, LCGRand(seed).rand()))

    test_numbers = [1, 3, 5, 2, 8, 3]
    first_numbers = ListRand(test_numbers)

    for _ in test_numbers:
        print('Number from the list:', first_numbers.rand())
