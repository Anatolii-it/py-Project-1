import unittest

from func import *
class TestFunc(unittest.TestCase):
    def test_sum_zero_and_negative_integer(self):
        result = my_sum(0, -5)
        assert result == -5
    def test_sum_zero_and_positive_integer(self):
        result = my_sum(0, 5)
        assert result == 5
    def test_sum_positive_integers(self):
        result = my_sum(2, 3)
        assert result == 5
    def test_sum_negative_integers(self):
        result = my_sum(-2, -3)
        assert result == -5
    def test_sum_positive_and_negative_integers(self):
        result = my_sum(2, -3)
        assert result == -1
    def test_sum_zero_and_decimal_number(self):
        result = my_sum(0, 1.5)
        assert result == 1.5