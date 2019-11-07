def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    square = []
    for k in range(n):
        if k % 3 == 1:
            square.append(k**2)
    return square


if __name__ == '__main__':
    if squares_by_loop(100) != squares_by_comp(100):
        print('ERROR!')
