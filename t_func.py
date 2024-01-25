import unittest

from func import *

class TestFunc(unittest.TestCase):
    def test_even_odd_count(self):
        numbers = [1, 2, 3, 4, 5]
        even_count, odd_count, _, _ = analyze_numbers(numbers)
        assert even_count == 2
        assert odd_count == 3
    def test_positive_negative_count(self):
        numbers = [-1, -2, 3, 4, -5]
        _, _, positive_count, negative_count = analyze_numbers(numbers)
        assert positive_count == 2
        assert negative_count == 3

    def test_all_counts(self):
        numbers = [-1, -2, 3, 4, -5]
        even_count, odd_count, positive_count, negative_count = analyze_numbers(numbers)
        assert even_count == 2
        assert odd_count == 3
        assert positive_count == 2
        assert negative_count == 3
    def test_one_even_number(self):
        numbers = [2]
        even_count, odd_count, positive_count, negative_count = analyze_numbers(numbers)
        assert even_count == 1
        assert odd_count == 0
        assert positive_count == 1
        assert negative_count == 0
    def test_one_positive_number(self):
        numbers = [5]
        even_count, odd_count, positive_count, negative_count = analyze_numbers(numbers)
        assert even_count == 0
        assert odd_count == 1
        assert positive_count == 1
        assert negative_count == 0
    def test_one_zero_number(self):
        numbers = [0]
        even_count, odd_count, positive_count, negative_count = analyze_numbers(numbers)
        assert even_count == 1
        assert odd_count == 0
        assert positive_count == 0
        assert negative_count == 0