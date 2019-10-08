"""
Program: search_and_sort_array_assignment
Author: Ryan Blankenship
Last Date Modified: 10/7/2019

The purpose of this program is to .
"""


def sort_array(a_array):
    """
    function to sort array of user input
    :param a_array: array of user input
    """
    pass


def search_array(a_array, a_number):
    """
    function to search array for item
    :param a_array: list from user input
    :param a_number: to search index
    :return: the index of item in array or item not found
    """
    try:
        index_listing = a_array.index(a_number)
    except ValueError:
        return -1
    else:
        return index_listing


if __name__ == '__main__':
    sort_array()
