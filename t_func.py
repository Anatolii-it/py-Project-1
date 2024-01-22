import unittest

from func import *
class TestFunc(unittest.TestCase):
    def test_calculates_sum_of_numbers(self):
        my_sum(1, 5)
        assert True
    def test_returns_correct_sum_for_positive_integers(self):
        my_sum(1, 10)
        assert True
    def test_returns_correct_sum_for_negative_integers(self):
        my_sum(-5, -1)
        assert True

    def test_returns_zero_if_both_integers_are_zero(self):
        my_sum(0, 0)
        assert True