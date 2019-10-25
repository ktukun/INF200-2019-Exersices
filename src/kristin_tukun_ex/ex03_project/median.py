def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    length_data = len(sorted_data)
    if length_data == 0:
        raise ValueError('The list must contain elements')
    if length_data == 1:
        return sorted_data[0]
    elif length_data % 2 == 1:
        return sorted_data[length_data//2]
    else:
        return (0.5 * (sorted_data[length_data//2 - 1]
                       + sorted_data[length_data//2]))
