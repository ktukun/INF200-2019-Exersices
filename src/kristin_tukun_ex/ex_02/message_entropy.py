def letter_freq(txt):
    from collections import Counter
    return Counter(txt.lower())


def entropy(message):
    from math import log2
    counted_message = letter_freq(message)
    n = len(counted_message)
    h = []
    for n_i in counted_message:
        p_i = counted_message[n_i] / n
        h.append(-p_i*log2(p_i))
    return sum(h)


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
