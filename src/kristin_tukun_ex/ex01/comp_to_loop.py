def squares_by_comp(n):
    """
    A function that squares every number that has a modulus equal to 1, up to the number n.
    :param n: An arbitrary integer.
    :return: A list of numbers that has modulus equal 1 squared for each number up to n.
    """
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    """
    A function that squares every number that has a modulus equal to 1, up to the number n using for loop.
    :param n: An arbitrary integer.
    :return: A list of numbers that has modulus equal 1 squared for each number up to n.
    """
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k**2)
    return [squares]


if __name__ == '__main__':
    if squares_by_comp(20) != squares_by_loop(20):
        print('ERROR!!!')
