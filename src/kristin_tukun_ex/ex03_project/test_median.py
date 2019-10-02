from kristin_tukun_ex.ex03_project.median import median
import pytest

__author__ = 'Kristin Tukun'
__email__ = 'kritu@nmbu.no'

def test_one_element_list():
    assert median([1]) == 1


def test_odd_number_og_elements():

    list_odd = [5, 1, 7, 15, 33, 27, 20, 4, 7]
    assert median(list_odd) == 7


def test_even_number_of_elements():
    list_even = [5, 1, 4, 0, 3, 22, 66, 28]
    assert median(list_even) == 4.5


def test_ordered_elements():
    list_ordered = [0, 1, 3, 4, 5, 22, 28, 66]
    assert median(list_ordered) == 4.5


def test_reversed_ordered_elements():
    list_reversed_ordered = [66, 28, 22, 5, 4, 3, 1, 0]
    assert median(list_reversed_ordered) == 4.5


def test_random_ordered_elements():
    list_random_ordered = [5, 1, 15, 33, 20, 4, 7]
    assert median(list_random_ordered) ==7


def test_value_error():
    with pytest.raises(ValueError):
        median([])


def test_original_data_unchanged():
    original = [3, 6, 1, 6]
    original_save = original
    median(original)
    assert original is original_save

def test_tuples():
    data_tuple = (3, 6, 1, 6)
    assert median(data_tuple) == 4.5


