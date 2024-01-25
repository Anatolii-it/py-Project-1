import unittest

from func import *

class TestFunc(unittest.TestCase):
    def test_returns_1_when_input_is_0(self):
        assert factorial(0) == 1
    def test_returns_correct_factorial_for_positive_integers(self):
        assert factorial(5) == 120
        assert factorial(10) == 3628800
    def test_returns_list_with_1_for_0(self):
        numbers = [0]
        expected = [1]
        assert c_factorials(numbers) == expected
    def test_returns_factorials_for_positive_integers(self):
        numbers = [1, 2, 3, 4, 5]
        expected = [1, 2, 6, 24, 120]
        assert c_factorials(numbers) == expected

    def test_returns_empty_list_for_empty_list(self):
        numbers = []
        expected = []
        assert c_factorials(numbers) == expected

