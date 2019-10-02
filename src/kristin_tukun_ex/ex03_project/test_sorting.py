# -*- coding: utf-8 -*-
from kristin_tukun_ex.ex_02.bubble_sort import bubble_sort
import random
import numpy as np
import pytest

__author__ = 'Kristin Tukun'
__email__ = 'kritu@nmbu.no'


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
    assert data is not sorted_data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)
    assert data is data


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    assert bubble_sort([1, 1, 1]) == [1, 1, 1]


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    """Test if the function sorts list_1 that is a list of integers with 
    positive and negative values from -50 to 50 and with a random length of 
    list from 2 to 100. We are testing 20 different lists.
    """

    for _ in range(20):
        list_1 = np.random.randint(low=-50, high=50,
                                   size=(random.randint(2, 100)))
        sorted_list_1 = bubble_sort(list_1)

        for small, large in zip(sorted_list_1[:-1], sorted_list_1[1:]):
            assert small <= large

    """Test if the function sorts list_1 that is a list of integers with 
    positive and negative values from -75 to 75 and with a random length of 
    list from 2 to 100. We are testing 20 different lists.
    """

    for _ in range(20):
        list_2 = np.random.uniform(low=-75, high=75,
                                   size=(random.randint(2, 100)))
        sorted_list_2 = bubble_sort(list_2)

        for small, large in zip(sorted_list_2[:-1], sorted_list_2[1:]):
            assert small <= large
