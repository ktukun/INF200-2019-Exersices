def bubble_sort(data):
    """
    A function that has a tuple as an input and then sorts this list by comparing all elements in for loops.

    :param data: A tuple that consists of numbers.
    :return: A new list that is a sorted version of the list.
    """
    sort_data = list(data)
    length_data = len(sort_data) - 1
    for j in range(0, length_data):
        for i in range(0, length_data-j):
            if sort_data[i] > sort_data[i+1]:
                sort_data[i], sort_data[i+1] = sort_data[i+1], sort_data[i]
    return sort_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
