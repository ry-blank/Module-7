"""
Program: search_and_sort_list_assignment
Author: Ryan Blankenship
Last Date Modified: 10/7/2019

The purpose of this program is to sort a list
or search a list for item then return index or
ValueError if item not found.
"""


def sort_list(a_list):
    """
    function to sort list of user input
    :param a_list: list of user input
    """
    try:
        a_list.sort()
    except ValueError:
        return -1


def search_list(a_list, a_number):
    """
    function to search list for item
    :return: the index of item in list or item not found
    :param a_list: list from user input
    :param a_number: to search index
    :return: the index of item in list or item not found
    """
    try:
        index_listing = a_list.index(a_number)
    except ValueError:
        return -1
    else:
        return index_listing


if __name__ == '__main__':
    sort_list()
    a_list = [5, 10, 15, 20, 25]
    sort_list(a_list)
    print(a_list)
