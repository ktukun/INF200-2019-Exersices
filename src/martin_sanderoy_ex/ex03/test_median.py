# -*- coding: utf-8 -*-

__author__ = 'Martin Sanderøy'
__email__ = 'martsand@nmbu.no'
import pytest

"""
median function is copied from yngvem from github.
But had to change it since it failed for single element.
Also changed it to raise ValueError for empty list.
"""
def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    sorted_data = sorted(data)
    length = len(sorted_data)
    if length == 0:
        raise ValueError
    elif length == 1:
        return sorted_data[0]
    elif length % 2 == 1:
        return sorted_data[length // 2]
    else:
        return 0.5 * (sorted_data[length // 2 - 1]
                      + sorted_data[length // 2])


def test_one_element():
    assert median([1]) == 1


def test_odd_number_element():
    data = [1, 3, 8, 4, 5]
    assert median(data) == 4


def test_even_number_element():
    data = [1, 3, 8, 4]
    assert median(data) == (3+4)/2


def test__ordered_elements():
    data = [1, 2, 3, 4, 5]
    assert median(data) == 3


def test__reverse_ordered_elements():
    data = [5, 4, 3, 2, 1]
    assert median(data) == 3


def test_unordered_elements():
    data = [3, 2, 5, 1, 4]
    assert median(data) == 3


def test_empty_element():
    with pytest.raises(ValueError):
        median([])


def test_original_data_unchanged():
    data = [3, 2, 5, 1, 4]
    data_save = data
    median(data)
    assert data is data_save


def test_tuple():
    data = (1, 2, 3, 4)
    assert median(data) == 2.5
