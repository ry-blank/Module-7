"""
Program: search_and_sort_array_assignment
Author: Ryan Blankenship
Last Date Modified: 10/7/2019

The purpose of this program is to .
"""
import array as arr


def sort_array(sorted_array):
    """
    function to sort array of user input
    :param sorted_array: array of user input
    """
    d = sorted_array.tolist()
    d.sort()
    sorted_array = arr.array('d', d)
    return sorted_array


def search_array(b_array, value):
    """
    function to search array for item
    :param b_array: array of user input
    :param value: to search index
    :return: the index of item in array or item not found
    """
    try:
        return b_array.index(value)
    except ValueError:
        return -1


if __name__ == '__main__':
    a = arr.array('d', [1.2, 6.3, 3.4])
    search_array(a, 2.5)
    print(sort_array(a))
