import unittest

from func import *

class TestFunc(unittest.TestCase):

    def test_handles_lists_with_different_lengths(self):
        my_list1 = [1, 2, 3]
        my_list2 = [4, 5]
        result = summa_lists(my_list1, my_list2)
        assert result == [1, 2, 3, 4, 5]

    def test_handles_lists_with_large_number_of_elements(self):
        my_list1 = [1] * 1000000
        my_list2 = [2] * 1000000
        result = summa_lists(my_list1, my_list2)
        assert len(result) == 2000000
        assert result[:1000000] == [1] * 1000000
        assert result[1000000:] == [2] * 1000000

    def test_handles_lists_with_very_small_number_of_elements(self):
        my_list1 = [1]
        my_list2 = [2]
        result = summa_lists(my_list1, my_list2)
        assert result == [1, 2]

    def test_handles_lists_with_none_values(self):
        my_list1 = [1, None, 3]
        my_list2 = [4, 5, None]
        result = summa_lists(my_list1, my_list2)
        assert result == [1, None, 3, 4, 5, None]

    def test_handles_empty_lists(self):
        my_list1 = []
        my_list2 = []
        result = summa_lists(my_list1, my_list2)
        assert result == []

    def test_returns_sum_of_two_lists(self):
        my_list1 = [1, 2, 3]
        my_list2 = [4, 5, -6]
        result = summa_lists(my_list1, my_list2)
        assert result == [1, 2, 3, 4, 5, -6]
    def test_different_data_types(self):
        my_list1 = [1, 'a', True]
        my_list2 = ['b', False, 2.5]
        result = summa_lists(my_list1, my_list2)
        assert result == [1, 'a', True, 'b', False, 2.5]
    def test_negative_values(self):
        my_list1 = [-1, -2, -3]
        my_list2 = [-4, -5, -6]
        result = summa_lists(my_list1, my_list2)
        assert result == [-1, -2, -3, -4, -5, -6]