"""
Program: basic_list_assignment
Author: Ryan Blankenship
Last Date Modified: 10/6/2019

The purpose of this program is to take user
input then display it in a list.
"""


def make_list():
    """
    function to return list of user input from function get_input()
    :return: returns list of user input
    """
    number_list = []
    attempts = 3
    for a in range(attempts):
        try:
            user_num = int(get_input())
        except ValueError:
            print("Please enter numbers only.")
        else:
            number_list.insert(len(number_list), user_num)
    return number_list


def get_input():
    """
    function to prompt user for input
    :return: returns a string
    """
    user_num = input("Please enter a number to add to your list: ")
    return user_num


if __name__ == '__main__':
    print(make_list())
