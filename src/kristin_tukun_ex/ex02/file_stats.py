def char_counts(textfilename):
    from collections import Counter

    with open(textfilename, encoding='utf-8') as f:
        file = f.read()
        ordinated = []
        for letter in file:
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
