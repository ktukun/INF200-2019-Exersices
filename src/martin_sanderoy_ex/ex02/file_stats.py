from collections import Counter


def char_counts(text_filename):
    with open(text_filename, 'rt', encoding='utf-8') as file:
        text = file.read()
        file.close()
    ordinated = []
    for letter in text:
        ordinated.append(ord(letter))
    return Counter(ordinated)


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
