from math import log2
from collections import Counter


def letter_freq(txt):
    return Counter(txt.lower())


def entropy(message):
    freq = letter_freq(message)
    message_length = len(message)
    h = []
    for letter in freq:
        p = freq[letter]/message_length
        h.append(-p*log2(p))
    return sum(h)


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
