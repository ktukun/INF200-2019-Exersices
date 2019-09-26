def letter_freq(txt):
    """
    This is a function with text as input, it will then count occurrence of letters and signs in the text. It does not
    differentiate on upper an lowercase letters.
    :param txt: A text string
    :return: A list of number of occurrences.
    """
    from collections import Counter
    letters = txt.lower()
    letters = sorted(letters)
    return Counter(letters)


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
