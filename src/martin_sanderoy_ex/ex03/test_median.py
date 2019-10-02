# -*- coding: utf-8 -*-

__author__ = 'Martin Sanderøy'
__email__ = 'martsand@nmbu.no'
"""
median function is copied from yngvem from github.
"""


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    length = len(sorted_data)
    return (sorted_data[length // 2] if length % 2 == 1
            else 0.5 * (sorted_data[length // 2 - 1]
                        + sorted_data[length // 2]))
