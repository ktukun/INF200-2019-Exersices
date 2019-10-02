# -*- coding: utf-8 -*-

__author__ = 'Martin Sanderøy'
__email__ = 'martsand@nmbu.no'


from random import randrange, uniform


def bubble_sort(data):
    sorting_data = list(data)
    n = len(sorting_data)
    for i in range(n-1):
        for j in range(n - i - 1):
            if sorting_data[j] > sorting_data[j + 1]:
                sorting_data[j], sorting_data[j + 1] = \
                    sorting_data[j + 1], sorting_data[j]
    return sorting_data


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data is not data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    data_save = data
    sorted_data = bubble_sort(data)
    assert data_save is data is not sorted_data


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    assert bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2]


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data = []  # Making a list for test with random numbers and length.
    for _ in range(randrange(0, 20)):
        data.append(uniform(-20, 20))

    sorted_list = bubble_sort(data)
    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        assert small <= large

    # Test if it works on an equal tuple
    sorted_tuple = bubble_sort(tuple(data))
    for small, large in zip(sorted_tuple[:-1], sorted_tuple[1:]):
        assert small <= large
