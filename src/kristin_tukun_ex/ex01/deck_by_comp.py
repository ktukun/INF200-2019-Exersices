SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    """
    A function that creates a deck of cards using for loops.
    :return: A list of tuples with suits and corresponding numbers.
    """
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    """
    A function that creates a deck of cards using list comprehension.
    :return: A list of tuples with suits and corresponding numbers.
    """
    return [(suit, val) for suit in SUITS for val in VALUES]


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
