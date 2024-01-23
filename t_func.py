import unittest

from func import *

class TestFunc(unittest.TestCase):

    def test_returns_zero_if_input_number_not_in_list(self):
        lst = [1, 2, 3, 4, 5]
        x = 6
        result = del_number(lst, x)
        assert result == 0

    def test_returns_number_of_times_input_number_appears(self):
        lst = [1, 2, 3, 4, 5, 5, 5]
        x = 5
        result = del_number(lst, x)
        assert result == 3

    def test_returns_zero_if_input_number_not_in_list(self):
        lst = [1, 2, 3, 4, 5]
        x = 6
        result = del_number(lst, x)
        assert result == 0

    def test_works_correctly_with_large_lists(self):
        lst = [1] * 1000
        x = 1
        result = del_number(lst, x)
        assert result == 1000

    def test_works_correctly_with_negative_numbers_in_list(self):
        # Arrange
        lst = [-1, -2, -3, -4, -5, -5, -5]
        x = -5
        result = del_number(lst, x)
        assert result == 3

    def test_works_correctly_with_negative_input_numbers(self):
        lst = [1, 2, 3, 4, 5]
        x = -5
        result = del_number(lst, x)
        assert result == 0