import unittest

from func import *

class TestFunc(unittest.TestCase):
    def test_correct_count(self):
        lst = [1, 2, 3, 4, 5, 5, 5]
        number = 5
        result = serch_number(lst, number)
        assert result == 3

    def test_return_count(self):
        lst = [1, 2, 3, 4, 5, 5, 5]
        number = 5
        result = serch_number(lst, number)
        assert isinstance(result, int)

    def test_various_lengths(self):
        lst1 = [1, 2, 3, 4, 5]
        lst2 = [1, 2, 3, 4, 5, 5]
        lst3 = [1, 2, 3, 4, 5, 5, 5]
        number = 5
        result1 = serch_number(lst1, number)
        result2 = serch_number(lst2, number)
        result3 = serch_number(lst3, number)
        assert result1 == 1
        assert result2 == 2
        assert result3 == 3

    def test_number_not_in_list(self):
        lst = [1, 2, 3, 4, 5]
        number = 6
        result = serch_number(lst, number)
        assert result == 0

    def test_empty_list(self):
        lst = []
        number = 5
        result = serch_number(lst, number)
        assert result == 0

    def test_single_element_list(self):
        lst = [5]
        number = 5
        result = serch_number(lst, number)
        assert result == 1
