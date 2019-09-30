from collections import Counter


def char_counts(textfilename):
    """
    A function that converts a message to utf8 numbers, and counts how many
    times this number occurs.
    :param textfilename: A file with text
    :return: A dictionary containing the number used in the message and
    how many times they occur.
    """
    with open(textfilename, encoding='utf-8') as f:
        file = f.read()
        utf8_translated = []
        for letter in file:
            utf8_translated.append(ord(letter))

    return Counter(utf8_translated)


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
