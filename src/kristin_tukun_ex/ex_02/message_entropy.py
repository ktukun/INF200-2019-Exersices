from collections import Counter


def letter_freq(txt):
    """
    This is a function with text as input, it will then count occurrence of
    letters and signs in the text. It does not
    differentiate on upper an lowercase letters.
    :param txt: A text string
    :return: A list of number of occurrences.
    """
    return Counter(txt.lower())


def entropy(message):
    """
    A function that calculates the entropy h of a message.
    :param message: A string of text
    :return: The calculated entropy h
    """
    from math import log2
    counted_message = letter_freq(message)
    length_message = sum(counted_message.values())
    h = []
    for occurences in counted_message:
        freq = counted_message[occurences] / length_message
        h.append(-freq*log2(freq))
    return sum(h)


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
