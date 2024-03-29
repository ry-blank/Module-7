import unittest
from fun_with_collections import sort_and_search_array


class SearchArray(unittest.TestCase):
    def test_search_array_for_item_found(self):
        self.assertEqual(sort_and_search_array.search_array([5, 10, 15, 20, 25], 25), 4)

    def test_search_array_for_item__not_found(self):
        self.assertEqual(sort_and_search_array.search_array([5, 10, 15, 20, 25], 30), -1)

    # def test_sort_list(self):
    #     self.assertEqual(sort_and_search_array.sort_array


if __name__ == '__main__':
    unittest.main()
