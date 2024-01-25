import unittest

from func import *

class TestFunc(unittest.TestCase):

    def test_returns_list_of_numbers_raised_to_power(self):
        list_stupendous = 2
        list_number = [1, 2, 3, 4, 5]
        result = stupen(list_stupendous, list_number)
        assert result == [1, 4, 9, 16, 25]

    def test_works_correctly_with_list_of_integers_and_positive_exponent(self):

        list_stupendous = 3
        list_number = [1, 2, 3, 4, 5]
        result = stupen(list_stupendous, list_number)
        assert result == [1, 8, 27, 64, 125]

    def test_works_correctly_with_empty_list_and_any_exponent(self):
        list_stupendous = 2
        list_number = []
        result = stupen(list_stupendous, list_number)
        assert result == []

    def test_works_correctly_with_list_of_negative_integers_and_odd_exponent(self):
        list_stupendous = 3
        list_number = [-1, -2, -3, -4, -5]
        result = stupen(list_stupendous, list_number)
        assert result == [-1, -8, -27, -64, -125]

    def test_works_correctly_with_list_of_floats_and_integer_exponent(self):
        list_stupendous = 2
        list_number = [1.5, 2.5, 3.5, 4.5, 5.5]
        result = stupen(list_stupendous, list_number)
        assert result == [2.25, 6.25, 12.25, 20.25, 30.25]
    def test_large_integers_and_exponent(self):
        list_stupendous = 1000
        list_number = [10**18, 10**19, 10**20]
        result = stupen(list_stupendous, list_number)
        assert result == [10**(18*1000), 10**(19*1000), 10**(20*1000)]
    def test_numbers_with_duplicates_and_any_exponent(self):
        list_stupendous = 3
        list_number = [1, 2, 2, 3, 3, 3]
        result = stupen(list_stupendous, list_number)
        assert result == [1, 8, 8, 27, 27, 27]