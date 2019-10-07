import unittest
from fun_with_collections import sort_and_search_list


class SearchList(unittest.TestCase):
    def test_search_list_for_item_found(self):
        self.assertEqual(sort_and_search_list.search_list([5, 10, 15, 20, 25], 25), 4)

    def test_search_list_for_item__not_found(self):
        self.assertEqual(sort_and_search_list.search_list([5, 10, 15, 20, 25], 30), -1)

    def test_sort_list(self):
        self.assertEqual(sort_and_search_list.sort_list([5, 25, 10, 20, 15]), [0])


if __name__ == '__main__':
    unittest.main()
