import unittest

from func import *

class TestFunc(unittest.TestCase):
    def test_returns_true_for_prime_numbers(self):
        assert p_p_number(2) == True
        assert p_p_number(3) == True
        assert p_p_number(5) == True
        assert p_p_number(7) == True
        assert p_p_number(11) == True
        assert p_p_number(13) == True
    def test_returns_false_for_non_prime_numbers(self):
        assert p_p_number(4) == False
        assert p_p_number(6) == False
        assert p_p_number(8) == False
        assert p_p_number(9) == False
        assert p_p_number(10) == False
        assert p_p_number(12) == False
    def test_returns_false_for_numbers_less_than_or_equal_to_1(self):
        assert p_p_number(0) == False
        assert p_p_number(1) == False
    def test_returns_false_for_0(self):
        assert p_p_number(0) == False

    def test_correctly_counts_prime_numbers(self):
        numbers = [2, 3, 5, 7, 11, 13]
        result = k_p_numbers(numbers)
        assert result == 6

    def test_returns_zero_for_empty_list(self):
        numbers = []
        result = k_p_numbers(numbers)
        assert result == 0

    def test_returns_zero_for_non_prime_numbers(self):
        numbers = [4, 6, 8, 9, 10]
        result = k_p_numbers(numbers)
        assert result == 0

    def test_returns_zero_for_list_with_only_zero(self):
        numbers = [0]
        result = k_p_numbers(numbers)
        assert result == 0

    def test_returns_zero_for_list_with_negative_numbers(self):
        numbers = [-2, -3, -5, -7]
        result = k_p_numbers(numbers)
        assert result == 0