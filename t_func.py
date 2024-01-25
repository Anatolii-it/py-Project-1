import unittest

from func import *

class TestFunc(unittest.TestCase):
    def test_reverse_list_of_integers(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = [5, 4, 3, 2, 1]
        actual_output = r_list(input_list[::-1])
        assert actual_output == expected_output

    def test_reverse_list_of_strings(self):
        input_list = ["apple", "banana", "cherry"]
        expected_output = ["cherry", "banana", "apple"]
        actual_output = r_list(input_list[::-1])
        assert actual_output == expected_output

    def test_reverse_list_with_none_values(self):
        input_list = [None, 1, None, 3, None]
        expected_output = [None, 3, None, 1, None]
        actual_output = r_list(input_list[::-1])
        assert actual_output == expected_output


