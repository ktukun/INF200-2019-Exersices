def letter_freq(txt):
    from collections import Counter
    letters = txt.casefold()
    letters = sorted(letters)
    counter = Counter(letters)
    return counter


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
